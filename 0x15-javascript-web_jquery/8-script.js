/*
 * Script that fetches and lists the title for all movies by using
 * this URL: https://swapi-api.alx-tools.com/api/films/?format=json
 * All movie titles must be list in the HTML tag UL#list_movies
 */
const web = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(web, function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
