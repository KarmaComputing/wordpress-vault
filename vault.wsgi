import os
import logging
from vault import create_app

PYTHON_LOG_LEVEL = os.getenv('PYTHON_LOG_LEVEL', logging.INFO)

logging.basicConfig(level=PYTHON_LOG_LEVEL)

application = create_app()
