from io import BytesIO
from flask import Flask, render_template, request, redirect, send_file, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'xml', 'pdf', 'jpg', 'jpeg'}

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
            #flash('Error! Could not add file!')
            #return redirect("/")
            return "Error! Could not add file!"
    else:
        page = request.args.get('page', 1, type=int)
        allFiles=FileUploadModel.query.order_by(FileUploadModel.date_created).paginate(page=page, per_page=5)
        return render_template('index.html',files=allFiles)
    

# Delete files
@app.route("/delete/<int:id>")
def delete(id):
    deleteFile = FileUploadModel.query.filter_by(id=id).first()
    db.session.delete(deleteFile)
    db.session.commit()
    return redirect("/")
    

# Update files
@app.route("/update/<int:id>",methods=['POST', 'GET'])
def update(id):
    updatetFile = FileUploadModel.query.get_or_404(id)
    if request.method == 'POST':
        updatetFile = FileUploadModel.query.filter_by(id=id).first()
        name = request.form['name']
        description = request.form['description']
        updatetFile.name=name
        updatetFile.description=description
        try:
            db.session.commit()
            return redirect("/")
        except:
            #flash("Error! Could not update file!", "info")
            #return redirect("/")
            return "Error! Could not update file!"
    else:
        return render_template('update.html', updatetFile=updatetFile)
    

# Download files
@app.route("/download/<int:id>", methods=['GET', 'POST'])
def download(id):
    upload = FileUploadModel.query.filter_by(id=id).first()
    return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)