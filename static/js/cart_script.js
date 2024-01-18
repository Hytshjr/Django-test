document.addEventListener('DOMContentLoaded', function () {
    const maxQuantity = 24;
    const minQuantity = 0;

    const quantityElements = document.querySelectorAll('.number-count-product');

    function updateQuantity(cartId, quantity, link, csrfToken) {

        return fetch(`/cart/${link}/${cartId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ quantity: quantity }),
        })
        .then(response => response.json())
        .catch(error => {
            console.error('Error:', error);
            throw new Error('Failed to update quantity.');
        });
    }

    function handleButtonClick(index, action, csrfToken) {
        let currentQuantity = parseInt(quantityElements[index].textContent);

        if (action === 'decrease' && currentQuantity > minQuantity) {
            quantityElements[index].textContent = currentQuantity - 1;

            if (quantityElements[index].textContent == 0) {
                const cartId = quantityElements[index].dataset.cartid;
                updateQuantity(cartId, quantityElements[index].textContent, 'delete_to_cart', csrfToken)
                    .then(() => window.location.reload())
                    .catch(error => console.error('Error:', error));
            } else {
                const cartId = quantityElements[index].dataset.cartid;
                updateQuantity(cartId, quantityElements[index].textContent, 'add_to_cart', csrfToken)
                    .then(() => null)
                    .catch(error => console.error('Error:', error));
            }
        }

        if (action === 'increase' && currentQuantity < maxQuantity) {
            quantityElements[index].textContent = currentQuantity + 1;

            const cartId = quantityElements[index].dataset.cartid;
            updateQuantity(cartId, quantityElements[index].textContent,'add_to_cart', csrfToken)
                .catch(error => console.error('Error:', error));
        }
    }

    const minusButtons = document.querySelectorAll('.menos-count-product button');
    const plusButtons = document.querySelectorAll('.plus-count-product button');

    minusButtons.forEach((button, index) => {
        button.addEventListener('click', () => handleButtonClick(index, 'decrease', csrfToken));
    });

    plusButtons.forEach((button, index) => {
        button.addEventListener('click', () => handleButtonClick(index, 'increase', csrfToken));
    });
});