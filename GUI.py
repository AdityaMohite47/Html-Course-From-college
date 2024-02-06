
# lecture 1 and 2 
# {
#  import  tkinter

# window2 = tkinter.Tk()
# window2.title("Colors")

# b1 = tkinter.Button(window2 , text="Red" , fg='red', background= 'black')
# b2 = tkinter.Button(window2 , text="Green" , fg='green', background= 'black')
# b3 = tkinter.Button(window2 , text="Black" , fg='black', background= 'white')
# b4 = tkinter.Button(window2 , text="Blue" , fg='blue', background= 'black')

# b2.pack(side='top')
# b4.pack(side='left')
# b1.pack(side='right')
# b3.pack(side='bottom')

# window2.mainloop()

# window = tkinter.Tk()
# window.title("GUI")
# l = tkinter.Label(window , text = "Welcome to Python Programming")
# l2 = tkinter.Label(window , text = "Today we are going to learn how to program a GUI using Python")
# b= tkinter.Button(window,text="Enter" )


# l.pack()
# l2.pack()
# b.pack()t.
# window.mainloop()   
# }


# lecture 3


# import tkinter as t
    
# window = t.Tk()
# window.config(bg='orange')

# def click():
#     l2.config(text = "Thank You")
#     l2.pack()

# def yes():
#     window2 = t.Tk()
#     window2.config(bg='orange')
#     l4= t.Label(window2 , text="Welcome" , bg='orange')
#     l4.pack()
#     click()
#     window2.mainloop()

# l = t.Label(window, text = "Welcome to FY Computer Science" , bg='orange')
# l.pack(side='top')
# l2 = t.Label(window , text = "Wish You Happy Learning" , font=("Italic" , 10) , bg='orange')
# l2.pack()
# b = t.Button(window , text = "OK" , command=yes)
# b.pack()

# window.mainloop()



# lecture 4

# Program 1

import tkinter as t

window1 = t.Tk()
window1.title("Login Page")
window1.geometry("700x600")


def submit():
    User = Username.get()
    Passowrd = Pass.get()

    Username.set("")
    Pass.set("")

    print(User)
    print(Passowrd)

    window2 = t.Tk()
    window1.title("Main Page")
    window2.geometry("700x600")
    window2.title("Main Page")
    l4= t.Label(window2 , text= f"Welcome {User}")
    l4.pack(side='top')
    window2.mainloop()


Username = t.StringVar()
Pass = t.StringVar()

l1 = t.Label(window1 , text="UserName")
l2 = t.Label(window1 , text = "Password")
b = t.Button(window1 , text="Submit" , command=submit)
e1 = t.Entry(window1 , textvariable=Username)
e2 = t.Entry(window1 , textvariable=Pass , show='*')

l1.grid(row=0 , column=0)
e1.grid(row =0 , column=1)
l2.grid(row= 1 , column=0)
e2.grid(column=1 , row=1)
b.grid(row=2 , column=1)

window1.mainloop()


#Program 2
# import tkinter as t

# window1 = t.Tk()
# window1.title("Login Page")
# window1.geometry("700x600")


# def submit():
#     a = n1.get()
#     b = n2.get()
#     c = a+b
#     n1.set(0)
#     n2.set(0)
#     sum_label.config(text=c)



# n1 = t.IntVar()
# n2 = t.IntVar()

# l1 = t.Label(window1 , text="Number1")
# l2 = t.Label(window1 , text = "Number2")
# b = t.Button(window1 , text="Add" , command=submit)
# e1 = t.Entry(window1 , textvariable=n1 , bg='black', fg='white')
# e2 = t.Entry(window1 , textvariable=n2 , bg='black', fg='white')
# sum_label =t.Label(window1)

# l1.grid(row=0 , column=0)
# e1.grid(row =0 , column=1)
# l2.grid(row= 1 , column=0)
# e2.grid(column=1 , row=1)
# b.grid(row=2 , column=0)
# sum_label.grid(row=2 , column=1)

# window1.mainloop()

