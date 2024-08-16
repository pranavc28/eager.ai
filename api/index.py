import time
from flask import Flask, request, jsonify
import sys
import os
import pathlib
import io
from openai import OpenAI
from two_sum_data import clusters
from two_sum_code_quality import code_quality_clusters
from flask_cors import CORS
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import which
from google.cloud import speech
from google.oauth2 import service_account
from gcs import GCStorage, STORAGE_CLASSES
from google.cloud import storage

client_file='chrisai-432605-f6bfd5c847bc.json'
credentials=service_account.Credentials.from_service_account_file(client_file)
google_client = speech.SpeechClient(credentials=credentials)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

def upload_media_to_gcs(gcs):
    # Step 1. prepare the variables
    # Convert the string to a Path object
    files_folder = pathlib.Path('app/uploads/audio/')
    bucket_name = 'chris_ai_audio'

    # Step 3. Create gcp_api_demo Cloud Storage bucket
    if not bucket_name in gcs.list_buckets():
        bucket_gcs = gcs.create_bucket('gcs_api_demo', STORAGE_CLASSES[0])
    else:
        bucket_gcs = gcs.get_bucket(bucket_name)

    # Step 4. Upload Files
    for file_path in files_folder.glob('*.*'):
        # use file name without the extension
        gcs.upload_file(bucket_gcs, 'without extension/' + file_path.stem, str(file_path))

        # use full file name
    gcs.upload_file(bucket_gcs, file_path.name, str(file_path))

def download_media_from_gcs(gcs, files_folder):
    # Step 5. Download & Delete Files
    gcs_demo_blobs = gcs.list_blobs('chris_ai_audio')
    for blob in gcs_demo_blobs:
        path_download = files_folder.joinpath(blob.name)
        if not path_download.parent.exists():
            path_download.parent.mkdir(parents=True)
        print(path_download)
        # blob.download_to_filename(str(path_download))
        # blob.delete()

def transcribe_model_selection_v2(
    model: str,
    audio_file: str,
):
    """Transcribe an audio file."""
    
    # Reads a file as bytes
    with io.open(audio_file, "rb") as f:
        content = f.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Transcribes the audio into text
    response = google_client.recognize(config=config, audio=audio)
    print(response)
    
    # Step 2. construct GCStorage instance
    storage_client = storage.Client(credentials=credentials)
    gcs = GCStorage(storage_client)
    
    upload_media_to_gcs(gcs)
    download_media_from_gcs(gcs)

    return response

