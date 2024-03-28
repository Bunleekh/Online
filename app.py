from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signal', methods=['POST'])
def receive_signal():
    data = request.json  # Extract JSON data from the request
    message = data.get('message')  # Get the 'message' field from the JSON data
    print("Received message:", message)
    return jsonify({"status": "success", "message": "Signal received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
