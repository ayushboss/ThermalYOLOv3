import glob
import json
import pprint
import os
from PIL import Image

setup_json = open("/Users/ayushboss/Desktop/Rice/train_2/thermal_annotations.json")
setup_data = json.load(setup_json)

annotation_dict = {}

max_id = 0
for annotation in setup_data['annotations']:
	max_id = max(max_id, annotation['image_id'])

print('max id: ' + str(max_id))

for i in range(max_id+1):
	annotation_dict[i] = []

annotation_categories = {}
for category in setup_data['categories']:
	annotation_categories[category['id']] = [category['name'], category['supercategory']]

for annotation in setup_data['annotations']:
	cur_id = annotation['image_id']
	annotation_dict[cur_id].append(annotation)

#pprint.pprint(annotation_dict)

image_train_set = glob.glob("/Users/ayushboss/Desktop/Rice/darknet/darknet/data/images/*.jpeg")
print(len(image_train_set))

image_id_to_annotations = {}

for annotation in setup_data['annotations']:
	object_class = annotation['category_id']
	bbox = annotation['bbox']
	x1 = bbox[0]
	y1 = bbox[1]
	x2 = bbox[0] + bbox[2]
	y2 = bbox[1] + bbox[3]
	image_id = int(annotation['image_id'])
	if image_id == 4152:
		print("gotcha")
	if image_id not in image_id_to_annotations.keys():
		image_id_to_annotations[image_id] = [annotation]
	else:
		image_id_to_annotations[image_id].append(annotation)
	#with open("/Users/ayushboss/Desktop/Rice/darknet/darknet/data/labels/

print(len(image_id_to_annotations.keys()))	


for image in image_train_set:
	with Image.open(image) as img:
		width, height = img.size
		str_image_id = image[-10:-5]
		image_id = int(str_image_id)
		if image_id in image_id_to_annotations.keys():
			affiliated_annotations = image_id_to_annotations[image_id]
			open("/Users/ayushboss/Desktop/Rice/darknet/darknet/data/labels/FLIR_"+str(str_image_id)+".txt", "w").close()
			for annotation in affiliated_annotations:
				bbox = annotation['bbox']
				bounding_box_w = bbox[2]
				bounding_box_h = bbox[3]

				bounding_box_center_x = bbox[0]
				bounding_box_center_y = bbox[1]

				with open("/Users/ayushboss/Desktop/Rice/darknet/darknet/data/labels/FLIR_"+str(str_image_id)+".txt", "a") as out_file:
					out_file.write(str(annotation['category_id']) + " " + str(bounding_box_center_x) + " " + str(bounding_box_center_y) + " " + str(float(bounding_box_w)/width) + " " + str(float(bounding_box_h)/height) + "\n")

