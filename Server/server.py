from flask import Flask, request, jsonify
import util
import os


app = Flask(__name__)

# Load artifacts when the server starts
print("🚀 Starting Python Flask Server For Home Price Prediction...")
util.load_artifacts()
print("✅ Artifacts loaded successfully!")


@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    ''' Get the location names'''
    response = jsonify({
        'location_name': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/predict_house_price", methods=["POST"])
def predict_house_price():
    ''' Predict the price based on the model'''
    print(request.form)

    # Add CORS headers for POST requests
    if request.method == "POST":
        data = request.form
        bath = data['bath']
        bhk = data['bhk']
        sqft = float(data['sqft'])
        location = data['location']
        prediction = util.get_prediction_price(bath, bhk, sqft, location)

        response = jsonify({'estimated_price': prediction})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return jsonify({"error": "Invalid HTTP Method"})


@app.route("/health", methods=["GET"])
def health_check():
    ''' Health check endpoint for Docker '''
    return jsonify({"status": "healthy", "message": "Server is running"})


if __name__ == "__main__":
    ''' Main function to run the flask server'''
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))

    # For Docker, run on 0.0.0.0 to allow external connections
    # But for single-container setup with nginx, use 127.0.0.1
    host = '127.0.0.1'  # Internal to container, nginx will proxy

    print(f"🏠 House Price Prediction API starting on {host}:{port}")
    app.run(host=host, port=port, debug=False)  # debug=False for production