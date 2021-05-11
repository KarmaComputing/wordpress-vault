import os
import requests
from flask import Flask, render_template, request
import subprocess
from urllib.parse import urlsplit

def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__)
    path = './vault' 

    @app.route('/')
    def index():

        return render_template('index.html')

    @app.route('/unlock', methods=["POST"])
    def unlock():
        
        if request.method == "POST":
            r = requests.post(validate(request.form['websiteURL']), data = {'log':request.form['username'], 'pwd':request.form['password']})
            #validating URL 
            if "wp-login.php" in request.form['websiteURL'] and r.status_code == 200:
                #validating Login
                request_comparison = "login_error" in r.content.decode('utf-8')
                if request_comparison == False: #True if password is wrong
                    print (validate(request.form['websiteURL']))
                    print ("Correct Password")
                    # subprocess.run(f"{path}/unlock_lock.sh", shell=True)
                    return render_template('unlock.html')
                return("Wrong Password or Username")
                print("Wrong Password")
            print("invalid URL") 
            return ("Please enter a valid wordpress URL")
        return render_template('index.html')
    
    @app.route('/lock', methods=["POST"])
    def lock():
            print ("your site is locked")
           #subprocess.run(f"{path}/lock.sh", shell=True)
            return render_template('lock.html')

    def validate(webaddress: str):
        if "://" in webaddress:
            return webaddress
        else: 
            webaddress = "http://" + webaddress
            return webaddress

    return app
