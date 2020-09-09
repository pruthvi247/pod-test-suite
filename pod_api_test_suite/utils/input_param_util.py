import json

def read_input_json(file_path):
    with open(file_path,'r') as f:
        confprop = json.load(f)
    return confprop