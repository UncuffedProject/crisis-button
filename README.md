# Crisis Button Project

## **Overview**
The Crisis Button Project is a web application designed to provide **Community Response in Situations Involving Stress**. The app offers a categorized list of crisis events, subcategories, and detailed descriptions to help users access relevant resources and information during emergencies.

---

## **Features**
- **Interactive UI**: A clean, mobile-friendly interface with a dynamic red crisis button.
- **Crisis Categories**: Comprehensive list of crisis events, including natural disasters, medical emergencies, and more.
- **Subcategories and Descriptions**: Detailed breakdown and descriptions for each crisis event.
- **Data Separation**: Modular design with crisis data stored in separate Python files for easy maintenance.
- **Extensibility**: Built using Flask, allowing easy addition of new features.

---

## **Project Structure**
```plaintext
crisis_button_project/
│
├── app.py                     # Main Flask application
│
├── static/                    # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css         # Stylesheet for the project
│   ├── js/
│   │   └── script.js          # JavaScript for interactivity
│   └── images/                # Images (optional)
│
├── templates/                 # HTML templates
│   └── index.html             # Main HTML file
│
├── disaster_types.py          # File containing all crisis categories
│
├── disaster_descriptions.py   # File containing detailed descriptions
│
├── requirements.txt           # Python dependencies
│
└── README.md                  # Project documentation
```

---

## **Technologies Used**
- **Frontend**:
  - HTML
  - CSS
  - JavaScript
- **Backend**:
  - Python
  - Flask
- **Other Libraries**:
  - `geopy` (for location-based features)

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
   python app.py
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

3. **View Descriptions**:
   - Click on a subcategory to see detailed descriptions and information.

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
This project is licensed under the [MIT License](LICENSE).

---

## **Contact**
For questions or support, reach out to **[The Uncuffed Project](https://uncuffed.org)**.
