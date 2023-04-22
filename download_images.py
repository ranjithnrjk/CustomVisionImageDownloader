import os
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
import json
import urllib.request as request

###################################################################
# Replace with a valid key of the TARGET Custom Vision
###################################################################
ENDPOINT = "YOUR ENDPOINT"
training_key = "TRAINING KEY"
projectid="PROJECT ID"
storeImageDirectry = "DIRECTORY TO STORE IMAGES"
###################################################################
###################################################################

'''
Image Classification JSONs look like
    {"fileName": "1.jpg","tags":["Negative"]}

Object Detection JSONs look like:
    {"fileName": "1.jpg", "regions": [{"tag_name": "Closed", "left": 0.00104166672, "top": 0.00208333344, "width": 0.288541675, "height": 0.5104167}]}
'''
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
currentFileNumber = 0
allTags = []

while currentFileNumber < trainer.get_tagged_image_count(project_id=projectid):
    print(currentFileNumber)
    for image in trainer.get_tagged_images(project_id=projectid, take=1, skip=currentFileNumber):
        currentFileNumber = currentFileNumber + 1
        configJSON = json.loads("{}")
        configJSON["fileName"] = str(currentFileNumber) + ".jpg"
        if image.regions != None:               # for Object Detection
            returnedRegions = []
            for region in image.regions:
                if region.tag_name not in allTags:
                    allTags.append(region.tag_name)
                returnedRegion = {}
                returnedRegion["tag_name"] = region.tag_name
                returnedRegion["left"] = region.left
                returnedRegion["top"] = region.top
                returnedRegion["width"] = region.width
                returnedRegion["height"] = region.height
                returnedRegions.append(returnedRegion)
            configJSON["regions"] = returnedRegions
        else:                                   # for Image Classification
            tags = []
            for tag in image.tags:
                tags.append(tag.tag_name)
                if tag.tag_name not in allTags:
                    allTags.append(tag.tag_name)
            configJSON["tags"] = tags

        myfile = os.open(os.path.join(storeImageDirectry, str(currentFileNumber) + ".json"), os.O_TRUNC|os.O_RDWR|os.O_CREAT)
        os.write(myfile, str.encode(json.dumps(configJSON)))
        os.close(myfile)
        print(returnedRegion["tag_name"] + " " + image.original_image_uri)
        error = False
        while error == False:
            try:
                request.urlretrieve(url=image.original_image_uri, filename=os.path.join(storeImageDirectry, str(currentFileNumber) + ".jpg"))
                error = True
            except:
                pass

myfile = os.open(os.path.join(storeImageDirectry, "allTags.json"), os.O_TRUNC|os.O_RDWR|os.O_CREAT)
os.write(myfile, str.encode(json.dumps(allTags)))
os.close(myfile)
