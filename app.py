from flask import Flask

app = Flask(__name__)

@app.route('/signal', methods=['POST'])
def receive_signal():
    # Perform actions upon receiving the signal
    print("Signal received from local app!")
    return "Signal received successfully", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
