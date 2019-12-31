from datetime import datetime, timedelta
import subprocess
import os
#import downloadFiles as dF

edgelist = './hamnetgraph'
if edgelist == './hamnet201_renamed':
    seeder = ['db0zb']
    servers = ['db0zb','db0hrf','db0hex','db0ins','db0wtl','db0taw','db0bi','db0rod','db0nhm','db0hbg']
elif edgelist == './hamnet100_renamed':
    seeder = ['db0zb']
    #servers = ['db0zb','db0hex','db0ins','db0taw','db0hbg','db0vox','db0uc','db0eam','db0hhb','db0bio'] #10
    #servers = ['db0zb']
    servers = ['db0gth', 'db0wof', 'db0mw', 'db0mhb', 'db0vox', 'db0bul', 'db0wk', 'db0cgw', 'dl1flo1', 'db0son', 'db0rvb', 'db0ins', 'db0kvk', 'db0mio', 'db0cha', 'dm0avh', 'db0mak', 'db0hsr', 'db0mac', 'db0kt', 'dm0hr', 'df0ann', 'db0uhf', 'db0bl', 'db0zw', 'db0bwl', 'db0zm', 'db0bt', 'db0zb', 'db0slk', 'db0fue', 'db0eam', 'db0ein', 'db0hal', 'db0uc', 'dm0ea', 'db0ea', 'db0eb', 'db0hhb', 'db0ktb', 'db0ktn', 'db0nes', 'db0mpq', 'db0oha', 'dg7rz1', 'db0bbg', 'db0fhc', 'db0fha', 'db0fhn', 'db0ase', 'db0tan', 'db0for', 'db0war', 'db0bio', 'df0esa', 'dl9nbj1', 'db0nhm', 'db0hof', 'db0khh', 'db0hol', 'dl8new1', 'db0bam', 'db0hq', 'db0jgk', 'db0noe', 'db0bay', 'db0sbn', 'db0kat', 'db0sn', 'db0cj', 'db0hnk', 'db0hw', 'db0hbs', 'db0dri', 'db0hbg', 'db0gj', 'db0taw', 'db0adb', 'db0hrc', 'db0faa', 'db0hzs', 'db0eml', 'df0as', 'dl1nux', 'db0hex', 'db0shg', 'dm0et', 'db0nu', 'db0yq', 'db0feu', 'db0yz', 'db0rom', 'db0fc', 'dm0svx', 'db0abc', 'db0abb', 'db0ab', 'db0abz', 'db0cra', 'db0erf'] #100
else:
    seeder = ['db0uc']
    servers = ['db0uc','db0ktn']

FNULL = open(os.devnull, 'w')

def useDownload():
    check = False
    while check == False:
        evaluate = raw_input("Evaluate download (y/n): ")
        if evaluate in ['y','Y','yes','Yes']:
            evaluate = 'y'
            check = True
        elif evaluate in ['n','N','no','No']:
            evaluate = 'n'
            check = True
        else:
            print 'Wrong input \n'
            check = False
        #print "%r" % (check) + evaluate
    if evaluate == 'y':
        return True
    else:
        return False

def chooseBoolean():
    check = False
    while check == False:
        input = raw_input("Simulate server outage? (y/n): ")
        if input in ['y','yes','Y','Yes','True','true']:
            check = True
            return True
        elif input in ['n','no','N','no','false','False']:
            check = True
            return False
        else:
            print 'Wrong input \n'
            check = False

def testIterations():
    check = False
    while check == False:
        input = raw_input('Please enter number of tests: ')
        if isinstance(input, (int, long)) == True:
            size = input
            check = True
        elif isinstance(int(input), (int, long)) == True:
            size = input
            check = True
        else:
            print 'Wrong input \n'
            check = False
    if check == True:
        return size
    else:
        return 'Merkwuerdiger Fehler'

