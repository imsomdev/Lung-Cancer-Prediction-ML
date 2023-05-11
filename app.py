from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np

app = Flask(__name__)
encoder = LabelEncoder()
encoder.fit(['M', 'F'])
model = pickle.load(open('finalized_model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb')) 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender=request.form.get('gender')
    age=int(request.form.get('age'))
    smoking=int(request.form.get('smoking'))
    yellowFingers=int(request.form.get('yellowFingers'))
    anxiety=int(request.form.get('anxiety'))
    peerPressure=int(request.form.get('peerPressure'))
    chronicDisease=int(request.form.get('chronicDisease'))
    fatigue=int(request.form.get('fatigue'))
    allergy=int(request.form.get('allergy'))
    wheezing=int(request.form.get('wheezing'))
    alcoholConsuming=int(request.form.get('alcoholConsuming'))
    coughing=int(request.form.get('coughing'))
    shortnessOfBreathe=int(request.form.get('shortnessOfBreathe'))
    swallowingDifficulty=int(request.form.get('swallowingDifficulty'))
    chestPain=int(request.form.get('chestPain'))

    gender = encoder.transform([gender])[0]
    app.logger.info(f"gender: {gender}, age: {age}, smoking: {smoking}, yellowFingers: {yellowFingers}, anxiety: {anxiety}, peerPressure: {peerPressure}, chronicDisease: {chronicDisease}, fatigue: {fatigue}, allergy: {allergy}, wheezing: {wheezing}, alcoholConsuming: {alcoholConsuming}, coughing: {coughing}, shortnessOfBreathe: {shortnessOfBreathe}, swallowingDifficulty: {swallowingDifficulty}, chestPain: {chestPain}")

    # Store all the input data in the array
    #prediction
    input_data=[gender,age,smoking,yellowFingers,anxiety,peerPressure,chronicDisease,fatigue,allergy,wheezing,alcoholConsuming,coughing,shortnessOfBreathe,swallowingDifficulty,chestPain]
    
    input_data = np.where(np.asarray(input_data) == 1, 0, 1)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = model.predict(std_data)
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=5000))
