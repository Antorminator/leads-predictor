import pickle

from flask import Flask, jsonify, request

from converted_predict_service import predict_single

app = Flask('converted-predict')

with open('models/converted-model.pck', 'rb') as f:
    model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    prediction = predict_single(customer, model)

    result = {
        'convert_prediction': prediction
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
