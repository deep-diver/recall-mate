function hide_chat() {
    const element1 = document.querySelector('.hidden_chat_container');
    const element2 = document.querySelector('.hidden_chat');

    element1.classList.remove('show');
    element2.classList.remove('show');
}