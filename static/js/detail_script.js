document.addEventListener('DOMContentLoaded', function () {
    const maxQuantity = 24;
    const minQuantity = 1;
    const quantityElements = document.querySelectorAll('.number-count-product');

    function handleButtonClick(index, action, ) {
        let currentQuantity = parseInt(quantityElements[index].textContent);

        if (action === 'decrease' && currentQuantity > minQuantity) {
            quantityElements[index].textContent = currentQuantity - 1;
        }

        if (action === 'increase' && currentQuantity < maxQuantity) {
            quantityElements[index].textContent = currentQuantity + 1;
        }
    }

    const minusButtons = document.querySelectorAll('.menos-count-product button');
    const plusButtons = document.querySelectorAll('.plus-count-product button');

    minusButtons.forEach((button, index) => {
        button.addEventListener('click', () => handleButtonClick(index, 'decrease'));
    });

    plusButtons.forEach((button, index) => {
        button.addEventListener('click', () => handleButtonClick(index, 'increase'));
    });
});

document.addEventListener('DOMContentLoaded', function () {
    async function buyButtonClick(index, user, csrfToken, productId) {
        const statusMessage = document.getElementById('status-message');

        if (user == 'True') {
            const quantity = parseInt(document.getElementById('quantity').textContent);

            try {
                const response = await fetch(`/cart/add_to_cart/${productId}/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                    },
                    body: JSON.stringify({ quantity: quantity }),
                });

                const data = await response.json();

                statusMessage.innerText = 'Product added';
                statusMessage.style.marginTop = '10px'; 
                statusMessage.style.marginBottom = '10px'; 
                statusMessage.style.display = 'block'; 
                console.log(data);
            } catch (error) {
                console.error('Error:', error);
                statusMessage.innerText = 'Error adding product';
                statusMessage.style.marginTop = '10px'; 
                statusMessage.style.marginBottom = '10px'; 
                statusMessage.style.display = 'block'; 
            }
        } else {
            statusMessage.innerText = 'Need login to buy.';
            statusMessage.style.marginTop = '10px'; 
            statusMessage.style.marginBottom = '10px'; 
            statusMessage.style.display = 'block'; 
        }
    }


    const buyButtons = document.querySelectorAll('.button-buy');
    
    buyButtons.forEach((button, index) => {
        button.addEventListener('click', () => buyButtonClick(index, user, csrfToken, productId));
    });
    
});
