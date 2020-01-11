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
    ls = []
    processList = {}
    for p in psutil.process_iter(attrs=['name']):
        if not (p.info['name'] in processList):
            processList[p.info['name']]=1
        else:
            processList[p.info['name']]=processList[p.info['name']]+1
    return processList


def main():
    pList = quantList()
   
    print(pList)
    
    
if __name__== "__main__":
  main()
