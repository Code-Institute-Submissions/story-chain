$(document).ready(function () {
    // Code from: https://bulma.io/documentation/components/navbar/

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function () {
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });

    $("#delete_story").click(function() {
        $(".modal").addClass("is-active");
    });
    $(".cancel").click(function() {
        $(".modal").removeClass("is-active");
})});  


// For collapsible cards and other elements, taken from: https://codepen.io/brussell98/pen/mEwxjP?js-preprocessor=livescript
document.addEventListener('DOMContentLoaded', function() {
	let cardToggles = document.getElementsByClassName('card-toggle');
	for (let i = 0; i < cardToggles.length; i++) {
		cardToggles[i].addEventListener('click', e => {
			e.currentTarget.parentElement.parentElement.childNodes[3].classList.toggle('is-hidden');
		});
	}
});