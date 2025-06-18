import tkinter as tk
import mysql.connector as con
import sys
root=tk.Tk()
def submit_form():
  
  name=name_entry.get()
  email=email_entry.get()
  db=con.connect(
    host='localhost',
    user='root',
    password='',
    database="mydb",
    port=3306
  )
  cursor=db.cursor()
  cursor.execute("insert into stud(name,mail)values(%s,%s)",(name,email))
  db.commit()
  cursor.close()
  db.close()
  name_entry.delete(0,tk.END)
  email_entry.delete(0,tk.END)
  print("form submited sucessfullyt")

def update_form():
  id=id_entry.get()
  name=name_entry.get()
  email=email_entry.get()
  db=con.connect(
    host='localhost',
    user='root',
    password='',
    database="mydb",
    port=3306
  )
  cursor=db.cursor()
  cursor.execute("update stud set name=%s,mail=%s where id=%s",(name,email,id))
  db.commit()
  cursor.close()
  db.close()
  id_entry.delete(0,tk.END)
  name_entry.delete(0,tk.END)
  email_entry.delete(0,tk.END)
  print("form update sucessfullyt")

def delete_form():
  id=id_entry.get()
  db=con.connect(
    host='localhost',
    user='root',
    password='',
    database="mydb",
    port=3306
  )
  cursor=db.cursor()
  cursor.execute("delete from stud where id=%i",(id))
  db.commit()
  cursor.close()
  db.close()
  # id_entry.delete(0,tk.END)
  print("form update sucessfullyt")
  
def display():
  db=con.connect(
    host='localhost',
    user='root',
    password='',
    database="mydb",
    port=3306
  )
  cursor=db.cursor()
  cursor.execute("select * from stud")
  my_data=cursor.fetchall()
  for row in my_data:
    label=tk.Label(root,text=str(row))
    label.pack()
  db.commit()
  cursor.close()
  db.close()
  print("form update sucessfullyt")
 
root.title("welcome to registraion form")
root.geometry('500x500')

tk.Label(root,text="Id").place(x=20,y=20)
id_entry=tk.Entry(root)
id_entry.place(x=120,y=20)

tk.Label(root,text="enter your name").place(x=20,y=60)
name_entry=tk.Entry(root)
name_entry.place(x=120,y=60)

tk.Label(root,text="enter your email").place(x=20,y=100)
email_entry=tk.Entry(root)
email_entry.place(x=120,y=100)

button=tk.Button(root,text="insert",command=submit_form)
button.place(x=10,y=150)
button=tk.Button(root,text="update",command=update_form)
button.place(x=100,y=150)
button=tk.Button(root,text="delete",command=delete_form)
button.place(x=200,y=150)

text_widget = tk.Text(root)
text_widget.pack()
sys.stdout = PrintRedirector(text_widget)
root.mainloop()