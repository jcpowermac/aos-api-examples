#!/usr/bin/env python

from subprocess import Popen, PIPE
import requests
import pprint
import json

def gettoken():

    p = Popen(['oc', 'whoami', '-t'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode 
    return output.rstrip('\n')


def aosget(url, token):

    headers = {'Authorization': 'Bearer %s' % token }
    req = requests.get(url, headers=headers, verify=False)

    if req.status_code == 200:
        json = req.json()
        return json
    return {}


def main():
   
    pp = pprint.PrettyPrinter(indent=4)
    token = gettoken()

    url = "https://origin-master1.virtomation.com:8443/oapi/v1/namespaces/testing/imagestreams/mysql-container"

    isiurl = "https://origin-master1.virtomation.com:8443/oapi/v1/namespaces/testing/imagestreamimages/%s"


    results = aosget(url, token)

    dockerImageReference = results['status']['tags'][0]['items'][0]['dockerImageReference'].split('/')[-1]


    isi_results = aosget( isiurl % dockerImageReference, token)
    #print isi_results
    pp.pprint( json.dumps(isi_results) )

if __name__ == '__main__':
    main()
