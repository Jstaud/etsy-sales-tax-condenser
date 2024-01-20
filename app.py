from flask import Flask, request, send_from_directory
import subprocess
import os 

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles file uploads.
    If the file part is not in the request, returns a message indicating that no file part was found.
    Otherwise, saves the file to a temporary location and calls an existing Python script to process the file.
    Returns a message indicating that the file was uploaded successfully.
    """
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    
    # Save the file to a temporary location
    temp_path = os.path.join("/tmp", file.filename)
    file.save(temp_path)
    
    # Call your existing Python script, passing the path to the saved file
    subprocess.run(["python3", "main.py", temp_path])

    # Return the output file for download
    return send_from_directory('outputs', 'output.csv', as_attachment=True)