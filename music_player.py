import pynput
#from pynput.keyboard import Key, Listener
import os
from pynput import keyboard
import time

from mutagen.mp3 import MP3
#/Users/kartiksingh/Downloads

from pygame import mixer
#create a linked list to store the song
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    #its like last get first and first get last like stack
    def push(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node

    #gives the position of the index
    def get_postion(self,index):
        first=self.head
        count=0
        while(first):
            count+=1
            if count==index:
                return first.data
            first=first.next


    def length(self):
        first=self.head
        count=0
        while(first):
            count=count+1
            first=first.next
        return count

    def printlist(self):
        first=self.head
        while(first):
            print(first.data)
            first=first.next

#path of song directory
path="/Users/kartiksingh/Downloads/"
#get name of all file in list.
files=os.listdir(path)
#get all songs file name that endswith .wav
song_list=[ songs for songs in files if songs.endswith('.mp3') or songs.endswith('.wav')]
for i in range(len(song_list)):
    print("["+str(i)+"]"+song_list[i])




def convert(seconds):
    seconds=seconds%(24*3600)
    hour=seconds//3600
    seconds%=3600
    minutes=seconds//60
    seconds%=60
    return f"{round(hour)}:{round(minutes)}:{round(seconds)}"


llist=Linked_list()

from pynput import keyboard
count_pointer_postion=0
count_back_front=0
flag=True

def on_press(key):
    mixer.init()
    global count_pointer_postion
    global count_back_front
    global flag
    print('{0} release'.format(key))
    # it is for horizontal movement in played song list 
    if key== keyboard.Key.left:
        if count_back_front>0:
            count_back_front-=1
            print("[-]Pointer of left on postion:{0}".format(count_back_front))

    if key== keyboard.Key.right:
        if count_back_front<llist.length():
            count_back_front+=1
            print("[-]Pointer of right on postion:{0}".format(count_back_front))
    
    if key==keyboard.KeyCode(char='p'):
        
        song=llist.get_postion(count_back_front)

        try:
            print("[<>]Now playing:{0}".format(song))
            mixer.music.load(path+song)
            mixer.music.play() 
        except Exception as e:
            print("Soory sir there is not any song recently played")
       



        #print(llist.get_postion(count_back_front))
    
    if key==keyboard.KeyCode(char='s'):
        flag=False
        mixer.music.stop()



      # song_player.terminate()
       
        
    if key in [keyboard.KeyCode(char = str(i)) for i in range(0,12)]:
        print(int(key.char))

    #it is for vertical movement in list of song
    if key==keyboard.Key.up:
        if count_pointer_postion>0:
            count_pointer_postion-=1
            #count_back_front=0
            print("[-]Pointer of up on postion:{0}".format(count_pointer_postion))
           

    if key==keyboard.Key.down:
        if count_pointer_postion<(len(song_list)-1):
            count_pointer_postion+=1
            #count_back_front=0
            print("[+]Pointer of down on postion:{0}".format(count_pointer_postion))
    
    if key==keyboard.KeyCode(char='q'):
        print("[*]Your song is paused..")
        mixer.music.pause()
    
    if key==keyboard.KeyCode(char='r'):
        print('[*]Your song is unpaused..')
        mixer.music.unpause()
   
    if key==keyboard.Key.enter:
        song=song_list[count_pointer_postion]
        llist.push(song)
        audio=MP3(path+song)
        song_len=audio.info.length
        duration=convert(song_len)
        print("[^v]Now playing:{0}.[{1}]".format(song,duration))
        mixer.music.load(path+song)
        mixer.music.play(-1)
        #llist.push(song)
        #llist.printlist()
       
    
    if key== keyboard.Key.esc:
        return False
#def on_release(key):

def listen():
    
    with keyboard.Listener(on_press=on_press,) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()


listen()


#press esc



