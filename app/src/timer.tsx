import React, { useState, useEffect } from 'react';

interface TimerProps {
    recording: boolean;
    setTimeLeft: any;
    timeLeft: number;
    className: string;
}

const Timer: React.FC<TimerProps> = ({recording, setTimeLeft, timeLeft, className}) => {

    function convertSecondsToTimeFormat(seconds: number) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        
        // Format the minutes and seconds to ensure they are always two digits
        const minutesFormatted = minutes.toString().padStart(2, '0');
        const secondsFormatted = remainingSeconds.toString().padStart(2, '0');
        
        return `${minutesFormatted}:${secondsFormatted}`;
      }

    useEffect(() => {
        let timerInterval: NodeJS.Timeout | null = null;
        
        if (recording) {
            // Start the countdown
            timerInterval = setInterval(() => {
            setTimeLeft((prevTime: number) => {
                if (prevTime > 0) return prevTime - 1;
                clearInterval(timerInterval!);
                return 0;
            });
            }, 1000);
        }
        
        return () => {
            if (timerInterval) clearInterval(timerInterval);
        };
    }, [recording]);

  return (
    <div className={className}>
    <p className="mt-2 text-xl mr-4 font-semibold">{convertSecondsToTimeFormat(timeLeft)}</p>
    </div>
  );
};

export default Timer;
