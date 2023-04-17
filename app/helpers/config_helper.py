import yaml
import pathlib

def get_config():
    # print(pathlib.Path(__file__))
    return yaml.safe_load(open("app/config/config.yaml"))

def test_dir():
    print(pathlib.Path(__file__))


# print(read_config("database", "username"))