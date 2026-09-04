
function getCSRFToken() {
    const token = document.querySelector('[name=csrfmiddlewaretoken]');
    if (token) {
        return token.value;
    }
    return '';
}

function col_add(mark, products_id){
    const quantityElement = document.getElementById(`quantity-${products_id}`)
    let quantity = parseInt(quantityElement.textContent) || 1
    if (mark === '+'){
        quantity++
    }
    if (mark === '-' && quantity > 1){
        quantity--
    }
    quantityElement.textContent = quantity
    updateTotalPrice();
    const data = {
        products_id:  products_id,
        quantity: quantity
    }
    console.log(data)
    fetch('/card/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(data)
        })
    }

function delete_product (button, delete_id){
    const closest_class = button.closest('.cart-item')
    closest_class.style.animation = 'fadeOut 0.3s ease'
    setTimeout(() => {
        closest_class.remove()
        updateCartCount()
        updateTotalPrice()
        }, 300)
    const data = {delete_id: delete_id}
    console.log(data)
    fetch('/card/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(data)
        })
}


//document.querySelectorAll('.remove-btn').forEach(btn => {
//    btn.addEventListener('click', function() {
//        const item = this.closest('.cart-item');
//        item.style.animation = 'fadeOut 0.3s ease';
//        setTimeout(() => {
//            item.remove();
//            updateCartCount();
//            updateTotalPrice();
//        }, 300);
//    });
//});

function updateCartCount() {
    const itemCount = document.querySelectorAll('.cart-item').length;
    const countElement = document.querySelector('.cart-count');
    if (countElement) {
        countElement.textContent = itemCount + ' товар' + getPluralEnding(itemCount);
    }
}

function getPluralEnding(count) {
    if (count % 10 === 1 && count % 100 !== 11) {
        return '';
    } else if ([2, 3, 4].includes(count % 10) && ![12, 13, 14].includes(count % 100)) {
        return 'а';
    } else {
        return 'ов';
    }
}

function updateTotalPrice() {
    let total = 0;

    document.querySelectorAll('.cart-item').forEach(item => {
        const priceElement = item.querySelector('.price-main');
        const quantityElement = item.querySelector('.quantity');

        if (priceElement && quantityElement) {
            const price = parseFloat(priceElement.textContent.replace(' р', '').replace(',', '.'));
            const quantity = parseInt(quantityElement.textContent);
            total += price * quantity;
        }
    });

    const totalElement = document.querySelector('.summary-total span:last-child');
    if (totalElement) {
        totalElement.textContent = total.toFixed(2) + ' р';
    }

    const itemsTotalElement = document.querySelector('.summary-line:first-child span:last-child');
    if (itemsTotalElement) {
        itemsTotalElement.textContent = total.toFixed(2) + ' р';
    }

    console.log('Обновление суммы: ' + total.toFixed(2) + ' р');
}

function updateDiscount(discount) {
    const discountElement = document.querySelector('.summary-line:nth-child(2) span:last-child');
    if (discountElement) {
        discountElement.textContent = '-' + discount.toFixed(2) + ' р';
        discountElement.style.color = '#2ecc71';
    }

    updateTotalPrice();
}

document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
    updateTotalPrice();

    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeOut {
            from { opacity: 1; transform: translateX(0); }
            to { opacity: 0; transform: translateX(-100px); }
        }

        .cart-item {
            transition: transform 0.2s, box-shadow 0.2s;
        }
    `;
    document.head.appendChild(style);
});

function addToCart(product) {
    console.log('Добавлен товар:', product);
}

function clearCart() {
    const cartItems = document.querySelector('.cart-items');
    if (cartItems) {
        cartItems.innerHTML = '';
        updateCartCount();
        updateTotalPrice();
    }
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        updateCartCount,
        updateTotalPrice,
        addToCart,
        clearCart,
        applyPromoCode
    };
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