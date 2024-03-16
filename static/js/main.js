(function () {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            var spinnerElement = document.getElementById('spinner');
            if (spinnerElement) {
                spinnerElement.classList.remove('show');
            }
        }, 1);
    };
    spinner();


    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    window.addEventListener('scroll', function () {
        var stickyTop = document.querySelector('.sticky-top');
        if (window.pageYOffset > 300) {
            stickyTop.style.top = '0px';
        } else {
            stickyTop.style.top = '-100px';
        }
    });


    // Dropdown on mouse hover
    var dropdowns = document.querySelectorAll(".dropdown");

    function handleDropdown(event) {
        var dropdown = this;
        var dropdownToggle = dropdown.querySelector(".dropdown-toggle");
        var dropdownMenu = dropdown.querySelector(".dropdown-menu");
        if (event.type === 'mouseenter') {
            dropdown.classList.add('show');
            dropdownToggle.setAttribute('aria-expanded', 'true');
            dropdownMenu.classList.add('show');
        } else if (event.type === 'mouseleave') {
            dropdown.classList.remove('show');
            dropdownToggle.setAttribute('aria-expanded', 'false');
            dropdownMenu.classList.remove('show');
        }
    }

    window.addEventListener("load", function () {
        if (window.matchMedia("(min-width: 992px)").matches) {
            dropdowns.forEach(function (dropdown) {
                dropdown.addEventListener('mouseenter', handleDropdown);
                dropdown.addEventListener('mouseleave', handleDropdown);
            });
        } else {
            dropdowns.forEach(function (dropdown) {
                dropdown.removeEventListener('mouseenter', handleDropdown);
                dropdown.removeEventListener('mouseleave', handleDropdown);
            });
        }
    });


    // Back to top button
    window.addEventListener('scroll', function () {
        var backToTop = document.querySelector('.back-to-top');
        if (window.pageYOffset > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });
    document.querySelector('.back-to-top').addEventListener('click', function () {
        var scrollOptions = {
            top: 0,
            behavior: 'smooth'
        };
        window.scrollTo(scrollOptions);
    });


    // Header carousel
    var headerCarousel = new Siema({
        selector: '.header-carousel',
        loop: true,
        duration: 1500,
        perPage: 1,
        easing: 'ease-out'
    });
    setInterval(function () {
        headerCarousel.next();
    }, 5000);


    // Testimonials carousel
    var testimonialCarousel = new Siema({
        selector: '.testimonial-carousel',
        loop: true,
        duration: 1000,
        perPage: {
            0: 1,
            768: 2,
            992: 3
        },
        easing: 'ease-out'
    });
    setInterval(function () {
        testimonialCarousel.next();
    }, 4000);

})();
