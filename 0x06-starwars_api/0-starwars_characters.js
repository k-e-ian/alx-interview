#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    const fetchCharacter = (characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    };

    const fetchAllCharacters = (urls) => {
      if (urls.length === 0) {
        return;
      }

      const characterUrl = urls.shift();
      fetchCharacter(characterUrl);

      // Fetch the next character after a short delay to avoid API rate limits
      setTimeout(() => {
        fetchAllCharacters(urls);
      }, 100);
    };

    fetchAllCharacters(characterUrls);
  }
});
