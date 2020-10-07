const app_left = document.getElementById('opponent')
const app_right = document.getElementById('type-values')

var urlParams = new URLSearchParams(window.location.search);

const type1 = (urlParams.get('type1')); 
const type2 = (urlParams.get('type2'));
const battletype = (urlParams.get('battletype'));


var request = new XMLHttpRequest();

request.open('GET', '/types/' + type1 + '/' + type2 + '?battletype=' + battletype, true);

request.onload = function () {
  var object = JSON.parse(this.response);
  console.log(object);

  function createTypeContainer(pdiv, id, clss, div_name) {
    div_name.setAttribute('id', id);
    div_name.setAttribute('class', clss);
    pdiv.appendChild(div_name);
  }

  function UpperFirstLet(string) {
    if (string != null){
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
  
  var x = 'value'

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
  createSingleTypeDiv(app_left, type1);
  createSingleTypeDiv(app_left, type2);

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
