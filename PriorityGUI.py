from tkinter import *
import Kicker as p

selected = set()
procs = p.fillPQList()
root = Tk() 
root.geometry("500x500") 
globalSelect = ""

mylabel = Label(root, text ='Priority Manager', font = "30", width = "200")
mylabel.pack()
myscroll = Scrollbar(root) 
mylist = Listbox(root, yscrollcommand = myscroll.set,selectmode='extended',width = "25") 
myscroll.pack(side = RIGHT, fill = Y) 
myscroll.config(command = mylist.yview) 
newList = Listbox(root, yscrollcommand = myscroll.set,selectmode="browse",width = "25")


for line in range(len(procs)): 
		mylist.insert(END , procs[line])

mylist.pack(side = LEFT, fill = BOTH )	
newList.pack(side = LEFT ,fill = BOTH )	
indiList = Listbox(root, yscrollcommand = myscroll.set,selectmode="browse",width = "100")
indiList.pack(side=LEFT,fill=BOTH)
v =IntVar()

def buttons():
	

	Radiobutton(root, 
				   text="Real Time",
				   padx = 20, 
				   variable=v, 
				   value=5).pack(anchor=W)
	Radiobutton(root, 
				   text="Above Normal",
				   padx = 20, 
				   variable=v, 
				   value=4).pack(anchor=W)
	Radiobutton(root, 
				   text="Above Normal",
				   padx = 20, 
				   variable=v, 
				   value=3).pack(anchor=W)
	
	Radiobutton(root, 
				   text="Normal",
				   padx = 20, 
				   variable=v, 
				   value=2).pack(anchor=W)
	Radiobutton(root, 
				   text="Idle",
				   padx = 20, 
				   variable=v,
				   value=1).pack(anchor=W)
	Radiobutton(root, 
				   text="Below Normal",
				   padx = 20, 
				   variable=v, 
				   value=0).pack(anchor=W)
				   
	
def cb(event):
	
	selection = str(mylist.get(mylist.curselection()))
	globalSelect = selection
	p.getNice(selection)
	if selection not in selected:
		selected.add(selection)
		newList.insert(END,str(mylist.get(mylist.curselection())))
		root.update()

def sublist(event):
	selection = str(newList.get(newList.curselection()))
	globalSelect = selection
	indiList.delete(0,END)
	for a in p.getNice(selection):
		indiList.insert(END,a)
	root.update()
	
	
def GUIStart():
	
	mylist.bind('<Double-1>', cb)	
	newList.bind('<Double-1>',sublist)
	buttons()
	def helloCallBack():
		selection = str(newList.get(newList.curselection()))
		p.setNice(selection,v.get())
		indiList.delete(0,END)
		for a in p.getNice(selection):
			indiList.insert(END,a)
		root.update()
		
	def pidCallBack():
		selection = indiList.get(indiList.curselection())
		pid = selection[0]
		name = selection[1]
		print(pid)
		print(name)
		p.setNicePID(pid,v.get())
		indiList.delete(0,END)
	
		for a in p.getNice(name):
			indiList.insert(END,a)
		root.update()	
	B = Button(root, text ="Change All Processes of this Name", command = helloCallBack)
	A = Button(root, text ="Change Individual Pid", command = pidCallBack)
	
	A.pack()
	B.pack()
	   

	root.mainloop() 
	
	
	
	
	
	
	
	
	
	
	
	
	