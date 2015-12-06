from tkinter import * 
import subprocess
import signal
import os

class GUI():
	def __init__(self, parent):
		self.parent = parent
		self.monitor = ""
		# parent.geometry("300x300")
		
		#start/stop monitor buttons
		self.start_monitor_btn = Button(parent, text="Start\nmonitor")
		self.start_monitor_btn.grid(row=0, column=0, padx=(10,0), pady=(10,0), ipadx=5, ipady=5)
		self.start_monitor_btn.bind("<Button-1>", self.start_monitor)

		self.stop_monitor_btn = Button(parent, text="Stop\nmonitor")
		self.stop_monitor_btn.grid(row=0, column=1, padx=10, pady=(10,0), ipadx=5, ipady=5)
		self.stop_monitor_btn.bind("<Button-1>", self.stop_monitor)


		#start/stop server buttons
		self.start_server_btn = Button(parent, text="Start\nserver ")
		self.start_server_btn.grid(row=1, column=0, padx=(10,0), pady=10, ipadx=5, ipady=5)
		self.start_server_btn.bind("<Button-1>", self.start_server)


		self.stop_server_btn = Button(parent, text="Stop\nserver ")
		self.stop_server_btn.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5)
		self.stop_server_btn.bind("<Button-1>", self.stop_server)

		#delete all images buttons
		self.delete_img_btn = Button(parent, text="Delete all images")
		self.delete_img_btn.grid(row=2, column=0, columnspan=2, pady=(0,10), ipadx=20, ipady=5)
		self.delete_img_btn.bind("<Button-1>", self.delete_images)


	def start_monitor(self, event):
		print(os.getcwd())
		os.chdir("../activity_monitor/")
		print(os.getcwd())
		cmd = ["sudo", "python3", "test.py"]
		self.monitor_pro = subprocess.Popen(cmd,  preexec_fn=os.setsid)
		
		

	def stop_monitor(self, event):
		os.chdir("/home/pi/python_lab/assignment/activity_monitor/")
		# self.monitor.kill()
		os.killpg(self.monitor_pro.pid, signal.SIGTERM)
		print("stopping")


	def start_server(self, event):
		print("server running on port 3000.")
		os.chdir("/home/pi/python_lab/assignment/flaskServer/")
		cmd = ["sudo", "python", "server.py"]
		self.server_pro = subprocess.Popen(cmd,  preexec_fn=os.setsid)


	def stop_server(self, event):
		print("stop_server")
		os.chdir("/home/pi/python_lab/assignment/flaskServer/")
		os.killpg(self.server_pro.pid, signal.SIGTERM)

	def delete_images(self, event):
		print("delete_images")



def main():
	root = Tk()
	root.title()
	root.resizable(width=FALSE, height=FALSE)
	app = GUI(root)
	root.mainloop()



if __name__ == '__main__':
	main()