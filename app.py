############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
from tkinter import *
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
from datetime import datetime as datetime
import time
import webbrowser

############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
   
    win = Tk()
    win.geometry("750x250")
    win.title("Contact Us")
    win.configure(background="white")
    #Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)

    a1 = tk.Label(win,text='    Roll Number               Names                                    Connect           ' ,bg='white',font=('times', 12, ' underline '))
    a1.place(x=50,y=10)
    a2 = tk.Label(win,text='   16900119027    Raunak Chatterjee          raunak.chatterjee@aot.edu.in        ',bg='white',font=('times', 12, ' bold '))
    a2.place(x=50,y=30)
    a3 = tk.Label(win,text='   16900119037         Sk Asif Ali                    sk.asifali@aot.edu.in     ',bg='white',font=('times', 12, ' bold '))
    a3.place(x=50,y=50)
    a4 = tk.Label(win,text='   16900119042    Sushavan Karmakar       sushavan.karmakar@aot.edu.in         ',bg='white',font=('times', 12, ' bold '))
    a4.place(x=50,y=70)
    a5 = tk.Label(win,text='   16900119044       Debraj Ghosh                 debraj.ghosh@aot.edu.in     '  ,bg='white',font=('times', 12, ' bold '))
    a5.place(x=50,y=90)
    a6 = tk.Label(win,text='   16900119072    Shuvranshu Halder         shuvranshu.halder@aot.edu.in   ',bg='white',font=('times', 12, ' bold '))
    a6.place(x=50,y=110)

    #Create a Label to display the link
    link = Label(win, text="Click Here for Source Code",font=('Helveticabold', 15), fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e:callback("https://github.com/Sushavan20/Face-recognition-based-attendance-system-project"))
    link.place(x=210,y=180)

    win.mainloop()


###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

###################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>>  2)Save Profile"
    message1.configure(text=res)

#######################################################################################




############################################# Password Game ################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password has been registered successfully!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return 
    mess._show(title='Password Changed', message='Password has been changed successfully!!')
    master.destroy()

###################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("500x206")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=210,y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=210, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=210, y=80)
    cancel=tk.Button(master,text="Cancel", command=master.destroy ,fg="#ffef8a", bg="#e0143d",height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=120, y=160)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="#091114", bg="#00cf9f", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=120, y=120)
    master.mainloop()

#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password has been registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################



############################################# Creating Dataset ################################################

