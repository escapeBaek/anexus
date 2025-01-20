// timer.js
let timerInterval;
let timeRemaining;
let examInProgress = false;

export function startTimer(duration) {
  if (examInProgress) return;
  
  examInProgress = true;
  timeRemaining = duration * 60; // Convert minutes to seconds
  
  // Update UI elements
  const startButton = document.getElementById('start-exam-btn');
  const endButton = document.getElementById('end-exam-btn');
  const timerInput = document.getElementById('set-timer-input');
  
  if (startButton) startButton.style.display = 'none';
  if (endButton) endButton.style.display = 'inline-block';
  if (timerInput) timerInput.disabled = true;

  // Update timer display
  updateTimerDisplay();

  timerInterval = setInterval(() => {
    timeRemaining--;
    updateTimerDisplay();

    if (timeRemaining <= 0) {
      stopTimer();
      handleExamEnd();
    }
  }, 1000);
}

export function stopTimer() {
  clearInterval(timerInterval);
  examInProgress = false;
  
  // Reset UI elements
  const startButton = document.getElementById('start-exam-btn');
  const endButton = document.getElementById('end-exam-btn');
  const timerInput = document.getElementById('set-timer-input');
  
  if (startButton) startButton.style.display = 'inline-block';
  if (endButton) endButton.style.display = 'none';
  if (timerInput) timerInput.disabled = false;
}

function updateTimerDisplay() {
  const minutes = Math.floor(timeRemaining / 60);
  const seconds = timeRemaining % 60;
  const display = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  
  const timerDisplay = document.getElementById('timer-display');
  if (timerDisplay) {
    timerDisplay.textContent = display;
  }
}

function handleExamEnd() {
  const form = document.getElementById('exam-form');
  if (!form) return;

  const questions = form.querySelectorAll('.question-card');
  let numCorrect = 0;
  let numIncorrect = 0;
  let numUnanswered = 0;
  const detailedResults = [];

  questions.forEach(question => {
    const selectedAnswer = question.querySelector('input[type="radio"]:checked');
    const correctOption = question.dataset.correctOption;
    const questionText = question.querySelector('.question-text').textContent;

    let result = {
      question: questionText,
      selected_answer: selectedAnswer ? selectedAnswer.value : '',
      correct_answer: question.dataset[`option${correctOption}`],
      result: 'unanswered'
    };

    if (selectedAnswer) {
      if (selectedAnswer.value === question.dataset[`option${correctOption}`]) {
        numCorrect++;
        result.result = 'correct';
      } else {
        numIncorrect++;
        result.result = 'incorrect';
      }
    } else {
      numUnanswered++;
    }

    detailedResults.push(result);
  });

  const resultData = {
    exam_id: new URLSearchParams(window.location.search).get('exam_id'),
    num_correct: numCorrect,
    num_incorrect: numIncorrect,
    num_unanswered: numUnanswered,
    detailed_results: detailedResults
  };

  submitResults(resultData);
}

function submitResults(resultData) {
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  fetch('/exam/save_exam_results/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    },
    body: JSON.stringify(resultData)
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'ok') {
      window.location.href = `/exam/exam_results/?result_id=${data.result_id}`;
    } else {
      alert('Error saving results. Please try again.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('Error saving results. Please try again.');
  });
}

export { handleExamEnd };