import os,threading,requests
from time import sleep,ctime,time

timeStart=int(round(time() * 1000))
class myThread(threading.Thread):
    def __init__(self,threadID,name,s,e):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.s = s
        self.e = e

    def run(self):
        print("Starting "+self.name+" "+ctime())
        
        lines = ""
        url = urls[self.s:self.e]
        for u in url:
                array = u.split('/')
                array.sort(key=lambda u:len(u),reverse=True)
                lines += "https://gd.link.oaak.bid/link/"+array[0]+"\n"
                # endpoint = "https://gd.link.oaak.bid/link/"+array[0]+"?output=json"
                # r = requests.get(endpoint)
                # data=r.json()
                # lines += data.get("result").get("url")+"\n"

        # mutex lock part
        threadLock.acquire()
        with open('downloadLinked.txt','a') as f:
            f.write(lines)
        threadLock.release()

def writeUrl(url):
    array = url.split('/')
    array.sort(key=lambda u:len(u),reverse=True)
    return "https://gd.link.oaak.bid/gd/"+array[0]+"\n"


urls = []
with open('share.txt','r') as f:
    urls = f.readline().split(',')

with open('downloadLinked.txt','w') as f:
    f.write("")


totalThread = 5
gap = len(urls)//totalThread

threadLock = threading.Lock()
threads = []

for i in range(totalThread):
    thread = 'thread%s' % i
    if i==0:
        thread = myThread(0,"Thread-%s" % i,0,gap)
    elif totalThread==i+1:
        thread = myThread(i,"Thread-%s" % i,i*gap,len(urls))
    else:
        thread = myThread(i,"Thread-%s" % i,i*gap,(i+1)*gap)
    threads.append(thread)

for i in range(totalThread):
    threads[i].start()

for t in threads:
    t.join()

print("Exiting Main Thread "+ctime())
timeEnd = int(round(time() * 1000))
print("Time elasped "+str(timeEnd-timeStart)+" ms")
