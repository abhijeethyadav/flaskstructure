from app import app
from flask import request
import git

@app.route('/update_server', methods=['GET'])
def webhook():
    if request.method == 'GET':
        repo = git.Repo('C:/Users/abhij/OneDrive/Documents/Git_Projects/Flask_Structure/')
        origin = repo.remotes.origin
        origin.pull('master')
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400