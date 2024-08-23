import { useState, useEffect } from 'react';

const useSpeechQualityFeedback = () => {
    const [output, setOutput] = useState<string>('');
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const getSpeechFeedback = () => {
        setLoading(true);
        fetch('http://127.0.0.1:5328/api/speech_quality_feedback', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        }).then(response => {
            return response.json();
        })
        .then(data => {
            console.log(data);
            setOutput(data.rating);  // Assuming you have a setFeedback state function
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
        getSpeechFeedback,
        setOutput,
    }
};

export default useSpeechQualityFeedback;
