import React from 'react';

interface RunCodeOutputProps {
    runCode: (code: string) => void;
    output: string;
    code: string;
}

const RunCodeOutput: React.FC<RunCodeOutputProps> = ({ runCode, output, code }) => {
    const handleClick = () => {
        runCode(code);
    }
  return (
    <div className="w-full mt-8 text-center">
      <button onClick={handleClick} className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Run Code
      </button>
      <pre className="w-11/12 p-4 mt-4 mx-auto bg-gray-100 text-sm text-left font-mono whitespace-pre-wrap border border-gray-300 rounded">
        {output}
      </pre>
    </div>
  );
};

export default RunCodeOutput;
