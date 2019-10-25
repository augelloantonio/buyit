/**
 * This function will give to the navbar the effect to hide it scrolling down by
 * moving the navbar out the viewport of the user adding the style "top: -50px";
 * When the page scroll up the bar will appear again by adding back the style "top: 0".
 * The scrolling has a transition effect added in the css file
 */

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "";
    } else {
        document.getElementById("navbar").style.top = "-50px";
    }
    prevScrollpos = currentScrollPos;
};

// jQuery functions
$(document).ready(function() {
    //collapse sidebar in dashboard

    $(".btn-expand-collapse").click(function(e) {
        $("#sidebar-wrapper").toggleClass("collapsed");
    });

    // Add style to total price if discount code is applied
    if ($("#new_total").is(":visible")) {
        $("#total").addClass("basic_price_lined");
        console.log("visible");
    } else {
        $("#total").removeClass("basic_price_lined");
        console.log("not visible");
    }

    // Auto Hide Messages
    setTimeout(function() {
        $(".alert").hide();
    }, 2000);
});

// Add script for spinner
$("#demo9").TouchSpin({
    buttondown_class: "btn btn-link",
    buttonup_class: "btn btn-link"
});

// Search Form activator
function searchToggle() {
    if ($("#input-search").hasClass("hidden-input")) {
        $("#input-search").removeClass("hidden-input");
    } else {
        $("#input-search").addClass("hidden-input");
    }
}