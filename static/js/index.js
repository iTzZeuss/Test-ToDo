const searchDiv = document.getElementById("searchDiv");
const text1 = document.getElementById("searchBar");
const searchBTN = document.getElementById("searchBtn");
const numOfDivs = 5;
const searchResults1 = document.getElementById("searchResults1");
const searchResults2 = document.getElementById("searchResults2");


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
    }
    else{    
    searchDiv.style.display = "block";
    searchResults1.style.display = "block";
    searchResults2.style.display = "block";
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

      // ...
    } else {
      console.error('No data returned from server'); // Handle error
    }
  })
  .catch(error => {
    console.error('Error:', error);  // Handle error
    })