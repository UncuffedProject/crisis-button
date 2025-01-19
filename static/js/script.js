async function showCategories() {
    try {
        const response = await fetch("/get_categories");
        const data = await response.json();

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
    } catch (error) {
        console.error("Error fetching categories:", error);
    }
}

async function showSubcategories(category) {
    try {
        const response = await fetch("/get_subcategories", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ category })
        });
        const data = await response.json();

        const grid = document.getElementById("grid-container");
        const descriptionBox = document.getElementById("description-box");
        grid.innerHTML = "";

        data.subcategories.forEach(subcategory => {
            const button = document.createElement("button");
            button.className = "button";
            button.textContent = subcategory;
            button.onclick = () => showDescription(subcategory);
            grid.appendChild(button);
        });

        descriptionBox.style.display = "none";
    } catch (error) {
        console.error("Error fetching subcategories:", error);
    }
}

async function showDescription(subcategory) {
    try {
        const response = await fetch("/get_description", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ subcategory })
        });
        const data = await response.json();

        const descriptionBox = document.getElementById("description-box");
        descriptionBox.textContent = data.description;
        descriptionBox.style.display = "block";
    } catch (error) {
        console.error("Error fetching description:", error);
    }
}
