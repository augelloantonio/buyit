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


$('.btn-expand-collapse').click(function(e) {
  $('#sidebar-wrapper').toggleClass('collapsed');
});