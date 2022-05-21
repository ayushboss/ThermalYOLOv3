import glob
import json
import pprint
import os
from PIL import Image

setup_json = open("/Users/ayushboss/Desktop/Rice/train_2/thermal_annotations.json")
setup_data = json.load(setup_json)

obj_names_outfile = open('/Users/ayushboss/Desktop/Rice/darknet/darknet/data/obj.names', 'w')
obj_data_outfile = open('/Users/ayushboss/Desktop/Rice/darknet/darknet/data/obj.data', 'w')

for category in setup_data['categories']:
    category_name = category['name']
    print(category_name, file = obj_names_outfile)

print(len(setup_data['categories']), obj_data_outfile)
print('train  = data/train.txt', obj_data_outfile)
print('valid  = data/valid.txt', obj_data_outfile)
print('names = data/obj.names', obj_data_outfile)
print('backup = backup/', obj_data_outfile)