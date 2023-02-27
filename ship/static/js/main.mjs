const package_info_container = document.getElementById("package-information")
const spinner = document.getElementById("spinner")
const tracking_btn = document.getElementById('tracking-btn')
const infos = document.getElementsByClassName('info')
const sender_data = document.getElementsByClassName('sender_data')
const receiver_data = document.getElementsByClassName('receiver_data')


tracking_btn.addEventListener('click', () => {
    if (document.getElementById('tracking-input').value === "") return
    get_info(document.getElementById('tracking-input').value)
})

async function get_info(tracking_num) {
    spinner.style.display = "block"
    spinner.style.animationPlayState = "running"
    let csrftoken = getCookie('csrftoken');

    const res = await fetch("track", {
        method: 'post',
        body: JSON.stringify({tracking: tracking_num}),
        headers: {"X-CSRFToken": csrftoken, 'Content-Type': 'application/json'}
    })

    const data = await res.json()
    if (res.status === 404) {
        setTimeout(() => {
            alert("No Package with that TRN")
            spinner.style.animationPlayState = "paused"
            spinner.style.display = "none"
            return (null)
        }, 200)
    }
    if (res.status === 200) {
        infos[0].textContent = `${data.package.package_name}`
        infos[1].textContent = `${data.package.package_id}`
        infos[2].textContent = `${data.package.date_shiped}`
        infos[3].textContent = `${data.package.delivery_date}`
        infos[4].textContent = `${data.package.delivery_status}`
        infos[5].textContent = `${data.package.weight}`
        infos[6].textContent = `${data.package.delivery_note}`

        sender_data[0].textContent = `${data.sender.name}`
        sender_data[1].textContent = `${data.sender.country}`
        sender_data[2].textContent = `${data.sender.city}`
        sender_data[3].textContent = `${data.sender.phone}`
        sender_data[4].textContent = `${data.sender.email}`

        receiver_data[0].textContent = `${data.receiver.name}`
        receiver_data[1].textContent = `${data.receiver.country}`
        receiver_data[2].textContent = `${data.receiver.city}`
        receiver_data[3].textContent = `${data.receiver.phone}`
        receiver_data[4].textContent = `${data.receiver.email}`


        setTimeout(() => {
            package_info_container.style.display = "flex"
            spinner.style.animationPlayState = "paused"
            spinner.style.display = "none"
        }, 5000)

    }

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


// function open_map() {
//     modal.style.display = 'block'
//     ymaps.ready(init);
//
//     function init() {
//         // Creating the map.
//         var myMap = new ymaps.Map("map", {
//             // The map center coordinates.
//             // Default order: “latitude, longitude”.
//             // To not manually determine the map center coordinates,
//             // use the Coordinate detection tool.
//             center: [55.76, 37.64],
//             // Zoom level. Acceptable values:
//             // from 0 (the entire world) to 19.
//             zoom: 12,
//             controls: [],
//         });
//         let placeMark = new ymaps.Placemark(myMap.getCenter(), {
//             hintContent: 'current location',
//         })
//
//         myMap.geoObjects.add(placeMark);
//
//     }
// }

