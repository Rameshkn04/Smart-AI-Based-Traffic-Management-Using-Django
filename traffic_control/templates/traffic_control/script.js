// Simulate traffic light changes
const trafficLights = document.querySelectorAll('.traffic-light');

function changeLight(trafficLight, activeColor) {
    const lights = trafficLight.querySelectorAll('.light');
    lights.forEach(light => {
        if (light.classList.contains(activeColor)) {
            light.style.backgroundColor = activeColor;
        } else {
            light.style.backgroundColor = 'gray';
        }
    });
}

// Cycle through traffic lights
let activeIndex = 0;
const colors = ['red', 'green', 'yellow'];

setInterval(() => {
    trafficLights.forEach((light, index) => {
        const activeColor = index === activeIndex ? colors[(activeIndex + 1) % colors.length] : 'red';
        changeLight(light, activeColor);
    });
    activeIndex = (activeIndex + 1) % trafficLights.length;
}, 2000);
