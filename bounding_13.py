import glob
import json
import pprint

setup_json = open("/Users/ayushboss/Desktop/Rice/train 2/thermal_annotations.json")
setup_data = json.load(setup_json)

annotation_dict = {}

max_id = 0
for annotation in setup_data['annotations']:
	max_id = max(max_id, annotation['image_id'])

print('max id: ' + str(max_id))

for i in range(max_id+1):
	annotation_dict[i] = []

for annotation in setup_data['annotations']:
	cur_id = annotation['image_id']
	annotation_dict[cur_id].append(annotation)

pprint.pprint(len(annotation_dict[0]))

