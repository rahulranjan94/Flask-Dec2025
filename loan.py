from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)  # __name__ -> "loan.py"

# Load the trained model
with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to the Loan Application Service!</h1>"

@app.route("/predict", methods=["GET"])
def predict():
    return """I will make the prediction for you.<br>
    Please send a POST request with the required data.<br>
    Endpoint:<br>
    http://127.0.0.1:5000/predict <br>

    Data required:
    {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 200,
        "CreditHistory": 1
    }
    """


@app.route("/predict", methods=["POST"])
def make_prediction():
    loan_req = request.get_json()

    # Encode Gender
    if loan_req['Gender'] == 'Male':
        Gender = 0
    else:
        Gender = 1

    # Encode Married
    if loan_req['Married'] == 'No':
        Married = 0
    else:
        Married = 1

    # Numeric values
    ApplicantIncome = loan_req['ApplicantIncome']
    CreditHistory = loan_req['CreditHistory']
    LoanAmount = loan_req['LoanAmount']

    # Model input
    input_data = [[Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]]

    # Prediction
    pred = model.predict(input_data)

    print(pred)

    

    if pred[0] == 1:
        pred = "Approved"
    else:
        pred = "Rejected"
    
    return {"loan_approval_status":pred}


if __name__ == "__main__":
    app.run(debug=True)
