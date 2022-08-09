import pymongo
from pymongo import collection
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("750x750")
window.title("STUDENT FORM")
window.config(bg="orange")

Ist= [['ID','name','email','course']]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def callback(event):
    global Istindex
    li = []
    li = event.widget._values
    cid.set(Ist[li[1]][0])
    cname.set(Ist[li[1]][1])
    cemail.set(Ist[li[1]][2])
    ccourse.set(Ist[li[1]][2][3])

def creategrid(n):
    Ist.clear()
    Ist.append(["ID", "Name", "Email", "Course"])
    cursor = mycol.find({})
    for text_fromDB in cursor:
        studid = str(text_fromDB["studid"])
        studname = str(text_fromDB["studname"].encode("utf-8").decode("utf-8"))
        studemail = str(text_fromDB["studemail"].encode("utf-8").decode("utf-8"))
        studcourse= str(text_fromDB["studcourse"].encode("utf-8").decode("utf-8"))
        Ist.append([studid, studname, studemail, studcourse])

    for i in range(len(Ist)):
        for j in range(len(Ist[0])):
            mgrid = tk.Entry(window, width=10)
            mgrid.insert(tk.END, Ist[i][j])
            mgrid.values = mgrid.get(), i
            mgrid.grid(row=i + 7, column=j + 6)
            mgrid.bind("<Button-1>", callback)
    if n == 1:
        for label in window.grid_slaves():
            if int(label.grid_info()["row"]) > 6:
                label.grid_forget()


def msgbox(msg, titlebar):
    result = messagebox.askokcancel(title=titlebar, message=msg)
    return result

def save():
    r = msgbox("save record?", "record")
    if r == True:
        newid = mycol.count_documents({})
    if newid != 0:
        newid = mycol.find_one(sort=[("studid", -1)])["studid"]
        id = newid + 1
        cid.set(id)
        mydict = {"studid": int(custid.get()), "studname": custname.get(), "studemail": custemail.get(),"studcourse":ccourse.get()}
        x = mycol.insert_one(mydict)
        creategrid(1)
        creategrid(0)



def update():
    r = msgbox("Update?", "record")
    if r == True:
        myquery = {"studid": int(custid.get())}
        newvalues = {"$set": {"studname": custname.get()}}
        mycol.update_one(myquery, newvalues)

        newvalues = {"$set": {"studemail": custemail.get()}}
        mycol.update_one(myquery, newvalues)

        newvalues = {"$set": {"studcourse": ccourse.get()}}
        mycol.update_one(myquery, newvalues)
        creategrid(2)
        creategrid(1)
        creategrid(0)


def delete():
    r = msgbox("Delete?", "record")
    if r == True:
        myquery = {"studid": int(custid.get())}
        mycol.delete_one(myquery)
        creategrid(1)
        creategrid(0)



label = tk.Label(window, text="students Enlistment Form", width=30, height=1, bg="yellow", anchor="center")
label.config(font=("Courier", 10))
label.grid(column=2, row=1)

label = tk.Label(window, text="Student ID:", width=10, height=1, bg="yellow")
label.grid(column=1, row=2)
cid = tk.StringVar()
custid = tk.Entry(window, textvariable=cid)
custid.grid(column=2, row=2)

label = tk.Label(window, text="Student name:", width=15, height=1, bg="yellow")
label.grid(column=1, row=3)
cname = tk.StringVar()
custname = tk.Entry(window, textvariable=cname)
custname.grid(column=2, row=3)

label = tk.Label(window, text="Student Email:", width=15, height=1, bg="yellow")
label.grid(column=1, row=4)
cemail = tk.StringVar()
custemail = tk.Entry(window, textvariable=cemail)
custemail.grid(column=2, row=4)

label = tk.Label(window, text="Student Course:", width=20, height=5)
label.grid(column=1, row=5)
ccourse = tk.StringVar()
custcourse = tk.Entry(window, textvariable=ccourse)
custcourse.grid(column=2, row=5)

creategrid(0)

savebtn = tk.Button(text= "Save", command=save)
savebtn.grid(column=1, row=6)
savebtn = tk.Button(text="Delete", command=delete)
savebtn.grid(column=2, row=6)
savebtn = tk.Button(text="Update", command=update)
savebtn.grid(column=3, row=6)
window.mainloop()