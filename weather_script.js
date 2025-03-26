const fetch = require('node-fetch');

const apiKey = '37b8c7bb26df7e9a1f437ca4850b41b9'; // Reemplaza con tu API Key de OpenWeather
const baseUrl = 'https://api.openweathermap.org/data/2.5/weather';

async function obtenerTemperatura(ciudad) {
    try {
        const url = `${baseUrl}?q=${ciudad},AR&units=metric&appid=${apiKey}`;
        const respuesta = await fetch(url);
        if (!respuesta.ok) {
            throw new Error('No se pudo obtener la información del clima.');
        }
        const datos = await respuesta.json();
        console.log(`La temperatura actual en ${ciudad} es de ${datos.main.temp}°C.`);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// Ejemplo de uso
const ciudad = 'Buenos Aires'; 
obtenerTemperatura(ciudad);

