import { useState, useEffect } from 'react';

const useRunCode = () => {
    const [output, setOutput] = useState<string>('');
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const runCode = (code: string) => {
        console.log(code);
        setLoading(true);
        fetch('http://127.0.0.1:5328/api/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            code
        }),
        }).then(response => {
        return response.json();
        })
        .then(data => {
            console.log(data);
            setOutput(data.output);  // Assuming you have a setFeedback state function
            setLoading(false);
        })
        .catch((error) => {
        console.log(error);
        setError(error);
        setLoading(false);
        });
    };

    return {
        output,
        error,
        loading,
        runCode
    }
};

export default useRunCode;
