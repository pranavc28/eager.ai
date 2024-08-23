"use client";

import React, { useState, useEffect } from 'react';
import useChatBot from '../hooks/useChatBot'
import {ChatLines } from 'iconoir-react';

interface ChatBoxProps {
  code: string;
}

const ChatBox: React.FC<ChatBoxProps> = ({ code }) => {
  const [questions, setQuestions] = useState<string[]>([]);
  const [replies, setReplies] = useState<string[]>([]);
  const [input, setInput] = useState<string>('');
  const [disableAskButton, setDisableAskButton] = useState<boolean>(false);
  const { feedback, error, loading, fetchFeedback } = useChatBot();

  useEffect(() => {
    console.log(feedback);
  }, [feedback]);
  
  const handleAsk = () => {
    if (input.trim() === '') return;
    fetchFeedback(code, input);
    setQuestions([...questions, input]);
    setReplies((prevReplies) => [...prevReplies, '...']);
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
  }, [feedback]);
  

  return (
    <div className="flex flex-col w-full h-full max-h-screen box-border overflow-hidden bg-white rounded-2xl">
    <div className="flex items-center w-full h-14 rounded-t-2xl bg-[#C8C6C6] p-2">
      <ChatLines className="ml-4" height={20} width={20} strokeWidth={2} />
      <p className="ml-2 font-semibold text-md">Ask Chris ...</p>
    </div>
    <div className="flex-grow overflow-y-auto pl-6 pr-6 mt-6">
      <div className="flex flex-col gap-5 text-4">
        <div className="self-start border-2 border-darkgrey rounded-lg p-2 max-w-[70%] bg-[#C8C6C6]">
          Hello, what is your question?
        </div>
        {questions.map((question, index) => (
          <div key={index} className="flex flex-col gap-5">
            <div className="self-end bg-lightgrey border-2 border-darkgrey rounded-lg p-2 max-w-[70%] bg-[#C8C6C6]">
              {question}
            </div>
            <div className="self-start bg-lightgrey border-2 border-darkgrey rounded-lg p-2 max-w-[70%] bg-[#C8C6C6]">
              {replies[index]}
            </div>
          </div>
        ))}
      </div>
    </div>

    <div className="flex w-full p-6">
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
        className={`ml-6 p-2 px-6 rounded-md text-white ${disableAskButton ? 'bg-[#5a5858] cursor-default' : 'bg-black cursor-pointer'}`}
      >
        Send
      </button>
    </div>
  </div>

  );
};

export default ChatBox;
