const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".login-container");

const sign_in_btn2 = document.querySelector("#sign-in-btn2");
const sign_up_btn2 = document.querySelector("#sign-up-btn2");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

sign_up_btn2.addEventListener("click", () => {
    container.classList.add("sign-up-mode2");
});
sign_in_btn2.addEventListener("click", () => {
    container.classList.remove("sign-up-mode2");
});

// document.addEventListener('DOMContentLoaded', function() {
//   const inputs = document.querySelectorAll('.sliding-placeholder');

//   inputs.forEach(input => {
//     input.addEventListener('focus', function() {
//       this.classList.add('active');
//     });

//     input.addEventListener('blur', function() {
//       if (this.value === '') {
//         this.classList.remove('active');
//       }
//     });
//   });
// });


// // Login Customization
// document.addEventListener('DOMContentLoaded', function() {
//   const inputs = document.querySelectorAll('.form-control');

//   inputs.forEach(function(input) {
//     input.addEventListener('focus', function() {
//       this.previousElementSibling.style.transform = 'translateY(-150%) scale(0.8)';
//     });

//     input.addEventListener('blur', function() {
//       if (this.value === '') {
//         this.previousElementSibling.style.transform = 'translateY(0) scale(1)';
//       }
//     });
//   });
// });


// // Sign up customization
// document.addEventListener('DOMContentLoaded', function() {
//   const inputs = document.querySelectorAll('.form-control');

//   inputs.forEach(function(input) {
//     input.addEventListener('focus', function() {
//       this.previousElementSibling.style.transform = 'translateY(-150%) scale(0.8)';
//     });

//     input.addEventListener('blur', function() {
//       if (this.value === '') {
//         this.previousElementSibling.style.transform = 'translateY(0) scale(1)';
//       }
//     });
//   });
// });
