# CSCE470 Final Project: Recipe Finder Web Application

## Project Overview
This project is a web-based application that allows users to find recipes based on a list of input ingredients. It uses a custom implementation of the BM25 ranking algorithm to score and display the best-matching recipes from a dataset.

## Features
- **Ingredient Autocomplete**: Search ingredients with autocomplete functionality.
- **BM25 Ranking**: Custom ranking algorithm for matching recipes based on input ingredients.
- **User-Friendly Interface**: Simple and clean UI with recipe cards and background images.

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.7+
- Flask
- Git
- Pip (Python package installer)

## Setup Instructions

### Step 1: Clone the Repository
Clone this project from GitHub to your local machine:
```bash
git clone https://github.com/jaymsteele/CSCE470_final_project.git
cd CSCE470_final_project
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
Create a virtual environment to keep your dependencies isolated:
```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

**Dependencies Include**:
- Flask
- Pandas
- Rank-BM25
- Gunicorn (optional for production)
- Other libraries specified in `requirements.txt`

### Step 4: Set Up Your Data
Ensure you have the `data/RAW_recipes.csv` file in your `data` folder. This file should not be pushed to GitHub due to its size. Refer to the project owner if you need this file locally.

### Step 5: Run the Application
Start the Flask development server:
```bash
flask run
```
Or use Python directly:
```bash
python app.py
```

Access the application by visiting `http://127.0.0.1:5000/` in your web browser.

## Project Structure
```
CSCE470_final_project/
│
├── app.py                     # Main application code
├── static/                    # Static files (CSS, images)
│   ├── css/
│   │   └── styles.css         # Main stylesheet
│   └── images/
│       └── background.png     # Background image for the site
├── templates/                 # HTML templates
│   ├── index.html
│   └── results.html
├── data/                      # Data folder (contains CSV and other data files)
│   └── RAW_recipes.csv        # Main recipes dataset (ensure this is below 100 MB)
├── README.md                  # Project documentation
└── requirements.txt           # List of dependencies
```

## Additional Notes
- **Large Files**: The `data/RAW_recipes.csv` file should be added manually and not pushed to GitHub. Ensure it's listed in `.gitignore`.
- **Git LFS**: If you use Git LFS for large files, ensure you install and track them properly.

## Contact
For questions, please contact s0802264@tamu.edu

