#!/usr/bin/env python

from docker import Client
import yaml

def main():
    cli = Client(base_url='unix://var/run/docker.sock', version='auto')

    dockerps = cli.containers()
    container_id = dockerps[0]['Id']
    
    pids = cli.top(container_id)

    print yaml.safe_dump(pids)
    #print dockerps



if __name__ == '__main__':
    main()
