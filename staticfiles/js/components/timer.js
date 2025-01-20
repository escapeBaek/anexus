let timerInterval;
let timeRemaining;

export function startTimer(duration) {
  timeRemaining = duration * 60;
  document.getElementById('start-exam-btn').style.display = 'none';
  document.getElementById('end-exam-btn').style.display = 'inline-block';
  document.getElementById('set-timer-input').disabled = true;

  // 고정된 타이머 요소 생성
  const fixedTimer = document.createElement('div');
  fixedTimer.className = 'fixed-timer';
  fixedTimer.innerHTML = '<div id="floating-timer-display" class="timer-display">00:00</div>';
  document.body.appendChild(fixedTimer);

  timerInterval = setInterval(function() {
    const minutes = Math.floor(timeRemaining / 60);
    const seconds = timeRemaining % 60;
    const displayTime =
      (minutes < 10 ? '0' : '') + minutes + ':' +
      (seconds < 10 ? '0' : '') + seconds;

    // 모든 타이머 디스플레이 업데이트
    document.getElementById('timer-display').textContent = displayTime;
    document.getElementById('floating-timer-display').textContent = displayTime;

    if (timeRemaining <= 300) { // 5분 남음
      fixedTimer.style.background = 'linear-gradient(135deg, #ff6b6b, #ff8e8e)';
      fixedTimer.style.animation = 'pulse 1s infinite';
    }

    if (timeRemaining <= 0) {
      clearInterval(timerInterval);
      endExam();
      document.body.removeChild(fixedTimer);
    }
    timeRemaining--;
  }, 1000);
}

export function stopTimer() {
  clearInterval(timerInterval);
  const fixedTimer = document.querySelector('.fixed-timer');
  if (fixedTimer) {
    document.body.removeChild(fixedTimer);
  }
}