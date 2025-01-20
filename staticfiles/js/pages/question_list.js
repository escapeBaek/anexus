import { startTimer, stopTimer } from "../components/timer.js";
import { initModal } from "../components/modal.js";
import { toggleBookmark } from "../components/bookmark.js";

function endExam() {
  stopTimer();

  const questionBlocks = document.querySelectorAll(".question-card");
  let numCorrect = 0,
    numIncorrect = 0,
    numUnanswered = 0,
    numNoanswer = 0;
  let detailedResults = [];

  questionBlocks.forEach((block) => {
    const questionText = block
      .querySelector(".question-text")
      .textContent.trim();
    const correctOptionKey = block.dataset.correctOption || "default";

    // Get all option texts from data attributes
    const optionTexts = {};
    for (let i = 1; i <= 5; i++) {
      const key = `option${i}`;
      if (block.dataset[key]) {
        optionTexts[key] = block.dataset[key];
      }
    }

    // Determine correct answer text
    let correctAnswerText = optionTexts[correctOptionKey] || correctOptionKey;

    // Get selected answer
    const selectedRadio = block.querySelector('input[type="radio"]:checked');
    const selectedAnswerText = selectedRadio ? selectedRadio.value : "";

    // Determine result type
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
      result: resultType,
    });
  });

  // Prepare the data
  const resultData = {
    exam_id: document.querySelector('input[name="exam_id"]')?.value || null,
    num_correct: numCorrect,
    num_incorrect: numIncorrect,
    num_unanswered: numUnanswered,
    num_noanswer: numNoanswer,
    detailed_results: detailedResults,
  };

  submitExamResults(resultData);
}

function submitExamResults(resultData) {
  const csrfToken = document.querySelector(
    'input[name="csrfmiddlewaretoken"]'
  ).value;

  fetch("/exam/save_exam_results/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(resultData),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data.status === "ok") {
        window.location.href = `/exam/exam_results/?result_id=${data.result_id}`;
      } else {
        console.error("Error:", data);
        alert("Error saving results. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("Error saving results. Please try again.");
    });
}

function toggleAnswer(id) {
  const element = document.getElementById(id);
  if (element.classList.contains("hidden")) {
    element.classList.remove("hidden");
    element.style.animation = "fadeIn 0.3s ease-out";
  } else {
    element.classList.add("hidden");
  }
}

function toggleVisibility(id) {
  const element = document.getElementById(id);
  if (element) {
    modal.show(element.innerHTML);
  }
}

// Initialize page
document.addEventListener("DOMContentLoaded", function () {
  const modal = initModal();

  document
    .getElementById("start-exam-btn")
    .addEventListener("click", function () {
      const duration = parseInt(
        document.getElementById("set-timer-input").value,
        10
      );
      if (!isNaN(duration) && duration > 0) {
        startTimer(duration);
      } else {
        showNotification("Please enter a valid duration in minutes", "warning");
      }
    });

  document
    .getElementById("end-exam-btn")
    .addEventListener("click", function () {
      if (confirm("Are you sure you want to end the exam?")) {
        endExam();
      }
    });

  // Expose necessary functions to global scope for HTML event handlers
  window.toggleAnswer = toggleAnswer;
  window.toggleVisibility = toggleVisibility;
  window.toggleBookmark = toggleBookmark;
});
