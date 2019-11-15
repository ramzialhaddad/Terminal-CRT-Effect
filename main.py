from time import sleep
from os import system
import platform
import sys

hertz = 60

if platform.system() == "Windows":
    clear_word = "cls"
else:
    clear_word = "clear"

blank = [
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0]
		]

box = 	[
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1]
		]

E = 	[
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,0,0,0,0,0,0,0,0],
		[1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1]
		]

message =	[
			[1,1,0,0,1,0,0,0,0,0],
			[1,0,0,1,0,1,0,0,0,0],
			[1,1,0,1,1,1,0,0,0,0],
			[1,0,0,1,0,1,0,0,0,0],
			[1,1,0,1,0,1,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0]
			]


def refreshScreen(display):
	system(clear_word)
	for line in display:
		for pixel in line:
			sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")




def boxGettingLarger():
	system(clear_word)
	for lines in range(30):
#----------------------------------------------------------- start
		for pixel in [1,1,1,1,1,1,1,1,1,1]:
			sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")
#-------------------------------------------------------------
		for line in range(lines):
			for pixel in [1,0,0,0,0,0,0,0,0,1]:
				sleep(1/hertz)
				if pixel == 1:
					print("\u2588\u2588\u2588\u2588", end="")
					sys.stdout.flush()
				else:
					print("    ", end="")
					sys.stdout.flush()
			print("\n",end="")
#------------------------------------------------------------ end
		for pixel in [1,1,1,1,1,1,1,1,1,1]:
			sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")
		system(clear_word)

def tallerTower():
	system(clear_word)
	for lines in range(30):
#----------------------------------------------------------- start
		for pixel in [1,1,1,1,1,1,1,1,1,1]:
			sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")
#-------------------------------------------------------------
		for line in range(lines):
			for pixel in [1,0,0,0,0,0,0,0,0,1]:
				sleep(1/hertz)
				if pixel == 1:
					print("\u2588\u2588\u2588\u2588", end="")
					sys.stdout.flush()
				else:
					print("    ", end="")
					sys.stdout.flush()
			print("\n",end="")
#------------------------------------------------------------ end
		for pixel in [1,1,1,1,1,1,1,1,1,1]:
			sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")

def smallBoxGettingLarger():
	system(clear_word)
	for lines in range(30):
#----------------------------------------------------------- start
		for pixel in [1,1,1,1,1]:
			#sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")
#-------------------------------------------------------------
		for line in range(lines):
			for pixel in [1,0,0,0,1]:
				#sleep(1/hertz)
				if pixel == 1:
					print("\u2588\u2588\u2588\u2588", end="")
					sys.stdout.flush()
				else:
					print("    ", end="")
					sys.stdout.flush()
			print("\n",end="")
#------------------------------------------------------------ end
		for pixel in [1,1,1,1,1]:
			#sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")
		system(clear_word)

def movingLargerSmallBox():
	system(clear_word)
	for lines in range(30):
#----------------------------------------------------------- start
		for space in range(lines):
			print("    ", end="")
			sys.stdout.flush()
		for pixel in [1,1,1,1,1]:
			#sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")
#-------------------------------------------------------------
		for line in range(lines):
			for space in range(lines):
				print("    ", end="")
				sys.stdout.flush()
			for pixel in [1,0,0,0,1]:
				#sleep(1/hertz)
				if pixel == 1:
					print("\u2588\u2588\u2588\u2588", end="")
					sys.stdout.flush()
				else:
					print("    ", end="")
					sys.stdout.flush()
			print("\n",end="")
#------------------------------------------------------------ end
		for space in range(lines):
				print("    ", end="")
				sys.stdout.flush()
		for pixel in [1,1,1,1,1]:
			#sleep(1/hertz)
			if pixel == 1:
				print("\u2588\u2588\u2588\u2588", end="")
				sys.stdout.flush()
			else:
				print("    ", end="")
				sys.stdout.flush()
		print("\n",end="")
		system(clear_word)

#refreshScreen(blank)
#refreshScreen(box)
#refreshScreen(E)
#refreshScreen(message)
#special()
#tallerTower()
#smallBoxGettingLarger()
movingLargerSmallBox()