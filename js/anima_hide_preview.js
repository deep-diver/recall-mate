function hide_preview() {
    const element1 = document.querySelector('.hidden_preview_container');
    const element2 = document.querySelector('.hidden_preview');

    element1.classList.remove('show');
    element2.classList.remove('show');
}