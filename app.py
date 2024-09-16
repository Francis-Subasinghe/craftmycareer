from flask import Flask, request, jsonify, render_template
import joblib
import spacy
import re

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('optimized_resume_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Load SpaCy NLP model
nlp = spacy.load('en_core_web_sm')

# Preprocessing function for resumes
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # Using 're' here
    text = re.sub(r'\s+', ' ', text).strip()  # Using 're' here
    return text

def preprocess_resume(resume_text):
    doc = nlp(clean_text(resume_text))
    return ' '.join([token.lemma_ for token in doc if not token.is_stop])

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')  # This will render the index.html page

# API route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    resume_text = request.form['resume_text']

    # Preprocess and vectorize the resume text
    processed_resume = preprocess_resume(resume_text)
    resume_vector = vectorizer.transform([processed_resume])

    # Make a prediction
    prediction = model.predict(resume_vector)

    # Return the predicted category
    return jsonify({'category': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
