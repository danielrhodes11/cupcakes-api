function fetchAndRenderCupcakes() {
    axios.get('/api/cupcakes')
        .then(response => {
            const cupcakes = response.data.cupcakes;
            const cupcakeList = document.getElementById('cupcake-list');
            cupcakeList.innerHTML = '';

            cupcakes.forEach(cupcake => {
                const listItem = document.createElement('li');
                listItem.textContent = `${cupcake.flavor} - Size: ${cupcake.size}, Rating: ${cupcake.rating}`;
                cupcakeList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching cupcakes:', error);
        });
}

// Fetch cupcakes and render them when the page loads
fetchAndRenderCupcakes();

// Add event listener for form submission
document.getElementById('add-cupcake-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = {
        flavor: document.getElementById('flavor').value,
        size: document.getElementById('size').value,
        rating: parseFloat(document.getElementById('rating').value),
        image: document.getElementById('image').value
    };

    axios.post('/api/cupcakes', formData)
        .then(response => {
            console.log('Cupcake added:', response.data.cupcake);
            fetchAndRenderCupcakes(); // Fetch and render cupcakes after adding a new one
        })
        .catch(error => {
            console.error('Error adding cupcake:', error);
        });
});


