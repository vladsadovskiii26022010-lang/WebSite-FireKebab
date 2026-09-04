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