def measureTime(title, bo, Instance, Test, iteration):
    timeDelta = [[] for i in range(int(iteration))]
    doc = open('./measurements/%s/%s/results/time_%s.txt' % (Instance,Test,title), 'w+')

    for node in name:
        if not node in seeder:
            for i in range(int(iteration)):
            #for i in range(1,int(iteration)+1):
                #print ('%s %s' % (node, i))
                #with open('./measurements/%s/%s/%s/time/%s.txt' % (Instance, Test, int(iteration), node)) as input:
                with open('./measurements/%s/%s/%s/time/%s.txt' % (Instance, Test, str(i+1), node)) as input:
                    lines = input.readlines()
                    time1 = lines[1]
                    time2 = lines[-1]
                    time1 = datetime.strptime(time1[:23], '%Y-%m-%d %H:%M:%S.%f') #2019-09-30 14:19:25.000
                    time2 = datetime.strptime(time2[:23], '%Y-%m-%d %H:%M:%S.%f')
                    tmp = time2 - time1
                    tmp = tmp.total_seconds()
                timeDelta[i].append(str(tmp))
                print timeDelta
            if bo == True:
                print node
                print tmp
        else:
            for i in range(int(iteration)):
                timeDelta[i].append('0')

    for m in range(int(iteration)):
        timeDelta[m].sort(key=float)
    for l in range(len(name)):
        for o in range(int(iteration)):
            #print ('#%s #%s' % (o, l))
            doc.write('%s ' % str(timeDelta[o][l]))
        doc.write('\n')

    #doc.write('%s, %s\n' % (node, str(timeDelta[name.index(node)])))
    doc.close()
    if bo == True:
        print (timeDelta)

def measureTraffic(title, bo, Instance, Test, iteration):
    bytesIN = [[] for i in range(int(iteration))]
    bytesOUT = [[] for i in range(int(iteration))]
    #print timeDelta
    docIN = open('./measurements/%s/%s/results/traffic_IN_%s.txt' % (Instance,Test,title), 'w+')
    docOUT = open('./measurements/%s/%s/results/traffic_OUT_%s.txt' % (Instance,Test,title), 'w+')

    for i in range(1 , int(iteration) + 1):
        for node in name:
            bytesIN[i-1].append(0)
            bytesOUT[i-1].append(0)
            with open('measurements/%s/%s/%s/traffic/%s_IN.txt' % (Instance, Test, i, node)) as inputIN:
                with open('measurements/%s/%s/%s/traffic/%s_OUT.txt' % (Instance, Test, i, node)) as inputOUT:
                    linesIN = inputIN.readlines()
                    linesOUT = inputOUT.readlines()
                    #print i
                    #print node
                    if len(linesIN) > 2:
                        for j in range(2,len(linesIN)): # first two lines are headers
                            #print j
                            tmp = linesIN[j].split() # tmp[1] = bytes
                            #print tmp
                            bytesIN[i-1][name.index(node)] = bytesIN[i-1][name.index(node)] + int(tmp[1])
                            #print bytesIN[i-1][name.index(node)]
                    if len(linesIN) > 2:
                        for k in range(2,len(linesOUT)):
                            #print k
                            tmp = linesOUT[k].split() # tmp[1] = bytes
                            bytesOUT[i-1][name.index(node)] = bytesOUT[i-1][name.index(node)] + int(tmp[1])

    for m in range(int(iteration)):
        bytesIN[m].sort(key=float)
        bytesOUT[m].sort(key=float)

    for l in range(len(name)):
        for o in range(int(iteration)):
            docIN.write('%s ' % str(bytesIN[o][l]))
            docOUT.write('%s ' % str(bytesOUT[o][l]))
        docIN.write('\n')
        docOUT.write('\n')
    docIN.close()
    docOUT.close()
    if bo == True:
        print (bytesIN)
        print (bytesOUT)

