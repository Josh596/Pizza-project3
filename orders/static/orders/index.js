document.addEventListener('DOMContentLoaded', () =>{
    
    
    
    //registering the modals and constant variables
    const modal = document.querySelector('.modals');
    const closeButton = document.querySelector('.close-button')


    //For displaying the modals
    function toggleModal() {
        modal.classList.toggle("show-modal");
    }

    function windowOnClick(event) {
        if (event.target === modal) {
            toggleModal();
        }
    }

    document.querySelectorAll('.cards').forEach(card =>{
        card.onclick = toggleModal
    })

    closeButton.addEventListener("click", toggleModal);
    window.addEventListener("click", windowOnClick);

























})