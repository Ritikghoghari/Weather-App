const btn = document.getElementById("btn");
const cityName = document.getElementById("city-name");
const cityTime = document.getElementById("city-time");
const cityTemp = document.getElementById("city-temp");
const input = document.getElementById("cityinput");

async function getData(cityName) {
  const promise = await fetch(
    `http://api.weatherapi.com/v1/current.json?key=c1c48b686498401582a214207241008&q=${cityName}&aqi=yes`
  );
  return await promise.json();
}

btn.addEventListener("click", async () => {
  const value = input.value;
  const result = await getData(value);
  cityName.innerText = `${result.location.name} , ${result.location.region} , ${result.location.country}`;
  cityTime.innerText = result.location.localtime;
  cityTemp.innerText = result.current.temp_c;
});
