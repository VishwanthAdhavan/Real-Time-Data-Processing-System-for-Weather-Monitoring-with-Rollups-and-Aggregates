// Add any client-side JavaScript functionality here
document.addEventListener('DOMContentLoaded', function() {
    const citySelect = document.getElementById('city-select');
    const weatherCard = document.getElementById('weather-card');
    const cityName = document.getElementById('city-name');
    const weatherIcon = document.getElementById('weather-icon');
    const temperature = document.getElementById('temperature');
    const feelsLike = document.getElementById('feels-like');
    const humidity = document.getElementById('humidity');
    const windSpeed = document.getElementById('wind-speed');
    const description = document.getElementById('description');
    const loading = document.getElementById('loading');
    const errorMessage = document.getElementById('error-message');
    const lastUpdated = document.getElementById('last-updated');

    let updateInterval;
    const UPDATE_INTERVAL = 5 * 60 * 1000; // 5 minutes in milliseconds

    citySelect.addEventListener('change', function() {
        const selectedCity = this.value;
        if (selectedCity) {
            getWeatherForCity(selectedCity);
            // Clear any existing interval and set a new one
            clearInterval(updateInterval);
            updateInterval = setInterval(() => getWeatherForCity(selectedCity), UPDATE_INTERVAL);
        } else {
            hideWeatherCard();
            clearInterval(updateInterval);
        }
    });

    function getWeatherForCity(city) {
        const csrfToken = document.querySelector('input[name="csrf_token"]').value;
        
        showLoading();
        hideError();

        fetch('/get_weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: `city=${encodeURIComponent(city)}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            displayWeather(data);
            updateLastUpdatedTime();
        })
        .catch(error => {
            showError(`Error fetching weather data: ${error.message}`);
            console.error('Error:', error);
        })
        .finally(() => {
            hideLoading();
        });
    }

    function displayWeather(data) {
        cityName.textContent = data.city;
        temperature.textContent = `${Math.round(data.temperature)}°C`;
        feelsLike.textContent = `Feels like: ${Math.round(data.feels_like)}°C`;
        humidity.textContent = `Humidity: ${data.humidity}%`;
        windSpeed.textContent = `Wind: ${data.wind_speed} m/s`;
        description.textContent = data.description;
        weatherIcon.className = `fas ${getWeatherIcon(data.weather_condition)}`;
        
        showWeatherCard();
    }

    function getWeatherIcon(condition) {
        const iconMap = {
            'Clear': 'fa-sun',
            'Clouds': 'fa-cloud',
            'Rain': 'fa-cloud-rain',
            'Thunderstorm': 'fa-bolt',
            'Snow': 'fa-snowflake',
            'Mist': 'fa-smog'
        };
        return iconMap[condition] || 'fa-cloud';
    }

    function showLoading() {
        loading.classList.remove('hidden');
        loading.style.opacity = '1';
    }

    function hideLoading() {
        loading.style.opacity = '0';
        setTimeout(() => loading.classList.add('hidden'), 300);
    }

    function showWeatherCard() {
        weatherCard.classList.remove('hidden');
        setTimeout(() => weatherCard.style.opacity = '1', 50);
    }

    function hideWeatherCard() {
        weatherCard.style.opacity = '0';
        setTimeout(() => weatherCard.classList.add('hidden'), 300);
    }

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('hidden');
        setTimeout(() => errorMessage.style.opacity = '1', 50);
    }

    function hideError() {
        errorMessage.style.opacity = '0';
        setTimeout(() => errorMessage.classList.add('hidden'), 300);
    }

    // Add a new function to update the last updated time
    function updateLastUpdatedTime() {
        if (lastUpdated) {
            const now = new Date();
            lastUpdated.textContent = `Last updated: ${now.toLocaleTimeString()}`;
            console.log("Last updated time set to:", lastUpdated.textContent);  // Debug log
        } else {
            console.error("Last updated element not found");  // Debug log
        }
    }
});
