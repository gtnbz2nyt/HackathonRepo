#!/usr/bin/env python
import os, sys

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from cloudinary.api import delete_resources_by_tag, resources_by_tag
import pprint
import json
import pandas

# config
os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
if os.path.exists('settings.py'):
    exec(open('settings.py').read())

DEFAULT_TAG = "python_sample_basic"

def get_info_from_json(sample):
    from pandas.io.json import json_normalize
    cols_to_keep = ['attributes.age',
       'attributes.emotion.anger', 'attributes.emotion.contempt',
       'attributes.emotion.disgust', 'attributes.emotion.fear',
       'attributes.emotion.happiness', 'attributes.emotion.neutral',
       'attributes.emotion.sadness', 'attributes.emotion.surprise']
    data = json_normalize(json_normalize(sample).iloc[0][0])[cols_to_keep]
    data.columns = [x.split('.')[-1] for x in list(b.columns.values)]
    #data['emotion'] = data[['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral','sadness', 'surprise']].idxmax(axis=1)
    #data = data[['age','emotion']]
    return data


def dump_response(response):
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))

def upload_files(filename):
    import json
    #print("--- Upload a local file")
    response = upload( './images/' + filename, tags = DEFAULT_TAG, detection="adv_face")
#     sample = json.dumps(response['info'])
    # sample = dump_response(response)
    #print("---------")
    print(response)
    #print("---------")
#    dump_response(response)
    url, options = cloudinary_url(response['public_id'],
        format = response['format'],
        width = 200,
        height = 150,
        crop = "fill"
    )
    # print(get_info_from_json(sample))

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

if len(sys.argv) > 1:
    if sys.argv[1] == 'upload': 
        filelist = os.listdir("./images")
        for filename in filelist:
            print(filename)
            upload_files(filename)

    if sys.argv[1] == 'cleanup': cleanup()
else:
    print("--- Uploading files and then cleaning up")
    print("    you can only one instead by passing 'upload' or 'cleanup' as an argument")
    print("")
    upload_files()
