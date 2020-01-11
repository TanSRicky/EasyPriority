import psutil

def lowerPrio(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == name:
            ls.append(p)
            p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
            print(p)
            print(p.nice())
    return ls

def quantList():
    "Return a list of processes matching 'name'."
    ls = []
    processList = {}
    for p in psutil.process_iter(attrs=['name']):
        if not (p.info['name'] in processList):
            processList[p.info['name']]=1
        else:
            processList[p.info['name']]=processList[p.info['name']]+1
    return processList

def getMenu():
    pList = quantList()
    keys = pList.keys()
    i = 1
    for k in keys:
        if (i < 10): print(i ,'',k.ljust(75,'.'), pList[k])
        if (i >= 10 ): print(i ,k.ljust(75,'.'), pList[k])
        i = i + 1
    
def main():
    getMenu()
    
    
if __name__== "__main__":
  main()
