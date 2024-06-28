document.addEventListener('DOMContentLoaded', () => {
    const cart = [];
    const cartBody = document.querySelector('.cart-body');
    const cartTotal = document.getElementById('cart-total');

    function updateCart() {
        cartBody.innerHTML = '';
        let total = 0;
        cart.forEach(item => {
            const row = document.createElement('div');
            row.classList.add('row', 'mb-3');
            row.innerHTML = `
                <div class="col-md-6">${item.name}</div>
                <div class="col-md-2">${item.price.toFixed(2)}</div>
                <div class="col-md-2">
                    <input type="number" class="form-control" value="${item.quantity}" min="1" data-id="${item.id}">
                </div>
                <div class="col-md-2">${(item.price * item.quantity).toFixed(2)}</div>
            `;
            cartBody.appendChild(row);
            total += item.price * item.quantity;
        });
        cartTotal.textContent = total.toFixed(2);
    }

    function addToCart(product) {
        const existingProduct = cart.find(item => item.id === product.id);
        if (existingProduct) {
            existingProduct.quantity += 1;
        } else {
            cart.push({ ...product, quantity: 1 });
        }
        updateCart();
    }

    // Aquí agregarías lógica para añadir productos al carrito desde otras partes de la página
    // Ejemplo:
    // addToCart({ id: 1, name: 'Parlantes Xtech Luces Leds', price: 15.00 });

    cartBody.addEventListener('input', (event) => {
        if (event.target.type === 'number') {
            const id = parseInt(event.target.dataset.id, 10);
            const quantity = parseInt(event.target.value, 10);
            const product = cart.find(item => item.id === id);
            if (product) {
                product.quantity = quantity;
                updateCart();
            }
        }
    });

    // Para pruebas, añadir algunos productos iniciales
    addToCart({ id: 1, name: 'Parlantes Xtech Luces Leds', price: 15.00 });
    addToCart({ id: 2, name: 'Pendrive Sandisk 32GB', price: 5.00 });
});
