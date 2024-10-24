// Add any client-side JavaScript functionality here
document.addEventListener('DOMContentLoaded', function() {
    const citySelect = document.getElementById('city-select');
    const weatherInfo = document.getElementById('weather-info');
    const loading = document.getElementById('loading');
    const lastUpdated = document.getElementById('last-updated');
    let updateInterval;

    citySelect.addEventListener('change', function() {
        const selectedCity = this.value;
        if (selectedCity) {
            fetchWeatherData(selectedCity);
            // Clear existing interval and set a new one
            clearInterval(updateInterval);
            updateInterval = setInterval(() => fetchWeatherData(selectedCity), 5 * 60 * 1000); // 5 minutes
        } else {
            weatherInfo.innerHTML = '';
            weatherInfo.classList.add('hidden');
            lastUpdated.textContent = '';
            clearInterval(updateInterval);
        }
    });

    function fetchWeatherData(city) {
        loading.classList.remove('hidden');
        weatherInfo.classList.add('hidden');
        weatherInfo.innerHTML = '';

        fetch('/get_weather', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: 'city=' + encodeURIComponent(city)
        })
        .then(response => response.json())
        .then(data => {
            loading.classList.add('hidden');
            if (data.error) {
                showError(data.error);
            } else {
                displayWeatherData(data);
            }
        })
        .catch(error => {
            loading.classList.add('hidden');
            showError(error.message);
        });
    }

    function displayWeatherData(data) {
        const weatherIcon = getWeatherIcon(data.weather_condition);
        weatherInfo.innerHTML = `
            <h2>${data.city}</h2>
            <div class="temperature">${data.temperature}°C</div>
            <div class="weather-icon">${weatherIcon}</div>
            <div class="weather-details">
                <p><i class="fas fa-info-circle"></i> ${data.description}</p>
                <p><i class="fas fa-tint"></i> Humidity: ${data.humidity}%</p>
                <p><i class="fas fa-wind"></i> Wind Speed: ${data.wind_speed} m/s</p>
            </div>
        `;
        weatherInfo.classList.remove('hidden');
        updateLastUpdated();
    }

    function showError(message) {
        weatherInfo.innerHTML = `<p class="error-message"><i class="fas fa-exclamation-triangle"></i> Error: ${message}</p>`;
        weatherInfo.classList.remove('hidden');
        clearInterval(updateInterval);
    }

    function updateLastUpdated() {
        const now = new Date();
        lastUpdated.textContent = `Last updated: ${now.toLocaleTimeString()}`;
    }

    function getWeatherIcon(condition) {
        const icons = {
            'Clear': '<i class="fas fa-sun"></i>',
            'Clouds': '<i class="fas fa-cloud"></i>',
            'Rain': '<i class="fas fa-cloud-rain"></i>',
            'Thunderstorm': '<i class="fas fa-bolt"></i>',
            'Snow': '<i class="fas fa-snowflake"></i>',
            'Mist': '<i class="fas fa-smog"></i>',
            'Smoke': '<i class="fas fa-smog"></i>',
            'Haze': '<i class="fas fa-smog"></i>',
            'Dust': '<i class="fas fa-smog"></i>',
            'Fog': '<i class="fas fa-smog"></i>',
            'Sand': '<i class="fas fa-smog"></i>',
            'Ash': '<i class="fas fa-smog"></i>',
            'Squall': '<i class="fas fa-wind"></i>',
            'Tornado': '<i class="fas fa-wind"></i>'
        };
        return icons[condition] || '<i class="fas fa-question-circle"></i>';
    }
});
