#!/usr/bin/python
# -*- coding: utf-8 -*-
# test.py

from progress.bar import Bar, IncrementalBar
from progress.spinner import Spinner
import time
import os
import subprocess
import settings as set

def check():
    #print 'check läuft'
    set.readNodes()
    sumB = 0
    babeld = []
    sumD = 0
    dfclient = []
    sumS = 0
    supernode = []
    for node in set.name:
        tmp = subprocess.check_output(['docker exec mn.%s docker ps' % node],shell=True)
        doc = open('./tmp.txt', 'w+')
        doc.write(tmp)
        doc.close()
        checkB = False #Check for babeld container
        checkD = False #Check for dragonfly_client container
        checkS = False #Check for opentracker container

        with open('./tmp.txt') as info:
            lines = info.readlines()
            for line in lines:
                tmp = line.split()
                #print tmp[-1]
                if tmp[-1] == 'babeld':
                    checkB = True
                if tmp[-1] == 'dfclient':
                    checkD = True
                if node in set.servers:
                    if tmp[-1] == 'supernode':
                        checkS = True
                else:
                    checkS = True
        if checkB == False:
            babeld.append(node)
            sumB = sumB + 1
        if checkD == False:
            if node in babeld:
                dfclient.append(node)
            sumD = sumD + 1
        if checkS == False:
            supernode.append(node)
            sumS = sumS + 1

    print ('%s container(s) not running babeld: %s' % (str(sumB),babeld))
    print ('%s container(s) not running dfclient: %s' % (str(sumD),dfclient))
    print ('%s container(s) not running supernode: %s' % (str(sumS),supernode))

    #print ('%s babeld container not running correctly\n%s dfclient container not running correctly\n%s supernode container not running correctly' % (str(sumB), str(sumD), str(sumS)))

    for node in babeld:
        if node in set.servers:
            subprocess.call(["docker exec mn.%s sh -c 'export IP=%s && docker-compose -f stack_server.yml up -d'" % (node, set.ip[set.name.index(node)])],shell=True)
        else:
            subprocess.call(["docker exec mn.%s sh -c 'export IP=%s && docker-compose -f stack_client.yml up -d'" % (node, set.ip[set.name.index(node)])],shell=True)
    for node in dfclient:
        if not node in babeld:
            if node in set.servers:
                subprocess.call(["docker exec mn.%s sh -c 'export IP=%s && docker-compose -f stack_server.yml up -d'" % (node, set.ip[set.name.index(node)])],shell=True)
            else:
                subprocess.call(["docker exec mn.%s sh -c 'export IP=%s && docker-compose -f stack_client.yml up -d'" % (node, set.ip[set.name.index(node)])],shell=True)
    for node in supernode:
        if not node in (babeld or dfclient):
            subprocess.call(["docker exec mn.%s sh -c 'export IP=%s && docker-compose -f stack_server.yml up -d'" % (node, set.ip[set.name.index(node)])],shell=True)
