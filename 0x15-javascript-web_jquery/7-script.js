$.get('http://swapi.co/api/people/5/?format=json', function (body) {
  $('div#character').text(body.name);
});
