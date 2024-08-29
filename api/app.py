from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Sample data (you can replace this with a more complex dataset)
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [150, 200, 250, 300, 350, 290]
}

@app.route('/data', methods=['GET'])
def get_data():
    df = pd.DataFrame(data)
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
