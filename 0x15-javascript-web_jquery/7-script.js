/*
 * Script that update the character name from
 * this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
 */
const web = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(web, function (data, textStatus) {
  $('DIV#character').text(data.name);
});
