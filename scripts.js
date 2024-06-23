function showPopup(type) {
    document.getElementById(type + '-popup').style.display = 'flex';
}

function closePopup(event) {
    if (event.target.classList.contains('popup')) {
        event.target.style.display = 'none';
    }
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeAllPopups();
    }
});

function closeAllPopups() {
    document.querySelectorAll('.popup').forEach(function(popup) {
        popup.style.display = 'none';
    });
}
