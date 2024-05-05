var host;
var deviceId;
var battery;
var longitude;
var latitude;
var url;

document.addEventListener('DOMContentLoaded', () => {
    host = document.getElementById('host');
    deviceId = document.getElementById('device-id');
    battery = document.getElementById('battery');
    longitude = document.getElementById('longitude');
    latitude = document.getElementById('latitude');
    url = document.getElementById('url');

    host.value = 'localhost'
    deviceId.value = 55667788
    battery.value = 50;
    longitude.value = 70;
    latitude.value = 30;
});

var show = () => {
    url.innerText = `http://${host.value}:5055?deviceid=${deviceId.value}&lat=${latitude.value}&lon=${longitude.value}&timestamp=${(new Date()).toISOString()}&speed=15&bearing=270&altitude=35&accuracy=10&hdop=0.8&batt=${battery.value}`;
}

var moveUp = () => {
    incrementLatitude();
    send();
}

var moveDown = () => {
    decrementLatitude();
    send();
}

var moveRight = () => {
    incrementLongitude();
    send();
}
var moveLeft = () => {
    decrementLongitude();
    send();
}

var send = () => {
    show();
    fetch(url.innerText);
}

var incrementLongitude = () => {
    increment(longitude, 89, 0.01);
}

var decrementLongitude = () => {
    decrement(longitude, -89, 0.01);
}

var incrementLatitude = () => {
    increment(latitude, 179, 0.01);
}

var decrementLatitude = () => {
    decrement(latitude, 1, 0.01);
}

var incrementBattery = () => {
    increment(battery, 100, 1);
}

var decrementBattery = () => {
    decrement(battery, 0, 1);
}

var increment = (element, limit, amount) => {
    const current = Number(element.value);
    const value = current < limit ? current + amount : current;
    element.value = value.toFixed(6).replace(/\.?0+$/, '');
}
var decrement = (element, limit, amount) => {
    const current = Number(element.value);
    const value = current > limit ? current - amount : current;
    element.value = value.toFixed(6).replace(/\.?0+$/, '');;
}