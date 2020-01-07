import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == name:
            ls.append(p)
            print("beep")
    return ls
	
	




def main():
  find_procs_by_name('Discord.exe')
  
if __name__== "__main__":
  main()
