import React, { useState, useRef } from "react";

const AudioRecorder: React.FC = () => {
  const [recording, setRecording] = useState<boolean>(false);
  const [audioURL, setAudioURL] = useState<string | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const CHUNK_SIZE = 1024 * 1024; // 1MB chunk size

  const startRecording = async () => {
    if (recording) return;

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);
      audioChunksRef.current = [];

      mediaRecorderRef.current.ondataavailable = (event: BlobEvent) => {
        audioChunksRef.current.push(event.data);
      };

      mediaRecorderRef.current.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: "audio/wav" });
        uploadBlob(audioBlob, "audio/wav")
        const url = URL.createObjectURL(audioBlob);
        setAudioURL(url);
      };

      mediaRecorderRef.current.start();
      setRecording(true);
    } catch (error) {
      console.error("Error accessing microphone:", error);
    }
  };

  function uploadBlob(audioBlob: Blob, fileType: string) {
    const formData = new FormData();
    formData.append('audio', audioBlob, 'file');
    formData.append('type', fileType || 'wav');
  
    // Your server endpoint to upload audio:
    const apiUrl = "http://127.0.0.1:5328/api/speech_quality_feedback";
  
    const data = fetch(apiUrl, {
      method: 'POST',
      headers: { 'Accept': 'application/json' },
      body: formData
    }).then(response => {
        return response.json();
    });
  }

  const stopRecording = () => {
    if (!recording) return;

    mediaRecorderRef.current?.stop();
    setRecording(false);
  };

  const replayAudio = () => {
    if (!audioURL) return;

    const audio = new Audio(audioURL);
    audio.play();
  };

  return (
    <div>
      <button className="border-2 border-black" onClick={startRecording} disabled={recording}>
        Start Recording
      </button>
      <button className="border-2 border-black" onClick={stopRecording} disabled={!recording}>
        Stop Recording
      </button>
      <button className="border-2 border-black" onClick={replayAudio} disabled={!audioURL}>
        Replay Audio
      </button>
      {audioURL && <audio src={audioURL} controls />}
    </div>
  );
};

export default AudioRecorder;
