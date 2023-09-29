$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'GET',
  success: function(response) {
    $('DIV#character').text(response.name);
  }
});