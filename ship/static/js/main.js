const modal = document.getElementsByClassName('modal')[0]
const close = document.getElementById('close')
const tracking_btn = document.getElementById('tracking-btn')

const destination =  document.getElementById('destination')
destination.textContent = 'lagos'

close.addEventListener('click', () =>{
    modal.style.display = 'none'
    console.log("working")
})

tracking_btn.addEventListener('click', () => {
    get_info()


})

async function get_info(){

    let csrftoken = getCookie('csrftoken');
    res = await fetch("track", {
        method:'post',
        body:JSON.stringify({tracking:'jojo'}),
        headers: { "X-CSRFToken": csrftoken },
    })
    console.log(res)
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