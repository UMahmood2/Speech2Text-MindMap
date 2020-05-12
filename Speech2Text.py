
from tkinter import *
from PIL import Image,ImageTk
import pyautogui # To save mind map image
import textwrap 
import os
from datetime import datetime
import speech_recognition as sr

# Get audio from user microphone
# instance of the recognizer class
r = sr.Recognizer()

scr_width = 1200
scr_height = 900

path = 'C:/Users/UsamaMahmood/Documents/Computer Science/CS3/IN3007 Final Year Project/MindMap/SpeechRec'

# Initialising the speech bubbles and the title bubble is also initialised.
bubbles = ['Bubble 1: ','Bubble 2: ','Bubble 3: ','Bubble 4: ','Title: ']

# some colours to chose from later in the code, some are used, some are not. 
back_1 = 'gray'
back_2 = 'green'
back_3 = 'cyan'
back_4 = '#DEB887' # Burwood (brownish)
back_5 = '#B0C4DE' # Light Steel Blue 
back_7 = '#7B68EE' # Medium Slate Blue 
back_8 = '#800000' # Maroon 
back_9 = '#263D42' # Greyish 
far_1 = 'white'

# Initialising the distances of speech bubbles inside the tkinter window 
dis_x1 = int(0.06*(scr_width))
dis_x2 = int(0.58*(scr_width))
dis_x3 = int(0.40*(scr_width))

dis_y1 = 75
dis_y2 = 93
dis_y3 = int(0.50*(scr_height))
dis_y4 = int(0.65*(scr_height))
gap = 42

root = Tk()
root.geometry('%dx%d%+d%+d' % (scr_width,scr_height,0,0))
root.title('Final Year Project')
root.config(bg=back_9)
icon_rec = PhotoImage(file='C:/Users/UsamaMahmood/Documents/Computer Science/CS3/IN3007 Final Year Project/MindMap/SpeechRec/icons/record.png')

open_file_but = Button(root, bg = back_1,width=8,height=1, command=lambda: open_dir(path),text = 'Open Map',font=('helvetica 12 bold'))
open_file_but.place(x=10,y=10)

save_map_but = Button(root, bg = back_1,width=8,height=1, command=lambda: save_map(),text = 'Save Map',font=('helvetica 12 bold'))
save_map_but.place(x=120,y=10)

win_title_lab = Label(root,bg=back_9,fg=far_1, width=68,height=2,bd=0,text = 'Voice Recognition Mind Map',font=('helvetica 15'))
win_title_lab.place(x=220,y=10)

map_img_lab = Label(root,bg=back_9,fg=far_1, width=154,height=41,bd=0)
map_img_lab.place(x=12,y=dis_y1)


text1_lab = Label(root,bg=back_4,fg=far_1, width=44,height=12,bd=0,text = 'Bubble 1: ',font=('helvetica 12'))
text1_lab.place(x=dis_x1,y=dis_y2)
text1_but = Button(root,bg=back_3, image=icon_rec, command= lambda: record_aud(text1_lab,bubbles[0],0,5), width=40,height=40,bd=0)
text1_but.place(x=dis_x1-gap,y=dis_y2)

text2_lab = Label(root,bg=back_4,fg=far_1, width=44,height=12,bd=0,text = 'Bubble 2: ',font=('helvetica 12'))
text2_lab.place(x=dis_x2,y=dis_y2)
text2_but = Button(root,bg=back_3, image=icon_rec, command= lambda: record_aud(text2_lab,bubbles[1],1,5), width=40,height=40,bd=0)
text2_but.place(x=dis_x2-gap,y=dis_y2)

text3_lab = Label(root,bg=back_4,fg=far_1, width=44,height=12,bd=0,text = 'Bubble 3: ',font=('helvetica 12'))
text3_lab.place(x=dis_x1,y=dis_y4)
text3_but = Button(root,bg=back_3, image=icon_rec, command= lambda: record_aud(text3_lab,bubbles[2],2,5), width=40,height=40,bd=0)
text3_but.place(x=dis_x1-gap,y=dis_y4)

text4_lab = Label(root,bg=back_4,fg=far_1, width=44,height=12,bd=0,text = 'Bubble 4: ',font=('helvetica 12'))
text4_lab.place(x=dis_x2,y=dis_y4)
text4_but = Button(root,bg=back_3, image=icon_rec, command= lambda: record_aud(text4_lab,bubbles[3],3,5), width=40,height=40,bd=0)
text4_but.place(x=dis_x2-gap,y=dis_y4)

map_title_lab = Label(root,bg=back_8,fg=far_1, width=18,height=3,bd=0,text = 'Title: ',font=('helvetica 15 bold'))
map_title_lab.place(x=dis_x3,y=dis_y3)
title_but = Button(root,bg=back_3, image=icon_rec, command= lambda: record_aud(map_title_lab,bubbles[4],4,2), width=40,height=40,bd=0)
title_but.place(x=dis_x3-gap,y=dis_y3)

roi = (0,0,1200,920) # roi = region of interest 
# To save the screenshot of the mind map, a screenshot of the 'region of interest' is taken.
def save_map():
    img = pyautogui.screenshot(region=roi)
    today = str(datetime.now())
    name = 'C:/Users/UsamaMahmood/Documents/Computer Science/CS3/IN3007 Final Year Project/MindMap/SpeechRec/Maps/Map '+str(bubbles[-1][8:])+' '+str(today[8:11])+str(today[5:8])+str(today[0:4])+'_'+str(today[11:13])+str(today[14:16])+str(today[17:19])+'.png'
    print(name)
    img.save(name)
    pass

def open_dir(path):
    path = os.path.realpath(path)
    os.startfile(path)

# Code for handling special characters
def to_print(voiceInput):
    if voiceInput == "full stop":
        print(".")

    elif voiceInput == "question mark":
        print("?")

    elif voiceInput == "exclamation mark":
        print("!")

    elif voiceInput == "comma":
        print(",")

    elif voiceInput == "hashtag":
        print("#")

    elif voiceInput == "hyphen":
        print("-")

    elif voiceInput == "forward slash":
        print("/")

    elif voiceInput == "asterisk":
        print("*")

    elif voiceInput == "colon":
        print(":")
    pass

# Handling voice recognition and outputting text in the appropriate bubble. 
# The 'for' loop handles the amount of latters before a new line in the bubble is created. 
source = sr.Microphone()
def record_aud(lab, bubble,no,dur):
    with source as voice:
        audio = r.listen(voice,dur)
    bub = r.recognize_google(audio)
    to_print(audio)
    n = 0
    new_bub = '\n'
    for j in bub:
        n +=1
        new_bub = new_bub + j 
        if n == 52: 
             new_bub = new_bub + '\n'
             n = 0 
    final_bub = bubble+new_bub
    bubbles[no] = final_bub
    lab.config(text=final_bub)
    pass
    


root.mainloop()

