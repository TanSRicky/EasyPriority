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
		if(p.info['name'] in processList) :
			processList.add()
    return processList

	
def main():
	quantList()
  
if __name__== "__main__":
  main()
