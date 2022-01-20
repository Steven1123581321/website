// check for saved 'darkMode' in localStorage
let darkMode = localStorage.getItem('darkMode');

const darkModeToggle = document.querySelector('#toggle-switch');

const enableDarkMode = () => {
    // 1. Add the class to the body
    document.body.classList.add('darkmode');
    // 2. Update darkMode in localStorage
    localStorage.setItem('darkMode', 'enabled');
}

const disableDarkMode = () => {
    // 1. Remove the class from the body
    document.body.classList.remove('darkmode');
    // 2. Update darkMode and toggle in localStorage 
    localStorage.setItem('darkMode', null);
}

// If the user already visited and enabled darkMode
// start things off with it on
if (darkMode === 'enabled') {
    enableDarkMode();
    // 3. toggle the checkbox
    darkModeToggle.setAttribute('checked', true);
}

// When someone clicks the button
darkModeToggle.addEventListener('click', () => {
    // get their darkMode setting
    darkMode = localStorage.getItem('darkMode');

    // if it not current enabled, enable it
    if (darkMode !== 'enabled') {
        enableDarkMode();
        // if it has been enabled, turn it off  
    } else {
        disableDarkMode();
    }
});

$(document).ready(function () {
    $("#searchEngine").on('change', function () {
        $(".form-inline").hide();
        $("#" + $(this).val()).fadeIn(700);
    });
});


const searchButton1 = document.getElementById('search-button1');
const searchInput1 = document.getElementById('search-input1');
const wolfram = 'https://www.wolframalpha.com/input?i=';

searchButton1.addEventListener('click', () => {
    const url = wolfram + searchInput1.value;
    const win = window.open(url, '_blank');
    win.focus();
});

const searchButton2 = document.getElementById('search-button2');
const searchInput2 = document.getElementById('search-input2');
const approach_zero = 'https://approach0.xyz/search?q=';

searchButton2.addEventListener('click', () => {
    const url = approach_zero + searchInput2.value;
    const win = window.open(url, '_blank');
    win.focus();
});

const searchButton3 = document.getElementById('search-button3');
const searchInput3 = document.getElementById('search-input3');
const google = 'https://www.google.com/search?q=';

searchButton3.addEventListener('click', () => {
    const url = google + searchInput3.value;
    const win = window.open(url, '_blank');
    win.focus();
});