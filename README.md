# Crisis Button Project

## **Overview**
The Crisis Button Project is a web application designed to provide **Community Response in Situations Involving Stress**. The app offers a categorized list of crisis events, subcategories, detailed descriptions, and now includes local resources to help users access relevant services during emergencies.

---

## **Features**
- **Interactive UI**: A clean, mobile-friendly interface with a dynamic red crisis button.
- **Crisis Categories**: Comprehensive list of crisis events, including natural disasters, medical emergencies, and more.
- **Subcategories and Descriptions**: Detailed breakdown and descriptions for each crisis event.
- **Local Resources Integration**: Fetches and displays nearby resources relevant to the selected crisis using the Geolocation API.
- **Data Separation**: Modular design with crisis data stored in separate Python files for easy maintenance.
- **Extensibility**: Built using Flask, allowing easy addition of new features.
- **Deployment Ready**: Includes Render-compatible files for easy deployment.

---

## **Project Structure**
```plaintext
crisis_button_project/
│
├── crisis_button.py                                 # Main Flask application
├── LICENSE                                          # License file (GPL-3.0)
├── ping_render.py                                   # Render-specific ping script
├── README.md                                        # Project documentation
├── requirements.txt                                 # Python dependencies
├── Procfile                                         # Process file for Render
├── runtime.txt                                      # Python runtime specification
│
├── disasters/                                       # Disaster-related logic and data
│   ├── __init__.py                                  # Package initialization file
│   ├── disaster_types.py                            # File containing all crisis categories
│   ├── disaster_descriptions/                       # Organized disaster descriptions
│   │   ├── __init__.py
│   │   ├── natural_disaster_descriptions.py
│   │   ├── man_made_disaster_descriptions.py
│   │   ├── medical_emergency_descriptions.py
│   │   ├── mental_health_crisis_descriptions.py
│   │   └── disaster_descriptions.py                 # Aggregated descriptions
│   ├── disaster_names/                              # Organized disaster names
│   │   ├── __init__.py
│   │   ├── natural_disaster_names.py
│   │   ├── man_made_disaster_names.py
│   │   ├── medical_emergency_names.py
│   │   └── mental_health_crisis_names.py
│
├── static/                                          # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css                               # Stylesheet for the project
│   ├── images/                                      # Images (optional)
│   └── js/
│       └── script.js                                # JavaScript for interactivity
│
└── templates/                                       # HTML templates
    └── index.html                                   # Main HTML file
```

---

## **Technologies Used**
- **Frontend**:
  - HTML
  - CSS
  - JavaScript (with Geolocation API)
- **Backend**:
  - Python
  - Flask
- **Deployment**:
  - Render
- **Other Libraries**:
  - `geopy` (for location-based features)
  - `requests` (for fetching external resources)

---

## **Setup and Installation**
Follow these steps to run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/UncuffedProject/crisis-button.git
   cd crisis-button
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python crisis_button.py
   ```

5. Open the application in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## **How to Use**
1. **Start the Application**:
   - Click on the red **CRISIS** button to display all available crisis categories.

2. **Explore Categories**:
   - Select a category to view related subcategories.

3. **View Descriptions and Resources**:
   - Click on a subcategory to see detailed descriptions.
   - If it's the last-level crisis, the app will also fetch and display local resources based on your device's location.

---

## **Contributing**
We welcome contributions to improve this project! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## **License**
This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

---

## **Contact**
For questions or support, reach out to **[The Uncuffed Project](https://www.TheUncuffedProject.org)**.
