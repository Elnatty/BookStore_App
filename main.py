from tkinter import *
from basics_sqlite3 import view, insert, search, delete, update
from tkinter.messagebox import showinfo

def view_all():
    list_area.delete(0, END)
    for row in view():
        list_area.insert(END, row)

def get_selected_row(event):
    global selected_tuple        # create a global variable to make it recognized anywhere in this script
    try:
        index = list_area.curselection()[0]
        selected_tuple = list_area.get(index)
        title_ent.delete(0, END)
        title_ent.insert(END, selected_tuple[1])
        author_ent.delete(0, END)
        author_ent.insert(END, selected_tuple[2])
        year_ent.delete(0, END)
        year_ent.insert(END,selected_tuple[3])
        isbn_ent.delete(0, END)
        isbn_ent.insert(END, selected_tuple[4])
    except Exception:
        print("No Record Selected")

def search_command():

    if (len(title_text.get())==0 and len(author_text.get())==0 and len( year_text.get()) ==0 and len(isbn_text.get())==0):
        msg = f'Fill at least One Entry'
        showinfo(title='Information',message = msg)
    else:
        list_area.delete(0, END)
        for row in search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            list_area.insert(END, row)

def add_command():
    if (len(title_text.get())==0 or len(author_text.get())==0 or len( year_text.get()) ==0 or len(isbn_text.get())==0):
        msg = f'Fill Entries Required'
        showinfo(title='Information',message = msg)
    else:

        insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        list_area.delete(0, END)
        list_area.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
def update_command():
    update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_all()
def delete_command():
    delete(selected_tuple[0])
    view_all()
#
window = Tk()

window.configure(bg='white')  # background color
window.wm_title('BookStore')  # app title
window.geometry("650x300")  # window size
# window.resizable(False, False)

# FRAME ONE
entry_frame = LabelFrame(window, bg='skyblue', fg='white', height=200, width=200, pady=70, padx=10,relief='flat')
entry_frame.pack(side=LEFT)

#  TKINTER LABELS
title_lbl = Label(entry_frame, text='Title', fg='white', bg='skyblue', pady =2)
title_lbl.grid(row=1, column=0)

author_lbl = Label(entry_frame, text='Author', fg='white', bg='skyblue')
author_lbl.grid(row=2, column=0)

year_lbl = Label(entry_frame, text='Year', fg='white', bg='skyblue')
year_lbl.grid(row=3, column=0)

isbn_lbl = Label(entry_frame, text='ISBN', fg='white', bg='skyblue')
isbn_lbl.grid(row=4, column=0)

#  TKINTER  ENTRIES
title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()

title_ent = Entry(entry_frame, width=20, bd=3, bg='black', fg='white', textvariable=title_text)
title_ent.grid(row=1, column=1, pady=5)
title_ent.configure(insertbackground='white')

author_ent = Entry(entry_frame, width=20, bd=3, bg='black', fg='white', textvariable=author_text)
author_ent.grid(row=2, column=1, pady=5)
author_ent.configure(insertbackground='white')

year_ent = Entry(entry_frame, width=20, bd=3, bg='black', fg='white', textvariable=year_text)
year_ent.grid(row=3, column=1, pady=5)
year_ent.configure(insertbackground='white')

isbn_ent = Entry(entry_frame, width=20, bd=3, bg='black', fg='white', textvariable=isbn_text)
isbn_ent.grid(row=4, column=1, pady=5)
isbn_ent.configure(insertbackground='white')

# FRAME TWO
display_frame = LabelFrame(window, bg='white', fg='white', height=200, width=200, pady=20, padx=10,relief='flat')
display_frame.pack(side=RIGHT)

list_frame = LabelFrame(display_frame)
list_frame.pack(side=TOP)

btn_frame = LabelFrame(display_frame, relief='groove')
#  relief "": must be flat, groove, raised, ridge, solid, or sunken
btn_frame.pack()

# Information ... Message
msg_lbl = Label(display_frame)
msg_lbl.pack(side=BOTTOM, pady=5)

# List frame Items

list_area = Listbox(list_frame,height=7, width=40, bd=3, bg='black', fg='red')
list_area.grid(row=0, column=0, rowspan=5)

yscroll = Scrollbar(list_frame, width=14)
yscroll.grid(row=0, column=1, rowspan=1, sticky=E)

# binding scrollbar to listbox ie list_area
list_area.configure(yscrollcommand=yscroll.set)
yscroll.configure(command=list_area.yview)

# binding listbox to the event variable
list_area.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
view_btn = Button(btn_frame, text="View All", fg="black", bg="skyblue", width=15,font='times 10 bold', command=lambda :view_all())

view_btn.grid(row=1, column=0, pady=1, padx=2)

search_btn = Button(btn_frame, text='Search Entry', width=15, fg='black', bd=3,font='times 10 bold', command=lambda: search_command())
search_btn.grid(row=2, column=0,pady=1, padx=2)

add_ent_btn = Button(btn_frame, text='Add Entry', width=15, fg='black', bd=3, font='times 10 bold',  command=lambda: add_command())
add_ent_btn.grid(row=3, column=0,pady=1, padx=2)

update_btn = Button(btn_frame, text='Update', width=15, fg='black', bd=3, font='times 10 bold',  command=lambda: update_command())
update_btn.grid(row=1, column=1,pady=1, padx=2)

delete_btn = Button(btn_frame, text='Delete',width=15, fg='black', bd=3, font='times 10 bold', command=lambda: delete_command())
delete_btn.grid(row=2, column=1,pady=1, padx=2)

exit_btn = Button(btn_frame, text='Close', width=15, fg='black', bd=3, font='times 10 bold', command=window.destroy)
exit_btn.grid(row=3, column=1,pady=1, padx=2)

window.mainloop()