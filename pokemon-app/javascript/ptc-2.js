const app_left = document.getElementById('left')
const app_right = document.getElementById('type-values')

var urlParams = new URLSearchParams(window.location.search);

const name = (urlParams.get('name'));
const battletype = (urlParams.get('battletype'));

const params = new URLSearchParams(window.location.search);
const battle = params.get('battletype');
console.log(battle)

var request = new XMLHttpRequest();

request.open('GET', 'http://127.0.0.1:5000/pokemon/'+ name + '?battletype=' + battletype, true);

request.onload = function () {
  var data = JSON.parse(this.response);
  pokemon = data.data.attributes;  
  console.log(pokemon);

  if (battle === 'normal') {
    var object = pokemon.type_values;
  } else if (battle === 'inverse') {
    var object = pokemon.weaknesses;
  }
  console.log(object)
  
  function createTypeContainer(pdiv, id, clss, div_name) {
    div_name.setAttribute('id', id);
    div_name.setAttribute('class', clss);
    pdiv.appendChild(div_name);
  }

  function UpperFirstLet(string) {
    if (string != null) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }

  function decodeHtml(html) {
    var txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
  }

  function getKeyByValue(object, value) { 
    return Object.keys(object).filter(key => 
            object[key] === value);
  }
  
  function createManyTypeDivs(pdiv, array, div_name) {
    for(let i = 0;i < array.length;i++){
      div_name = document.createElement('p')
      div_name.setAttribute('id', (array[i]));
      div_name.setAttribute('class', 'type_divs')
      div_name.textContent = UpperFirstLet(array[i]);
      pdiv.appendChild(div_name);
    }
  }

  function createSingleTypeDiv(pdiv, type, div_name) {
    div_name = document.createElement('p');
    div_name.setAttribute('id', type);
    div_name.setAttribute('class', 'type_divs');
    div_name.textContent = UpperFirstLet(type);
    pdiv.appendChild(div_name);
  }


  var x = 'value'

  const container = document.createElement('span');
  container.setAttribute('id', 'img-container');
  app_left.appendChild(container);

  const container_2 = document.createElement('span');
  container_2.setAttribute('id', 'name');
  app_left.appendChild(container_2);

  const container_3 = document.createElement('span');
  createTypeContainer(app_left, 'type', x, container_3)

  const container_4 = document.createElement('span');
  createTypeContainer(app_right, 'vve-tvs', x, container_4);

  const container_5 = document.createElement('span');
  createTypeContainer(app_right, 've-tvs', x, container_5);

  const container_6 = document.createElement('span');
  createTypeContainer(app_right, 'e-tvs', x, container_6);

  const container_7 = document.createElement('span');
  createTypeContainer(app_right, 'i-tvs', x, container_7);

  const container_8 = document.createElement('span');
  createTypeContainer(app_right, 'vi-tvs', x, container_8);

  const container_9 = document.createElement('span');
  createTypeContainer(app_right, 'ne-tvs', x, container_9);

  const img = document.createElement('img');
  img.setAttribute('alt', 'pokemon-sprite');
  img.setAttribute('id', 'sprite');
  img.setAttribute('class', 'col-xs-2');
  img.src = pokemon.sprite;
  container.appendChild(img);

  const ball = document.createElement('img');
  ball.src = "ball.png";
  ball.setAttribute('alt', 'pokeball');
  ball.setAttribute('id', 'ball');
  container_2.appendChild(ball);

  const dex_num = document.createElement('p');
  dex_num.setAttribute('id', 'dex-num');
  dex_num.textContent = '#'+pokemon.dex_num;
  container_2.appendChild(dex_num);

  const name_val = document.createElement('p');
  name_val.setAttribute('id', 'name-val')
  name_val.textContent = UpperFirstLet(pokemon.name);
  container_2.appendChild(name_val);

  const type_text = document.createElement('p');
  type_text.setAttribute('id', 'type-text');
  type_text.textContent = 'Type: ';
  container_3.appendChild(type_text);

  createSingleTypeDiv(container_3, pokemon.type1);

  if (pokemon.type2 !== 'null') {
    createSingleTypeDiv(container_3, pokemon.type2);
  } 

  const types_4 = getKeyByValue(object, 4);
  if (types_4.length != 0) {
    const vve_tv_text = document.createElement('p');
    vve_tv_text.setAttribute('class', 'text');
    vve_tv_text.textContent = '4x Damage:';
    container_4.appendChild(vve_tv_text);
    createManyTypeDivs(container_4, types_4);
  }

  const types_2 = getKeyByValue(object, 2);
  if (types_2.length != 0) {
    const ve_tv_text = document.createElement('p');
    ve_tv_text.setAttribute('class', 'text');
    ve_tv_text.textContent = '2x Damage:';
    container_5.appendChild(ve_tv_text);
    createManyTypeDivs(container_5, types_2);
  }

  const types_1 = getKeyByValue(object, 1); 
  if (types_1.length !== 0) {
    const e_tv_text = document.createElement('p');
    e_tv_text.setAttribute('class', 'text');
    e_tv_text.textContent = '1x Damage:';
    container_6.appendChild(e_tv_text);
    createManyTypeDivs(container_6, types_1);
  }

  
  const types_half = getKeyByValue(object, .5); 
  if (types_half.length !== 0) {
    var str = decodeHtml('&frac12;x Damage:');
    const i_tv_text = document.createElement('p');
    i_tv_text.setAttribute('class', 'text');
    i_tv_text.textContent = str;
    container_7.appendChild(i_tv_text);
    createManyTypeDivs(container_7, types_half);
  }
  
  const types_quarter = getKeyByValue(object, .25); 
  if (types_quarter.length !== 0) {
      var str2 = decodeHtml('&frac14;x Damage:');
      const vi_tv_text = document.createElement('p');
      vi_tv_text.setAttribute('class', 'text');
      vi_tv_text.textContent = str2;
      container_8.appendChild(vi_tv_text);
      createManyTypeDivs(container_8, types_quarter);
  }

  const types_0 = getKeyByValue(object, 0);
  if (types_0.length !== 0) {
    const ne_tv_text = document.createElement('p');
    ne_tv_text.setAttribute('class', 'text');
    ne_tv_text.textContent = '0x Damage:';
    container_9.appendChild(ne_tv_text);
    createManyTypeDivs(container_9, types_0);
    
  }
}

request.send();
