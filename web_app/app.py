from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def print_reply():
    data = request.json  # Data sent from the frontend
    response = {'message': f"Hello, {data['molecule']}!"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
