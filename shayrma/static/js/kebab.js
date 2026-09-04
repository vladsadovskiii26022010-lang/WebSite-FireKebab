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

function getCSRFToken() {
    const token = document.querySelector('[name=csrfmiddlewaretoken]');
    if (token) {
        return token.value;
    }
    return '';
}
function updatemass(mass, product_ID) {
    const massa = document.getElementById(`massa-${product_ID}`);
    const price = document.getElementById(`price-${product_ID}`);

    if (mass == 300) {
        massa.textContent = `Масса: ${mass} г`;
        price.textContent = '8 BYN';
    }
    if (mass == 400) {
        massa.textContent = `Масса: ${mass} г`;
        price.textContent = '12.5 BYN';
    }
    if (mass == 500) {
        massa.textContent = `Масса: ${mass} г`;
        price.textContent = '14 BYN';
    }
    if (mass == 650) {
        massa.textContent = `Масса: ${mass} г`;
        price.textContent = '16.5 BYN';
    }
    const data = {
        mass: mass,
        product_id: product_ID
    }
    console.log('Отправка:', data);
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(data)
        })
}