import React, { ChangeEvent, KeyboardEvent } from 'react';
import { Code } from 'iconoir-react';

interface CodeEditorProps {
    code: string;
    setCode: (code: string) => void;
    handleKeyDown?: (event: KeyboardEvent) => void;
}
  
const CodeEditor: React.FC<CodeEditorProps> = ({ code, setCode, handleKeyDown }) => {
    const handleChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
      const target = event.target as HTMLTextAreaElement;
      setCode(target.value);
    };
  
    return (
      <div className="code-editor-container w-full mx-auto text-center">
        <div className="flex items-center w-full h-10 rounded-t-2xl bg-[#C8C6C6] p-2">
        <Code className="ml-4" height={20} width={20} strokeWidth={2} />
      <p className="ml-2 font-semibold text-md">Code</p>
      </div>
      <textarea
        className="code-textarea w-full p-2 text-sm box-border overflow-y-auto font-mono h-[40vh] resize-none rounded-b-2xl"
        placeholder="Type your answer here"
        value={code}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
        />
      </div>
    );
};
  
export default CodeEditor;
