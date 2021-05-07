import os

from flask import Flask, render_template, request
import subprocess
def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__, template_folder='/home/karma/www/vault-karmacomputing/vault/template/')


    @app.route('/')
    def index():

        return render_template('index.html')

    @app.route('/unlock', methods=["POST"])
    def unlock():
          
        subprocess.run("./unlock_lock.sh", shell=True)
        
        return render_template('unlock.html')

    @app.route('/lock')
    def lock():

        subprocess.run("./lock.sh", shell=True)

        return render_template('lock.html')

    return app
