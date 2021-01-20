import os,sys,argparse
from time import sleep
import pathlib,re
ap=argparse.ArgumentParser()
ap.add_argument("-n","--new",nargs='?' ,required=False,help="Initializing ...")
ap.add_argument("-f","--freeze",nargs='?' ,required=False,help="Freezing modules")
ap.add_argument("-i","--install",nargs='?' ,required=False,help="Installing modules")
ap.add_argument("-p","--python",default="3",required=False,help="Install for one version of python")
ap.add_argument("-c","--count",required=False,help="Count of modules to install")

ap.add_argument("-a","--auto",nargs='?' ,required=False,help="Auto freezing and installing modules")
path="$HOME/.fire"
args=vars(ap.parse_args())
args["freeze"] = "s "
args["install"] = " s" 
home=pathlib.Path.home()
nhome=re.findall(r"\w*",str(home))
home="/"+nhome[1]+"/"+nhome[3]
def Help():
	print("""
	1- -n --> Initializing ...
	2- -f --> Freezing Modules 
	3- -i --> installing Modules 
	4- -i -c 20 installing 20 Modules only
	5- -f -i -c 20 -->  Freezing and installing 20 Modules only
	6- -p --> install module for one version of python 
	7- -a --> auto freezing and installing modules

Example :
	fire [command]:
	[+]- fire -n --> Initializing ...
	[+]- fire -a -p 3 -c 10 --> Freezing and inastalling 10\n\t\tmodule for python3	
	""")
def Initialize():
	if os.path.exists("%s/.fire"%home):
		if os.path.isfile("%s/.fire/logs"%home) and os.path.isfile("%s/.fire/Modules"%home):
			print("you are also initialized ... :)")
	else:
		print("WELCOME TO fire :)")
		print("Initializing ...")
		print("Please wite ...")
		sleep(2)

		os.system("mkdir $HOME/.fire >> $HOME/.fire/logs")
		os.system("touch $HOME/.fire/logs >> $HOME/.fire/logs;touch $HOME/.fire/Modules >> $HOME/.fire/logs")
		#os.system("echo $HOME > .initialize")
		print("Initializing Finished ! :)")
def Freezer():
	print("WELCOME To fire :)")
	print("Freezing a modules ...")
	print("Please wite ...")
	os.system("echo Freezing >> %s/logs;date >> %s/logs;cp %s/Modules %s/Modules.backup >> %s/logs;python%s -m pip freeze > Modules;mv Modules %s/Modules"%(path,path,path,path,path,args["python"],path))
	print("Freezing Finished ! :)")

def Installer():
	print("Strating installation ...")
	if "-c" in sys.argv[:]:
		scope=sys.argv[:].index("-c")
		scope=sys.argv[scope+1]
		count=0
		with open("%s/.fire/Modules"%(home),"r") as file:
			for line in file.readlines(int(scope)):
					try:
						os.system("echo Installing >> %s/logs;date >> %s/loga;python%s -m pip install %s >> %s/logs"%(path,path,args["python"],line,path))
						count+=1
					except:
						print("Error : Please Checking help")
						file.close()
						Help()
	else:
		with open("%s/.fire/Modules"%(home),"r") as file:
			for line in file.readlines():
				try:
					os.system("echo Intsalling >> %s/logs;date >> %s/logs;python%s -m pip install %s >> %s/logs"%(path,path,args["python"],line,path))
					count+=1
				except:
					print("Error : Please Checking help")
					file.close()
					Help()
					break

def RUN():
	if "-n" in sys.argv[:]:
		Initialize()
	elif "-f" in sys.argv[:]:
		Freezer()
	elif "-i" in sys.argv[:]:
		Installer()
	elif "-a" in sys.argv[:]:
		Freezer()
		Installer()
	else:
		print("Error : Please enter following argument to works",end="")
		Help()
RUN()