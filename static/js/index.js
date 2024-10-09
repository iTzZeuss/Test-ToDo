let searchDiv = document.getElementById("searchDiv");
const text1 = document.getElementById("searchBar");
const searchBTN = document.getElementById("searchBtn");
const numOfDivs = 5;

for (i = 1; i <= numOfDivs; i++) {
    let newDiv = document.createElement("div")
    newDiv.textContent = "" //will do these 2 tmrw
    newDiv.className = ""
}

function handleInputChange(event) {
    const value = event.target.value;
    //console.log("Current input value:", value);   optional/debug
}
text1.addEventListener('input', handleInputChange);

function findTask() {
    if (text1.value === "") {
        searchDiv.style.display = "none";
    }
    else{    
    searchDiv.style.display = "block";
    }
}
