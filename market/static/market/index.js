document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('#ten').addEventListener('click', () => setCredit(10);
    document.querySelector('#twenty').addEventListener('click', () => setCredit(20));
    document.querySelector('#Hundred').addEventListener('click', () => setCredit(100));
});

function setCredit(amount) {
    document.querySelector('#credit_amount').value = amount;
    document.querySelector('h3').innerHTML = `Your credit is ${amount}`;
}



document.addEventListener("DOMContentLoaded", function () {
    function addGoods(name, price) {
        let goodsElement = document.createElement('div');
        goodsElement.innerText = `${name} - ${price}$`;
        document.querySelector('.goods').appendChild(goodsElement);
    }
});

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('checkout').addEventListener('click', function (event) {
        let totalPrice = parseFloat('{{ total_price }}');
        let userCredit = parseFloat('{{ request.user.credit_user }}');

        if (userCredit < totalPrice) {
            // Create a custom element to display the message
            let alertElement = document.createElement('div');
            alertElement.className = 'alert alert-danger';
            alertElement.textContent = 'Insufficient credit. Please add credit to your account.';

            // Insert the alert above the checkout button
            let checkoutButton = document.getElementById('checkout');
            checkoutButton.parentNode.insertBefore(alertElement, checkoutButton);

            // Prevent the default action (going to the credit increase page)
            event.preventDefault();
        }
    });
});
