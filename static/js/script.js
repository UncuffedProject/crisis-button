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
                <p>Website: <a href="${resource.website}" target="_blank">${resource.website || "Not available"}</a></p>
            `;
            descriptionBox.appendChild(resourceElement);
        });

        descriptionBox.style.display = "block";
    } catch (error) {
        console.error("Error loading description and resources:", error);
        alert("Failed to load description and resources. Please try again.");
    }
}

function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                console.log("Current Location:", latitude, longitude);
                fetchResourcesWithLocation(latitude, longitude);
            },
            (error) => {
                alert("Unable to fetch your location. Please try again.");
                console.error("Geolocation Error:", error);
            }
        );
    } else {
        alert("Geolocation is not supported by your browser.");
    }
}

function useManualLocation() {
    const location = document.getElementById("manual-location").value;
    if (!location) {
        alert("Please enter a location.");
        return;
    }
    console.log("Manual Location:", location);

    fetch("/geocode_location", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ location: location })
    })
    .then(response => response.json())
    .then(data => {
        if (data.latitude && data.longitude) {
            fetchResourcesWithLocation(data.latitude, data.longitude);
        } else {
            alert("Could not fetch coordinates for the entered location.");
        }
    })
    .catch(error => console.error("Error geocoding location:", error));
}

function fetchResourcesWithLocation(latitude, longitude) {
    const subcategory = "Earthquakes"; // Replace this with the selected subcategory dynamically.
    fetch("/get_description", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            subcategory: subcategory,
            latitude: latitude,
            longitude: longitude
        })
    })
    .then(response => response.json())
    .then(data => {
        const descriptionBox = document.getElementById("description-box");
        descriptionBox.innerHTML = `<p>${data.description || "Description not available."}</p>`;

        if (data.resources && data.resources.length > 0) {
            const resourcesList = document.createElement("ul");
            data.resources.forEach(resource => {
                const resourceItem = document.createElement("li");
                resourceItem.innerHTML = `
                    <strong>${resource.name || "Name not available"}</strong><br>
                    Address: ${resource.address || "Not available"}<br>
                    Phone: ${resource.phone || "Not available"}<br>
                    Website: <a href="${resource.website || "#"}" target="_blank">${resource.website || "Not available"}</a>
                `;
                resourcesList.appendChild(resourceItem);
            });
            descriptionBox.appendChild(resourcesList);
        } else {
            descriptionBox.innerHTML += `<p>No resources found nearby.</p>`;
        }
    })
    .catch(error => console.error("Error fetching resources:", error));
}
