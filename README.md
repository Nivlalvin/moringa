# 📘 Quote Generator

A simple web-based application that generates inspirational quotes at the click of a button. This project demonstrates how backend logic (Flask) can seamlessly interact with a frontend interface to deliver dynamic content.

---

## 📝 Description

This project is a beginner-friendly Flask application that displays random quotes whenever the user clicks a button. It is designed to help new developers understand the basics of Flask routing, template rendering, and front-end interaction using JavaScript.

---

## ✨ Key Features

- Random quote generation
- Simple Flask backend with dynamic routes
- Interactive UI with vanilla JavaScript
- Clean project structure using Flask templates

---

## 🛠️ Technologies Used

- Flask (Python web framework)  
- HTML5  
- CSS3 (optional)  
- JavaScript (Fetch API)  
- Jinja2 templates  

---

⚙️ Installation & Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

2️⃣ Create a Virtual Environment
python -m venv venv

3️⃣ Activate the Virtual Environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

4️⃣ Install Dependencies
pip install flask

5️⃣ Run the Application
python app.py

6️⃣ Open the Browser

Visit: http://127.0.0.1:5000/

🚀 Usage Example

Start the server with:

python app.py


Open your browser

Click the "Show Quote" button

A new inspirational quote will appear

API Example (Optional)

GET /quote

Response:

{
  "quote": "Believe you can and you're halfway there."
}

📁 Project Structure Overview
[project-name]/
 ├── app.py               # Main Flask application
 ├── templates/
 │    └── index.html      # UI template
 ├── static/
 │    └── script.js       # JavaScript for button functionality
 ├── venv/ (optional)     # Virtual environment
 └── README.md            # Project documentation

🔧 Configuration Options
Quotes List (in app.py)

You can add or remove quotes:

quotes = [
    "Your new quote here",
    "Another inspirational quote"
]

Port / Debug Mode

Customize the Flask run command:

app.run(debug=True, port=5001)

🐞 Troubleshooting
❗ 1. ModuleNotFoundError: No module named 'flask'

You likely forgot to install Flask or activate the virtual environment.
Fix:

pip install flask

❗ 2. Button not showing quote

Ensure script.js is correctly linked

Check your browser console for errors

Confirm that the /quote route exists

❗ 3. Cannot activate virtual environment (Windows)

Try:

Set-ExecutionPolicy Unrestricted -Scope Process


Then activate the environment again.

🤝 Contributing

Contributions are welcome!

To contribute:

Fork the repository

Create a new branch

Commit your changes

Open a pull request

Please ensure your code is clean and well-documented.

📄 License

This project is licensed under the MIT License.
You may use, modify, and distribute this project under the terms of the license.
