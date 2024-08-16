"use client";

import { useEffect } from "react";
import useFetch from "../hooks/useFetch"

type example = {
    input: string;
    output: string;
    explanation: string;
};

interface QuestionData {
    question: string;
    examples: example[];
}


export default function Questions() {
 // Split the question by newline characters to display them as separate lines
 const { data, loading, error } = useFetch<QuestionData>("/api/question");
 const questionLines = (data && data?.question?.split('\n')) ?? "";

 useEffect(() => {
    console.log(data)
 }, [data])

 return (
   <div className="question-container">
     <div className="question">
       <h2 className="question-title">Two Sum</h2>
       {questionLines && questionLines?.map((line: string, index: number) => (
         <p key={index}>{line}</p>
       ))}
     </div>
     {data && data.examples.map((example: example, index: number) => (
       <div key={index} className="example">
         <h3>Example {index + 1}</h3>
         <div className="example-details">
           <p><strong>Input:</strong> {example.input}</p>
           <p><strong>Output:</strong> {example.output}</p>
           {example.explanation && <p><strong>Explanation:</strong> {example.explanation}</p>}
         </div>
       </div>
     ))}
   </div>
 );   
}