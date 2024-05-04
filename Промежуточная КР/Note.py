from sys import stdin
import os
import time
import datetime

class View:

    def comand(self):
        print("Введите команду: ")
        cmnd = stdin.readline()
        return cmnd

    def title(self):
        print("Введите имя заметки: ")
        title = stdin.readline()
        return title
    
    def msg(self):
        print("Введите тело заметка: ")
        msg = stdin.readline()
        return msg

    

class Nodes:
    def __init__(self,f,file,dictionary):
        self.dictionary = dictionary
        self.file = file
        self.f = f

    def add(self, title,msg):
        node = Node(title,msg)
        self.f.write(node.str_node())
        t = os.path.getmtime(file)
        self.f.write(" ; " +  str(t))
        dictionary[title] = node.str_node()

    def deletion(self,title):
        del dictionary[title]
         
        with open(self.file, "w", encoding='UTF-8') as f: 
      
            for number,value in enumerate(dictionary.values()) : 
           
                f.write(value) 

    def editing(self,title,msg):
        node = Node(title,msg)
        dictionary[title] = node.str_node() + str(datetime.datetime.now())
        with open(self.file, "w", encoding='UTF-8') as f: 
      
            for value in dictionary.values() : 
           
                f.write(value)

    def read(self, title):
        print(dictionary[title])

        
class Controll:
    view = View()
    

    def __init__(self,f, file,dictionary):
        self.f = f
        self.file = file
        self.nodes = Nodes(f,file,dictionary)

    def start(self):
        
        while(True):
            cmnd = (self.view.comand()).strip()
            if cmnd == '0':
                break
            print(cmnd)
            match cmnd:
                case "add":
                    self.nodes.add(self.view.title().strip(),self.view.msg().strip())
                case "del":
                    self.nodes.deletion(self.view.title().strip())
                case "editing":
                    self.nodes.editing(self.view.title().strip(), self.view.msg().strip())
                case "read":
                    self.nodes.read(self.view.title().strip())


class Node:
    ind = 0
    def __init__(self,title, msg):
        Node.log()
        self.id = self.ind
        self.title = title
        self.msg = msg

    @staticmethod
    def log():
        Node.ind+=1
        
    def set_ind(ind):
        Node.ind = ind

    def str_node(self):
        return str(self.id) + " ; " + self.title + " ; " + self.msg




file = "None.csv"
f = open(file,'r+',encoding='UTF-8')
dictionary = {}
if os.stat(file).st_size != 0:
    for line in f:
        arr = line.split(" ; ")
        dictionary[arr[1]] = line
    Node.set_ind(int(arr[0]))

controll = Controll(f,file,dictionary)
controll.start()

f.close()