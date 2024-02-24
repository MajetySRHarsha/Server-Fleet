import json
from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
import pickle
from banksInterest import calculate_interest_bank, data

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
filename = 'model.pickle'
sample_row = [
    2,  # no_of_dependents: Example person has 2 dependents
    0,  # education: Assuming this is years of education, 16 could represent a Bachelor's degree
    0,  # self_employed: Assuming binary, 0 means not self-employed, 1 means self-employed
    50000    ,  # income_annum: Example income of $50,000 per annum
    150000,  # loan_amount: Requesting a loan of $150,000
    30,  # loan_term: Loan term of 30 years
    750,  # cibil_score: A CIBIL score of 750, assuming a range of 300-900
    200000,  # residential_assets_value: $200,000 value in residential assets
    50000,  # commercial_assets_value: $50,000 value in commercial assets
    10000,  # luxury_assets_value: $10,000 value in luxury assets
    250000  # bank_asset_value: $250,000 in bank assets
]
features = [
    'no_of_dependents', 'education', 'self_employed',
    'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
    'residential_assets_value', 'commercial_assets_value',
    'luxury_assets_value', 'bank_asset_value']


@app.get('/')
def hello():
    

# Create a DataFrame for the sample
    sample_df = pd.DataFrame([sample_row], columns=features)
    prediction = loaded_model.predict(sample_df)
    print(prediction)
    return prediction[0]

@app.route('/risk-status',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            data= request.get_json()
            #  reading the inputs given by the user
            request_payload=[
                int(data.get('no_of_dependents')),
                int(data.get('education')),
                int(data.get('self_employed')),
                int(data.get('income_annum')),
                int(data.get('loan_amount')),
                int(data.get('loan_term')),
                int(data.get('cibil_score')),
                int(data.get('residential_assets_value')),
                int(data.get('commercial_assets_value')),
                int(data.get('luxury_assets_value')),
                int(data.get('bank_asset_value'))
            ]
            print(request_payload)
            sample_df = pd.DataFrame([request_payload], columns=features)
            prediction = loaded_model.predict(sample_df)
            print(prediction)
            return str(prediction[0])
            
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'


@app.route('/calculate-interest',methods=['POST','GET'])
def calculate_interest():
    if request.method == 'POST':
        try:
            request_data= request.get_json()
            result= dict()
            for bank in list(data.keys()):
                result[bank] =calculate_interest_bank(request_data.get('loan_amount'),request_data.get('time'),bank)
            return result
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

if __name__ == '__main__':
    
    loaded_model = pickle.load(open(filename, 'rb'))
    app.run(debug=True)