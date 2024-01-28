document.addEventListener('DOMContentLoaded', () => {

    // update chips from ingredients saved in session storage upon refreshing page
    let ingredientList = getIngredientList()
    ingredientList.forEach((ingredient) => {
        addIngredientChip(ingredient)
    })
    resetEventListeners() // set all necessary event listeners
})

// get selected ingredients from session storage
function getIngredientList() {
    return JSON.parse(sessionStorage.getItem("ingredients") || "[]")  // if item not in storage, return empty array
}

function addIngredient(inputBox) {
    // validate input
    let ingredients = inputBox.value.split(',')
    ingredients = ingredients.map(function(s) { 
        s = s.trim();
        return s
    }).filter(function(s) {
        return s.length > 0
    });
    if(ingredients == ['']) return alert('No ingredients received!');
    let ingredientList = getIngredientList();
    
    ingredients.map(function(e) {
        if (!ingredientList.includes(e)) {
            ingredientList.push(e);
            addIngredientChip(e);
        }
    })
    // add input to session storage ingredient list
    // ingredientList.push(ingredient)
    sessionStorage.setItem("ingredients", JSON.stringify(ingredientList));
    // reset input box
    inputBox.value = '';
};

function addIngredientChip(ingredient) {
    let chipsDiv = document.querySelector('#chips')
    // template chip html
    let chipInnerHTML = `
        <span>${ingredient}</span>
        <button class="chip-x" aria-label="Remove tag"><i class="fa-solid fa-x fa-xs"></i></button>
    `
    // create chip from template html
    let chip = document.createElement('div')
    chip.classList.add('chip')
    chip.innerHTML = chipInnerHTML
    // add functionality to remove button in chip
    let removeBtn = chip.querySelector('button')
    setupRemoveChipBtn(removeBtn)
    // add chip to DOM
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

function resetEventListeners() {
    let inputBox = document.querySelector('#search')  // get input box element
    let addIngredientBtn = document.querySelector('#add-ingredient')  // get add ingredient button element
    let pageLogo = document.querySelector('#page-logo')
    // Add ingredient on button press
    addIngredientBtn.addEventListener('click', () => {
        addIngredient(inputBox)
        // animate logo
        pageLogo.classList.remove('anim')
        void pageLogo.offsetWidth;
        pageLogo.classList.add('anim')
    })

    // Add ingredient by clicking enter on keyboard
    inputBox.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
          event.preventDefault();
          addIngredientBtn.click();
        }
    })
     // send ingredients from sessionStorage to backend on button press
     document.getElementById('submit').onclick = function() {
        let ingredients = sessionStorage.getItem("ingredients");
        if (!(ingredients == [])) {
            $.ajax({
                type: "POST",
                url: "/",
                data: JSON.stringify(ingredients),
                contentType: "application/json; charset=utf-8",
                // successful ajax request-response
                success: function(text) {
                    // render html to window
                    document.documentElement.innerHTML = text
                    // update ingredient chips
                    let chips = document.querySelector('#chips')
                    chips.childNodes.forEach(e => {
                        if(e.nodeName != '#text' && e.nodeName != '#comment'){ // ignore whitespace and comments
                            btn = e.querySelector('button')
                            setupRemoveChipBtn(btn)
                        }
                        // reset event listeners
                        resetEventListeners()
                    })
                }
            });
        } else {
            alert("Please add at least one ingredient.")
        }
     };
}