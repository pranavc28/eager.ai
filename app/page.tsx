"use client";

import React, { useState, useEffect, KeyboardEvent } from 'react';
import Questions from "./src/questions"
import CodeEditor from "./src/codeEditor"
import ChatBot from "./src/chatBot"
import useRunCode from './hooks/useRunCode';
import RunCodeOutput from './src/runCodeOutput';
import useCodeQualityFeedback from './hooks/useCodeQualityFeedback';
import AudioRecorder from './src/audioRecorder';

export default function Home() {
  const [code, setCode] = useState('');
  const { output, error, loading, runCode } = useRunCode();
  const {output: codeQualityOutput, error: codeQualityError, loading: codeQualityLoading, getFeedback } = useCodeQualityFeedback();

  const handleSubmit = () => {
    getFeedback(code);
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

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">  
    <AudioRecorder />
    <button className="border-2 border-black" onClick={handleSubmit}> Submit </button>
    <div className="flex flex-row w-full gap-4">
    <div className="flex-1">
      <ChatBot code={code} />
    </div>
    <div className="main-container">
  <div className="columns flex">
    <div className="flex-1">
      <Questions />
    </div>
    <div className="flex-1">
      <CodeEditor code={code} setCode={setCode} handleKeyDown={handleKeyDown} />
    </div>
  </div>
  <div className="full-width mt-4">
    <RunCodeOutput
      output={output}
      runCode={runCode}
      code={code}
    />
  </div>
</div>
  </div>
    </main>
  )
}
