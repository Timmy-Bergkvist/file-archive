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

```
    
  V.   Run the application
```shell
python app.py
Open the website at http://127.0.0.1:5000
```