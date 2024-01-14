document.addEventListener('DOMContentLoaded', () => {
    let inputBox = document.querySelector('#search')  // get input box element
    let addIngredientBtn = document.querySelector('#add-ingredient')  // get add ingredient button element
    
    addIngredientBtn.addEventListener('click', () => {
        addIngredient(inputBox)
    })

    // update chips from ingredients saved in session storage upon refreshing page
    let ingredientList = getIngredientList()
    ingredientList.forEach((ingredient) => {
        addIngredientChip(ingredient)
    })
})

// get selected ingredients from session storage
function getIngredientList() {
    return JSON.parse(sessionStorage.getItem("ingredients") || "[]")  // if item not in storage, return empty array
}

function addIngredient(inputBox) {
    // validate input
    let ingredient = inputBox.value.trim()
    if(!ingredient) return; 
    let ingredientList = getIngredientList();
    if(ingredientList.includes(ingredient)) return; 
    
    // add input to session storage ingredient list
    ingredientList.push(ingredient)
    sessionStorage.setItem("ingredients", JSON.stringify(ingredientList))
    // reset input box
    inputBox.value = ''
    addIngredientChip(ingredient)
};

function addIngredientChip(ingredient) {
    let chipsDiv = document.querySelector('#chips')
    let chipInnerHTML = `
        <span>${ingredient}</span>
        <button class="chip-x" aria-label="Remove tag"><i class="fa-solid fa-x fa-xs"></i></button>
    `
    let chip = document.createElement('div')
    chip.classList.add('chip')
    chip.innerHTML = chipInnerHTML

    let removeBtn = chip.querySelector('button')
    setupRemoveChipBtn(removeBtn)
    chipsDiv.appendChild(chip)
}

function setupRemoveChipBtn(btn) {
    btn.addEventListener('click', () => {
        removeIngredient(btn.parentElement)
    })
}

function removeIngredient(chip) {
    // get ingredient from chip
    let ingredientSpan = chip.querySelector('span')
    let ingredient = ingredientSpan.innerText
    
    // remove ingredient from session storage array
    let ingredientList = getIngredientList()
    let idx = ingredientList.indexOf(ingredient)
    console.log(chip)
    if (idx > -1) { // only splice of found value; if not, remove chip and assume it no longer exists in storage
        ingredientList.splice(idx, 1)
    }
    sessionStorage.setItem('ingredients', JSON.stringify(ingredientList))
    // remove chip
    removeIngredientChip(chip)
}

function removeIngredientChip(chip) {
    chip.remove()
}