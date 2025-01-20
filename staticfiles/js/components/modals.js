export function initModal() {
    const modal = document.getElementById('commentModal');
    const modalContent = document.getElementById('modalBodyContent');
    const spanClose = document.querySelector('.close');
  
    function showModal(content) {
      modalContent.innerHTML = content;
      modal.style.display = 'block';
      document.body.style.overflow = 'hidden';
    }
  
    function closeModal() {
      modal.style.display = 'none';
      document.body.style.overflow = 'auto';
    }
  
    // Event listeners
    spanClose.onclick = closeModal;
    window.onclick = (event) => {
      if (event.target === modal) {
        closeModal();
      }
    };
  
    return {
      show: showModal,
      close: closeModal
    };
  }