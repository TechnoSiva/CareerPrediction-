# Career Prediction Web Application

This is a Flask-based web application that predicts a suitable career path based on user inputs such as GPA and programming skills. The application uses a machine learning model (Random Forest Classifier) trained on a dataset of various careers and skill levels to provide career recommendations along with relevant skills, resources, and advice.

## Features

- Input form to enter GPA and skill levels in Python, SQL, and Java.
- Predicts a career based on the input features.
- Provides career-specific recommendations including skills to develop, learning resources, and advice.
- Simple and clean user interface.

## Installation

1. Clone the repository or download the project files.

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r Requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

3. Fill in the form with your GPA and skill levels in Python, SQL, and Java.

4. Click the "Predict Career" button to see the predicted career and recommendations.

## Input Fields

- **GPA**: Your Grade Point Average (scale 0 to 10).
- **Python Skill**: Your proficiency in Python (Weak, Average, Strong).
- **SQL Skill**: Your proficiency in SQL (Weak, Average, Strong).
- **Java Skill**: Your proficiency in Java (Weak, Average, Strong).

*Note: Although the form includes an Age field, it is currently not used in the prediction model.*

## Model

The application uses a Random Forest Classifier trained on a dataset of careers and associated skill levels. The model predicts the most suitable career based on the input features.

## Dependencies

- Flask==2.1.1
- scikit-learn==1.5.2
- joblib==1.2.0

## Project Structure

- `app.py`: Main Flask application script.
- `Requirements.txt`: Python dependencies.
- `templates/`: Contains HTML templates for the web pages.
- `career_prediction_model.pkl`: Serialized machine learning model (not currently loaded in app.py).
- `label_encoder.pkl`: Serialized label encoder (not currently loaded in app.py).

## Notes

- The current implementation trains the model on startup using a hardcoded dataset in `app.py`. For production use, consider loading a pre-trained model from the `.pkl` files.
- The Age input field is present in the form but not used in the prediction logic.
- The application runs in debug mode for development purposes.

## License

This project is open source and free to use.
