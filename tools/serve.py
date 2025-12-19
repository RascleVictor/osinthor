from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/mail/holehe', methods=['POST'])
def run_holehe():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({'error': 'Missing "email" in request'}), 400

    email = data['email']

    cmd = ["holehe", email]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )
        return jsonify({
            'email': email,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Command timed out'}), 504
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mail/zehef', methods=['POST'])
def run_zehef():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({'error': 'Missing "email" in request'}), 400

    email = data['email']
    zehef_dir = "/workspace/Zehef"
    cmd = ["python3.12", "zehef.py", email]

    try:
        result = subprocess.run(
            cmd,
            cwd=zehef_dir,
            capture_output=True,
            text=True,
            timeout=120
        )
        return jsonify({
            'tool': 'zehef',
            'email': email,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Command timed out'}), 504
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
