let timerInterval;
let timeRemaining;

function startTimer(duration) {
  timeRemaining = duration * 60;
  timerInterval = setInterval(function() {
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;
    document.getElementById('timer-display').textContent =
      (minutes < 10 ? '0' : '') + minutes + ':' + (seconds < 10 ? '0' : '') + seconds;

    if (timeRemaining <= 0) {
      clearInterval(timerInterval);
      endExam();
    }
    timeRemaining--;
  }, 1000);
}

function endExam() {
  clearInterval(timerInterval);

  const questionBlocks = document.querySelectorAll('.question-block');
  let numCorrect = 0, numIncorrect = 0, numUnanswered = 0, numNoanswer = 0;
  let detailedResults = [];

  questionBlocks.forEach((block) => {
    // 문제 텍스트
    let questionText = "";
    const questionTextBox = block.querySelector('.question-text-box');
    if (questionTextBox) {
      questionText = questionTextBox.textContent.trim();
    } else {
      const questionNode = block.querySelector('.question-text');
      questionText = questionNode ? questionNode.textContent.trim() : "";
    }

    // data-* 에서 정답 key 및 보기 텍스트 가져오기
    const correctOptionKey = block.dataset.correctOption || "default";
    const option1Text = block.dataset.option1 || "";
    const option2Text = block.dataset.option2 || "";
    const option3Text = block.dataset.option3 || "";
    const option4Text = block.dataset.option4 || "";
    const option5Text = block.dataset.option5 || "";

    // Correct Answer 텍스트 결정 (Fallback 로직)
    let correctAnswerText = "";
    if (correctOptionKey === "option1") correctAnswerText = option1Text;
    else if (correctOptionKey === "option2") correctAnswerText = option2Text;
    else if (correctOptionKey === "option3") correctAnswerText = option3Text;
    else if (correctOptionKey === "option4") correctAnswerText = option4Text;
    else if (correctOptionKey === "option5") correctAnswerText = option5Text;
    else if (correctOptionKey === "default") {
      // noanswer
      correctAnswerText = "";
    } else {
      // fallback: correctOptionKey 자체가 정답
      correctAnswerText = correctOptionKey;
    }

    // 사용자가 선택한 답변
    let selectedAnswerText = "";
    block.querySelectorAll('input[type="radio"]').forEach((opt) => {
      if (opt.checked) {
        selectedAnswerText = opt.value.trim();
      }
    });

    // 결과 분기
    let resultType;
    if (correctOptionKey === "default") {
      numNoanswer++;
      resultType = "noanswer";
    } else if (!selectedAnswerText) {
      numUnanswered++;
      resultType = "unanswered";
    } else if (selectedAnswerText === correctAnswerText) {
      numCorrect++;
      resultType = "correct";
    } else {
      numIncorrect++;
      resultType = "incorrect";
    }

    detailedResults.push({
      question: questionText,
      selected_answer: selectedAnswerText,
      correct_answer: correctAnswerText,
      result: resultType
    });
  });

  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  fetch("{% url 'save_exam_results' %}", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({
      exam_id: {{ exam.id }},
      num_correct: numCorrect,
      num_incorrect: numIncorrect,
      num_unanswered: numUnanswered,
      num_noanswer: numNoanswer,
      detailed_results: detailedResults,
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 'ok') {
      window.location.href = `{% url 'exam_results' %}?result_id=${data.result_id}`;
    } else {
      alert('An error occurred while saving the results.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

// 모달 로직
const modal = document.getElementById('commentModal');
const modalContent = document.getElementById('modalBodyContent');
const spanClose = document.querySelector('.close');

function showModal(content) {
  modalContent.innerHTML = content;
  modal.style.display = 'block';
}

spanClose.addEventListener('click', () => {
  modal.style.display = 'none';
});
window.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});

// Toggle answer
function toggleAnswer(id) {
  const element = document.getElementById(id);
  element.classList.toggle("hidden");
}

// Toggle comment
function toggleVisibility(id) {
  const element = document.getElementById(id);
  if (element) {
    showModal(element.innerHTML);
  }
}

// Start & End Exam
document.getElementById('start-exam-btn').addEventListener('click', function() {
  const duration = parseInt(document.getElementById('set-timer-input').value, 10);
  if (!isNaN(duration) && duration > 0) {
    startTimer(duration);
    document.getElementById('start-exam-btn').style.display = 'none';
    document.getElementById('end-exam-btn').style.display = 'inline-block';
  } else {
    alert('Please enter a valid duration in minutes.');
  }
});

document.getElementById('end-exam-btn').addEventListener('click', function() {
  endExam();
});