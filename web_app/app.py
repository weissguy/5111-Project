from flask import Flask, render_template, request, jsonify, send_file
from atomic_sound import make_sound
import os
from atomic_image import create_visualisation


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def print_reply():
    data = request.json  # Data sent from the frontend
    response = {'message': f"Hello, {data['molecule']}!"}
    return jsonify(response)

@app.route('/visualize', methods=['POST'])
def visualise():
    data = request.json
    molecule_name = data.get('molecule', '')
    try:
        image_path = create_visualisation(molecule_name)
        return send_file(image_path, mimetype='image/png')
    except ValueError as e:
        return {'error': str(e)}, 400
    except Exception as e:
        return {'error': f"An unexpected error occurred: {str(e)}"}, 500

@app.route('/api/generate', methods=['POST'])
def generate_sound():
    print("received a post request")
    data = request.json
    # mol_name = data.get('molecule', 'unknown')
    mol_name = {data['molecule']}

    # Call the atomic sound generator
    audio_path = make_sound(mol_name)

    if audio_path and os.path.exists(audio_path):
        return jsonify({'audio_url': f'/static/{os.path.basename(audio_path)}'})
    else:
        return jsonify({'error': 'Failed to generate sound'}), 500

# Route to serve static files (e.g., audio files)
@app.route('/static/<filename>')
def serve_file(filename):
    return send_file(f"sonification/wav_files/{filename}")


if __name__ == "__main__":
    app.run(debug=True)
