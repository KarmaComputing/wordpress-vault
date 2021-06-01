import json
import os
import subprocess

os.system("source venv/bin/activate")

from dotenv import load_dotenv

load_dotenv(verbose=True)

ALLOWED_SITES = os.getenv("ALLOWED_SITES")
ALLOWED_SITES = json.loads(ALLOWED_SITES)  # converted to dict


for site in ALLOWED_SITES.keys():

    command = (
        f"./update-WP.sh {ALLOWED_SITES[site]['path']} {ALLOWED_SITES[site]['user']}"
    )
    print(command)
    subprocess.run(command, shell=True)  # noqa
