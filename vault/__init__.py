import requests
from flask import Flask, render_template, request, flash
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
    app.secret_key = app.config["SECRET_KEY"]

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/unlock", methods=["POST"])
    def unlock():
        if request.method == "POST":

            URL = validate(request.form["websiteURL"]).geturl()
            DOMAIN = validate(request.form["websiteURL"]).netloc
            ALLOWED_SITES = json.loads(app.config["ALLOWED_SITES"])

            if DOMAIN not in ALLOWED_SITES:
                sign_up_url = app.config["SIGN_UP_URL"]
                flash("Please check the URL, otherwise, start using Vault today!")
                return render_template("index.html", sign_up_url=sign_up_url)
            if wordpress_login_success(URL) is False:
                sign_up_url = app.config["SIGN_UP_URL"]
                flash("Wrong username or password")
                return render_template("index.html", sign_up_url=sign_up_url)
            WP_PATH = ALLOWED_SITES[DOMAIN]["path"]
            subprocess.run(
                app.config["PATH_TO_UNLOCK_SCRIPT"] + " " + WP_PATH, shell=True
            )
            return render_template("unlock.html")
        return render_template("index.html")

    @app.route("/lock", methods=["POST"])
    def lock():
        if request.method == "POST":

            DOMAIN = validate(request.form["websiteURL"]).netloc
            ALLOWED_SITES = json.loads(app.config["ALLOWED_SITES"])

            if DOMAIN not in ALLOWED_SITES:
                sign_up_url = app.config["SIGN_UP_URL"]
                flash("Please check the URL, otherwise, start using Vault today!")
                return render_template("index.html", sign_up_url=sign_up_url)
            WP_PATH = ALLOWED_SITES[DOMAIN]["path"]
            subprocess.run(
                app.config["PATH_TO_LOCK_SCRIPT"] + " " + WP_PATH, shell=True
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
