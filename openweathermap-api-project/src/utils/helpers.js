export const formatWeatherData = (data) => {
    if (!data || !data.main) {
        throw new Error('Invalid weather data');
    }

    const { temp, humidity } = data.main;
    const { name } = data;
    const weatherDescription = data.weather[0].description;

    return {
        city: name,
        temperature: temp,
        humidity,
        description: weatherDescription,
    };
};