/**
 * This function will give to the navbar the effect to hide it scrolling down by
 * moving the navbar out the viewport of the user adding the style "top: -50px";
 * When the page scroll up the bar will appear again by adding back the style "top: 0".
 * The scrolling has a transition effect added in the css file
 */

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    if (window.pageYOffset >= 60) {
        var currentScrollPos = window.pageYOffset;
        if (prevScrollpos > currentScrollPos) {
            document.getElementById("navbar").style.top = "";
        } else {
            document.getElementById("navbar").style.top = "-60px";
        }
        prevScrollpos = currentScrollPos;
    }
};

// jQuery functions
$(document).ready(function () {
    //collapse sidebar in dashboard

    $(".btn-expand-collapse").click(function (e) {
        $("#sidebar-wrapper").toggleClass("collapsed");
    });

    // Add style to total price if discount code is applied
    if ($("#new_total").is(":visible")) {
        $("#total").addClass("basic_price_lined");
    } else {
        $("#total").removeClass("basic_price_lined");
    }

    // Auto Hide Messages
    setTimeout(function () {
        $(".alert").hide();
    }, 4000);
});

// Add script for spinner
$("#quantityspinner").TouchSpin({
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


//EmailJs 
function sendMail(contactForm) {
    emailjs.send("gmail", "buyit", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "order": contactForm.order.value,
            "enquiry": contactForm.enquiry.value
        })
        .then(
            function (response) {
                var alert = '<div class="alert alert-success" role="alert"> Your message has been sent.You will receive an answer as soon as possible.</div>'
                document.getElementById("email-alert").innerHTML = alert;
            },
            function (error) {
                var alert = '<div class="alert alert-danger" role="alert">Your message was not sent. Please check that all the details are correct.</div>'
                document.getElementById("email-alert").innerHTML = alert;
            }
        );
    return false; // To block from loading a new page
}