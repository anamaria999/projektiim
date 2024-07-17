// function heartChange() {
//     let heart = document.getElementById("heart")
//     heart.classList.toggle("fa-solid")
// }

let AllHearts = document.getElementsByClassName("heart")

for (let i in AllHearts) {
    AllHearts[i].addEventListener("click", function () {
        AllHearts[i].classList.toggle("fa-solid")
    })
}