import tkinter as tkk
from tkinter import *
import requests
from PIL import ImageTk,Image
import random

auth = ""
for i in range(5):
    auth += str(random.randint(0,9))
print(auth)

app = Tk()
app.geometry('920x700')
app.title("Branch International")
app.iconbitmap(r'build\icons\branch_logo.ico')
app['background']="lavender"

img = ImageTk.PhotoImage(Image.open('build\icons\\branchimage.png'))
msg=Label(image=img, background='lavender')
msg.pack()
#creating a mainframe
main_frame = Frame(app)
main_frame.pack(fill=BOTH, expand=1)
main_frame['background']='lavender'

#creating a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_canvas['background']='lavender'

#add scrollbar to the Canvas
my_scrollbar = tkk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#create another frame inside canvas
second_frame = Frame(my_canvas)
second_frame['background']='lavender'

#Add new frame to the window in the canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#msg=Label(image=img)
#msg=Label(second_frame,text=" Branch International ",background="lavender",foreground="darkorange1", font=("Times",34, "bold"))
#msg.grid(row=0,column=2,padx=25,pady=20)
#msg.pack()


class customers:              #Creating a class called restaurant
    def __init__(self, link):  #initializing the link and header file
        self.link = link
        self.hdr = {
            'apikey': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNuZG9oeGV5Z3Npb2hvZnF2bHpzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2NzU2NDExOSwiZXhwIjoxOTgzMTQwMTE5fQ.FjOs3gzzURUVeuonOBw2K-_FfB97Sx3fzZaX9bndM_g",
            'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNuZG9oeGV5Z3Npb2hvZnF2bHpzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2NzU2NDExOSwiZXhwIjoxOTgzMTQwMTE5fQ.FjOs3gzzURUVeuonOBw2K-_FfB97Sx3fzZaX9bndM_g"
}
        r = requests.get(self.link, headers=self.hdr)
        self.data = r.json()
        #print('**',self.data)

    def getuid(self,data):
        self.uid = []
        for i in data:
            self.uid.append(i['User ID'])
        return self.uid

    def getmessage(self,data):
        self.msg = []
        for i in data:
            self.msg.append(i['Message'])
        return self.msg

    def gettime(self,data):
        self.time = []
        for i in data:
            self.time.append(i['Timestamp'])
        return self.time

    def getid(self,data):
        self.id = []
        for i in data:
            self.id.append(i['id'])
        return self.id

    def getresponse(self,data):
        self.response = []
        for i in data:
            self.response.append(i['Response'])
        return self.response

    def getrid(self,data):
        self.rid = []
        for i in data:
            self.rid.append(i['Response ID'])
        return self.rid

    def updatedata(self):
        '''link = 'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service'
        obj4 = customers(link)
        data = obj4.savedata()
        obj4.filterdata(data)'''
        return self.ext_data


    def savedata(self):
        data = self.data
        userid=obj.getuid(data)
        message=obj.getmessage(data)
        timestamp=obj.gettime(data)
        response=obj.getresponse(data)
        rid=obj.getrid(data)
        id = obj.getid(data)

        self.main_data=[]
        for i in range(len(userid)):
            self.main_data.append([userid[i],message[i],timestamp[i],response[i],rid[i],id[i]])
            #print([userid[i],message[i],timestamp[i],response[i],rid[i]])
        return self.main_data

    def search(self):
        new_data=[]
        key = searchE.get()

        link = 'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service'

        obj2 = customers(link)
        data = obj2.savedata()

        for ele in data:
            i = 0
            j = len(key)
            if len(ele[1])>=len(key):
                while j+1<=len(ele[1]):
                    if ele[1][i:j].lower()==key.lower():
                        new_data.append(ele)
                        break
                    i += 1
                    j += 1
        self.filterdata(new_data)

    def authenticate(self,data):
        self.hdr['Content-Type'] = 'application/json'
        self.hdr['Prefer'] = 'return=representation'
        for ele in data:
            x = str(ele[-1])
            d = {'Response ID': auth}
            url = f'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service?id=eq.{x}'
            r = requests.patch(url, headers=self.hdr, json=d)


    #filters the records and gets the top 10 queries tp look after
    def filterdata(self, data):
        self.ext_data = []
        for ele in data:
            if ele[3] == None or ele[3] == '':
                if ele[4] == auth:
                    self.ext_data.append(ele)
        count = len(self.ext_data)
        for ele in data:
            if ele[3] == None or ele[3] == '':
                if ele[4] == None or ele[4]=='':
                    self.ext_data.append(ele)
                    count += 1
                    if count >= 10:
                        break
                else:
                    continue
            else:
                pass
        for i in self.ext_data:
            print(i)
        self.authenticate(self.ext_data)

        self.application(self.ext_data)

    def upload(self,req,d):
        self.hdr['Content-Type'] = 'application/json'
        self.hdr['Prefer'] = 'return=representation'
        x=str(req[-1])

        d = {'Response': d}
        url = f'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service?id=eq.{x}'
        r = requests.patch(url, headers=self.hdr, json=d)

    def delauth(self,req,d):
        self.hdr['Content-Type'] = 'application/json'
        self.hdr['Prefer'] = 'return=representation'
        x = str(req[-1])

        d = {'Response ID': d}
        url = f'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service?id=eq.{x}'
        r = requests.patch(url, headers=self.hdr, json=d)

    def deauthenticate(self):
        link = 'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service'
        obj1 = customers(link)
        data = obj1.savedata()
        auth_data = []
        for ele in data:
            if ele[-2] != None and ele[-2] != '':
                auth_data.append(ele)
        s = ''
        for ele in auth_data:
            self.delauth(ele,s)


    def b1ex(self):
        ext = self.updatedata()
        req=ext[0]
        d = r1E.get()
        self.upload(req,d)

    def b2ex(self):
        ext = self.updatedata()
        req = ext[1]
        d = r2E.get()
        self.upload(req, d)

    def b3ex(self):
        ext = self.updatedata()
        req = ext[2]
        d = r3E.get()
        self.upload(req, d)

    def b4ex(self):
        ext = self.updatedata()
        req = ext[3]
        d = r4E.get()
        self.upload(req, d)

    def b5ex(self):
        ext = self.updatedata()
        req = ext[4]
        d = r5E.get()
        self.upload(req, d)

    def b6ex(self):
        ext = self.updatedata()
        req = ext[5]
        d = r6E.get()
        self.upload(req, d)

    def b7ex(self):
        ext = self.updatedata()
        req = ext[6]
        d = r7E.get()
        self.upload(req, d)

    def b8ex(self):
        ext = self.updatedata()
        req = ext[7]
        d = r8E.get()
        self.upload(req, d)

    def b9ex(self):
        ext = self.updatedata()
        req = ext[8]
        d = r9E.get()
        self.upload(req, d)

    def b10ex(self):
        ext = self.updatedata()
        req = ext[9]
        d = r10E.get()
        self.upload(req, d)

    #the below function is for the application to display our results
    def application(self,data):
        row_val = 5
        for ele in data:
            # User ID
            p = Label(second_frame, text='User ID : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
            p.grid(row=row_val, column=0, padx=20, pady=10, columnspan=2)
            p = Label(second_frame, text=ele[0], bd=1, background="lavender", foreground="tomato3",
                      font=("Times", 11, "bold"))
            p.grid(row=row_val, column=2, padx=15, pady=20, columnspan=2)
            row_val += 1

            # Message Body
            p = Label(second_frame, text='Message : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
            p.grid(row=row_val, column=0, padx=5, pady=10, columnspan=2)
            l = Text(second_frame, width=80, height=3, background='floral white', foreground='Black',
                     font=("Arial", 10))
            l.insert(1.0, ele[1])
            l.grid(row=row_val, column=2, padx=10, pady=10)
            row_val += 1

            p = Label(second_frame, text=' ', background="lavender",
                      foreground="lightsteelblue2",
                      font=("Arial", 14))
            p.grid(row=row_val, column=1, padx=10, pady=10)
            row_val += 1

def refresh():
    link = 'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service'

    obj1 = customers(link)
    data = obj1.savedata()
    obj1.filterdata(data)


def history():
    app1 = Toplevel()
    app1.geometry('880x700')
    app1.title("Chat History")
    app1.iconbitmap(r'build\icons\branch_logo.ico')
    app1['background'] = "lavender"

    # creating a mainframe
    main_frame = Frame(app1)
    main_frame.pack(fill=BOTH, expand=1)
    main_frame['background'] = 'lavender'

    # creating a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_canvas['background'] = 'lavender'

    # add scrollbar to the Canvas
    my_scrollbar = tkk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # create another frame inside canvas
    third_frame = Frame(my_canvas)
    third_frame['background'] = 'lavender'

    # Add new frame to the window in the canvas
    my_canvas.create_window((0, 0), window=third_frame, anchor="nw")

    resta = Label(third_frame, text="                       Recent Chats                       ", background="Slate grey", foreground="bisque",
                  font=("MS Sans Serif", 32, "bold"))
    resta.grid(row=0, column=0, padx=25, pady=20, columnspan=3)

    link = 'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service'
    obj1 = customers(link)
    data = obj1.savedata()
    his_data = []
    for i in data:
        if i[3]==None or i[3]=='':
            continue
        else:
            his_data.append(i)

    row_val=1
    for ele in his_data:
        # User ID
        p = Label(third_frame, text='User ID : ', bd=1, background="lavender", foreground="maroon",
                  font=("Arial", 11, "bold"))
        p.grid(row=row_val, column=0, padx=20, pady=10, columnspan=1)
        p = Label(third_frame, text=ele[0], bd=1, background="lavender", foreground="tomato3",
                  font=("Times", 11, "bold"))
        p.grid(row=row_val, column=1, padx=15, pady=20, columnspan=2)
        row_val += 1

        # Message Body
        p = Label(third_frame, text='Message : ', bd=1, background="lavender", foreground="maroon",
                  font=("Arial", 11, "bold"))
        p.grid(row=row_val, column=0, padx=5, pady=10, columnspan=1)
        l = Text(third_frame, width=100, height=3, background='floral white', foreground='Black',
                 font=("Arial", 10))
        l.insert(1.0, ele[1])
        l.grid(row=row_val, column=1, padx=10, pady=10, columnspan=2)
        row_val += 1

        # reply box
        p = Label(third_frame, text='Response : ', bd=1, background="lavender", foreground="maroon",
                  font=("Arial", 11, "bold"))
        p.grid(row=row_val, column=0, padx=5, pady=10, columnspan=1)
        l = Text(third_frame, width=100, height=3, background='floral white', foreground='Black',
                 font=("Arial", 10))
        l.insert(1.0, ele[3])
        l.grid(row=row_val, column=1, padx=2, pady=3, columnspan=2)
        row_val += 1

        p = Label(third_frame, text=' ', background="lavender",
                  foreground="lightsteelblue2",
                  font=("Arial", 14))
        p.grid(row=row_val, column=1, padx=10, pady=10)
        row_val += 1
        row_val += 2



link = 'https://sndohxeygsiohofqvlzs.supabase.co/rest/v1/Customer Service'

obj = customers(link)
data = obj.savedata()

p = Label(second_frame, text='Search', bd=1, background="lavender", foreground="Sienna",
              font=("Arial", 13, "bold"))
p.grid(row=2, column=0, padx=5, pady=10, columnspan=2)
searchE = Entry(second_frame, width=90, background='floral white', foreground='Black',
             font=("Arial", 10))
searchE.grid(row=2, column=2, padx=10, pady=10)
B=Button(second_frame, text="search",command=obj.search,foreground='Sienna', background='bisque',width=8, font=("MS Sans Serif",10,'bold'))
B.grid(row=2,column=4,padx=15,pady=25, columnspan=2)

p = Label(second_frame, text=' ', background="lavender",
              foreground="lightsteelblue2",
              font=("Arial", 14))
p.grid(row=3, column=1, padx=10, pady=10)

p = Label(second_frame, text='                                        Customer Queries                                        ', bd=1, background="slate grey", foreground="white",
              font=("MS Sans", 22,"bold"))
p.grid(row=4, column=0, padx=5, pady=10, columnspan=6)

obj.filterdata(data)


# Response Entry and Button fields
r=7
# field1
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r1E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r1E.grid(row=r, column=2, padx=2, pady=5)

B1 = Button(second_frame, text="reply", command=obj.b1ex, foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B1.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field 2
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r2E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r2E.grid(row=r, column=2, padx=2, pady=5)

B2 = Button(second_frame, text="reply", command=obj.b2ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B2.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field 3
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r3E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r3E.grid(row=r, column=2, padx=2, pady=5)

B3 = Button(second_frame, text="reply", command=obj.b3ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B3.grid(row=13, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field4
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r4E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r4E.grid(row=r, column=2, padx=2, pady=5)

B4 = Button(second_frame, text="reply", command=obj.b4ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B4.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field 5
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r5E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r5E.grid(row=r, column=2, padx=2, pady=5)

B5 = Button(second_frame, text="reply", command=obj.b5ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B5.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field6
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r6E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r6E.grid(row=r, column=2, padx=2, pady=5)

B6 = Button(second_frame, text="reply", command=obj.b6ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B6.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field 7
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r7E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r7E.grid(row=r, column=2, padx=2, pady=5)

B7 = Button(second_frame, text="reply", command=obj.b7ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B7.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field 8
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r8E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r8E.grid(row=r, column=2, padx=2, pady=5)

B8 = Button(second_frame, text="reply", command=obj.b8ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B8.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field 9
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r9E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r9E.grid(row=r, column=2, padx=2, pady=5)

B9 = Button(second_frame, text="reply", command=obj.b9ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B9.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

# field 10
p = Label(second_frame, text='Reply : ', bd=1, background="lavender", foreground="Sienna",
                      font=("Arial", 13, "bold"))
p.grid(row=r, column=0, padx=5, pady=5, columnspan=2)
r10E = Entry(second_frame, width=80, background='floral white', foreground='Black', font=("Arial", 10))
r10E.grid(row=r, column=2, padx=2, pady=5)

B10 = Button(second_frame, text="reply", command=obj.b10ex,foreground='Maroon', background='bisque', width=8, font=("Courier New",10,"bold"))
B10.grid(row=r, column=4, padx=15, pady=25, columnspan=2)
r = r+3

#Bref = Button(second_frame, text="Refresh", command=refresh,foreground='maroon3', background='thistle2', width=15, font=("Arial",10,"bold"))
#Bref.grid(row=3, column=0, padx=15, pady=25, columnspan=2)

Bresp = Button(second_frame, text="Chat History", command=history, foreground='maroon3', background='thistle2', width=15, font=("Arial",10,"bold"))
Bresp.grid(row=3, column=2, padx=15, pady=25, columnspan=2)

mainloop()

obj.deauthenticate()