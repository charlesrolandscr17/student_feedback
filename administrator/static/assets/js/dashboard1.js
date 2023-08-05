const backgrounds = [
    '{% static "assets/images/hall.jpg" %}',
    '{% static "assets/images/design1.jpg" %}',
    '{% static "assets/images/main_gate.jpg" %}',
    '{% static "assets/images/student1.jpg" %}',
    '{% static "assets/images/leaders.jpg" %}',    
];
const heroSection = document.querySelector('.hero');

let currentBackgroundIndex = 0;

function changeBackground() {
    heroSection.style.backgroundImage = `url(${backgrounds[currentBackgroundIndex]})`;
    currentBackgroundIndex = (currentBackgroundIndex + 1) % backgrounds.length;
}

// Change background every 5 seconds
setInterval(changeBackground, 5000);
