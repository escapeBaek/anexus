export function toggleBookmark(questionId, button) {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  
    fetch(`/exam/bookmark/${questionId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'ok') {
        if (data.is_bookmarked) {
          button.classList.add('bookmarked');
        } else {
          button.classList.remove('bookmarked');
        }
      } else {
        alert('Error toggling bookmark.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Error toggling bookmark.');
    });
  }