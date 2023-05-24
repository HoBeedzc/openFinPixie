# App Entry
import argparse
import os
import sys

from src import *
# from src import app
# from src import config
# from src import logger
# from src import utils

# Parse arguments
parser = argparse.ArgumentParser(description='Run the app')
parser.add_argument('--config', type=str, default='config.yaml', help='Path to config file')
parser.add_argument('--log', type=str, default='logging.yaml', help='Path to logging config file')


def main():
    args = parser.parse_args()
    # config_path = args.config
    # if not os.path.exists(config_path):
    #     print("Config file not found: {}".format(config_path))
    #     sys.exit(1)
    # config.load_config(config_path)
    # logger.init_logger(config.get_config().get('log'))
    # utils.init_utils(config.get_config().get('utils'))
    # app.run()

if __name__ == "__main__":
    main()

