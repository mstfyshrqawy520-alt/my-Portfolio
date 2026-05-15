from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# تحميل الموديل والـ scaler
model = pickle.load(open('wine_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
    float(request.form['fixed_acidity']),
    float(request.form['volatile_acidity']),
    float(request.form['citric_acid']),
    float(request.form['residual_sugar']),
    float(request.form['chlorides']),
    float(request.form['free_sulfur_dioxide']),
    float(request.form['total_sulfur_dioxide']),
    float(request.form['density']),
    float(request.form['pH']),
    float(request.form['sulphates']),
    float(request.form['alcohol'])
]
    final_features = np.array(features).reshape(1, -1)

    # Scaling
    final_features = scaler.transform(final_features)
    
    # التنبؤ
    prediction = model.predict(final_features)[0]
    
    output = 'Good Wine' if prediction == 1 else 'Not Good Wine'
    
    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

