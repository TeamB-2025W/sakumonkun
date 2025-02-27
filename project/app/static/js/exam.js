"use strict";

const examForm = document.getElementById('examForm');
const submitModal = document.getElementById('submitModal');
const confirmButton = document.getElementById('confirmButton');
const cancelButton = document.getElementById('cancelButton');

examForm.addEventListener('submit', function(e) {
    e.preventDefault();
    submitModal.style.display = 'block';
});

cancelButton.onclick = function() {
    submitModal.style.display = 'none';
}

confirmButton.onclick = function() {
    examForm.submit();
    submitModal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == submitModal) {
        submitModal.style.display = 'none';
    }
}