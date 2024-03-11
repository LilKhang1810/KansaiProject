from tkinter import *
root = Tk()
root.title('Kansai Project')
root.geometry("810x720")
root.resizable(width=False, height=False)
Label(root,text='Kansai Project',fg='black',font=('cambria',36)).grid(row=0)
listbox = Listbox(root,width=89,height=20).grid(row=1,columnspan=2)
# Tạo các widget
label1 = Label(root, text='Link of sheet',font=('cambria',26))
label2 = Label(root, text='Request',font=('cambria',26))
entry1 = Entry(root,width=30,font=('cambria',26))
entry2 = Entry(root,width=30,font=('cambria',26))
button = Button(root, text='Generate',width=10,height=2)
# Sử dụng grid để xác định vị trí của các widget
label1.grid(row=2, column=0)
label2.grid(row=3, column=0)
entry1.grid(row=2, column=1)
entry2.grid(row=3, column=1)
button.grid(row=4,column=1)


root.mainloop()