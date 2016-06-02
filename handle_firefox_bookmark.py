#!/usr/bin/python
import json
import sys
#from pprint import pprint 

file_name=''.join(sys.argv[1:]) or '/mnt/share/bookmarks-2016-06-02.json'
uri_data=[]

with open(file_name) as json_file:
    data=json.load(json_file)
    for uri_item in data['children'][2]['children']:
        uri_data.append(uri_item['uri'])
print '\n'.join(str(x) for x in uri_data) 
