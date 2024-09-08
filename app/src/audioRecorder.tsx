import React, { useState, useRef, useEffect } from "react";
import { PlaySolid, PauseSolid, Pause } from 'iconoir-react';

interface AudioRecorderProps {
    setRecording: (recording: boolean) => void;
    recording: boolean;
};

const AudioRecorder: React.FC<AudioRecorderProps> = ({setRecording, recording}) => {
  const [audioURL, setAudioURL] = useState<string | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const currentChunkSizeRef = useRef<number>(0);

  const CHUNK_SIZE = 1024 * 1024; // 1MB chunk size

  const startRecording = async () => {
    if (recording) return;

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      
      // Use a supported MIME type such as "audio/webm" or "audio/ogg"
      mediaRecorderRef.current = new MediaRecorder(stream, { mimeType: "audio/webm" });
      audioChunksRef.current = [];
      currentChunkSizeRef.current = 0;

      mediaRecorderRef.current.ondataavailable = (event: BlobEvent) => {
        audioChunksRef.current.push(event.data);
        currentChunkSizeRef.current += event.data.size;
      };

      mediaRecorderRef.current.start(1000); // Collect audio data every second
      setRecording(true);
    } catch (error) {
      console.error("Error accessing microphone:", error);
    }
  };

  const sendAudioData = () => {
    if (audioChunksRef.current.length > 0) {
        const audioBlob = new Blob(audioChunksRef.current, { type: "audio/webm" });
        console.log(`Sending audio chunk, size: ${audioBlob.size}`);
        uploadChunk(audioBlob);
        audioChunksRef.current = [];
        currentChunkSizeRef.current = 0;
    }
  };

  const uploadChunk = async (audioBlob: Blob) => {
    const formData = new FormData();
    formData.append("audio", audioBlob, "chunk.webm");

    try {
      const response = await fetch("http://127.0.0.1:5328/api/add_speech_to_transcriptions", {
        method: "POST",
        body: formData,
      });
      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }
      console.log("Chunk uploaded successfully!");
    } catch (error) {
      console.error("Error uploading audio chunk:", error);
    }
  };

  const stopRecording = () => {
    if (!recording) return;

    mediaRecorderRef.current?.stop();
    console.log(currentChunkSizeRef.current);
    setRecording(false);
    sendAudioData(); // Send any remaining data after stopping
  };

  useEffect(() => {
    return () => {
      if (mediaRecorderRef.current) {
        mediaRecorderRef.current.stop();
      }
    };
  }, []);

  return (
    <div className="flex items-center space-x-4">
        <PlaySolid color="black" height={36} width={36} onClick={startRecording} className="cursor-pointer" />
        {!recording ? <PauseSolid color="black" height={36} width={36} onClick={stopRecording} className="cursor-pointer" /> : <Pause color="black" height={36} width={36} onClick={stopRecording} className="cursor-pointer" />}
    </div>
  );
};

export default AudioRecorder;
