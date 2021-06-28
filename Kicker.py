import psutil
prios = [
	psutil.BELOW_NORMAL_PRIORITY_CLASS,
	psutil.IDLE_PRIORITY_CLASS,
	psutil.NORMAL_PRIORITY_CLASS,
	psutil.ABOVE_NORMAL_PRIORITY_CLASS,
	psutil.HIGH_PRIORITY_CLASS,
	psutil.REALTIME_PRIORITY_CLASS
]
procs = {
    p : p.info
    for p in psutil.process_iter(['pid','name', 'username'])
}

processList = {}
choiceList = []



def getNice(name):
	subList = []
	for p in psutil.process_iter(attrs = ['name','pid']):
		if p.info['name'] == name :
			subList.append([p.info['pid'],p.info['name'],p.nice()])
	return subList

def setNicePID(pid,index):

    for p in psutil.process_iter(attrs = ['pid']):
        if p.info['pid'] == pid:
            p.nice(prios[index])

    return "Success"


def setNice(name,index):

    for p in psutil.process_iter(attrs = ['name']):
        if p.info['name'] == name:
            p.nice(prios[index])

    return "Success"


def fillPQList():
    global processList
    for k, v in procs.items():
        if v['username'] == None: continue
        if not(v['name'] in processList):
            choiceList.append(v['name'])
            processList[v['name']] = 1
        else :
            processList[v['name']] = processList[v['name']] + 1
    return choiceList

def getNameList():
    pList = quantList()
    keys = pList.keys()
    ls = []
    for k in keys:
        ls.append(k)
    return ls

def getMenu():
    delim = "-"
    i = 1
    for(k,v) in processList.items():
        if( v >= 2 ) : delim = "+"
        k = str(i) + ". " + k
        print(k  ,str(v).rjust(50-len(str(k)),delim))
        delim = "-"
        i = i + 1
  
def kvProcs():
    for k, v in procs.items():
        if v['username'] != None: print(k, v)