def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    assure_path_exists("StudentRecord/")
    assure_path_exists("TrainingImage/")
    serial = 0

    exists = os.path.isfile("StudentRecord\StudentRecord.csv")
    if exists:
        with open("StudentRecord\StudentRecord.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentRecord\StudentRecord.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()

    Id = (txt.get())
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video width
        cam.set(4, 480) # set video height
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Initialize individual sampling face count
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                cv2.imshow('Taking Images', img)
                print("Sample-",sampleNum)
                
            if cv2.waitKey(100) & 0xFF == 27: # wait for 100 miliseconds or Press 'ESC' for exiting video
                print("All ",sampleNum, " Samples have been captured.")
                break
            elif sampleNum > 100: # Take 100 face sample and stop video
                print("All ",sampleNum, " Samples have been captured.")
                break
        
        print("\n [INFO] Storing Data, Exiting Function TakeImages() and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for Roll No : " + Id
        row = [serial, '', Id, '', name]
        with open('StudentRecord\StudentRecord.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            message.configure(text=res)



############################################# Training Dataset ################################################


def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return

    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text='Total Registrations till now  : ' + str(ID[0]))
    print("\n [INFO] all the faces have been trained.... Ending TrainImages() Program and cleanup stuff")

# function to get the images and label data
def getImagesAndLabels(path):
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

    

############################################# Live Recognition ################################################

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentRecord/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return 

    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    font = cv2.FONT_HERSHEY_SIMPLEX

    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentRecord\StudentRecord.csv")
    if exists1:
        df = pd.read_csv("StudentRecord\StudentRecord.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing!! please check and retry!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()

    while True:
        ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        my_list = []
        name_list = []
        date_list = []
        time_list = []
        space_list = []
    
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            serial, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if (confidence < 100):
                date = datetime.now().strftime('%d-%m-%Y')
                timeStamp = datetime.now().strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
            else:
                Id = 'Unknown'
                bb = str(Id)
           
            #print(ID)
            if ID not in my_list:
                my_list.append(str(ID))
                name_list.append(str(bb))
                date_list.append(str(date))
                time_list.append(str(timeStamp))
                space_list.append("")
            else:
                pass

            cv2.putText(img, str(ID), (x+2,y-25), font, 1, (255,255,255), 2)
            cv2.putText(img, str(bb), (x+40,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        cv2.imshow('Taking Attendance', img)
        if (cv2.waitKey(1) == 27):
            break

    date = datetime.now().strftime('%d-%m-%Y')
    nested_list = zip(my_list, space_list, name_list, space_list, date_list, space_list, time_list)
    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if exists:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as filepro:
            writer = csv.writer(filepro)
            for row in nested_list:
                writer.writerow(row)
        filepro.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as filepro:
            writer = csv.writer(filepro)
            writer.writerow(col_names)
            for row in nested_list:
                writer.writerow(row)
        filepro.close()

    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()

    print("\n [INFO] Recognition & Marking Attendance are done.... Exiting TrackImages() Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()

######################################################################################



######################################## USED STUFFS ############################################
    
global key
key = ''
ts = time.time()
date = datetime.now().strftime('%d-%m-%Y')
day,month,year=date.split("-")
mont={'01':'January', '02':'February', '03':'March',
      '04':'April', '05':'May', '06':'June',
      '07':'July', '08':'August', '09':'September',
      '10':'October', '11':'November', '12':'December'
      }

######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1500x750")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#01140b') #262523

frame1 = tk.Frame(window, bg="#01140b")#00aeff
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#01140b")#00aeff
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Face Recognition Based Attendance System" , fg="#35e69c", bg="#01140b" , width=55 , height=1, font=('Terminal',23,'bold'))
message3.place(x=16, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"   |  ", fg="orange", bg="#01140b", width=55 , height=1, font=('times',22,'bold'))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3, fg="orange", bg="#01140b" , width=55 , height=1, font=('times',22,'bold'))
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="         For New Registrations            ", fg="#0b0233", bg="#54d7ff", font=('Courier New',17,'bold'))
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="         For Already Registered           ", fg="#0b0233", bg="#54d7ff", font=('Courier New',17,'bold'))
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Enter Roll Number", width=20 , height=1 , fg="#c7fce9", bg="#01140b", font=('Comic Sans MS',17,'bold'))
lbl.place(x=130, y=50)

txt = tk.Entry(frame2, width=24, fg="black",font=('Euphemia',15,'normal'))
txt.place(x=100, y=90)

lbl2 = tk.Label(frame2, text="Enter Name", width=20, fg="#c7fce9", bg="#01140b", font=('Comic Sans MS',17,'bold'))
lbl2.place(x=130, y=140)

txt2 = tk.Entry(frame2, width=24, fg="black", font=('Euphemia',15,'normal'))
txt2.place(x=100, y=177)

message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile" , bg="#01140b", fg="#c7fce9", width=36, height=1, activebackground = "yellow" , font=('Courier New',15,'bold'))
message1.place(x=67, y=250)

message = tk.Label(frame2, text="", bg="#01140b", fg="#c7fce9", width=39, height=1, activebackground = "yellow", font=('Terminal',13,'bold'))
message.place(x=100, y=460)#00aeff

lbl3 = tk.Label(frame1, text="Attendance Sheet", width=21 , fg="#c7fce9", bg="#01140b", height=1, font=('times', 17, ' bold '))
lbl3.place(x=110, y=105)

res=0
exists = os.path.isfile("StudentRecord\StudentRecord.csv")
if exists:
    with open("StudentRecord\StudentRecord.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='Roll No.')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')

exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
if exists:
    i=0
    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()

###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=clear, fg="#ffef8a", bg="#e0143d", width=11, activebackground = "white", font=('Prestige Elite Std',12,'bold'))
clearButton.place(x=400, y=88)
clearButton2 = tk.Button(frame2, text="Clear", command=clear2, fg="#ffef8a", bg="#e0143d", width=11, activebackground = "white", font=('Prestige Elite Std',12,'bold'))
clearButton2.place(x=400, y=175)    
takeImg = tk.Button(frame2, text="Take Images", command=TakeImages, fg="#091114", bg="#00cf9f", width=25, height=1, activebackground = "white", font=('times',15,'bold'))
takeImg.place(x=150, y=300)
trainImg = tk.Button(frame2, text="Save Profile", command=psw, fg="#091114", bg="#00cf9f", width=25, height=1, activebackground = "white", font=('times',15,'bold'))
trainImg.place(x=150, y=370)
trackImg = tk.Button(frame1, text="Mark Attendance", command=TrackImages, fg="#091114", bg="#00cf9f", width=25, height=1, activebackground = "white", font=('times',15,'bold'))
trackImg.place(x=100,y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy, fg="#ffef8a", bg="#e0143d", width=15, height=1, activebackground = "white", font=('Prestige Elite Std',12,'bold'))
quitWindow.place(x=160, y=467)

##################### END ######################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################



