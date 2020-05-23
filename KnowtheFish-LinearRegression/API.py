import sys
import subprocess
import pkg_resources
""""Checking required packages"""
required = {'flask', 'sklearn','joblib','numpy','pandas'}#Required modules
installed = {pkg.key for pkg in pkg_resources.working_set}#get installed modules
missing = required - installed

if missing:
    print("Installing Missing modules")
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
print("All required modules are already available")
    
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
    
    from joblib import dump, load#Using joblib insted of sklearn.external
    model =load('Fish_weight_Predictor.ml')
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