const modal = document.getElementsByClassName('modal')[0]
const close = document.getElementById('close')
const tracking_btn = document.getElementById('tracking-btn')
const infos = document.getElementsByClassName('infos')

import Count from "./count.mjs";

close.addEventListener('click', () => {
    modal.style.display = 'none'
    console.log("working")
})

tracking_btn.addEventListener('click', () => {
    console.log('clicking')
    get_info(document.getElementById('tinput').value)
})

async function get_info(tracking_num) {

    let csrftoken = getCookie('csrftoken');
    const res = await fetch("track", {
        method: 'post',
        body: JSON.stringify({tracking: tracking_num}),
        headers: {"X-CSRFToken": csrftoken, 'Content-Type': 'application/json'},

    })
    const data = await res.json()

    infos[0].textContent = `Details :${data.details}`
    infos[1].textContent = `Destination :${data.destination}`
    infos[2].textContent = `Current Location :${data.current_location}`
    infos[3].textContent = `Sent From :${data.from_destination}`
    open_map(0)
    Count(10)
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function open_map() {
    modal.style.display = 'block'
    ymaps.ready(init);

    function init() {
        // Creating the map.    
        var myMap = new ymaps.Map("map", {
            // The map center coordinates.
            // Default order: “latitude, longitude”.
            // To not manually determine the map center coordinates,
            // use the Coordinate detection tool.
            center: [55.76, 37.64],
            // Zoom level. Acceptable values:
            // from 0 (the entire world) to 19.
            zoom: 12,
            controls: [],
        });
        let placeMark = new ymaps.Placemark(myMap.getCenter(), {
            hintContent: 'current location',
        })

        myMap.geoObjects.add(placeMark);

    }
}