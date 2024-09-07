import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
window=tk.Tk()
window.geometry('600x400')
window.minsize(600,400)
import database

class EntryWidget(ttk.Frame):
        def __init__(self,parent,label_text):
                super().__init__(master=parent)
                self.rowconfigure((0,1),weight=1)
                self.columnconfigure((0),weight=1,uniform='a')
                ttk.Label(self,text=label_text).grid(row=0,column=0,sticky='nesw',pady=10,padx=5)
                self.entry=ttk.Entry(self)
                self.entry.grid(row=1,column=0,sticky='ew',padx=10)
                #self.pack(expand=True,fill='both',padx=10,pady=10)

        def get_input(self):
                x=self.entry.get()
                self.entry.delete(0,tk.END)
                return x
        
        def clear(self):
                return self.entry.delete(0,tk.END)
        
class SpinWidget(ttk.Frame):
        def __init__(self,parent,label_text):
                super().__init__(master=parent)
                self.rowconfigure((0,1),weight=1)
                self.columnconfigure((0),weight=1,uniform='a')
                ttk.Label(self,text=label_text).grid(row=0,column=0,sticky='nesw',pady=5,padx=10)
                self.entry=ttk.Spinbox(self)
                self.entry.grid(row=1,column=0,sticky='ew',padx=10)
                #self.pack(expand=True,fill='both',padx=10,pady=10)

        def get_input(self):
                x=self.entry.get()
                self.entry.delete(0,tk.END)
                return x
        
        def clear(self):
                return self.entry.delete(0,tk.END)

class ComWidget(ttk.Frame):
        def __init__(self,parent,label_text):
                super().__init__(master=parent)
                self.rowconfigure((0,1),weight=1)
                self.columnconfigure((0),weight=1,uniform='a')
                ttk.Label(self,text=label_text).grid(row=0,column=0,sticky='nesw',pady=10,padx=5)
                self.entry=ttk.Combobox(self,values=['Male','Female','No Show'])
                self.entry.grid(row=1,column=0,sticky='ew',padx=10)
                #self.pack(expand=True,fill='both',padx=10,pady=10)

        def get_input(self):
                x=self.entry.get()
                self.entry.delete(0,tk.END)
                return x
        
        def clear(self):
                return self.entry.delete(0,tk.END)

class ButtonWidget(ttk.Frame):
        def __init__(self,parent,label_text,comment_text):
                super().__init__(master=parent)
                self.rowconfigure((0),weight=1)
                self.columnconfigure((0),weight=1,uniform='a')
                self.button=ttk.Button(self,text=label_text,command=comment_text)
                self.button.grid(row=0,column=0,sticky='ew',padx=10)

class ComWidget(ttk.Frame):
        def __init__(self,parent,label_text,val_text):
                super().__init__(master=parent)
                self.rowconfigure((0,1),weight=1)
                self.columnconfigure((0),weight=1,uniform='a')
                ttk.Label(self,text=label_text).grid(row=0,column=0,sticky='nesw',pady=10,padx=5)
                self.entry=ttk.Combobox(self,values=val_text)
                self.entry.grid(row=1,column=0,sticky='ew',padx=10)
                #self.pack(expand=True,fill='both',padx=10,pady=10)

        def get_input(self):
                x=self.entry.get()
                self.entry.delete(0,tk.END)
                return x
        
        def clear(self):
                return self.entry.delete(0,tk.END)
        
class CheckWidget(ttk.Frame):
        def __init__(self,parent,label_text,check_text):
                super().__init__(master=parent)
                self.rowconfigure((0,1),weight=1)
                self.columnconfigure((0),weight=1,uniform='a')
                ttk.Label(self,text=label_text).grid(row=0,column=0,sticky='nesw',pady=0,padx=5)
                self.entry=ttk.Checkbutton(self,text=check_text)
                self.entry.grid(row=1,column=0,sticky='ew',padx=10)
                #self.pack(expand=True,fill='both',padx=10,pady=10)

        def get_input(self):
                x=self.entry.get()
                self.entry.delete(0,tk.END)
                return x
        
        def clear(self):
                return self.entry.delete(0,tk.END)


state=[
    "Kachin State",
    "Kayah State",
    "Kayin State",
    "Chin State",
    "Mon State",
    "Rakhine State",
    "Shan State",
    "Sagaing Region",
    "Tanintharyi Region",
    "Bago Region",
    "Magway Region",
    "Mandalay Region",
    "Yangon Region",
    "Ayeyarwady Region",
    "Naypyidaw Union Territory"
]
towns = [
     "Yankin","Ahlon", "Bahan", "Botataung", "Dagon", "Dagon Myothit (East)", "Dagon Myothit (North)", 
    "Dagon Myothit (South)", "Dagon Myothit (Seikkan)", "Dala", "Hlaing", "Hlaingthaya", 
    "Insein", "Kamaryut", "Kawhmu", "Khayan", "Kyeemyindaing", "Kyauktada", "Kyauktan", 
    "Lanmadaw", "Latha", "Mayangone", "Mingaladon", "Mingalartaungnyunt", "North Okkalapa", 
    "Pabedan", "Pazundaung", "Sanchaung", "Seikgyikanaungto", "Shwepyithar", "South Okkalapa", 
    "Tamwe", "Thanlyin", "Thaketa", "Thingangyun", "Thongwa", "Twantay"
]

