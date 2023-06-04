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

    const fetchAllCharacters = async (urls) => {
      for (const characterUrl of urls) {
        await new Promise((resolve) => {
          fetchCharacter(characterUrl);
          resolve();
        });
      }
    };

    fetchAllCharacters(characterUrls);
  }
});
