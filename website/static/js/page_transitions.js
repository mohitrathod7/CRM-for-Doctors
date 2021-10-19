const page = gsap.timeline();

var home = document.getElementById('home').className.split(/\s+/);
var shop = document.getElementById('shop').className.split(/\s+/);
var user = document.getElementById('user').className.split(/\s+/);
var chat = document.getElementById('chat').className.split(/\s+/);

var duration = 20;
var ease = "power2.in";
var to_left = 1200;
var to_right = (to_left*-1);
var to_up = 1000;
var to_down = (to_up*-1);

// For Home page
for (var i = 0; i < home.length; i++) {
    if (home[i] === 'active') {
        // to left
        $("footer #shop").click(function(event) {
            event.preventDefault();
            
            // Animate here
            // alert("The required page will not be open");
            page.from('.content', { ease: ease, duration: duration, x: to_left })
    
            // Link will open
            location.href = $(this).attr("href");
        });

        // to right
        $("footer #user").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, x: to_right })
    
            // Link will open
            location.href = $(this).attr("href");
        });
   
        // to up
        $("nav #chat").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, y: to_up })
    
            // Link will open
            location.href = $(this).attr("href");
        });
    }
}

// For Shop page
for (var i = 0; i < shop.length; i++) {
    if (shop[i] === 'active') {
        // to right
        $("footer #home").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, x: to_right })
    
            // Link will open
            location.href = $(this).attr("href");
        });

        // to right
        $("footer #user").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, x: to_right })
    
            // Link will open
            location.href = $(this).attr("href");
        });
        
        // to up
        $("nav #chat").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, y: to_up })
    
            // Link will open
            location.href = $(this).attr("href");
        });
    }
}

// For User page
for (var i = 0; i < user.length; i++) {
    if (user[i] === 'active') {
        // to left
        $("footer #home").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, x: to_right })
    
            // Link will open
            location.href = $(this).attr("href");
        });

        // to left
        $("footer #shop").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, x: to_right })
    
            // Link will open
            location.href = $(this).attr("href");
        });
        
        // to up
        $("nav #chat").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, y: to_up })
    
            // Link will open
            location.href = $(this).attr("href");
        });
    }
}


// For Chat page
for (var i = 0; i < chat.length; i++) {
    if (chat[i] === 'active') {
        // to down
        $("footer #home").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, x: to_down })
    
            // Link will open
            location.href = $(this).attr("href");
        });

        // to down
        $("footer #shop").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, x: to_down })
    
            // Link will open
            location.href = $(this).attr("href");
        });
        
        // to down
        $("nav #chat").click(function(event) {
            event.preventDefault();
            
            // Animate here
            page.from('.content', { ease: ease, duration: duration, y: to_down })
    
            // Link will open
            location.href = $(this).attr("href");
        });
    }
}
