const app_left = document.getElementById('opponent')
const right_4 = document.getElementById('vve-tvs')
const right_2 = document.getElementById('ve-tvs')
const right_1 = document.getElementById('e-tvs')
const right_12 = document.getElementById('i-tvs')
const right_14 = document.getElementById('vi-tvs')
const right_0 = document.getElementById('ne-tvs')

var urlParams = new URLSearchParams(window.location.search);

const type1 = (urlParams.get('type1')); 
const type2 = (urlParams.get('type2'));


var request = new XMLHttpRequest();

request.open('GET', 'http://127.0.0.1:5000/'+ type1 + '/' + type2, true);

request.onload = function () {
  var type_values = JSON.parse(this.response);
  console.log(type_values);

  function UpperFirstLet(string) {
    if (string != null){
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }

  function getKeyByValue(object, value) { 
    return Object.keys(object).filter(key =>  
            object[key] === value); 
  }
  
  function createManyTypeDivs(pdiv, array, div_name) {
    for(let i = 0;i < array.length;i++){
      div_name = document.createElement('p');
      div_name.setAttribute('id', (array[i]));
      div_name.setAttribute('class', 'type_divs')
      if (array[i]=== ' ') {
        pdiv.setAttribute('hidden');
        pdiv.appendChild(div_name);
      }
      else {
        div_name.textContent = UpperFirstLet(array[i]);
        pdiv.appendChild(div_name);
      }
    }
  }

  function createSingleTypeDiv(pdiv, type, div_name) {
      div_name = document.createElement('p');
      div_name.setAttribute('id', type);
      div_name.setAttribute('class', 'type_divs');
      div_name.textContent = UpperFirstLet(type);
      pdiv.appendChild(div_name);
  }
  
  createSingleTypeDiv(app_left, type1);
  createSingleTypeDiv(app_left, type2);

  const types_4 = getKeyByValue(type_values, 4);
  createManyTypeDivs(right_4, types_4);

  const types_2 = getKeyByValue(type_values, 2);
  createManyTypeDivs(right_2, types_2);

  const types_1 = getKeyByValue(type_values, 1); 
  createManyTypeDivs(right_1, types_1);

  const types_half = getKeyByValue(type_values, .5); 
  createManyTypeDivs(right_12, types_half);

  const types_quarter = getKeyByValue(type_values, .25); 
  createManyTypeDivs(right_14, types_quarter);

  const types_0 = getKeyByValue(type_values, 0);
  createManyTypeDivs(right_0, types_0);
  
}

request.send();