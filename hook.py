from flask import Flask
import subprocess
import os
import logging

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():


	#logger = logging.getLogger(__name__)
	#logger.setLevel(logging.INFO)

	# create a file handler

	#handler = logging.FileHandler('/tmp/BitbucketResponse.log')
	#handler.setLevel(logging.INFO)

	# create a logging format

	#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	#handler.setFormatter(formatter)

	# add the handlers to the logger

	#logger.addHandler(handler)

	#print subprocess.call(['pwd'])
	subprocess.call(["whoami"])
	subprocess.call(["cat" ,"/var/www/.ssh/www-data.pub"])
	os.chdir( '/home/ubuntu/apps/dietray-app/dietray-flask-app' )
	#print subprocess.call(['pwd'])
	#print subprocess.call(['whoami'])
	output = subprocess.check_output(["git", "pull"])
	
	subprocess.call(["touch","README.md"])
	return output
    

@app.route('/')
def index():
    return '{message: Dietray CI Server!, success:True}'


if __name__ == '__main__':
    app.run( port=8080, debug=True)
 