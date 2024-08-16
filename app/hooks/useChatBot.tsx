import { useState, useEffect } from 'react';

const useFetchFeedback = () => {
    const [feedback, setFeedback] = useState('');
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    const fetchFeedback = (code: string, question: string) => {
        fetch('http://127.0.0.1:5328/api/feedback', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code,
                question,
            }),
        })
        .then(response => {
            console.log(response);
            return response.json();
        })
        .then(data => {
            console.log(data);
            setFeedback(data.feedback);  // Assuming you have a setFeedback state function
        })
        .catch(e => {
            setError(e.message);  // Assuming you have a setError state function
            console.error(e);
        });
    };

    return {
        feedback,
        error,
        loading,
        fetchFeedback
    }
};

export default useFetchFeedback;
