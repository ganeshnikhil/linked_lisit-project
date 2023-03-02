import pynput
#from pynput.keyboard import Key, Listener
import os
from pynput import keyboard
import time
from tqdm import tqdm
from mutagen.mp3 import MP3
import colorama
from colorama import Fore, Back, Style
import pyautogui

from pygame import mixer
import pyautogui 
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
songs=[ songs for songs in files if songs.endswith('.mp3') or songs.endswith('.wav')]

#created a file to check which song gets more hit 
filename='music_counter.txt'
#open that file in read mode      
file_hit=open(filename,'r')
 #create a empty list 
all_played_count=[]
#get all data of file in list..
songs_hit=file_hit.readlines()
 #run the loop equal to the length of songs we have ..
for i in range(len(songs)):
    #now append the hits on song and song name in 'all_played_count list'
    all_played_count.append([songs[i],int(songs_hit[i]),i])
file_hit.close()
#now sort the all_played_count 2-d list on behalf of hits it gets...
new_played_count=sorted(all_played_count,key=lambda x:x[1], reverse=True)
#print(new_played_count)  
#intialize the song_list to empty  
song_list=[] 
for i in range(len(new_played_count)):
    #print the song 
  print(Fore.GREEN+"["+str(i)+"]"+new_played_count[i][0]+Fore.GREEN)
  #append the song name and song.index to the list for future uses ..
  song_list.append([new_played_count[i][0],new_played_count[i][2]])



#genrate  the song runtime..
def convert(seconds):
    seconds=seconds%(24*3600)
    hour=seconds//3600
    seconds%=3600
    minutes=seconds//60
    seconds%=60
    return f"{round(hour)}:{round(minutes)}:{round(seconds)}"

def processing_bar(lenght):
   for i in tqdm(range(0, int(lenght)),colour="green",desc="Status"):
      time.sleep(1)
      


#call a linked list that we created intially
llist=Linked_list()

from pynput import keyboard
#intialize a variable. using this variable we can go up and down in song list
count_pointer_postion=0
#intialize a variable . using this variable we can move in already played songs 
count_back_front=0
flag=True
file_hit=open('music_counter.txt','r')
songs_hit=file_hit.readlines()
file_hit.close()
#print(songs_hit)
def on_press(key):
    mixer.init()
    global count_pointer_postion
    global count_back_front
    global flag
    global songs_hit
    print('{0} release'.format(key))
    # it is for horizontal movement in played song list 
    if key== keyboard.Key.left:
        if count_back_front>0:
            count_back_front-=1
            print("[-]Pointer of left on postion:{0}".format(count_back_front))

    if key==keyboard.Key.right:
        if count_back_front<llist.length():
            count_back_front+=1
            print("[-]Pointer of right on postion:{0}".format(count_back_front))
    
   
    #it is for vertical movement in list of song
    if key==keyboard.Key.up:
        if count_pointer_postion>0:
            count_pointer_postion-=1
            count_back_front=0
            print("[-]Pointer of up on postion:{0}".format(count_pointer_postion))

    if key==keyboard.Key.down:
        if count_pointer_postion<(len(song_list)-1):
            count_pointer_postion+=1
            count_back_front=0
            print("[+]Pointer of down on postion:{0}".format(count_pointer_postion))
        else:
            
            count_pointer_postion=0#len(song_list)-1
            print("[+]Pointer of down on postion:{0}".format(count_pointer_postion))
    
    if key==keyboard.KeyCode(char='q'):
        print("[*]Your song is paused..")
        mixer.music.pause()
    
    if key==keyboard.KeyCode(char='r'):
        print('[*]Your song is unpaused..')
        mixer.music.unpause()
   
    if key==keyboard.Key.enter:
        if count_back_front==0:
            #check the counter value and choose the song 
            song=song_list[count_pointer_postion][0]



            

                #run the loop to the lenght of song_hit list
            for i in range(len(song_list)):
                    #if played song at 'counter_pointer_postion' is same as iterater 'i' postion
                    #it means we have increment that songs hit in 'music_counter.txt' file
                   
                if song_list[i][0].strip()==song_list[count_pointer_postion][0].strip():            
                    #intially orignal index of song is added to the list previously. now we can use it as index
                    index=song_list[i][1]
                    #increment hit at that index
                    songs_hit[index]=str(int(songs_hit[index])+1)+'\n'
                    #print(songs_hit)

                
            #push the played song to linked list 
            llist.push(song)
            #get the path of song and get the lenght of song.
            audio=MP3(path+song)
            song_len=audio.info.length
            
            duration=convert(song_len)
            
            #then covnvert lenght into time format using convert() function and print it to screen
            print("[^v]Now playing:{0}.[{1}]".format(song,duration))
           
            #then play the song repatedly until new song is not chossen by user..
            mixer.music.load(path+song)
            mixer.music.play(-1)

         
            processing_bar(int(song_len))
           
            pyautogui.press('down')
            time.sleep(0.5)
            pyautogui.press('enter')

        else:
            #this is for playing song alreday played stored in linked list as history ..
            song=llist.get_postion(count_back_front)

            try:
                    print("[<>]Now playing:{0}".format(song))
                    mixer.music.load(path+song)
                    mixer.music.play() 
            except Exception as e:
                    print("Soory sir there is not any song recently played")
            
                
            
        
    if key== keyboard.Key.esc:
        time.sleep(1)
        return False
#def on_release(key):

def listen():
    
   with keyboard.Listener(on_press=on_press,) as listener:
      listener.join()
   listener = keyboard.Listener(on_press=on_press)
   listener.start()


listen()

#print(songs_hit)
with open('music_counter.txt','w') as f:
    for i in range(len(songs_hit)):
        f.write(songs_hit[i])
    

#press esc



