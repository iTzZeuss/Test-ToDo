let searchDiv = document.getElementById("searchDiv");
const text1 = document.getElementById("searchBar");
const searchBTN = document.getElementById("searchBtn");
const numOfDivs = 5;

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

fetch('/tasklist', {
  method: 'GET', 
  headers: {
    'Content-Type': 'application/json',
  },
})
  .then(response => response.json())
  .then(data => {
    console.log(data);
    let head = document.getElementById("head");
    head.innerHTML = data[0].header
    let desc = document.getElementById("desc");
    desc.innerHTML = data[0].description
  })