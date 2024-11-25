/* Slick Carousel */
$(document) .ready(function(){
    $('.post-wrapper').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        nextArrow: $('.next'),
        prevArrow: $('.prev'), 

        responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                infinite: true,
                dots: true
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
          ]
      });
});


const scrollToTop = document.querySelector('#scroll');

window.addEventListener("scroll", () => {
  if (window.pageYOffset > 100 || window.scrollY > 100) {
    scrollToTop.classList.add("active");
  } else {
     scrollToTop.classList.remove("active");
  }
})

scrollToTop.addEventListener('click', () => {
  if (scrollToTop.classList.contains('active')) {
    window.scrollTo({
      top : 0,
      behavior : "smooth"
    });
  }
});


/* Aside nav bar */
let open = false;

const openNavBar = document.querySelector("#open-sidBar");
let closeSideBar = document.querySelector("#close-sideBar");

const newDiv = document.createElement('div');
document.body.appendChild(newDiv);
newDiv.classList.add("bg-transparent");



openNavBar.addEventListener("click", () => {
  if (open === false) {
    const sideBar = document.querySelector("#sideBar");
    closeSideBar = document.querySelector("#close-sideBar");
    sideBar.style.transform = "translateX(0%)";
    closeSideBar.style.transform = "translateY(0%)";
    newDiv.style.transform = "translateX(0%)";
  }
  open = true;
})


closeSideBar.addEventListener("click", () => {
  if (open === true) {
    const sideBar = document.querySelector("#sideBar");
    sideBar.style.transform = "translateX(-100%)";
    const closeSideBar = document.querySelector("#close-sideBar");
    closeSideBar.style.transform = "translateY(-100%)";
   newDiv.style.transform = "translateX(-100%)";
  }
  open = false;
});




/**
 * On scroll effect for the Nav
 */

 const navToBeScrolled = document.querySelector('.header-content-container');

 window.addEventListener("scroll", () => {
   if (scrollY > 500) {
      navToBeScrolled.id = "nav-scrolled";
   } else {
     navToBeScrolled.id = "";
   }
 });


 // Admin sideBar