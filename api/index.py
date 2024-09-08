import time
from flask import Flask, request, jsonify
import sys
import os
import io
from openai import OpenAI
from pydub import AudioSegment
from two_sum_data import clusters
from two_sum_code_quality import code_quality_clusters
from flask_cors import CORS
import speech_recognition as sr
from speech_quality_rubric import speech_rubric_content
from database import run_sample_test

MODEL = "gpt-4o"
UPLOAD_FOLDER = 'app/uploads/'
TRANSCRIPTIONS_TXT_FILE = 'transcriptions.txt'
TRANSCRIPTIONS_FILE_PATH = os.path.join(UPLOAD_FOLDER, TRANSCRIPTIONS_TXT_FILE)
interview_question = 'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.'
answer = 'The Python code iterates through a list of numbers (`nums`) to find two distinct elements that sum up to a given `target`, using a dictionary (`digs`) to store the indices of the elements. If such a pair is found, it returns their indices; otherwise, it returns an empty list.'

# export OPENAI_API_KEY='sk-proj-LhvuRIDZ5LTkPQo7X0GaT3BlbkFJmdOcUvs9717OEYmFybxL'
client = OpenAI(
    organization='org-b7eWSRacp3SdwnJr0qm9O1sZ',
    project='proj_7vmgneF3f7mNXFeZ4ld2kk4o',
    api_key=os.environ.get("OPENAI_API_KEY"),
)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

def convert_to_supported_format(audio_file, output_format='mp3'):
    audio = AudioSegment.from_file(audio_file, format='webm')
    output_file = f"converted_audio.{output_format}"
    audio.export(output_file, format=output_format)
    return output_file

def transcribe_model_selection_v2(
    model: str,
    audio_file: str,
):
    """Transcribe an audio file."""
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Transcribes the audio into text
    response = google_client.recognize(config=config, audio=audio_file)
    print(response, file=sys.stdout)

    return response

def handle_transcriptions_file(): 
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    with open(TRANSCRIPTIONS_FILE_PATH, 'w') as file:
        file.write('')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.remove(TRANSCRIPTIONS_FILE_PATH)
    with open(TRANSCRIPTIONS_FILE_PATH, 'w') as file:
        file.write('')

@app.route('/api/add_speech_to_transcriptions', methods=['POST'])
def add_to_transcriptions():
    audio_file = request.files.get('audio')

    if audio_file:
        # Convert the audio to a supported format
        converted_audio_path = convert_to_supported_format(audio_file, output_format='mp3')

        # Open the converted file
        with open(converted_audio_path, 'rb') as audio_data:
            # Call the OpenAI Whisper API
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_data,  # Pass the file-like object
            )
        
        # Write to a transcriptions file locally
        with open(TRANSCRIPTIONS_FILE_PATH, 'a') as f:
                f.write(transcription.text + '\n')

        # Optionally, delete the converted file if it's no longer needed
        os.remove(converted_audio_path)

        print(transcription.text)
        return jsonify({'status': "OK", 'transcription': transcription.text})
    else:
        print("No audio file received.", file=sys.stdout)
        return jsonify({'status': "No audio file received"}), 400

@app.route('/api/question')
def get_question():
    return {
        'question':
            'Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.\n\n You can return the answer in any order.',
        'examples': [{'input': 'nums = [2,7,11,15], target = 9', 'output': '[0,1]', 'explanation': 'Because nums[0] + nums[1] == 9, we return [0, 1].'}, {'input': 'nums = [3,2,4], target = 6', 'output': '[1,2]'}, {'input': 'nums = [3,3], target = 6', 'output': '[0,1]'}],
        'title': 'Two Sum'
    }
    
@app.route('/api/speech_quality_feedback', methods=['GET'])
def get_speaking_feedback():

    prompt = f"""
    You are evaluating a candidate's communication skills during a technical interview.

    ### Task:
    Evaluate the provided transcript to determine if the candidate correctly answered the following coding question:

    **Coding Question:** {interview_question}

    **Expected Answer:** {answer}

    ### Instructions:
    - If the transcript accurately reflects the expected answer or a similar correct approach, consider this a correct response.
    - If the transcript fails to answer the question correctly or doesn't resemble the expected answer, consider this an incorrect response.

    Rate the candidate's performance based on the accuracy and clarity of their response. Assign a score of 0 if the answer is incorrect or absent.
    
    I want the following structure as output:
    1. Rubric type.
    2. Score rating. (If there is no possible score rating, then give a 1. Put a "/4" after the rating.)
    3. Maximum 3 sentence explanation all on the same paragraph. No references.
    """

    assistant = client.beta.assistants.create(
        name="Software Engineer Interviewer",
        instructions=prompt,
        model=MODEL,
        tools=[{"type": "file_search"}],
    )
    
    # Create a vector store caled "Financial Statements"
    vector_store = client.beta.vector_stores.create(name="Transcription")
    
    # Ready the files for upload to OpenAI
    file_streams = [open(TRANSCRIPTIONS_FILE_PATH, "rb")]
    
    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )
    
    # You can print the status and the file counts of the batch to see the result of this operation.
    print(file_batch.status)
    print(file_batch.file_counts)
    
    assistant = client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )
    
    rating_content = ''
    
    for content in speech_rubric_content:
    
        # Create a thread and attach the file to the message
        thread = client.beta.threads.create(
            messages=[
                {
                "role": "user",
                "content": content,
                }
            ]
        )

        # The thread now has a vector store with that file in its tool resources.
        print(thread.tool_resources.file_search)
        
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id, assistant_id=assistant.id
        )

        messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

        message_content = messages[0].content[0].text
        
        rating_content += message_content.value + '\n\n'

        print(message_content.value, file=sys.stdout)
        
    return {'rating': rating_content}
    # print("\n".join(citations))

@app.route('/api/code_quality_feedback', methods=['POST'])
def code_quality_feedback():
    data = request.get_json()
    code = data['code']

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
        f"You are given a sample list of feedback, per aspect of code quality: {drafter_answers}. "
        "Rate the interview out of 8 (one for each element of the list if the element says that the interviewee has shown mastery in the topic associated to that element). "
        "You should return a number out of 8 in the answer (follow it with a '/4'), and a maximum of 3 of the most valid feedbacks from the list above. Do not make anything up. Limit your answer to 6 sentences."
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

handle_transcriptions_file()
run_sample_test()
