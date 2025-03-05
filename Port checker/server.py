from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            if sock.connect_ex((target_ip, port)) == 0:
                open_ports.append(port)
    return open_ports

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target_ip = data.get("targetIp")
    start_port = int(data.get("startPort"))
    end_port = int(data.get("endPort"))

    open_ports = scan_ports(target_ip, start_port, end_port)
    return jsonify({"open_ports": open_ports})

if __name__ == "__main__":
    app.run(debug=True)
