# file-archive-project

**Local deployment**

The following instructions are based on Windows 10 and VS Code editor.


  I.    Clone the repository in Github
 ```shell
  git clone https://github.com/Timmy-Bergkvist/file-archive.git
 ```
    
  II.   Create an environment
```shell
 py -3 -m venv venv
```

  III.   Activate the environment
```shell
venv\Scripts\activate
```

  IV.   Install all the packages that are required
```shell
pip install Flask
pip install flask_sqlalchemy
```

  V.   Database setup
  1: Open your terminal and type python and hit Enter
  2: in the terminal type from app import db and hit enter
  3: next type db.create_all() and hit enter
```shell
>>> from app import db
>>> db.create_all()
```
  4: when that done type exit() and hit enter
```shell
>>> exit()
```

  VI.   Run the application
```shell
python app.py
Open the website at http://127.0.0.1:5000
```