
# Model Deployment
We've deployed our kidney disease prediction model using Flask and PythonAnywhere, making it accessible as a web application. This setup allows users to interact with our model through a user-friendly interface.

### Deployment Stack

- **Web Framework**: Flask
- **Hosting Platform**: PythonAnywhere
- **Frontend**: HTML/CSS
- **Backend**: Python

### Deployment Process

1. **Flask Application**: 
   - We created a Flask application that serves as the backend for our prediction service.
   - The application handles user inputs, processes them through our model, and returns predictions.

2. **Model Integration**:
   - We uplaoded the Random Forest model pipeline to the cloud service.
   - The Flask app loads this pipeline to make real-time predictions.

3. **HTML Interface**:
   - An `index.html` file was created to serve as the frontend of our application.
   - This file provides a user-friendly form for inputting patient data and displays the prediction results.

4. **PythonAnywhere Hosting**:
   - We utilized PythonAnywhere to host our Flask application.
   - This platform provides a Python-friendly environment that's well-suited for machine learning deployments.

### Accessing the Application

Our kidney disease prediction tool is now live and can be accessed at:

[[CKD classfication]](https://fate24.pythonanywhere.com/)

### Using the Deployed Model

1. Navigate to the application URL.
2. Enter the required patient information in the provided form fields:
   - Age
   - Blood Glucose Random (BGR)
   - Blood Urea (BU)
   - Serum Creatinine (SC)
3. Click the "Predict" button.
4. The application will display the prediction result, indicating the likelihood of kidney disease.




