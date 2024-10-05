from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pipeline
with open('random_forest_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        age = float(request.form['age'])
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        sc = float(request.form['sc'])

        # Create DataFrame for prediction
        input_data = pd.DataFrame({
            'age': [age],
            'bgr': [bgr],
            'bu': [bu],
            'sc': [sc]
        })

        # Make prediction
        prediction = pipeline.predict(input_data)[0]

        return render_template('results.html',
                               prediction=prediction,
                               age=age,
                               bgr=bgr,
                               bu=bu,
                               sc=sc)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/dietplan')
def dietplan():
    return render_template('dietplan.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)