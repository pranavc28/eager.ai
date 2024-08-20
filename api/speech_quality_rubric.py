communication_content = """Rate the interviewee based on the rubric attached put of 4 points. Give the exact value, then an explanation.:
    Please carefully read through it and assign a communication score to the candidate based on the following rubric:

    Communication Rubric:

    - 4 Points: The candidate communicated with perfect clarity throughout the interview. The interviewer had no difficulty understanding the candidate's thought process, the trade-offs of different approaches, and how the candidate approached the problem. The candidate's answers were well-organized and succinct.
    
    - 3 Points: The candidate communicated adequately throughout the interview. The interviewer may have needed to ask follow-up questions about the candidate's thought process, approach, etc., but overall, communication was clear.

    - 2 Points: The candidate did not communicate very well or clearly throughout the interview. The interviewer may have had difficulty following the candidate's thought process. The candidate's answers may have been disorganized, or they may have jumped into coding without properly explaining themselves.

    - 1 Point: The candidate could not communicate with any clarity. The interviewer had extreme difficulty following or understanding the candidate's thought process or approach. The candidate may have stayed silent for much of the interview, even when directly addressed. The candidiate clearly did not know how to solve the problem, or said fewer than 10 sentences.

    After assigning a score, please provide a brief explanation for your rating.
"""

algorithms_content = """Rate the interviewee based on the rubric attached put of 4 points. Give the exact value, then an explanation:

    The solution to the problem should be: 'The Python code iterates through a list of numbers (`nums`) to find two distinct elements that sum up to a given `target`, using a dictionary (`digs`) to store the indices of the elements. If such a pair is found, it returns their indices; otherwise, it returns an empty list.'

    Please carefully read through the transcript and and assign a algorithms score to the candidate based on the following rubric and if it resonates with the solution:

    Algorithms Rubric:

    - 4 Points: The candidate effortlessly illustrated several solutions along with their drawbacks. The candidate selected the most optimal algorithm to solve the problem, and in doing so, clearly displayed a deep understanding of algorithms.
    
    - 3 Points: The candidate solved the problem but not optimally. The candidate demonstrated some or adequate knowledge of algorithms.

    - 2 Points: The candidate chose a sub-optimal algorithm for their solution. The candidate may have struggled with developing their solution, requiring some guidance from the interviewer. The candidate displayed some misunderstanding regarding algorithms and data structures.

    - 1 Point: The candidate could not solve the problem. The candidate demonstrated little to no understanding of algorithms and data structures.

    After assigning a score, please provide a brief explanation for your rating.
"""

problem_solving_content = """Rate the interviewee based on the rubric attached put of 4 points. Give the exact value, then an explanation.:
    Please carefully read through it and assign a problem solving score to the candidate based on the following rubric:

    Problem Solving Rubric:

    - 4 Points: The candidate had no trouble finding a well-thought-out and accurate solution to the problem. The candidate did so with enough time to discuss trade-offs, related problems, and alternatives while asking the interviewer clarifying questions. They have also definitely mentioned the time and space complexity of the solution.
    
    - 3 Points: The candidate developed a working and accurate solution but did not have much time to discuss sub-problems, alternatives, or trade-offs.

    - 2 Points: The candidate showed some adequate problem-solving skills in their solution. The candidate's approach may have been unorganized or arbitrary at some points. The candidate did not ask clarifying questions or touch on additional information regarding the problem.

    - 1 Point: The candidate's problem-solving skills were poor. The candidate may have been unable to solve the problem or did so without much thought. Their approach was highly unorganized, random, and ineffective at solving the problem at hand.
"""

speech_rubric_content = [communication_content, algorithms_content, problem_solving_content]