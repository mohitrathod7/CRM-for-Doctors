// Change Theme -----------------------------------------------------------------------------------

document.documentElement.style.setProperty("--primary-bg", "#1f2227");


// Hide and Remove Flashed messages ---------------------------------------------------------------
$(document).ready(function($){
    setTimeout(function() {
        $('.flash').remove();
    }, 5000);
});



// Clear Form -------------------------------------------------------------------------------------
function clearForm(){
    document.getElementById("form").reset();
}

function submitForm() {
    document.getElementById("form").submit();
    document.getElementById("form").reset();
}


// Scroll to Top function -------------------------------------------------------------------------

//Get the button
var toTopButton = document.getElementById("toTop");
var content = document.getElementsByClassName("content")[0];

// When the user scrolls down 100px from the top of the document, show the button
content.onscroll = function() {
    scrollFunction()
};

function scrollFunction() {
    if (content.scrollTop > 100) {
        toTopButton.style.display = "block";
    } else {
        toTopButton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function toTop() {
    content.scrollTop = 0;
}


// Animation of Loading Screen --------------------------------------------------------------------

const loading_section = document.querySelector(".loading");

window.addEventListener("load", () =>{
    $('.loading').delay(0).fadeOut(500);
    $('.doctor-card').delay(1500).fadeIn(1000);
});

// Deleting Loading HTML DOM
$(document).ready(function($){
    setTimeout(function() {
        $('.loading').remove();
    }, 2000);
});
