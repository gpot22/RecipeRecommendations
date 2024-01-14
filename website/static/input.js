document.addEventListener('DOMContentLoaded', () => {
    let inputBox = document.querySelector('#search')  // get input box element
    let addIngredientBtn = document.querySelector('#add-ingredient')  // get add ingredient button element
    
    addIngredientBtn.addEventListener('click', () => {
        addIngredient(inputBox)
    })
})

function addIngredient(inputBox) {
    let ingredient = inputBox.value.trim()
    if(!ingredient) return;
    let ingredientList = JSON.parse(sessionStorage.getItem("ingredients") || "[]");
    if(ingredientList.includes(ingredient)) return;
    ingredientList.push(ingredient)
    sessionStorage.setItem("ingredients", JSON.stringify(ingredientList))
    inputBox.value = ''
    // // Adding ingredient
    // ingredients.push(ingredient);

    // // Saving
    // sessionStorage.setItem("ingredients", JSON.stringify(ingredients));
    // // console.log('hi')
    // // console.log(ingredients)

    // // Don't submit form
    // return false;
};