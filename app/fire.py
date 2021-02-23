#!/usr/bin/python3

## --> this is just for fun :)

#these is a require library for run app 
import os,sys,argparse
from time import sleep
import pathlib,re
import shutil
#define a arguments in following lines  
ap=argparse.ArgumentParser()
ap.add_argument("-n","--new",nargs='?' ,required=False,help="Initializing ...")
ap.add_argument("-f","--freeze",nargs='?' ,required=False,help="Freezing modules")
ap.add_argument("-i","--install",nargs='?' ,required=False,help="Installing modules")
ap.add_argument("-p","--python",default="3",required=False,help="working on this version of python")
ap.add_argument("-c","--count",required=False,help="Count of modules to install")
ap.add_argument("-a","--auto",nargs='?' ,required=False,help="Auto freezing and installing modules")
ap.add_argument("-m","--modules",nargs='?' ,required=False,help="Print a number of your modules")
ap.add_argument("-u","--upgrade",nargs='?' ,required=False,help="Upgrade all modules")
ap.add_argument("-v","--version",nargs='?' ,required=False,help="Print a version of fire app")



args=vars(ap.parse_args())

#fine, this is a path variable of program folder 
path="$HOME/.fire/out"

#following lines is gete and saved a path of home 
home=pathlib.Path.home()
nhome=re.findall(r"\w*",str(home))
home="/"+nhome[1]+"/"+nhome[3]

#this is a help function 
def Help():
	#in here, printing a valid argument for work
	print("""
	1- -n --> Initializing ...
	2- -f --> Freezing Modules 
	3- -m --> number of your modules
	4- -i -p --> installing Modules for this version of python
	5- -i -c 20 --> installing 20 Modules only
	6- -f -i -c 20 -->  Freezing and installing 20 Modules only
	7- -p --> working on this version of python 
	8- -a -p 3 --> auto freezing and installing all modules\n\tfor this version of python 
	9- -u -p --> upgrade all modules of this version of python
	10- -v --> version of fire app

Example :
	fire [command]:
	[+]- fire -n --> Initializing ...
	[+]- fire -m --> number of your modudles is --> 
	[+]- fire -a -p 3 -c 10 --> Freezing and inastalling 10\n\tmodule for python3	
	""")

#this function is intitalizer
def Initialize():
	pwd = os.getcwd()
	fh = home+"/.fire"
	if os.path.exists("%s/.fire"%home):
		if os.path.isfile("%s/.fire/out/logs"%home) and os.path.isfile("%s/.fire/out/Modules"%home):
			print("[!]- you are also initialized ... :)")
	else:
		print("[+]- Initializing ...")
		h = home+"/.fire"
		os.mkdir(h)
		os.chdir(fh)
		os.mkdir("app")
		os.mkdir("out")
		os.chdir("out")
		os.system("touch logs Modules")
		os.chdir(pwd)
		shutil.copy("fire.py", fh+"/app")
		os.chdir("../")
		for i in os.listdir("."):
			if os.path.isfile(i):
				shutil.copy(i, fh)

		#os.system("touch $HOME/.fire/out/logs;touch $HOME/.fire/out/Modules")
		os.chdir(home+"/")
		status = False
		for file in os.listdir("."):
			if file == ".bashrc":
				with open(".bashrc", "a+") as file:
					for line in file.readlines():
						if line == "alias fire":
							status = True
					if status == False:
						file.write("alias fire = \"python3 $HOME/.fire/app/fire,py\" ")
				file.close()
			elif file == ".zshrc":
				with open(".zshrc", "a+") as file:
					for line in file.readlines():
						if line == "alias fire":
							status = True
					if status == False:
						file.write("alias fire = \"python3 $HOME/.fire/app/fire,py\" ")
				file.close()	

		print("[+]- fire app installed in %s/.fire"%home)
		print("[+]- You can after restart, type fire <argument> to running app !")
		print("[+]- Initializing Finished ! :)")

#this function is modules freezer
def Freezer():
	print("[+]- Freezing a modules ...")
	os.system("echo Freezing >> %s/logs;date >> %s/logs;cp %s/Modules %s/Modules.backup >> %s/logs;python%s -m pip freeze > %s/Modules;"%(path,path,path,path,path,args["python"],path))
	print("[+]- Freezing Finished ! :)")

#this function is modules intaller 
def Installer():
	print("[+]- Strated installation ...")
	if "-c" in sys.argv[:]:
		scope=sys.argv[:].index("-c")
		scope=sys.argv[scope+1]
		count=0
		with open("%s/.fire/out/Modules"%(home),"r") as file:
			for line in file.readlines(int(scope)):
					try:
						os.system("echo Installing >> %s/logs;date >> %s/loga;python%s -m pip install %s >> %s/logs"%(path,path,args["python"],line,path))
						count+=1
					except:
						print("[!]- Error : Please Checking internet connection and help")
						file.close()
						Help()
		file.close()			

	else:
		with open("%s/.fire/out/Modules"%(home),"r") as file:
			for line in file.readlines():
				try:
					os.system("echo Intsalling >> %s/logs;date >> %s/logs;python%s -m pip install %s >> %s/logs"%(path,path,args["python"],line,path))
					count+=1
				except:
					print("[!]- Error : Please Checking help")
					file.close()
					Help()
					break
		file.close()
#fine, this is main function for manage and run functions
def upgrade(pipv=3):
	print("[+]- Strated upgrading ...")
	with open("%s/.fire/out/Modules"%(home),"r") as modules:
		for line in modules:
			co = "pip"+str(pipv)+" install  --upgrade "+line
			print(co)
			os.system(co)
	print("[+]- Finished upgrading ...")
def modules():
	num = 0
	with open("%s/.fire/out/Modules"%(home),"r") as modules:
		for line in modules:
			num += 1
	print("[+]- number of your modules is --> %i"%num)
	modules.close()
def version():
	print("[+]- Fire version 1.0 ")
#fine, this is main function for manage and run functions
def RUN():
	if "-n" in sys.argv[:]:# this is run the initialize function
		Initialize()
	elif "-f" in sys.argv[:]:# this is calling the freezer function
		Freezer()
	elif "-i" in sys.argv[:]:# and this is run the installer function
		Installer()
	elif "-a" in sys.argv[:]: # this is auto first run freeze function and second run installer function
		Freezer()
		Installer()
	elif "-m" in sys.argv[:]:
		modules()
	elif "-u" in sys.argv[:]:
		if pipv:=args["python"]:
			upgrade(pipv)
		else:
			upgrade()
	elif "-v" in sys.argv[:]:
		version()
	else:
		print("[!]- Error : Please enter following argument to works",end="")
		Help()

#in following line, called run function for run program
RUN()
