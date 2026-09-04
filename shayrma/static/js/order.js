const located = document.getElementById('located')

function searchlocation (){
    const latitude = 53.9070978;
    const longitude = 27.4461857;
    const address = 'ул.Притыцкого 78, Минск';
    const encodedAddress = encodeURIComponent(address);
    const isMobile = /Android|iPhone|iPad|iPod|BlackBerry|Opera Mini|IEMobile/i.test(navigator.userAgent);
    window.open(`https://www.google.com/maps/dir//${latitude},${longitude}`, '_blank');
}



located.addEventListener('click', searchlocation)


document.addEventListener('DOMContentLoaded', phone)
function phone (){
    const element = document.getElementById('InputPhone');

    const maskOptions = {
        mask: '+{375} (00) 000-00-00',
        lazy: false
    };

    // Инициализация маски
    const mask = IMask(element, maskOptions);
}
const modal = document.getElementById('modal');
const burer_btn = document.getElementById('burer_btn');
const closeBtn = document.querySelector('.close-btn');

function open_model_window(){
    modal.style.display = 'flex';
}
function close_model_window(){
    modal.style.display = 'none'
}
burer_btn.addEventListener('click', open_model_window)
closeBtn.addEventListener('click', close_model_window)
window.addEventListener('click', (event) =>{
    if (event.target == modal) {
        modal.style.display = 'none';
    }
})