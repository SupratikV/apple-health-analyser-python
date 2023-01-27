import code
import customtkinter 
import workouttt
from tkinter import filedialog

root=customtkinter.CTk()
# label=tkinter.Label(root,text='hello world')
# label.pack()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root.geometry=('1280x720')
def steps():
    code.createstepsfile('2021-10-03')
def raise_frame(frame):
    frame.tkraise()
def datesheart():
    l=code.datelist()
    return(l)

s=workouttt.workout_data
# workouttt.plot_workouts(s)
#code for frame 1
frame1=customtkinter.CTkFrame(master=root)
frame1.pack(pady=20,padx=60,fill='both',expand=True)
label1=customtkinter.CTkLabel(master=frame1,text='Apple health analyser')
label1.pack(pady=12,padx=10)
# entry11=customtkinter.CTkEntry(master=frame1,placeholder_text='username')
# entry11.pack(pady=12,padx=10)
# entry12=customtkinter.CTkEntry(master=frame1,placeholder_text='password',show='*')
# entry12.pack(pady=12,padx=10)
def openFile():
    filepath = filedialog.askopenfilename()
    code.pathhh=filepath
    label222=customtkinter.CTkLabel(master=frame1,text=code.pathhh)
    label222.pack(pady=12,padx=10)
button111=customtkinter.CTkButton(master=frame1,text='choose file:',command=lambda:openFile())
button111.pack(pady=12,padx=10)
button1=customtkinter.CTkButton(master=frame1,text='Heart',command=lambda:raise_frame(frame2))
button1.pack(pady=12,padx=10)
button2=customtkinter.CTkButton(master=frame1,text='Steps',command=lambda:raise_frame(frame3))
button2.pack(pady=12,padx=10)
button311=customtkinter.CTkButton(master=frame1,text='Workout pie chart',command=lambda:workouttt.plot_workouts(s))
button311.pack(pady=12,padx=10)
checkbox=customtkinter.CTkCheckBox(master=frame1,text='remember me')
checkbox.pack(pady=12,padx=10)
# button311=customtkinter.CTkButton(master=frame1,text='Workout pie chart',command=workouttt.plot_workouts(workouttt.workout_data))
# button311.pack(pady=12,padx=10)


#code for frame 2
frame2=customtkinter.CTkFrame(master=root)
# frame2.pack(pady=20,padx=60,fill='both',expand=True)
label2=customtkinter.CTkLabel(master=frame2,text='Heart analysis')
label2.pack(pady=12,padx=10)

d=code.dates()
combobox_varr = customtkinter.StringVar(value=d[0])  # set initial value

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

comboboxx = customtkinter.CTkComboBox(master=frame2,
                                     values=d,
                                     command=combobox_callback,
                                     variable=combobox_varr)
comboboxx.pack(padx=20, pady=10)
print(comboboxx.get())

button21=customtkinter.CTkButton(master=frame2,text='show graph',command=(lambda:code.createheartfile(combobox.get())))
button21.pack(pady=12,padx=10)
button22=customtkinter.CTkButton(master=frame2,text='home',command=lambda:raise_frame(frame1))
button22.pack(pady=12,padx=10)
checkbox2=customtkinter.CTkCheckBox(master=frame2,text='its working')
checkbox2.pack(pady=12,padx=10)


#code for frame3
frame3=customtkinter.CTkFrame(master=root)
# frame3.pack(pady=20,padx=60,fill='both',expand=True)
label3=customtkinter.CTkLabel(master=frame3,text='Steps analysis')
label3.pack(pady=12,padx=10)
d=code.datestep()
combobox_var = customtkinter.StringVar(value=d[0])  # set initial value

def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(master=frame3,
                                     values=d,
                                     command=combobox_callback,
                                     variable=combobox_var)
combobox.pack(padx=20, pady=10)
print(combobox.get())
button31=customtkinter.CTkButton(master=frame3,text='show graph',command=(lambda:code.createstepsfile(combobox.get())))
button31.pack(pady=12,padx=10)
button3=customtkinter.CTkButton(master=frame3,text='home',command=lambda:raise_frame(frame1))
button3.pack(pady=12,padx=10)#2021-10-03
checkbox3=customtkinter.CTkCheckBox(master=frame3,text='its working')
checkbox3.pack(pady=12,padx=10)


for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='news')
raise_frame(frame1)
root.mainloop()