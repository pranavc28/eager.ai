import React from 'react';
import { InputOutput } from 'iconoir-react';

interface RunCodeOutputProps {
    output: string;
}

const RunCodeOutput: React.FC<RunCodeOutputProps> = ({ output }) => {
  return (
    <div className="flex flex-col w-full text-center">
      <div className="flex items-center w-full h-10 rounded-t-2xl bg-[#C8C6C6] p-2">
        <InputOutput className="ml-4" height={20} width={20} strokeWidth={2} />
      <p className="ml-2 font-semibold text-md">Output</p>
    </div>
      <pre className="p-[8vh] bg-gray-100 text-sm text-left font-mono border border-gray-300 rounded-b-2xl">
        {output}
      </pre>
    </div>
  );
};

export default RunCodeOutput;
