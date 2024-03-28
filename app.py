from flask import Flask

app = Flask(__name__)
online_apps = []

@app.route('/signal', methods=['POST'])
def receive_signal():
    # Add the IP address of the sender to the list of online apps
    ip_address = request.remote_addr
    if ip_address not in online_apps:
        online_apps.append(ip_address)
    return 'Signal received'

@app.route('/online_apps', methods=['GET'])
def get_online_apps():
    return str(len(online_apps))

if __name__ == '__main__':
    app.run(debug=True)