def findInterfaces():
    for node in name:
        interfaces = []
        #print node
        doc = open('./interfaces/%s.txt' % (node), 'w+')
        with open(edgelist) as input:
            lines = input.readlines()
            for line in lines:
                #print line
                if '%s ' % node in line:
                    tmp = line[:line.find(' {')]
                    #print tmp
                    nodes = tmp.split()
                    if tmp.startswith('%s ' % node) == True:
                        interfaces.append('%s-%s' % (node, nodes[1]))
                        #print tmp
                    else:
                        interfaces.append('%s-%s' % (node, nodes[0]))
                        #print tmp

        for i in range(len(interfaces)):
            if not i == len(interfaces) - 1:
                doc.write('%s\n' % interfaces[i])
            else:
                doc.write(interfaces[i])
        doc.close

def serverList():
    #readNodes()
    global serverString_1
    serverString_1 = ''
    global serverString_2
    serverString_2 = ''
    #print name
    #print ip
    for node in servers:
        serverString_1 = serverString_1 + '    - %s:8002\n' % (ip[name.index(node)])
        serverString_2 = serverString_2 + '"%s:8002",' % (ip[name.index(node)])

def dfdaemon(host_ip):
    #serverList()
    #print serverString_1
    #print serverString_2
    doc = open('dfdaemon.yml', 'w+')
    doc.write('supernodes:\n%s\n' % (serverString_1))
    # fuer private registry
    '''
    doc.write('proxies:\n- regx: blobs/sha256.*\n')
    doc.write('hijack_https:\n  cert: df.crt\n  key: df.key\n  hosts:\n')
    for node in seeder:
        doc.write('  - regx: %s\n    insecure: true\n' % (ip[name.index(node)]))
    '''
    # --notbs funktioniert nicht in dfdaemon.yml
    '''
    doc.write('dfget_flags: ["--notbs","--node",%s"--verbose","--ip","%s","port","--expiretime","3m0s","--alivetime","5m0s"]' % (serverString_2, host_ip))
    #if not name[ip.index(host_ip)] in seeder:
        #doc.write('dfget_flags: ["--notbs","--node",%s"--verbose","--ip","%s","--port","15001"]\n' % (serverString_2, host_ip))
        #doc.write('dfget_flags: ["--node",%s"--verbose","--ip","%s"]\n\nsupernodes:\n%s' % (serverString_2, host_ip, serverString_1))
        #doc.write('dfget_flags: ["--node",%s"--verbose","--ip","%s","--notbs"]\n\nsupernodes:\n%s' % (serverString_2, host_ip, serverString_1))
    #else:
        #doc.write('dfget_flags: ["--node",%s"--verbose","--ip","%s","--port","15001"]\n' % (serverString_2, host_ip))
        #doc.write('supernodes:\n%s\n' % (serverString_1))
        #doc.write('dfget_flags: ["--node",%s"--verbose","--ip","%s"]\n\nsupernodes:\n%s' % (serverString_2, host_ip, serverString_1))
        #doc.write('dfget_flags: ["--node",%s"--verbose","--ip","%s","--notbs"]\n\nsupernodes:\n%s' % (serverString_2, host_ip, serverString_1))
    #doc.write('dfget_flags: ["--node",%s"--verbose","--ip","%s","port","15001","--expiretime","3m0s","--alivetime","5m0s","-f","filterParam1&filterParam2"]' % (serverString2,host_ip))
    '''
    doc.close()

def supernode(host_ip):
    doc = open('supernode.yml', 'w+')
    doc.write('base:\n  advertiseIP: %s\n\n  peerUpLimit: 1000\n\n  peerDownLimit: 1000\n\n  eliminationLimit: 1000\n\n  failureCountLimit: 1000' % (host_ip))
    doc.close()

def readNodes():
    global name
    name = []
    global ip
    ip = []
    with open('./infoName.txt') as infoName:
        #linesName = infoName.readlines()
        #if len(name) < len(linesName):
        for line in infoName.readlines():
            #print line
            if not line == "":
                tmp = line
                tmp = tmp.strip("\n")
                name.append(tmp)
    with open('./infoIP.txt') as infoIP:
        #linesIP = infoIP.readlines()
        #if len(ip) < len(linesIP):
        for line in infoIP.readlines():
            #print line
            if not line == "":
                tmp = line
                tmp = tmp.strip("\n")
                ip.append(tmp)
    print name
    print ip

