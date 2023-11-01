$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const results = data.results;
  results.forEach(element => {
    $('UL#list_movies').append(`<li>${element.title}</li>`);
  });
});
