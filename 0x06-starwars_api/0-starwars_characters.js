#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Movie ID is required.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    process.exit(1);
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;
  const characterNames = [];

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie.');
    process.exit(0);
  }

  let charactersFetched = 0;

  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Invalid response:', response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      characterNames[index] = character.name;
      charactersFetched++;

      if (charactersFetched === characters.length) {
        characterNames.forEach((name) => {
          console.log(name);
        });
      }
    });
  });
});
