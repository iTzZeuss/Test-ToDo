const numOfDivs = 1;
let txt1 = document.getElementById("task_header").value;

function getDiv () {
    for (i = 1; i <= numOfDivs; i++) {
        let newDiv = document.createElement("div")
        newDiv.textContent = txt1
        newDiv.className = newTask
        newDiv.style.display = "block";

    }
}