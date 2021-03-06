//jshint esversion: 6

$(document).ready(function () {
    // Code from: https://bulma.io/documentation/components/navbar/

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });

    // Modal for delete functions
    // https://stackoverflow.com/questions/27650584/multiple-modals#27650708
    $(".button").click(function(){
    $(".modal").removeClass("is-active");
    var Type = $(this).data("modal-type");
    $("#"+Type).addClass("is-active");
});
});
// Close function for notifications: https://martincarlin.uk/2016/02/15/bulma-css-framework-add-functionality-to-dismiss-notifications/
$(document).on('click', '.notification > button.delete', function() {
    $(this).parent().addClass('is-hidden');
    return false;
});