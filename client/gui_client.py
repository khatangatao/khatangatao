"""
Implement a GUI for viewing and updating blog
"""
from itertools import chain
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import shelve

shelvename = 'class-shelve'
fieldnames = ('title', 'author', 'body', 'created_at', 'modified_at')


def makeWidgets():
    global entries
    window = Tk()
    window.title('khatangatao blog')
    form = Frame(window)
    form.pack()
    entries = {}

    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent

    Button(window, text='Проверить доступность', command=checkAvaibility).pack(side=LEFT)
    Button(window, text="Найти статью", command=fetchRecord).pack(side=LEFT)
    Button(window, text="Обновить", command=updateRecord).pack(side=LEFT)
    Button(window, text="Выход", command=window.quit).pack(side=RIGHT)
    return window


def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]                                                # fetch by key, show in GUI
    except:
        showerror(title='Error', message='Такой статьи нет!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]                                                # update existing record
    else:
        from person import Person                                       # make/store new one for key
        record = Person(name='?', age='?')                              # eval: strings must be quoted
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record


def checkAvaibility():
    import subprocess
    reply = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'],
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           )
    # todo должно открыться окно с результатом проверки
    if reply.returncode == 0:
        showinfo(title='popup', message='Работает!')
    else:
        showinfo(title='popup', message='Не работает!')


db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()                                                              # back here after quit or window close