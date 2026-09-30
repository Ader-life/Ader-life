const envelope = document.getElementById("envelope-container");
const letter = document.getElementById("letter-container");
const noBtn = document.querySelector(".no-btn");
const yesBtn = document.querySelector(".yes-btn");

const title = document.getElementById("letter-title");
const catImg = document.getElementById("letter-cat");
const buttons = document.getElementById("letter-buttons");
const finalText = document.getElementById("final-text");
const letterWindow = document.querySelector(".letter-window");
const readLetter = document.getElementById("read-letter");
const heartLetter = document.getElementById("heart-letter");

envelope.addEventListener("click", () => {
    envelope.style.display = "none";
    letter.style.display = "flex";

    setTimeout(() => {
        letterWindow.classList.add("open");
    }, 50);
});

function moveNoButton() {
    const distance = 150 + Math.random() * 100;
    const angle = Math.random() * Math.PI * 2;
    const moveX = Math.cos(angle) * distance;
    const moveY = Math.sin(angle) * distance;

    noBtn.style.transition = "transform 0.25s ease";
    noBtn.style.transform = `translate(${moveX}px, ${moveY}px)`;
}

noBtn.addEventListener("mouseover", moveNoButton);
noBtn.addEventListener("touchstart", (event) => {
    event.preventDefault();
    moveNoButton();
}, { passive: false });

yesBtn.addEventListener("click", () => {
    title.textContent = "Yippeeee! I love you, layu! ♡";
    catImg.src = "cat_dance.gif";

    letterWindow.classList.add("final");
    buttons.style.display = "none";
    finalText.style.display = "block";
});

readLetter.addEventListener("click", () => {
    heartLetter.classList.add("show");
    readLetter.style.display = "none";
    heartLetter.scrollIntoView({ behavior: "smooth", block: "center" });
});
