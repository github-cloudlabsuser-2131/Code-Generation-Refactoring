// filepath: openweathermap-api-project/openweathermap-api-project/src/index.js
// This file serves as the entry point of the application.
// It initializes the application and may include code to call the OpenWeatherMap API using functions from the openWeatherMap.js module.

import { fetchWeatherData } from './api/openWeatherMap.js';

const apiKey = 'YOUR_API_KEY'; // Replace with your OpenWeatherMap API key
const city = 'London'; // Example city

async function getWeather() {
    try {
        const weatherData = await fetchWeatherData(city, apiKey);
        console.log(weatherData);
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

getWeather();