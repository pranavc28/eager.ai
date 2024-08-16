import React, { ChangeEvent, KeyboardEvent } from 'react';

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
        <textarea
          className="code-textarea w-full p-2 text-sm box-border overflow-auto resize-y font-mono"
          placeholder="Enter your code here"
          value={code}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          rows={10}
        />
      </div>
    );
};
  
export default CodeEditor;
