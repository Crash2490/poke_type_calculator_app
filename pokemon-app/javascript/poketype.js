var request = new XMLHttpRequest();

request.open('GET', 'http://127.0.0.1:5000/pokemon', true);

var names = []

request.onload = function () {
  var data = JSON.parse(this.response);
  pokemon_list = document.getElementById("pokemon-list")
  data.data.forEach((pokemon) => {
    console.log(pokemon.attributes.name);  
    pokemon_list.innerHTML += "<option>" + pokemon.attributes.name + "</option>"
  });
}

request.send();


const form1 = document.getElementById("name-div");

function handleSubmitName() {
  const formData = new FormData(form1);
  const data = [...formData.entries()];
  const asString = data
      .map(x => `${encodeURIComponent(x[0])}=${encodeURIComponent(x[1])}`)
      .join('&');
  console.log(asString);
  window.location.href=("ptc-2.html?"+ asString)
}


const form2 = document.getElementById("type-div");

function handleSubmitTypes() {
  const formData = new FormData(form2);
  const data = [...formData.entries()];
  const asString = data
      .map(x => `${encodeURIComponent(x[0])}=${encodeURIComponent(x[1])}`)
      .join('&');
  console.log(asString);
  window.location.href=("ptc-3.html?"+ asString)
}
