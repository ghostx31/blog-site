// ===============loader=========
var preloader = document.getElementById('loading');
function loadingfunction(){
  preloader.style.display = 'none';
}
//===============dark mode==========
function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
}
//===========responsive navbar=============
function Function() {
  var x = document.getElementById("myTopnav");
  if (x.className === "navbar") {
    x.className += " responsive";
  } else {
    x.className = "navbar";
  }
}

