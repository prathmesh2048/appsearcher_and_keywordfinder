function getOption(){
  var e = document.getElementById('inputoption');
  var option = e.options[e.selectedIndex].text;
    if (option == 'Play store') {
    document.getElementById("appstore").style.display = "none";
    document.getElementById("playstore").style.display = "block";
  }else if (option == 'App store') {
    document.getElementById("appstore").style.display = "block";
    document.getElementById("playstore").style.display = "none";
  }

}



