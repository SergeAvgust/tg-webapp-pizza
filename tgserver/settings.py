import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'tgserver.yaml'
TG_TOKEN = '5738040826:AAE6-BIugfiuTPRHgipGq7NVD1ys0e9olRY'

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)