from flask import Flask, render_template, request, redirect, send_from_directory, current_app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fileArchive.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize database
db=SQLAlchemy(app)

# Database files model
class FileUploadModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)
    name=db.Column(db.String(200), nullable=False) # Uploaded buy
    description = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) :
        return '<Name %r>' % self.id


# Add files
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method =='POST':
        file = request.files['file']
        name=request.form['name']
        description=request.form['description']
        files=FileUploadModel(name=name, description=description, filename=file.filename, data=file.read())
        try:
            db.session.add(files)
            db.session.commit()
            return redirect('/')
        except:
            return "Error! Could not add file!"
    else:
        allFiles=FileUploadModel.query.order_by(FileUploadModel.date_created)
        return render_template('index.html',files=allFiles)


# Delete files
@app.route("/delete/<int:id>")
def delete(id):
    
    return redirect("/")
    

# Update files
@app.route("/update/<int:id>",methods=['POST', 'GET'])
def update(id):
    
    return render_template('update.html')
    


# Download files
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    
    return send_from_directory()

if __name__ == "__main__":
    app.run(debug=True)