//Nav selected function
function selected(link) {
  let options = document.querySelectorAll('#links a');
  options[0].className = '';
  options[1].className = '';
  options[2].className = '';
  options[3].className = '';
  options[4].className = '';
  link.className = 'selected';

  let x = document.getElementById('nav');
  x.className = ''
}

//Shows the responsive menu
function responsiveMenu() {
  let x = document.getElementById("nav");
  if (x.className === "") {
    x.className = "responsive";
  } else {
    x.className = "";
  }
}