cities = [
    "Yangon", "Mandalay", "Naypyidaw", "Mawlamyine", "Bago", "Pathein", "Taunggyi", "Monywa", 
    "Sittwe", "Myitkyina", "Dawei", "Pyay", "Hpa-An", "Meiktila", "Magway", "Lashio", 
    "Hakha", "Kyaukphyu", "Nyaung-U", "Kengtung", "Pakokku", "Thandwe", "Loikaw", "Shwebo", 
    "Kalaw", "Tachileik", "Kyaukme", "Myeik", "Bogale", "Mudon", "Kawthoung", "Maubin", 
    "Kyaikto", "Pyin Oo Lwin", "Heho", "Inle Lake", "Thayet", "Bhamo", "Sagaing", "Myingyan", 
    "Hinthada", "Wakema", "Letpadan", "Panglong", "Namhkam", "Pinlaung", "Tamu", 
    "Hsipaw", "Tantabin", "Thanlyin", "Yenangyaung", "Pyu", "Kyauktaw", "Mrauk U", 
    "Minbu", "Kyaukse", "Maungdaw", "Ngapali", "Kanpetlet", "Falam", "Paletwa"
]

gender=['Male','Female']

def Add():
        first_name=Fname.entry.get()
        last_name=Lname.entry.get()
        gen_der=Gender.entry.get()
        age=int(Age.entry.get())
        region=Region.entry.get()
        city=City.entry.get()
        no=int(No.entry.get())
        street=Street.entry.get()
        town=Town.entry.get()
        #print(first_name,last_name,gen_der,age,region,city,no,street,town)
        if not ( first_name and last_name and gen_der and age and region and city and no and street and town):
                messagebox.showerror('Error','Enter all fields.')
        
        else:
                
                messagebox.showinfo('Success','Data has been inserted.')
                database.create_db()
                database.insert_students(first_name,last_name,gen_der,age,region,city,no,street,town)
                print(first_name,last_name,gen_der,age,region,city,no,street,town)

        
main=ttk.Frame(window)
main.pack(expand=True,fill='both',padx=10,pady=10)
main.rowconfigure((0),weight=2,uniform='a')
main.rowconfigure((1),weight=2,uniform='a')
main.rowconfigure((2),weight=1,uniform='a')
main.columnconfigure((0),weight=1,uniform='a')

top=ttk.LabelFrame(main,text="Student Information")
top.grid(row=0,column=0,sticky='nesw')
top.rowconfigure((0,1),weight=1,uniform='a')
top.columnconfigure((0,1,2),weight=1,uniform='a')

Fname=EntryWidget(top,'First Name')
Lname=EntryWidget(top,'Last Name')
Gender=ComWidget(top,'   Gender',gender)
Age=SpinWidget(top,"   Age")
Region=ComWidget(top,'Region',state)
City=ComWidget(top,'City',cities)


Fname.grid(row=0,column=0,sticky='nesw')
Lname.grid(row=0,column=1,sticky='nesw')
Gender.grid(row=0,column=2,sticky='nesw')
Age.grid(row=1,column=0,sticky='nesw')
Region.grid(row=1,column=1,sticky='nesw')
City.grid(row=1,column=2,sticky='nesw')


middle=ttk.LabelFrame(main,text='Current Live')
middle.grid(row=1,column=0,sticky='nesw')
middle.rowconfigure((0,1),weight=1,uniform='a')
middle.columnconfigure((0,1,2),weight=1,uniform='a')

No=SpinWidget(middle,'No')
No.grid(row=0,column=0,sticky='nesw')
Street=EntryWidget(middle,"Street Name")
Street.grid(row=0,column=1,sticky='nesw')
Town=ComWidget(middle,'Town',towns)
Town.grid(row=0,column=2,sticky='nesw')

buttom=ttk.LabelFrame(main,text='Manage')
buttom.grid(row=2,column=0,sticky='nesw')
buttom.rowconfigure((0,1),weight=1,uniform='a')
buttom.columnconfigure((0,1,2),weight=1,uniform='a')

button1=ButtonWidget(buttom,'Add Student',Add)
button1.grid(row=0,column=0,sticky='nesw')

window.mainloop()