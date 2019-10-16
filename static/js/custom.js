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
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
};

// jQuery functions
//collapse sidebar in dashboard
$(document).ready(function() {
  $(".btn-expand-collapse").click(function(e) {
    $("#sidebar-wrapper").toggleClass("collapsed");
  });

  // If screen size < 960px use sidebar collepsed
  if ($(window).width() < 960) {
    $("#sidebar-wrapper").addClass("collapsed");
  } else {
    $("#sidebar-wrapper").removeClass("collapsed");
  }

  // Add style to total price if discount code is applied
  if ($("#new_total").is(":visible")) {
    $("#total").addClass("basic_price_lined");
    console.log("visible");
  } else {
    $("#total").removeClass("basic_price_lined");
    console.log("not visible");
  }
});
