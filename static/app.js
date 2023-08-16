function fetchAndRenderCupcakes() {
    axios.get('/api/cupcakes')
        .then(response => {
            const cupcakes = response.data.cupcakes;
            const cupcakeList = document.getElementById('cupcakes-list');
            cupcakeList.innerHTML = '';

            cupcakes.forEach(cupcake => {
                const listItem = document.createElement('li');
                listItem.textContent = `Flavor: ${cupcake.flavor} - Size: ${cupcake.size}, Rating: ${cupcake.rating}`;

                if (cupcake.image) {
                    const image = document.createElement('img');
                    image.src = cupcake.image;
                    image.alt = `Image of ${cupcake.flavor} Cupcake`;
                    listItem.appendChild(image);
                }

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
            fetchAndRenderCupcakes();
        })
        .catch(error => {
            console.error('Error adding cupcake:', error);
        });
});

