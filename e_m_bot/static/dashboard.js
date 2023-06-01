const buttons = document.querySelectorAll(".btn");

function random(number) {
    return Math.floor(Math.random() * (number + 1));
}
for (const button of buttons) {
    button.addEventListener("click", reroute);
}

function reroute() {
        
}