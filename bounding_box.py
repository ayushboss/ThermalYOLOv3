import glob
from PIL import Image, ImageDraw
import json
import sys
fileNames = glob.glob("/Users/ayushboss/Desktop/Rice/FLIR_ADAS_v2/images_thermal_train/data"+"/*.jpg")
flag=False
# print(fileNames[:5])

f = open("/Users/ayushboss/Desktop/Rice/FLIR_ADAS_v2/images_thermal_train/index.json")

file_indices = []
idx = 0
for name in fileNames:
	if name.find('2Af3dwvs6YPfwSSf6') != -1:
		file_indices.append(idx)
	idx+=1

data = json.load(f)

idx = 0
index_json_indices = []

for frame in data['frames']:
	if frame['videoMetadata']['videoId'] == '2Af3dwvs6YPfwSSf6':
		index_json_indices.append(idx)
	idx+=1

sample_file_idx = index_json_indices[0]

# print (file_indices)
pertinent_filenames = []
file_indices.sort()
for cur_file_idx in file_indices:
	pertinent_filenames.append(fileNames[cur_file_idx])
pertinent_filenames.sort()

print(index_json_indices)

idx=0
for cur_file in pertinent_filenames:
	with Image.open(cur_file) as im:
		# print(data['frames'][index_json_indices[idx]]['annotations'])		
		if str(cur_file)[106:-4] != data['frames'][index_json_indices[idx]]['datasetFrameId']:
			continue
		print(str(cur_file)[106:-4] + " " + data['frames'][index_json_indices[idx]]['datasetFrameId'])
		
		for annotation in data['frames'][index_json_indices[idx]]['annotations']:
			# print(annotation)
			if 'labelboxGeometry' not in annotation['source']['meta'].keys():
				idx+=1
				continue
			boxes = annotation['source']['meta']['labelboxGeometry']
			draw = ImageDraw.Draw(im)
			draw.line((boxes[0]['x'], boxes[0]['y'], boxes[1]['x'], boxes[1]['y']), fill=0)
			draw.line((boxes[0]['x'], boxes[0]['y'], boxes[2]['x'], boxes[2]['y']), fill=0)
			draw.line((boxes[1]['x'], boxes[1]['y'], boxes[3]['x'], boxes[3]['y']), fill=0)
			draw.line((boxes[2]['x'], boxes[2]['y'], boxes[3]['x'], boxes[3]['y']), fill=0)

			label = ""
			for annotation_label in annotation['labels']:
				label += annotation_label+", "
			draw.text((boxes[0]['x'], boxes[0]['y']), label)
		# im.show()
		im.save('/Users/ayushboss/Desktop/Rice/output_images/frame'+str(idx)+'.png')
		idx+=1

    # print(data['frames'].keys())