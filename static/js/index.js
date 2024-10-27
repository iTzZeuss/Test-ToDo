const searchDiv = document.getElementById("searchDiv");
const text1 = document.getElementById("searchBar");
const searchBTN = document.getElementById("searchBtn");
const numOfDivs = 5;
//temp
const searchResults1 = document.getElementById("searchResults1");
const searchResults2 = document.getElementById("searchResults2");
const head1 = document.getElementById("head1");
const head2 = document.getElementById("head2");
const desc1 = document.getElementById("desc1");
const desc2 = document.getElementById("desc2");
const searchA1 = document.getElementById("searchA1");
const searchA2 = document.getElementById("searchA2");


function handleInputChange(event) {
    const value = event.target.value;
    //console.log("Current input value:", value);   seeing what user types
}
text1.addEventListener('input', handleInputChange);

function findTask() {                           //display or hide search results
    if (text1.value === "") {
        searchDiv.style.display = "none";
        searchResults1.style.display = "none";
        searchResults2.style.display = "none";
        head1.style.display = "none";
        head2.style.display = "none";
        desc1.style.display = "none";
        desc2.style.display = "none";
    }
    else{    
    searchDiv.style.display = "block";
    searchResults1.style.display = "block";
    searchResults2.style.display = "block";
    head1.style.display = "block";
    head2.style.display = "block";
    desc1.style.display = "block";  
    desc2.style.display = "block";
    }
}

fetch('/tasklist', {          //fetch data from server
  method: 'GET', 
  headers: {
    'Content-Type': 'application/json',
  },
})
  .then(response => response.json())
  .then(data => {                                   //print the data on search
    if (data && data.length > 0) {
      console.log(data);
      let head = document.getElementById("head1");    
      head.innerHTML = data[0].header
      let desc = document.getElementById("desc1");
      desc.innerHTML = data[0].description
      let head1 = document.getElementById("head2");
      head1.innerHTML = data[1].header
      let desc1 = document.getElementById("desc2");
      desc1.innerHTML = data[1].description
      for (let i = 0; i < data.length; i++) {
        let div = document.createElement("div");
        div.className = "searchResults";
        searchDiv.appendChild(div);
      }
    }
    else if (data && data.length === 0) {
      let taskWarning = document.createElement("h1");
      taskWarning.className = "taskWarning";
      taskWarning.innerHTML = "Create a task first!";
      searchDiv.appendChild(div);
      searchA1.style.display = "none";
      searchA2.style.display = "none";
    }
    }
  )
  .catch(error => {
    console.error('Error:', error);  // Handle error
    })