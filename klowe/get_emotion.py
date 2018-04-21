#!/usr/bin/env python
import os, sys

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from pandas.io.json import json_normalize
import pprint
import json
import pandas

# config
os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
if os.path.exists('settings.py'):
    exec(open('settings.py').read())

DEFAULT_TAG = "python_sample_basic"

def get_info_from_json(data):
    import pandas as pd
    dat1 = json_normalize(data)
    dat2 = json_normalize(dat1['info.detection.adv_face.data'][0])
    cols_to_keep = ['attributes.age', 'attributes.gender',
           'attributes.emotion.anger', 'attributes.emotion.contempt',
           'attributes.emotion.disgust', 'attributes.emotion.fear',
           'attributes.emotion.happiness', 'attributes.emotion.neutral',
           'attributes.emotion.sadness', 'attributes.emotion.surprise']
    dat3 = dat2[cols_to_keep]
    dat3.columns = [x.split('.')[-1] for x in list(dat3.columns.values)]
    dat3['tmp']='1'
    cols_to_keep_2 = ['created_at','etag','public_id','signature']
    dat1 = dat1[cols_to_keep_2]
    dat1['tmp'] = '1'
    DF = pd.merge(dat3, dat1, on=['tmp'])
    DF.drop('tmp', axis=1)
    return DF

def dump_response(response):
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))

def upload_files(filename):
    import json
    #print("--- Upload a local file")
    response = upload( './foo/' + filename, tags = DEFAULT_TAG, detection="adv_face")
    print(response)
    url, options = cloudinary_url(response['public_id'],
        format = response['format'],
        width = 200,
        height = 150,
        crop = "fill"
    )
    print(get_info_from_json(sample))

def cleanup():
    response = resources_by_tag(DEFAULT_TAG)
    resources = response.get('resources', [])
    if not resources:
        print("No images found")
        return
    print("Deleting {0:d} images...".format(len(resources)))
    delete_resources_by_tag(DEFAULT_TAG)
    print("Done!")
    pass

def getemotion():
    response = resources_by_tag(DEFAULT_TAG, max_results=500)
    resources = response.get('resources', [])
    print(resources)
    if not resources:
        print("No images found")
        return
    pass


if len(sys.argv) > 1:
    if sys.argv[1] == 'upload': 
        filelist = os.listdir("./images")
        for filename in filelist:
            print(filename)
            upload_files(filename)

    if sys.argv[1] == 'cleanup': cleanup()
    if sys.argv[1] == 'getemotion': getemotion()
else:
    print("--- Uploading files and then cleaning up")
    print("    you can only one instead by passing 'upload' or 'cleanup' as an argument")
    print("")
    upload_files()
