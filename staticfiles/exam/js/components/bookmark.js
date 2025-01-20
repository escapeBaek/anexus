export function initBookmark() {
  // Add click handlers to all bookmark buttons
  document.querySelectorAll('.bookmark-button').forEach(button => {
      button.addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          const questionId = this.dataset.questionId;
          toggleBookmark(questionId, this);
      });
  });
}

function toggleBookmark(questionId, button) {
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

  fetch(`/exam/bookmark/${questionId}/`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
      },
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      return response.json();
  })
  .then(data => {
      if (data.status === 'ok') {
          // Toggle the bookmarked class
          button.classList.toggle('bookmarked');
          
          // Toggle the star icon fill
          const starIcon = button.querySelector('i.fas.fa-star');
          if (data.is_bookmarked) {
              starIcon.style.color = '#ffd700';  // Gold color when bookmarked
          } else {
              starIcon.style.color = '#ddd';     // Default color when not bookmarked
          }
      } else {
          console.error('Error toggling bookmark:', data.message);
      }
  })
  .catch(error => {
      console.error('Error:', error);
  });
}