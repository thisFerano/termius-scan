import os
import socket
import json
import time

# termius password
password = ''

# username for all hosts
username = 'root'

# scan mutliple ip ranges
def scanmultiple():
    # usage:
    # scan(port, ip, start, end)
    # [port] is the port to scan
    # [ip] are only the first 3 parts of the ip address
    # [start], [end] are the range of the ip address
    # [group] is the group to add the hosts to
    # example:
    scan(80, '192.168.178', 1, 2, 'Home (auto)')
    scan(22, '10.0.0', 5, 6, 'RZ (Auto)')
    scan(80, '192.168.178', 9, 10, 'test3')



    
##########
## MAIN ##
##########

# scanner main
def scan(port, ip, start, end, group):
    end += 1
    for p in range(start, end):
        temp_ip = ip + '.' + str(p)
        if temp_ip in getHosts():
            print('host already exists: ' + temp_ip)
            continue
        
        if group is not None:
            if group in checkgroups():
                continue
            else:
                createGroup(group)
        
        if porttry(port, temp_ip):
            createHost(temp_ip, temp_ip, group)


# portscanner on single host
def porttry(port, ip):
    try:
        print('Scanning ' + ip)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        res = sock.connect_ex((ip, port))
        sock.settimeout(None)
        if res == 0:
            return True
        sock.close()
    except Exception as e:
        return False

# push termius hosts
def push(password):
    res = os.system('termius push --password ' + password)
    if res == 0:
        return True
    elif res == 1:
        return False

# pull termius hosts
def pull(password):
    res = os.system('termius pull --password ' + password)
    if res == 0:
        return True
    elif res == 1:
        return False

# create new host
def createHost(ip, label, group):
    cmd = 'termius host --address ' + ip + ' --label ' + label + ' --username ' + username
    if group is not None:
        cmd += ' --group ' + group
    os.system(cmd)
    print('created host: ' + ip)

# get existing hosts
def getHosts():
    hosts = []
    url = 'C:\\Users\\' + os.getlogin() + '\\.termius\\storage'
    f = open(url, 'r')
    content = json.loads(f.read())
    content = content['host_set']
    for e in content:
        hosts.append(e['address'])
    return sorted(hosts)

def createGroup(name):
    os.system('termius group --label ' + name)
    print('created group: ' + name)

def checkgroups():
    groups = []
    url = 'C:\\Users\\' + os.getlogin() + '\\.termius\\storage'
    f = open(url, 'r')
    content = json.loads(f.read())
    content = content['group_set']
    for e in content:
        groups.append(e['label'])
    return sorted(groups)

def __main__():
    # pull termius data
    pull(password)
    # wait 10 seconds for the data to be pulled
    time.sleep(10)
    # get all hosts
    existing_hosts = getHosts()
    # scan multiple ip ranges
    scanmultiple()

    push(password)


if __name__ == '__main__':
    __main__()
