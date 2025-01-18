function showCategories() {
    fetch("/get_categories")
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById("grid-container");
            grid.innerHTML = "";
            data.categories.forEach(category => {
                const button = document.createElement("button");
                button.className = "button";
                button.textContent = category;
                button.onclick = () => showSubcategories(category);
                grid.appendChild(button);
            });
            grid.style.display = "grid";
        });
}

function showSubcategories(category) {
    fetch("/get_subcategories", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ category })
    })
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById("grid-container");
            const descriptionBox = document.getElementById("description-box");
            grid.innerHTML = "";
            data.subcategories.forEach(subcategory => {
                const button = document.createElement("button");
                button.className = "button";
                button.textContent = subcategory;
                button.onclick = () => {
                    if (category === "Natural Disasters") {
                        showSubcategories(subcategory); // Handle nested subcategories
                    } else {
                        showDescription(subcategory); // Handle leaf nodes
                    }
                };
                grid.appendChild(button);
            });
            descriptionBox.style.display = "none";
        });
}

function showDescription(subcategory) {
    fetch("/get_description", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ subcategory })
    })
        .then(response => response.json())
        .then(data => {
            const descriptionBox = document.getElementById("description-box");
            descriptionBox.textContent = data.description;
            descriptionBox.style.display = "block";
        });
}
