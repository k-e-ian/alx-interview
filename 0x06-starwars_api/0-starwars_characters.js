#!/usr/bin/node

const request = require('request');

// Function to fetch movie characters
function getMovieCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const film = JSON.parse(body);
      const characterUrls = film.characters;

      // Fetch each character and print their names
      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (err, resp, characterBody) => {
          if (!err && resp.statusCode === 200) {
            const character = JSON.parse(characterBody);
            console.log(character.name);
          } else {
            console.log('Error:', err);
          }
        });
      });
    } else {
      console.log('Error:', error);
    }
  });
}

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Call the function to get movie characters
getMovieCharacters(movieId);
