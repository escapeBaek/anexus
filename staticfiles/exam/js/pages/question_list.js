// question_list.js
import { startTimer, stopTimer, handleExamEnd } from './timer.js';

document.addEventListener('DOMContentLoaded', function() {
  const startExamBtn = document.getElementById('start-exam-btn');
  const endExamBtn = document.getElementById('end-exam-btn');

  if (startExamBtn) {
    startExamBtn.addEventListener('click', function() {
      const duration = parseInt(document.getElementById('set-timer-input').value, 10);
      if (!isNaN(duration) && duration > 0) {
        startTimer(duration);
      } else {
        alert('Please enter a valid duration in minutes');
      }
    });
  }

  if (endExamBtn) {
    endExamBtn.addEventListener('click', function() {
      if (confirm('Are you sure you want to end the exam?')) {
        stopTimer();
        handleExamEnd();
      }
    });
  }
});

// Functions for question interactions
function toggleAnswer(id) {
  const element = document.getElementById(id);
  if (element.classList.contains('hidden')) {
    element.classList.remove('hidden');
    element.style.animation = 'fadeIn 0.3s ease-out';
  } else {
    element.classList.add('hidden');
  }
}

function toggleVisibility(id) {
  const element = document.getElementById(id);
  if (element && modal) {
    modal.show(element.innerHTML);
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializePage);

// Export functions for global use
window.toggleAnswer = toggleAnswer;
window.toggleVisibility = toggleVisibility;