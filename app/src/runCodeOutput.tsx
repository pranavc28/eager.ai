import React from 'react';

interface RunCodeOutputProps {
    output: string;
}

const RunCodeOutput: React.FC<RunCodeOutputProps> = ({ output }) => {
  return (
    <div className="w-full mt-8 text-center">
      <pre className="w-11/12 p-4 mt-4 mx-auto bg-gray-100 text-sm text-left font-mono whitespace-pre-wrap border border-gray-300 rounded">
        {output}
      </pre>
    </div>
  );
};

export default RunCodeOutput;
