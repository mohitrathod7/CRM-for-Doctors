$('.fa-filter').click(function(){ 
    $(".overlay").css("display", "block");
    $(".filter").css("display", "block");
    $("body").css("pointer-events", "none");
        
    $('.fa-times').click(function(){ 
        $(".filter").css("display", "none");
        $("body").css("pointer-events", "all");
        $(".overlay").css("display", "none");
    });
});

$('.fa-exchange').click(function(){ 
    $(".overlay").css("display", "block");
    $(".sort").css("display", "block");
    $("body").css("pointer-events", "none");
        
    $('.fa-times').click(function(){ 
        $(".sort").css("display", "none");
        $("body").css("pointer-events", "all");
        $(".overlay").css("display", "none");
    });
});
