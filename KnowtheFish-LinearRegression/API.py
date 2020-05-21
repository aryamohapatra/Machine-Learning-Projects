import flask
from flask import request
app = flask.Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route('/')

def default():
    
    return '<h1> API server is working </h1>'

@app.route('/predict')

def predict():
    
    from sklearn.externals import joblib
    model = joblib.load('Fish_weight_Predictor.ml')
    import pandas as pd
    from sklearn.preprocessing import StandardScaler,LabelEncoder
    Fish_details = pd.read_csv('Fish.csv')
    scaler = StandardScaler()
    labelencoder = LabelEncoder()
    Fish_details['Species'] = labelencoder.fit_transform(Fish_details['Species'])
    X = Fish_details.drop(['Weight'],axis=1).values
    X= scaler.fit_transform(X)
    Y = scaler.transform([[request.args['Species'],
                           request.args['Length1'],
                           request.args['Length2'],
                           request.args['Length3'],
                           request.args['Height'],
                           request.args['Width']]])
    weight = model.predict(Y)
    return str(weight)

app.run(debug=True)