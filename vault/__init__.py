import requests
from flask import Flask, render_template, request, redirect
import subprocess
from dotenv import load_dotenv
import os
from urllib.parse import urlsplit
import urllib
import json

load_dotenv(verbose=True)  # get environment variables from .env


def create_app(test_config=None):

    app = Flask(__name__)
    app.config.update(os.environ)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/unlock", methods=["POST"])
    def unlock():
        if request.method == "POST":
            domain = validate(request.form["websiteURL"]).geturl()
            dictionary = json.loads(app.config["ALLOWED_SITES"])
            wp_path = dictionary[domain]
            if domain not in dictionary:
                return redirect("https://subscriptionwebsitebuilder.co.uk", code=301)
            if wordpress_login_success(domain) is False:
                return "Wrong Password or Username"
            print(wp_path)
            subprocess.run(
                app.config["PATH_TO_UNLOCK_SCRIPT"] + " " + wp_path, shell=True
            )
            return render_template("unlock.html")
        return render_template("index.html")

    @app.route("/lock", methods=["POST"])
    def lock():
        if request.method == "POST":
            domain = validate(request.form["websiteURL"]).geturl()
            dictionary = json.loads(app.config["ALLOWED_SITES"])
            wp_path = dictionary[domain]
            if domain not in dictionary:
                return redirect("https://subscriptionwebsitebuilder.co.uk", code=301)
            print(wp_path)
            print(app.config["PATH_TO_LOCK_SCRIPT"] + wp_path)
            subprocess.run(
                app.config["PATH_TO_LOCK_SCRIPT"] + " " + wp_path, shell=True
            )
            return render_template("lock.html")
        return render_template("index.html")

    return app


def wordpress_login_success(domain: str) -> bool:

    login_url = f"{domain}/wp-login.php"
    try:
        wordpress_login = requests.post(
            login_url,
            data={
                "log": request.form["username"],
                "pwd": request.form["password"],
            },
        )
        if "login_error" in wordpress_login.text:
            return False
        if "<h1>Dashboard</h1>" in wordpress_login.text:
            return True
    except requests.exceptions.ConnectionError:
        print("requests.exceptions.ConnectionError")
        return False
    return False


def validate(webaddress: str) -> urllib.parse.SplitResult:
    """From webaddres return just the domain."""

    webaddress = webaddress if "://" in webaddress else "https://" + webaddress
    url = urlsplit(webaddress)
    return url
