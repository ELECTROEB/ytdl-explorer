import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import webbrowser
import re
import argparse
import urllib.request

global ff

############################################# COMMENT OLD LINES 
 
def comment_all():
    comment_hosts=""
    with open('C:\Windows\System32\drivers\etc\hosts','r') as hosts:
        for line in hosts:
            if line[0] != "#":
                comment_hosts+="#" + line.strip()+"\n"
            else:
                comment_hosts+=line.strip()+"\n"
        comment_hosts+="-"*40+"\n"
    with open('C:\Windows\System32\drivers\etc\hosts','w') as hosts:
        hosts.write(comment_hosts)
 
############################################# IP PARSING
 
def regex(host, digest, option):
 
    hostsfile = open("C:\Windows\System32\drivers\etc\hosts", option)
 
    for hosts in host:
        for line in digest:
            
            match = re.search(re.compile(r'\b{}\b'.format(hosts)), line)
            if match:
                ip = re.search(re.compile(
                    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'), line)
                node = re.match(re.compile(r'\b{}\b'.format(hosts)), line)
                print("#", node.group())
                hostsfile.write("# {}\n".format(node.group()))
                print(ip.group(), host[hosts])
                hostsfile.write("{} {}\n".format(ip.group(), host[hosts]))
 
    hostsfile.close()
 
############################################# MAIN PROGRAM 
 
def main(text,command):
    host = {
        'Simulator / UI node': 'ips-opsui',
        'Simulator': 'ips-simulator',
        'Database node': 'ips-db',
        'Service node 1': 'ips-node1',
        'Service node 2': 'ips-node2',
        'Service node 3': 'ips-node3',
        'Service node 4': 'ips-node4',
    }
    
    # if args.url:
    #     file = urllib.request.urlopen(url).read().decode('utf-8')
    #     digest = file.split('\r\n')
    #     regex(host, digest)
    
    if command == "rewrite" :
        digest = text.split("\n")
        regex(host, digest, "w")
    elif command == "insert" :
        digest = text.split("\n")
        comment_all()
        regex(host, digest, "a+")
 
 
 
############################################# COMMAND PARSER
 
 
# parser = argparse.ArgumentParser()
# parser.add_argument("-u", "--url", help="Paste hosts URL")
# parser.add_argument("-f", "--file", help="Paste hosts file")
# args = parser.parse_args()
# url = args.url
 

 
############################################# GUI block
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x250')
 
# Text editor
text = tk.Text(root, height=12)
text.pack()
 
########## FUNCTIONS FOR BUTTONS
 
def re_write():
 
    command = "rewrite" 
    ff = text.get("1.0", "end - 1 chars")
 
    main(ff, command)
    messagebox.showinfo("Information","The file was re-writed. IPs were added")
 
def add_ip(): 
 
    command = "insert" 
    ff = text.get("1.0", "end - 1 chars")
 
    main(ff,command)
    messagebox.showinfo("Information","Old IPs were commented. New IPs were added")
 
def open_file(): 
    webbrowser.open("C:\Windows\System32\drivers\etc\hosts")
 
def close(): 
    root.destroy()
 
########## BUTTONS
 
reWrite = ttk.Button(
    root,
    text='Re-write the Hosts',
    command= re_write
)
 
addIP = ttk.Button(
    root,
    text='Comment old and Write new IPs',
    command= add_ip
)
 
open_hosts = ttk.Button(
    root,
    text='Open Hosts',
    command= open_file
)
 
close_program = ttk.Button(
    root,
    text='Close',
    command= close
)
 
########## BUTTONS FORMAT
 
reWrite.pack(ipadx=10,    ipady=10, side='left')
addIP.pack(ipadx=10,    ipady=10, side='left')
close_program.pack(ipadx=10,    ipady=10, side='right')
open_hosts.pack(ipadx=10,    ipady=10, side='right')
 
root.mainloop()