def checkNetwork():
    sum = 0
    for node in set.name:
        if 'mn.'+ set.name in subprocess.check_output(['docker ps'],shell=True):
            sum = sum + 1
        else:
            print (node + ' is missing in network')
    if sum < len(set.name):
        print ('Network is not running correctly')
        exit()
    else:
        print 'Network up and running'

def setupIptables():
    for node in name:
        #print node
        subprocess.call(["docker exec -it mn.%s sh -c 'iptables -N IN'" % node ],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
        subprocess.call(["docker exec -it mn.%s sh -c 'iptables -N OUT'" % node ],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
        subprocess.call(["docker exec -it mn.%s sh -c 'iptables -N FOR'" % node ],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
        with open('interfaces/%s.txt' % (node)) as input:
            for line in input.readlines():
                if not line == '':
                    #print line
                    subprocess.call(["docker exec -it mn.%s sh -c 'iptables -I INPUT -i %s -j IN'" % (node, line)],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
                    subprocess.call(["docker exec -it mn.%s sh -c 'iptables -I OUTPUT -o %s -j OUT'" % (node, line)],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
                    subprocess.call(["docker exec -it mn.%s sh -c 'iptables -I FORWARD -i %s -j FOR'" % (node, line)],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
                    subprocess.call(["docker exec -it mn.%s sh -c 'iptables -I FORWARD -o %s -j FOR'" % (node, line)],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)

def restartExited(): #restart stopped container
    subprocess.call(["docker ps -a | grep Exited > exited.txt"],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
    with open('./exited.txt') as doc:
        for line in doc.readlines():
            tmp = line.split()
            subprocess.call(["docker restart %s" % tmp[-1] ],stdout=FNULL, stderr=subprocess.STDOUT,shell=True)
            print ('%s was restarted' % tmp[-1])

#global name
#name = [] #db0son, db0zb, db0mio, db0drh, dl0new, db0nu, db0adb, db0bt, db0uc, dl1nux, db0ktn, db0rom, db0ren, db0taw, db0fhc
#global ip #db0son, db0zb, db0mio, db0drh, dl0new, db0nu, db0adb, db0bt, db0uc, dl1nux, db0ktn, db0rom, db0ren, db0taw, db0fhc
#ip = []
readNodes()
#global serverString_1 #db0son, db0zb, db0mio, db0drh, dl0new, db0nu, db0adb, db0bt, db0uc, dl1nux, db0ktn, db0rom, db0ren, db0taw, db0fhc
#serverString_1 = ''
#global serverString_2 #db0son, db0zb, db0mio, db0drh, dl0new, db0nu, db0adb, db0bt, db0uc, dl1nux, db0ktn, db0rom, db0ren, db0taw, db0fhc
#serverString_2 = ''
serverList()

#readNodes()
#serverString_1 = ''
#serverString_2 = ''
#for node in servers:
    #serverString_1 = serverString_1 + '    - %s\n' % (ip[name.index(node)])
    #serverString_2 = serverString_2 + '"%s",' % (ip[name.index(node)])
#print serverString_1
#print serverString_2

def __init__():
    #readNodes()
    '''
    serverString_1 = ''
    serverString_2 = ''
    for node in servers:
        serverString_1 = serverString_1 + '    - %s\n' % (ip[name.index(node)])
        serverString_2 = serverString_2 + '"%s",' % (ip[name.index(node)])
    print serverString_1
    print serverString_2
    '''
    #return serverString_1
    #return serverString_2
    #serverList()
    checkNetwork()
    currentInstance = datetime.strftime(datetime.now(),'%Y%m%d%H%M')
