import json
import sys
import configparser


def json_to_csv(file):
    config = configparser.ConfigParser()

    with open(file) as f:
        data = json.load(f)

        for key in data:
            config[key] = data[key]

        with open('config.ini', 'w') as configfile:
            config.write(configfile)


json_to_csv(sys.argv[1])
