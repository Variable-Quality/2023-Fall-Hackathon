import React, { useState } from 'react';

class Question {
  constructor(text, answers) {
    this.text = text;
    this.answers = answers;
  }
}

class Answer {
  constructor(text, scoreChanges) {
    this.text = text;
    this.scoreChanges = scoreChanges;
  }
}

function Questionnaire() {
  const [scores, setScores] = useState({
    score1: 0,
    score2: 0,
  });

  const questions = [
    new Question('Question 1: I enjoy learning new things.', [
      new Answer('Strongly Disagree', { score1: -2, score2: 1 }),
      new Answer('Disagree', { score1: -1, score2: 1 }),
      new Answer('Neutral', { score1: 0, score2: 0 }),
      new Answer('Agree', { score1: 1, score2: 2 }),
      new Answer('Strongly Agree', { score1: 2, score2: 2 }),
    ]),
    new Question('Question 2: I feel confident in my abilities.', [
      new Answer('Strongly Disagree', { score1: -1, score2: -2 }),
      new Answer('Disagree', { score1: 0, score2: -1 }),
      new Answer('Neutral', { score1: 0, score2: 0 }),
      new Answer('Agree', { score1: 1, score2: 1 }),
      new Answer('Strongly Agree', { score1: 2, score2: 2 }),
    ]),
    // Add more questions here
  ];

  const handleAnswer = (questionIndex, answerIndex) => {
    const selectedAnswer = questions[questionIndex].answers[answerIndex];
    const updatedScores = { ...scores };

    for (const score in selectedAnswer.scoreChanges) {
      updatedScores[score] += selectedAnswer.scoreChanges[score];
    }

    setScores(updatedScores);
  };

  return (
    <div>
      <h1>Questionnaire</h1>
      <div>
        {questions.map((question, questionIndex) => (
          <div key={questionIndex}>
            <p>{question.text}</p>
            <div>
              {question.answers.map((answer, answerIndex) => (
                <button
                  key={answerIndex}
                  onClick={() => handleAnswer(questionIndex, answerIndex)}
                >
                  {answer.text}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>
      <p>Scores:</p>
      <ul>
        {Object.keys(scores).map((scoreKey) => (
          <li key={scoreKey}>
            {scoreKey}: {scores[scoreKey]}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Questionnaire;
