// ==================dark mode=================
function myFunction() {
   var element = document.body;
   element.classList.toggle("dark-mode");
}

//==========responsive nav bar================
function Function() {
  var x = document.getElementById("myTopnav");
  if (x.className === "navbar") {
    x.className += " responsive";
  } else {
    x.className = "navbar";
  }
}
