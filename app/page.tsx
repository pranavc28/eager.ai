"use client";

import React, { useState, useEffect, KeyboardEvent } from 'react';
import { CloudUpload, Running } from 'iconoir-react';
import CodeEditor from "./src/codeEditor"
import ChatBot from "./src/chatBot"
import useRunCode from './hooks/useRunCode';
import RunCodeOutput from './src/runCodeOutput';
import useCodeQualityFeedback from './hooks/useCodeQualityFeedback';
import useSpeechQualityFeedback from './hooks/useSpeechQualityFeedback';
import AudioRecorder from './src/audioRecorder';
import Timer from './src/timer'

export default function Home() {
  const [code, setCode] = useState('');
  const { output, error, loading, runCode } = useRunCode();
  const [showFeedback, setShowFeedback] = useState(false);
  const {output: codeQualityOutput, error: codeQualityError, loading: codeQualityLoading, getFeedback } = useCodeQualityFeedback();
  const {output: speechQualityOutput, error: speechQualityError, loading: speechQualityLoading, getSpeechFeedback } = useSpeechQualityFeedback();
  const [recording, setRecording] = useState<boolean>(false);
  const [timeLeft, setTimeLeft] = useState(60*30); // Assuming a 60-second timer
  const [isFlashing, setIsFlashing] = useState(false);

  const handleSubmit = () => {
    getFeedback(code);
    getSpeechFeedback();
    setShowFeedback(true); // Trigger the feedback view
  }

  const handleRun = () => {
    runCode(code);
  }

  const handleKeyDown = (event: KeyboardEvent) => {
    if (event.key === 'Tab') {
      event.preventDefault();
      const target = event.target as HTMLTextAreaElement;
      const selectionStart = target.selectionStart ?? 0;
      const selectionEnd = target.selectionEnd ?? 0;
      const lines = code.split('\n');

      const startLine = code.substring(0, selectionStart).split('\n').length - 1;
      const endLine = code.substring(0, selectionEnd).split('\n').length - 1;

      if (event.shiftKey) {
        // Unindent all highlighted lines
        const newLines = lines.map((line, index) => {
          if (index >= startLine && index <= endLine) {
            if (line.startsWith('\t')) {
              return line.substring(1);
            } else if (line.startsWith('    ')) {
              return line.substring(4);
            }
          }
          return line;
        });

        const newValue = newLines.join('\n');
        setCode(newValue);

        setTimeout(() => {
          target.selectionStart = selectionStart;
          target.selectionEnd = selectionEnd;
        }, 0);
      } else {
        // Indent all highlighted lines
        const newLines = lines.map((line, index) => {
          if (index >= startLine && index <= endLine) {
            return '\t' + line;
          }
          return line;
        });

        const newValue = newLines.join('\n');
        setCode(newValue);

        setTimeout(() => {
          target.selectionStart = selectionStart + 1;
          target.selectionEnd = selectionEnd + 1;
        }, 0);
      }
    }
  };

  if (showFeedback) {
    return (
      <main className="flex min-h-screen flex-col items-center justify-between p-20">
        <div className="flex flex-row w-full gap-4">
          <div className="flex-1 border-2 border-black p-4">
            <h2>Code Quality Feedback</h2>
            <p>{codeQualityOutput}</p>
          </div>
          <div className="flex-1 border-2 border-black p-4">
            <h2>Speech Quality Feedback</h2>
            <p>{speechQualityOutput}</p>
          </div>
        </div>
        <button className="border-2 border-black mt-4" onClick={() => setShowFeedback(false)}>
          Back to Home
        </button>
      </main>
    );
  }

  return (
    <main className="flex min-h-screen flex-col items-center p-20">  
      <div className="flex items-center justify-between w-full">
        <h1 className="text-[#51523B] font-bold text-4xl flex-shrink-0">eager.ai</h1>
        <div className="flex items-center space-x-4">
          <AudioRecorder setRecording={setRecording} recording={recording} handleSubmit={handleSubmit} />
          <button
            className="border-2 border-black pt-1 pb-1 pl-3 pr-3 flex items-center rounded-[10px] bg-[#C8C6C6] text-black"
            onClick={handleSubmit}
          >
            <CloudUpload strokeWidth='2'/>
            <p className="ml-2 font-semibold">Submit</p>
          </button>
          <button
            className="border-2 border-black pt-1 pb-1 pl-3 pr-3 flex items-center rounded-[10px] bg-[#C8C6C6] text-black"
            onClick={handleRun}
          >
            <Running strokeWidth='2'/>
            <p className="ml-2 font-semibold">Run</p>
          </button>
        </div>
        <Timer className="flex-shrink-0" recording={recording} setTimeLeft={setTimeLeft} timeLeft={timeLeft} />
      </div>
      <div className="flex flex-row w-full h-screen gap-16 mt-16">
  <div className="flex-1 h-full">
    <ChatBot code={code} />
  </div>
  <div className="flex flex-col h-full overflow-hidden">
    <div className="flex-1 overflow-auto">
      <CodeEditor code={code} setCode={setCode} handleKeyDown={handleKeyDown} />
    </div>
    <div className="flex-shrink-0 mt-4 overflow-auto">
      <RunCodeOutput output={output} />
    </div>
  </div>
</div>


    </main>
  )
}
