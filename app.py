from flask import Flask, render_template, request, redirect, send_from_directory
from models import db, FileUploadModel
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



# Add files
@app.route("/", methods=['POST', 'GET'])
def index():
    
    return render_template('index.html')


# Delete files
@app.route("/delete/<int:id>")
def delete(id):
    
    return redirect("/")
    

# Update files
@app.route("/update/<int:id>",methods=['POST', 'GET'])
def update_todo(id):
    
    return render_template('update.html')
    


# Download files
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    
    return send_from_directory()

if __name__ == "__main__":
    app.run(debug=True)