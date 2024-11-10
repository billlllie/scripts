import socket,random,os

# execDir = "/root/AutoRclone/rclone_sa_magic.py"
# workDir = "/root/AutoRclone"
# beginDir = "/root/scripts/begin"
workDir = '<work dir>'
execDir = '<rclone_sa_magic.py dir>'
beginDir = "<being dir>"

def isInuse(ipList, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for ip in ipList:
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            print (port,' is in use')
            return True
        except:
            print (port,' is free')
            return False

def getRandPort(start,end):
    ipList = ["localhost"]
    port = int(random.uniform(start,end))
    while isInuse(ipList,port):
        port = int(random.uniform(start,end))
    return str(port)

def getSARange():
    dst = int(random.uniform(1,588))
    while not checkSAAvai(dst):
        dst = int(random.uniform(1,588))
    return dst

def checkSAAvai(dst):
    begins = []
    with open(beginDir,"r") as f:
        array=f.readline()
        if len(array)!=0:
            begins = eval(array)
        
        
    # case no such file
    if len(begins)==0:
        begins.append(dst)
        with open(beginDir,"w") as f:
            f.write(str(begins))
        return True
    else:
        for i in range(len(begins)):
            # case first dst
            if i==0:
                if dst+9<begins[0] or begins[0]+9<dst:
                    if len(begins)==1:
                        if dst<begins[0]:
                            begins.insert(0,dst)
                        else:
                            begins.insert(1,dst)
                        with open(beginDir,"w") as f:
                            f.write(str(begins))
                        return True
                    continue
                else:
                    return False
            else:
                if i==len(begins)-1:
                    if dst>begins[i]+9:
                        begins.append(dst)
                        with open(beginDir,"w") as f:
                            f.write(str(begins))
                        return True
                if dst>begins[i-1]+9 and dst+9<begins[i]:
                    begins.insert(i,dst)
                    with open(beginDir,"w") as f:
                        f.write(str(begins))
                    return True
        return False

def revokeSA(dst):
    begins = []
    with open(beginDir,"r") as f:
        array=f.readline()
        if len(array)!=0:
            begins = eval(array)
    
    begins.remove(dst)
    with open(beginDir,"w") as f:
        f.write(str(begins))

def popUpInter():
    source = input("Source id: ")
    dirName = input("Dir name: ")
    os.chdir(workDir)
    begin = getSARange()
    end = begin+10
    command = "python "+execDir+" -s "+source+" -d 0ADjAjf54ao08Uk9PVA -dp "+dirName+" -b "+str(begin)+" -e "+str(end)+" -p "+getRandPort(5000,65000)
    # print(command)
    os.system(command)
    revokeSA(begin)
    os.system("pause")

popUpInter()