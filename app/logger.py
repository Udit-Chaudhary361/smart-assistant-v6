import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_FILE = os.path.join(BASE_DIR, "data", "History.txt")

def logger(log):
    with open(LOG_FILE, "a") as f:
        f.write(log + "\n")