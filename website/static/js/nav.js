/* Display Nav */
function openNav(){
    $(".sidePanel").css("width", "250px");
    $(".fa-bars").css("display", "none");
    $("nav .fa-times").css("display", "block");
    $("body").css("pointer-events", "none");
    $(".fa-times").css("pointer-events", "all");
    $(".sidePanel").css("pointer-events", "all");
}

const sidePanel = gsap.timeline({ defaults: {duration: 1 }});

$('nav .fa-bars').click(function(){
    openNav();

    sidePanel
        .from('.sidePanel-item', { ease: 'power2.in', duration: 0.4, x: -300, stagger: 0.15 })
})


$('nav .fa-times').click(function(){        
    function hidepanel() {
        $(".sidePanel").css("width", "0");
        $(".fa-bars").css("display", "block");
        $("nav .fa-times").css("display", "none");
        $("body").css("pointer-events", "all");
        $(".sidePanel").css("pointer-events", "all");
    }

    sidePanel
        .to('.sidePanel-item', { ease: 'power2.in', duration: 0.4, x: -300, stagger: 0.15 })
        .to('.sidePanel-item', { ease: 'power2.in', duration: 0.4, x: 0 })
    
    setTimeout(hidepanel, 1000);
})