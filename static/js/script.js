// Function to show top-level categories
async function showCategories() {
    try {
        const response = await fetch("/get_categories");
        if (!response.ok) throw new Error("Failed to fetch categories.");

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
        console.error("Error loading categories:", error);
        alert("Failed to load categories. Please try again.");
    }
}

// Function to show subcategories for a selected category
async function showSubcategories(category) {
    try {
        const response = await fetch("/get_subcategories", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ category })
        });
        if (!response.ok) throw new Error("Failed to fetch subcategories.");

        const data = await response.json();
        const grid = document.getElementById("grid-container");
        const descriptionBox = document.getElementById("description-box");
        grid.innerHTML = "";

        data.subcategories.forEach(subcategory => {
            const button = document.createElement("button");
            button.className = "button";
            button.textContent = subcategory;
            button.onclick = () => handleSubcategoryClick(subcategory);
            grid.appendChild(button);
        });

        descriptionBox.style.display = "none";
    } catch (error) {
        console.error("Error loading subcategories:", error);
        alert("Failed to load subcategories. Please try again.");
    }
}

// Handle click on a subcategory button
async function handleSubcategoryClick(subcategory) {
    try {
        const response = await fetch("/get_subcategories", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ category: subcategory })
        });

        if (!response.ok) throw new Error("Failed to fetch subcategories or description.");

        const data = await response.json();

        if (data.subcategories && data.subcategories.length > 0) {
            // If there are further subcategories, show them
            showSubcategories(subcategory);
        } else {
            // If no further subcategories, show description
            showDescription(subcategory);
        }
    } catch (error) {
        console.error("Error handling subcategory click:", error);
        alert("Failed to process the subcategory. Please try again.");
    }
}

// Function to show the description for a selected subcategory
async function showDescription(subcategory) {
    try {
        const response = await fetch("/get_description", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ subcategory })
        });
        if (!response.ok) throw new Error("Failed to fetch description.");

        const data = await response.json();
        const descriptionBox = document.getElementById("description-box");
        descriptionBox.textContent = data.description || "No description available.";
        descriptionBox.style.display = "block";
    } catch (error) {
        console.error("Error loading description:", error);
        alert("Failed to load description. Please try again.");
    }
}
