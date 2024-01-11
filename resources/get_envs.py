import os
from dotenv import load_dotenv


def get_enviroment_variables():
    load_dotenv()

    environment_variables = {
        'SLACK_WEBHOOK': os.getenv('SLACK_WEBHOOK'),
        'BASE_API': os.getenv('BASE_API'),
        'BASE_URL': os.getenv('BASE_URL')
    }

    return environment_variables