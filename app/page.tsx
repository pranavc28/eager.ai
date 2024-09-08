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
import { DotArrowLeft, CodeBrackets, Microphone } from 'iconoir-react';
import useFetch from './hooks/useFetch';
import { TailSpin } from "react-loader-spinner";
import { useUser } from '@clerk/nextjs'

interface QuestionOutput {
  title: string;
}

export default function Home() {
  const { isLoaded, isSignedIn, user } = useUser()
  const [code, setCode] = useState('');
  const { output, error, loading, runCode } = useRunCode();
  const { data: questionOutput } = useFetch('http://127.0.0.1:5328/api/question') as { data: QuestionOutput };
  const [showFeedback, setShowFeedback] = useState(false);
  const {output: codeQualityOutput, error: codeQualityError, loading: codeQualityLoading, getFeedback, setOutput: setCodeQualityOutput } = useCodeQualityFeedback();
  const {output: speechQualityOutput, error: speechQualityError, loading: speechQualityLoading, getSpeechFeedback, setOutput: setSpeechQualityOutput } = useSpeechQualityFeedback();
  const [recording, setRecording] = useState<boolean>(false);
  const [timeLeft, setTimeLeft] = useState(60*30); // Assuming a 60-second timer

  const isLoading = !codeQualityOutput && !speechQualityOutput;

  useEffect(() => {
    console.log(user);
  }, [isSignedIn, user])

  const handleSubmit = () => {
    getFeedback(code);
    getSpeechFeedback();
    setShowFeedback(true); // Trigger the feedback view
  }

  const handleBack = () => {
    setSpeechQualityOutput('');
    setCodeQualityOutput('');
    setShowFeedback(false); // Trigger the feedback view
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
      <main className="flex min-h-screen flex-col items-center pt-20 pr-20 pl-20 pb-10">
        <div className="flex items-center justify-between w-full">
          <h1 className="text-[#51523B] font-bold text-4xl flex-shrink-0">eager.ai</h1>
          <button className="flex flex-row ml-6 p-2 px-6 rounded-md text-white bg-black cursor-pointer mt-2" onClick={handleBack}>
            <DotArrowLeft className="mr-3" strokeWidth={2}/>
            Back to Home
          </button>
          <h1 className="flex-shrink-0 text-[#51523B] font-bold text-2xl mr-4">/feedback</h1>
      </div>
      {isLoading ? 
        <div
          className="fixed inset-0 flex items-center justify-center"
        >
          <div style={{ width: "200px", height: "200px", display: "flex", alignItems: "center", justifyContent: "center", color: "black" }}>
            <TailSpin color={"#000000"}/>
          </div>
        </div> : 
        <div className="flex flex-row w-full space-x-4 mt-6 items-start">
          <div className="flex flex-col w-1/2 min-h-0">
            <div className="flex items-center w-full h-10 rounded-t-2xl bg-[#C8C6C6] p-2">
              <CodeBrackets className="ml-4" height={20} width={20} strokeWidth={2} />
              <p className="ml-2 font-semibold text-md">Code Quality Feedback</p>
            </div>
            <pre className="p-[8vh] bg-gray-100 text-sm text-left font-mono border border-gray-300 rounded-b-2xl whitespace-pre-wrap">
              {codeQualityOutput}
            </pre>
          </div>
          <div className="flex flex-col w-1/2 min-h-0">
            <div className="flex items-center w-full h-10 rounded-t-2xl bg-[#C8C6C6] p-2">
              <Microphone className="ml-4" height={20} width={20} strokeWidth={2} />
              <p className="ml-2 font-semibold text-md">Speech Quality Feedback</p>
            </div>
            <pre className="p-[8vh] bg-gray-100 text-sm text-left font-mono border border-gray-300 rounded-b-2xl whitespace-pre-wrap">
              {speechQualityOutput}
            </pre>
          </div>
        </div>
      }
      </main>
    );
  }

  return (
    <main className="flex min-h-screen flex-col items-center pt-14 pl-20 pr-20">  
      <div className="flex items-center justify-between w-full">
        <h1 className="text-[#51523B] font-bold text-4xl flex-shrink-0">eager.ai</h1>
        <div className="flex items-center space-x-4">
          <AudioRecorder setRecording={setRecording} recording={recording} />
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
      <div className="flex flex-row w-full h-[70vh] gap-16 mt-10">
        <div className="h-full w-[60%]">
          <ChatBot code={code} />
        </div>
        <div className="w-[40vw] flex flex-col h-full overflow-hidden">
        <div className="flex-grow overflow-auto">
          <CodeEditor code={code} setCode={setCode} handleKeyDown={handleKeyDown} />
        </div>
        <div className="flex-shrink-0 mt-4 overflow-auto">
          <RunCodeOutput output={output} />
        </div>
      </div>
      </div>
      <div className="flex items-center justify-between w-full">
        <h1 className="text-black font-bold text-2xl ml-4 mt-8 flex-shrink-0">Question - {questionOutput?.title}</h1>
      </div>
    </main>
  )
}
