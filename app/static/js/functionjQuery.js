$(document).ready(function () {
    console.log("Hello! Do not give up!!!")
    // Text dhe html
    // $(".text > button").on("click", function () {
    //     let h2 = $(".text h2")
    //     // h2.text("Hello jQuery!")
    //     h2.html('<img src="images/banner.jpg">')
    //     $("img").css({ width: "200px", height: "200px", objectFit: "cover" })
    // })
    $(".text > button").on({
        "click": function () {
            let h2 = $(".text h2")
            // h2.text("Hello jQuery!")
            h2.html('<img src="images/banner.jpg">')
            $("img").css({ width: "200px", height: "200px", objectFit: "cover" })
        },
        "mouseenter": function () {
            let h2 = $(".text h2")
            h2.css("color", "red")
        },
        "mouseleave": function () {
            let h2 = $(".text h2")
            h2.text("color")
        }
    })
    // Form
    // $("form").on("submit", function (event) {
    //     event.preventDefault()
    //     let firstName = $("#firstName").val()
    //     let lastName = $("#lastName").val()
    //     let email = $("#email").val()
    //     let comment = $("#comment").val()

    //     if (firstName == "" || lastName == "" || email == "" || comment == "") {
    //         $(".sms").text("Ju lutemi te plotesoni fushat")
    //         $(".sms").addClass("alert-danger")
    //         $(".sms").removeClass("alert-success")
    //     } else {
    //         $(".sms").text("Faleminderit " + firstName + " " + lastName +
    //             ". Do t'ju kontaktojme ne adresen " + email + " .")
    //         $(".sms").addClass("alert-success")
    //         $(".sms").removeClass("alert-danger")
    //     }

    // })

    // Navbar
    let nav = $("nav")
    $(window).on("scroll", function () {
        let heightWindow = $(window).scrollTop()
        console.log(heightWindow)
        if (heightWindow > 400) {
            nav.css("background-color", "rgb(104, 70, 39)")
        } else {
            nav.css("background-color", "transparent")
        }
    })
})