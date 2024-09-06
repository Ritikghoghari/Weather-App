# Weather-App
This is a simple weather application that allows users to search for the current weather conditions of any city worldwide. The app displays the city name, local time, and temperature.

Features
Search for current weather by city name
Display the city's name, region, and country
Show local time and current temperature in Celsius
Built using an API from WeatherAPI
Technologies Used
HTML/CSS: For the structure and styling of the app.
JavaScript: For fetching weather data and updating the DOM.
WeatherAPI: To retrieve real-time weather information.
Installation
To run this project locally:

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/Weather-App.git
Navigate into the project directory:
bash
Copy code
cd Weather-App
Open the index.html file in your browser to run the app.
Usage
Enter the name of any city in the input box.
Click the "Search" button to retrieve the city's current weather data.
The app will display the city name, local time, and temperature.
API Key
You will need to provide your own WeatherAPI key. Replace the API key in the script.js file:

javascript
Copy code
const promise = await fetch(
  `http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=${cityName}&aqi=yes`
);
Contributing
Contributions are welcome! If you’d like to contribute to this project:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is open source and available under the MIT License.
