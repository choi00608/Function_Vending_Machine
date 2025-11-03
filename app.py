from flask import Flask, render_template, request
import os
from core import generate_function

app = Flask(__name__)

# IMPORTANT: Set the GOOGLE_API_KEY environment variable before running the app.

@app.route('/', methods=['GET', 'POST'])
def index():
    function_code = None
    form_data = {}
    if request.method == 'POST':
        form_data['language'] = request.form['language']
        form_data['function_name'] = request.form['function_name']
        form_data['function_description'] = request.form['function_description']
        form_data['inputs'] = request.form['inputs']
        form_data['outputs'] = request.form['outputs']
        function_code = generate_function(
            form_data['language'], 
            form_data['function_name'], 
            form_data['function_description'], 
            form_data['inputs'], 
            form_data['outputs']
        )
    return render_template('index.html', function_code=function_code, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)