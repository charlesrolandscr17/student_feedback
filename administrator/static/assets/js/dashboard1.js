const backgrounds = [
    '{% static "assets/images/3.jpg" %}',
        
];
const heroSection = document.querySelector('.hero');

let currentBackgroundIndex = 0;

function changeBackground() {
    heroSection.style.backgroundImage = `url(${backgrounds[currentBackgroundIndex]})`;
    currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
}

// Change background every 5 seconds
setInterval(changeBackground, 5000);
