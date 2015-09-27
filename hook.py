from flask import Flask
import subprocess
import os
import logging

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

	os.chdir( 'GIT_REPO_FOLDER' )

	output = subprocess.check_output(["git", "pull"])
	
	# if you are deploying another Python app , you should reload it on code changes using uwsgi touch reload functionality
	subprocess.call(["touch","README.md"])
	 return '{message: '+output+' , success:True}'
    

@app.route('/')
def index():
    return '{message: Project CI Server!, success:True}'


if __name__ == '__main__':
    app.run( port=8080, debug=True)
 
