import settings as set
global serverString_1
global serverString_2
'''
def serverList1():
    set.readNodes()
    serverString1 = ''
    print set.name
    #print set.servers
    for node in set.servers:
        serverString_1 = serverString_1 + '    - %s\n' % (set.ip[set.name.index(node)])
    return serverString1

def serverList2():
    set.readNodes()
    serverString_2 = ''
    #print set.name
    #print set.servers
    for node in set.servers:
        serverString_2 = serverString_2 + '"%s",' % (set.ip[set.name.index(node)])
    return serverString_2
    #return serverString
'''
def serverList():
    set.readNodes()
    serverString_1 = ''
    serverString_2 = ''
    #print set.name
    #print set.servers
    for node in set.servers:
        serverString_1 = serverString_1 + '    - %s\n' % (set.ip[set.name.index(node)])
        serverString_2 = serverString_2 + '"%s",' % (set.ip[set.name.index(node)])
    #return serverString

def dfdaemon(host_ip):
    serverList()
    print serverString_1
    print serverString_2
    doc = open('dfdaemon.yml', 'w+')
    doc.write('dfget_flags: ["--notbs","--node",%s"--verbose","--ip","%s","port","--expiretime","3m0s","--alivetime","5m0s"\n\nsupernodes:\n%s]' % (serverString_2, host_ip, serverString_1))
    #doc.write('dfget_flags: ["--node",%s"--verbose","--ip","%s","port","15001","--expiretime","3m0s","--alivetime","5m0s","-f","filterParam1&filterParam2"]' % (serverString2,host_ip))
    doc.close()


#def rewriteConfig():
def __init__():
    set.readNodes()
    serverList()
    global serverString1
    global serverString2
    print set.servers
    print set.name
    print set.ip

#def __init__():
    #set.readNodes()
