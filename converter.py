# Json to XML
import json as j
import xml.etree.ElementTree as e

# Open the JSON file and load its data
with open("2.json", "r") as json_file:
    data = j.load(json_file)

# Create an XML root element
root = e.Element("data")

# Create subelements for each key-value pair in the dictionary
for key, value in data.items():
    sub = e.SubElement(root, key)
    sub.text = str(value)

# Write the XML tree to a file
tree = e.ElementTree(root)
tree.write("data.xml")


# # XML to JSON
# import xmltodict as x
# import json as j

# # Open the XML file and parse its data
# with open("2.xml", "r") as xml_file:
#     data = x.parse(xml_file.read())

# # Open a new JSON file and dump the data
# with open("data.json", "w") as json_file:
#     j.dump(data, json_file)

# # Close both files
# xml_file.close()
# json_file.close()


j = {'annotation': {'folder': 'CustomModel', 'filename': '2.jpg', 'path': '/home/ranjith/Documents/TRIDE/Workspace/Road_data/CustomModel/2.jpg', 'source': {'database': 'Unknown'}, 'size': {'width': '640', 'height': '480', 'depth': '3'}, 'segmented': '0',
                    'object': [{'name': 'signal', 'pose': 'Unspecified', 'truncated': '0', 'difficult': '0', 'bndbox': {'xmin': '114', 'ymin': '19', 'xmax': '173', 'ymax': '167'}}, {'name': 'car', 'pose': 'Unspecified', 'truncated': '0', 'difficult': '0', 'bndbox': {'xmin': '278', 'ymin': '340', 'xmax': '455', 'ymax': '478'}}]}}
