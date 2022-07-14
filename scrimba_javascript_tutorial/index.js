let countEl = document.getElementById("count-el")
let saveEl = document.getElementById("save-el")
let count = 0

function increment() {
    count += 1
    countEl.innerText = count
}

function save() {
    let update = count + " - "
    saveEl.textContent += update
    console.log(count)
    count = 0
    countEl.textContent = 0
}