document.addEventListener('DOMContentLoaded', () => {
    let inputBox = document.querySelector('#search')  // get input box element
    let addIngredientBtn = document.querySelector('#add-ingredient')  // get add ingredient button element
    
    addIngredientBtn.addEventListener('click', () => {
        addIngredient(inputBox)
    })
})

function addIngredient(inputBox) {
    // validate input
    let ingredient = inputBox.value.trim()
    if(!ingredient) return; 
    let ingredientList = JSON.parse(sessionStorage.getItem("ingredients") || "[]"); // get selected ingredients from session storage
    if(ingredientList.includes(ingredient)) return; 
    
    // add input to session storage ingredient list
    ingredientList.push(ingredient)
    sessionStorage.setItem("ingredients", JSON.stringify(ingredientList))
    // reset input box
    inputBox.value = ''
};