 
import json
from datetime import datetime

def serialize_datetime(obj): 
    if isinstance(obj, datetime): 
        return obj.isoformat() 
    raise TypeError("Type not serializable") 
 
def read_json_data(name):
    with open(f'{name}.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
    
    return json_object

def save_json_data(name, data):
    with open(f'{name}.json', "w") as outfile:
        json.dump(data, outfile, default=serialize_datetime)

