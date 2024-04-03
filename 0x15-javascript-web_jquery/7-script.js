$.get('https://swapi.co/api/people/5/?format=json', function (link) {
  $('DIV#character').text(link.name);
});
