const navHamburger = document.getElementsByClassName('navHamburger')[0]
const menu = document.getElementsByClassName('menu')[0]
const submenu = document.getElementsByClassName('submenu')[0]

let isOpen = false

navHamburger.addEventListener('click', () => {
    isOpen = !isOpen
    menu.classList.add('mobNavOpen')
    menu.style.display = 'flex'
})

submenu.addEventListener('click', () => {
    if (isOpen) {
        menu.style.display = 'none'
    }
})