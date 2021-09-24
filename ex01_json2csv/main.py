import pandas as pd
import sys


def json_to_ini(file):
    df = pd.read_json(file)
    df.to_csv(r'config.csv', index=None)


json_to_ini(sys.argv[1])
