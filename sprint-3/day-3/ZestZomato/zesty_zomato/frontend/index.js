const dishesContainer = document.getElementById('dishes');

async function fetchDishes() {
    const response = await fetch('/menu/dishes/');
    const data = await response.json();

    let dishesHTML = '<h2>Menu</h2><ul>';
    data.forEach(dish => {
        dishesHTML += `<li>${dish.dish_name} - $${dish.price}</li>`;
    });
    dishesHTML += '</ul>';

    dishesContainer.innerHTML = dishesHTML;
}

fetchDishes();
