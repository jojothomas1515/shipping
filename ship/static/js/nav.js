const toggler = document.getElementById("toggler")
const nav_ul = document.getElementById("navid")


nav_ul.style.left = "-100%"
toggler.addEventListener("click", ()=>{
    if (nav_ul.style.left === "-100%")
        nav_ul.style.left = "0";
    else
        nav_ul.style.left = "-100%"
    console.log("this is working")
})