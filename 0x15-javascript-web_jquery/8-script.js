$.get('http://swapi.co/api/films?format=json', function (body) {
  $.each(body.results, function (key, value) {
    $('ul#list_movies').append($('<li></li>').text(value.title));
  });
});