MODEL = "gpt-4o-mini"
# Define the path where you want to save the uploaded audio files
UPLOAD_FOLDER = 'app/uploads/audio/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# export OPENAI_API_KEY='sk-proj-LhvuRIDZ5LTkPQo7X0GaT3BlbkFJmdOcUvs9717OEYmFybxL'
client = OpenAI(
    organization='org-b7eWSRacp3SdwnJr0qm9O1sZ',
    project='proj_7vmgneF3f7mNXFeZ4ld2kk4o',
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.route('/api/speech_quality_feedback', methods=['POST'])
def get_speaking_feedback():
    audio_file = request.files.get('audio')
    print(audio_file, file=sys.stdout)
    
    audio_mp3_path = os.path.join(UPLOAD_FOLDER, 'audioFile.mp3')
    audio_file.save(audio_mp3_path)
        
    response = transcribe_model_selection_v2(model="video", audio_file=audio_mp3_path)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(f"Transcript: {result.alternatives[0].transcript}")
    
    return jsonify({'status': "OK", 'text': 'test'})


@app.route('/api/question')
def get_question():
    return {
        'question':
            'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\n\n You can return the answer in any order.',
        'examples': [{'input': 'nums = [2,7,11,15], target = 9', 'output': '[0,1]', 'explanation': 'Because nums[0] + nums[1] == 9, we return [0, 1].'}, {'input': 'nums = [3,2,4], target = 6', 'output': '[1,2]'}, {'input': 'nums = [3,3], target = 6', 'output': '[0,1]'}]
    }

@app.route('/api/code_quality_feedback', methods=['POST'])
def code_quality_feedback():
    data = request.get_json()
    code = data['code']

    interview_question = 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.'    
    answer = 'The Python code iterates through a list of numbers (`nums`) to find two distinct elements that sum up to a given `target`, using a dictionary (`digs`) to store the indices of the elements. If such a pair is found, it returns their indices; otherwise, it returns an empty list.'

    drafter_answers = []
    temp = 0.3
    
    for cluster in code_quality_clusters:
        type = cluster[0]
        documents = cluster[1]
        prompt = (
            "You are a software engineer interviewer tasked with evaluating an interviewee's code quality. "
            "The interviewee was given the following coding question: '" + interview_question + "'. "
            "This is the code written by the interviewee : '" + code + ". "
            "The correct answer to the coding question is: '" + answer + "'. "
            "You have been trained on the attached documents about '" + type + "'. "
            "Each prompt below includes example error codes, feedback hints, and the actual output. "
            "Evaluate whether the interviewee has demonstrated mastery of the topic. "
            "Provide your judgment with 'Yes' or 'No' followed by 2 sentences of feedback. "
            "Structure your reply as follows: Topic, Mastery (Yes/No), Feedback. "
            "Do not include any code examples in your response. Base your feedback on the following documents: " + documents
        )

        
        assistant = client.beta.assistants.create(
            name="Drafter",
            description="Drafter assistant to give code feedback to tool",
            instructions=prompt,
            model=MODEL,
            temperature=temp,
        )

        thread = client.beta.threads.create()
        messages = client.beta.threads.messages.create(thread_id=thread.id, content=code, role='user')
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        while run.status == 'completed': 
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            drafter_answers.append(messages.data[0].content[0].text.value)
            break
        else:
            print(run.status)

    print(drafter_answers, file=sys.stdout)
    
    prompt_generalist = (
        f"You are a software engineer interviewer.  Your task is to judge an interviewee based on their code quality. "
        f"The interviewee was given the following coding question: '{interview_question}'. "
        f"This is the code written by the interviewee : '{code}'. "
        f"The correct answer to the coding question is: '{answer}'. If the code does not seem at all similar to the answer, and does not compile give the rating 0. "
        f"You are given a list of feedback, per aspect of code quality: {drafter_answers}. "
        "Rate the interview out of 8 (one for each element of the list if the element says that the interviewee has shown mastery in the topic associated to that element). "
        "You should return a number out of 8 in the answer, and a maximum of 3 of the most valid feedbacks from the list above. Do not make anything up. Limit your answer to 6 sentences."
    )

    generalist_assistant = client.beta.assistants.create(
        name="Generalist",
        description="Generalist assistant to give code feedback to tool",
        instructions=prompt_generalist,
        model=MODEL,
        temperature=temp,
    )

    # Am I using the right data structure?
    thread_generalist = client.beta.threads.create()
    messages_generalist = client.beta.threads.messages.create(thread_id=thread.id, content=code, role='user')
    run_generalist = client.beta.threads.runs.create_and_poll(
        thread_id=thread_generalist.id,
        assistant_id=generalist_assistant.id
    )

    final_text = ''
    while run_generalist.status == 'completed': 
        messages_generalist = client.beta.threads.messages.list(
            thread_id=thread_generalist.id
        )
        final_text = messages_generalist.data[0].content[0].text.value
        print(final_text, file=sys.stdout)
        break
    else:
        print(run.status)
    
    return {'code_quality_feedback': final_text}

@app.route('/api/feedback', methods=['POST'])
def get_feedback():
    data = request.get_json()
    code = data['code']
    question = data['question']

    interview_question = 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.'    
    answer = 'The Python code iterates through a list of numbers (`nums`) to find two distinct elements that sum up to a given `target`, using a dictionary (`digs`) to store the indices of the elements. If such a pair is found, it returns their indices; otherwise, it returns an empty list.'

    print(question)
    print('----------------question----------------')
    print(code)
    print('----------------code----------------')
    print(len(clusters))
    drafter_answers = []
    temp = 0.6
    
    for cluster in clusters:
        print('here')
        type = cluster[0]
        documents = cluster[1]
        prompt = (
            "You are a software engineer interviewer. Your task is to respond to a question from an interviewee regarding a coding question, but do not provide the answer to the question they ask. "
            "The interviewee was given the following coding question: '" + interview_question + "'. "
            "Here is the code they wrote: '" + code + "'. "
            "The answer to the coding question (not the question the interviewee asks) is: '" + answer + "'. "
            "You have been trained on the attached documents on the topic: '" + type + "'. Each prompt below includes an example error code, the hint to be given, and the actual output. "
            "Provide an answer based on these documents. It should contain a similar form of error without revealing the actual answer—only a hint. You cannot directly say the data structure or algorithm to use. You can only guide the interviewee in that direction. "
            "You are limited to 4 sentences. Documents: " + documents
        )

        assistant = client.beta.assistants.create(
            name="Drafter",
            description="Drafter assistant to give feedback to tool",
            instructions=prompt,
            model=MODEL,
            temperature=temp,
        )

        thread = client.beta.threads.create()
        messages = client.beta.threads.messages.create(thread_id=thread.id, content=question, role='user')
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        while run.status == 'completed': 
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            drafter_answers.append(messages.data[0].content[0].text.value)
            break
        else:
            print(run.status)

    print(drafter_answers, file=sys.stdout)
    
    prompt_generalist = (
        f"You are a software engineer interviewer. Your task is to respond to a question from an interviewee regarding a coding question, but do not provide the answer to the question they ask. "
        f"The interviewee was given the following coding question: '{interview_question}'. "
        f"Here is the code they wrote: '{code}'. "
        f"The answer to the coding question (not the question the interviewee asks) is: '{answer}'. "
        f"You have to pick the best answer possible from the following list of answers: {drafter_answers}. "
        "It should contain a similar form of error without revealing the actual answer—only a hint. "
        "For example, you cannot let the answer contain how many loops are required, the correct data structure to use, or what the optimal algorithm is."
    )

    generalist_assistant = client.beta.assistants.create(
        name="Generalist",
        description="Generalist assistant to give feedback to tool",
        instructions=prompt_generalist,
        model=MODEL,
        temperature=temp,
    )

    # Am I using the right data structure?
    thread_generalist = client.beta.threads.create()
    messages_generalist = client.beta.threads.messages.create(thread_id=thread.id, content=question, role='user')
    run_generalist = client.beta.threads.runs.create_and_poll(
        thread_id=thread_generalist.id,
        assistant_id=generalist_assistant.id
    )
    
    # Am I using the righr data structure?

    final_text = ''
    while run_generalist.status != 'completed': 
        time.sleep(1)  # Sleep for a short time to avoid overwhelming the server with requests
        run_generalist = client.beta.threads.get_status(thread_id=thread_generalist.id)  # Update the status

    # Once the status is 'completed', proceed to retrieve and print messages
    messages_generalist = client.beta.threads.messages.list(
        thread_id=thread_generalist.id
    )
    print(messages_generalist.data[0], file=sys.stdout)
    final_text = messages_generalist.data[0].content[0].text.value
    print(final_text, file=sys.stdout)

    resp = jsonify(success=True)
    resp.feedback = final_text
    print(resp, file=sys.stdout)
    return jsonify({'feedback': final_text})

@app.route('/api/run', methods=['POST'])
def run():
    data = request.get_json()
    print(data)
    code = data['code']
    
    try:
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        sys.stdout = new_stdout = io.StringIO()

        # Execute the code
        exec(code)

        # Get the output
        output = new_stdout.getvalue()

        # Restore stdout
        sys.stdout = old_stdout
        
        return jsonify({'output': output})
    except Exception as e:
        return jsonify({'output': str(e)}) 