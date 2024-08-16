"use client";

import React, { useState, useEffect } from 'react';
import useChatBot from '../hooks/useChatBot'

interface ChatBoxProps {
  code: string;
}

const ChatBox: React.FC<ChatBoxProps> = ({ code }) => {
  const [questions, setQuestions] = useState<string[]>([]);
  const [replies, setReplies] = useState<string[]>([]);
  const [input, setInput] = useState<string>('Am I using the right data structure?');
  const [disableAskButton, setDisableAskButton] = useState<boolean>(false);
  const { feedback, error, loading, fetchFeedback } = useChatBot();

  useEffect(() => {
    console.log(feedback);
  }, [feedback])
  const handleAsk = () => {
    if (input.trim() === '') return;
    fetchFeedback(code, input);
    setQuestions([...questions, input]);
    setReplies([...replies, '...']);
    setInput('');
  };

  useEffect(() => {
    if (feedback !== '') {
      setReplies((prevReplies) => {
        const newReplies = [...prevReplies];
        newReplies[newReplies.length - 1] = feedback;
        return newReplies;
      });

      if (replies.length > 2) {
        setDisableAskButton(true);
      }
    }
  }, [feedback, replies.length]);

  return (
    <div className="flex flex-col w-full h-full max-h-screen p-2 box-border overflow-hidden">
      <div className="flex-grow overflow-y-auto flex flex-col gap-5 max-h-[calc(100vh-140px)] text-[15px]">
        <div className="self-start bg-lightgrey border-2 border-darkgrey rounded-lg p-2 max-w-[70%]">
          Hello, what is your question?
        </div>
        {questions.map((question, index) => (
          <div key={index} className="flex flex-col gap-5">
            <div className="self-end bg-lightgrey border-2 border-darkgrey rounded-lg p-2 max-w-[70%]">
              {question}
            </div>
            <div className="self-start bg-lightgrey border-2 border-darkgrey rounded-lg p-2 max-w-[70%]">
              {replies[index]}
            </div>
          </div>
        ))}
      </div>
      <div className="flex w-full flex-shrink-0 mt-5">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          className="flex-grow p-2 border-2 border-darkgrey rounded-md"
        />
        <button
          onClick={handleAsk}
          disabled={disableAskButton}
          className={`ml-2 p-2 px-4 rounded-md text-white ${disableAskButton ? 'bg-[#5a5858] cursor-default' : 'bg-black cursor-pointer'}`}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBox;
