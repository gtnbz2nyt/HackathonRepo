#!/usr/bin/env python 

from utility.helpers import getArgs
from utility.helpers import kairosAuthConfig
import json
import kairos_face


def getImage():
    import cv2

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("PhotoBooth")

    while True:
        ret, frame = cam.read()
        cv2.imshow("PhotoBooth", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 32:
            # SPACE pressed
            img_name = "portrait.png"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break

    cam.release()

    cv2.destroyAllWindows()
    return("portrait.png")

options = getArgs()
conf = kairosAuthConfig(options.credentials, options.profile)

app_id=conf['app_id']
app_key=conf['app_key']

kairos_face.settings.app_id = app_id
kairos_face.settings.app_key = app_key

galleries_list = kairos_face.get_galleries_names_list()

image_file=getImage()

foo = kairos_face.enroll_face(file=image_file, subject_id='subject1', gallery_name='a-gallery')
print(json.dumps(foo, indent=4))

