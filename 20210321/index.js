const btn = document.querySelector('.mobile-menu__btn');
const container = document.querySelector('#container');

btn.addEventListener('click', function(){
        container.classList.toggle('inview');
    }
);