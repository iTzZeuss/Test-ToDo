const searchDiv = document.getElementById("searchDiv");
const text1 = document.getElementById("searchBar");
const searchBTN = document.getElementById("searchBtn");
const numOfDivs = 5;
const searchResults1 = document.getElementById("searchResults1");
const searchResults2 = document.getElementById("searchResults2");


function handleInputChange(event) {
    const value = event.target.value;
    //console.log("Current input value:", value);   optional/debug
}
text1.addEventListener('input', handleInputChange);

function findTask() {
    if (text1.value === "") {
        searchDiv.style.display = "none";
        searchResults1.style.display = "none";
        searchResults2.style.display = "none";
    }
    else{    
    searchDiv.style.display = "block";
    searchResults1.style.display = "block";
    searchResults2.style.display = "block";
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
    let head = document.getElementById("head1");
    head.innerHTML = data[0].header
    let desc = document.getElementById("desc1");
    desc.innerHTML = data[0].description
  })

  fetch('/tasklist', {
    method: 'GET', 
    headers: {
      'Content-Type': 'application/json',
    },
  })
    .then(response => response.json())
    .then(data => {
      let head = document.getElementById("head2");
      head.innerHTML = data[1].header
      let desc = document.getElementById("desc2");
      desc.innerHTML = data[1].description
    })