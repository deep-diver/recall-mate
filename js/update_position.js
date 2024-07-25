function updatePosition() {
    const markdownElem = document.querySelector('.follow-cursor');
    const highlighted_text = document.querySelector('#highlight_txt .textfield');
    const notSelectableElements = document.querySelectorAll('.no-cat');

    // Add event listener to the document
    document.addEventListener('click', (event) => {
        // Flag to check if the click was inside any selectable element
        let clickedInsideSelectable = true;

        // Check if the click happened inside any selectable element
        notSelectableElements.forEach(function(element) {
            if (element.contains(event.target)) {
                clickedInsideSelectable = false;
            }
        });

        // Check if the click happened inside markdownElem
        if (markdownElem.contains(event.target)) {
            clickedInsideSelectable = false;
        }

        if (clickedInsideSelectable) {
            let mouseX = event.clientX;
            let mouseY = event.clientY;

            if (markdownElem) {
                markdownElem.style.top = (mouseY + 10) + 'px'; // Adjust for offset
                markdownElem.style.left = (mouseX + 10) + 'px'; // Adjust for offset
            }
        }

        if (!highlighted_text.contains(event.target)) {
            if (markdownElem.contains(event.target)) {
                markdownElem.style.display = "block";
            } else {
                markdownElem.style.display = "none";
            }
        } else {
            if (!clickedInsideSelectable) {
                markdownElem.style.display = "none";
            } else {
                markdownElem.style.display = "block";
            }
        }
    });
}