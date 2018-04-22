#!/usr/bin/env python
import os, sys

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from cloudinary.api import delete_resources_by_tag, resources_by_tag, update
from pandas.io.json import json_normalize
import pprint
import json
import pandas

# config
os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
if os.path.exists('settings.py'):
    exec(open('settings.py').read())

DEFAULT_TAG = "python_sample_basic"


def generate_sql(df):
   inserts = []
   for i in range(len(df)):
       AGE = df['age'][i]
       GENDER = df['gender'][i]
       ANGER = df['anger'][i]
       CONTEMPT = df['contempt'][i]
       DISGUST = df['disgust'][i]
       FEAR = df['fear'][i]
       HAPPINESS = df['happiness'][i]
       NEUTRAL = df['neutral'][i]
       SADNESS = df['sadness'][i]
       SURPRISE = df['surprise'][i]
       CREATED_AT = df['created_at'][i]
       PUBLIC_ID = df['public_id'][i]
       sql = f'''INSERT INTO hackathon.flat_rsp (age, gender, anger, contempt, disgust, fear, happiness, neutral, sadness, surprise, created_at, public_id) VALUES({AGE}, '{GENDER}', {ANGER}, {CONTEMPT}, {DISGUST}, {FEAR}, {HAPPINESS}, {NEUTRAL}, {SADNESS}, {SURPRISE}, '{CREATED_AT}', '{PUBLIC_ID}');'''
       inserts.append(sql)
   return inserts

def get_info_from_json(data):
   import pandas as pd
   try:
       data['info']['detection']['adv_face']['data']
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
       cols_to_keep_2 = ['created_at','public_id']
       dat1 = dat1[cols_to_keep_2]
       dat1['tmp'] = '1'
       DF = pd.merge(dat3, dat1, on=['tmp'])
       DF.drop('tmp', axis=1)
       return DF
   except Exception:
       pass


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
    payload = []
    response = resources_by_tag(DEFAULT_TAG, max_results=300)
    # print(response)
    resources = response.get('resources', [])
    
    if not resources:
        print("No images found")
        return
    pass
    for item in resources:
        # print(item["public_id"])
        face = update(item["public_id"], detection="adv_face")
        # print("face:", type(face))
        # print(face["info"]["detection"])
        
        if 'data' in face["info"]["detection"]["adv_face"]:
           # print("Found")
           # print(get_info_from_json(face))
           dbrow = get_info_from_json(face)
           print(generate_sql(dbrow))
        else:
           pass
        # print(get_info_from_json(face))
        # dbrow = get_info_from_json(face)
        # print(dbrow)
        # payload.append(dbrow)


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
