let searchDiv = document.getElementById("searchDiv");
const text1 = document.getElementById("searchBar");

function addTask() {
    
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