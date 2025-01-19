// Function to get the user's current location
async function getUserLocation() {
    return new Promise((resolve, reject) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                position => resolve(position.coords),
                error => reject(error)
            );
        } else {
            reject("Geolocation is not supported by this browser.");
        }
    });
}

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

// Function to show the description for a selected subcategory and fetch local resources
async function showDescription(subcategory) {
    try {
        // Fetch the description
        const descriptionResponse = await fetch("/get_description", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ subcategory })
        });
        if (!descriptionResponse.ok) throw new Error("Failed to fetch description.");

        const descriptionData = await descriptionResponse.json();
        const descriptionBox = document.getElementById("description-box");
        descriptionBox.innerHTML = `<p>${descriptionData.description || "No description available."}</p>`;

        // Fetch local resources
        const coords = await getUserLocation();
        const resourcesResponse = await fetch("/get_local_resources", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                disaster: subcategory,
                latitude: coords.latitude,
                longitude: coords.longitude
            })
        });
        if (!resourcesResponse.ok) throw new Error("Failed to fetch local resources.");

        const resourcesData = await resourcesResponse.json();
        descriptionBox.innerHTML += `<h3>Local Resources for ${subcategory}</h3>`;
        resourcesData.resources.forEach(resource => {
            const resourceElement = document.createElement("div");
            resourceElement.innerHTML = `
                <p><strong>${resource.name}</strong></p>
                <p>Address: ${resource.address}</p>
                <p>Phone: ${resource.phone}</p>
            `;
            descriptionBox.appendChild(resourceElement);
        });

        descriptionBox.style.display = "block";
    } catch (error) {
        console.error("Error loading description and resources:", error);
        alert("Failed to load description and resources. Please try again.");
    }
}
