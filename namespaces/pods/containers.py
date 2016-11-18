#!/usr/bin/env python

from subprocess import Popen, PIPE
import requests
import pprint
import json
import yaml

def gettoken():

    p = Popen(['oc', 'whoami', '-t'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode 
    return output.rstrip('\n')


def aosget_text(url, token):

    headers = {'Authorization': 'Bearer %s' % token, 'Accept': 'application/yaml'}
    req = requests.get(url, headers=headers, verify=False)

    if req.status_code == 200:
        text = req.text
        return text 
    return ""

def aosget_yaml(url, token):

    headers = {'Authorization': 'Bearer %s' % token, 'Accept': 'application/yaml'}
    req = requests.get(url, headers=headers, verify=False)

    if req.status_code == 200:
        text = req.text
        return yaml.load(text)
    return {}

def aosget(url, token):

    headers = {'Authorization': 'Bearer %s' % token }
    req = requests.get(url, headers=headers, verify=False)

    if req.status_code == 200:
        print "here"
        json = req.json()
        return json
    print req.text
    return {}


def main():
   
    pp = pprint.PrettyPrinter(indent=4)
    token = gettoken()

    url = "https://origin-master1.virtomation.com:8443/api/v1/namespaces/cake/pods"
    #url = "https://origin-master1.virtomation.com:8443/oapi/v1/projects/cake/pods"

    results = aosget_text(url, token)
    
    print results 



if __name__ == '__main__':
    main()
