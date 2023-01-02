import pynput
from pynput.keyboard import Key, Listener
import os
from pynput import keyboard
#import winaudio
import winsound
 

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    
    def push(self,value):
        new_node=node(value)
        new_node.next=self.head
        self.head=new_node


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
path="C:\\Users\\USER\\Downloads\\"
#get name of all file in list.
files=os.listdir(path)
#get all songs file name that endswith .wav
song_list=[ songs for songs in files if songs.endswith('.wav')]
for i in range(len(song_list)):
    print("["+str(i)+"]"+song_list[i])
llist=Linked_list()
#path="c:\\Users\\USER\\Downloads\\128-Roohedaariyaan - B Praak 128 Kbps.mp3"
from pynput import keyboard
count_pointer_postion=0
count_back_front=0
def on_press(key):
    global count_pointer_postion
    global count_back_front
    print('{0} release'.format(key))
    # it is for horizontal movement in played song list 
    if key== keyboard.Key.left:
        if count_back_front<llist.length():
            count_back_front+=1
            print("Pointer of left on postion{0}".format(count_back_front))

    if key== keyboard.Key.right:
        if count_back_front>0:
            count_back_front-=1
            print("Pointer of right on postion{0}".format(count_back_front))
    
    if key==keyboard.KeyCode(char='p'):
        song=llist.get_postion(count_back_front)
        #print(count_back_front)
        print(path+song)
        winsound.PlaySound(path+song,  winsound.SND_ASYNC)      
        #print(llist.get_postion(count_back_front))
    
    if key==keyboard.KeyCode(char='s'):
        winsound.PlaySound(None, winsound.SND_ASYNC)
      # song_player.terminate()
       
        
    if key in [keyboard.KeyCode(char = str(i)) for i in range(0,12)]:
        print(int(key.char))

    #it is for vertical movement in list of song
    if key==keyboard.Key.up:
        if count_pointer_postion<len(song_list):
            count_pointer_postion=count_pointer_postion+1
            print("Pointer of up on postion{0}".format(count_pointer_postion))

    if key==keyboard.Key.down:
        if count_pointer_postion>0:
            count_pointer_postion=count_pointer_postion-1
            print("Pointer of down on postion{0}".format(count_pointer_postion))

    if key==keyboard.Key.enter:
        song=song_list[count_pointer_postion]
        winsound.PlaySound(path+song,  winsound.SND_ASYNC)
        llist.push(song)
        #song_player = vlc.MediaPlayer(path+song)
       # song_player.play()

    if key== keyboard.Key.esc:
        return False
def listen():
    with keyboard.Listener(on_press=on_press,) as listener:
        listener.join()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
print(song_list)
listen()
#press esc

#data=input("enter the song you wana play")
#print(data)



#C:\Users\USER\Downloads