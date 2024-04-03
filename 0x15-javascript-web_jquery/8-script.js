$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (link) {
  $('UL#list_movies').append(...link.results.map(movie => `<li>${movie.title}</li>`));
});
