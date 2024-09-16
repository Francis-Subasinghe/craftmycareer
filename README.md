# Resume Classifier Flask App

This is a Flask web application that allows users to classify resumes into job categories such as "Data Scientist", "Software Engineer", and more using machine learning. 
Users input their resume text, and the app predicts the most relevant job category based on the resume content.

## Features
- Classifies resumes into multiple job categories.
- Uses SpaCy for text preprocessing (tokenization, lemmatization).
- Scikit-learn machine learning model for predictions.
- Frontend form for resume input.

## Technologies Used
- Python (Flask, Scikit-learn, SpaCy)
- HTML/CSS for frontend
- JavaScript for API interaction

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create and activate a virtual environment
bash

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
3. Install the dependencies
bash

pip install -r requirements.txt
4. Run the Flask app
bash

python app.py
Open http://127.0.0.1:5000/ in your browser to access the app.

How It Works
Users input their resume text into a form.
The text is preprocessed using SpaCy (tokenization, lemmatization).
The preprocessed text is vectorized using TF-IDF, and the machine learning model predicts the job category.
The predicted category is displayed on the web page.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request to contribute.

License
This project is licensed under the MIT License.

Contact
Feel free to contact me at imeshshenal1222@gmai.com or open an issue on the repository.
