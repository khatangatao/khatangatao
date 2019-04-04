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
    # key = entries['key'].get()
    # try:
    #     record = db[key]                                                # fetch by key, show in GUI
    # except:
    #     showerror(title='Error', message='Такой статьи нет!')
    # else:
    #     for field in fieldnames:
    #         entries[field].delete(0, END)
    #         entries[field].insert(0, repr(getattr(record, field)))

    import requests
    # todo нужна валидация полей, введенных юзером
    recordNumber = entries['key'].get()

    target = 'http://khatangatao.com/api/entry/' + recordNumber
    headers = {"Authorization": "Bearer 56a4f78b7f4a6990d3ae6c223a73249b8765c0c1"}

    r = requests.get(target, headers=headers)
    print(r.status_code)
    print(r.json())
    if r.status_code == 200:
        for field in fieldnames:
            print(field)
            # entries[field] = r.json().get(field)
            entries[field].delete(0, END)
            entries[field].insert(0, r.json().get(field, ''))
            print(entries[field].get())
    elif r.status_code == 404:
        showerror(title='Error', message='Такой статьи нет!')



def updateRecord():
    # key = entries['key'].get()
    # if key in db:
    #     record = db[key]                                                # update existing record
    # else:
    #     from person import Person                                       # make/store new one for key
    #     record = Person(name='?', age='?')                              # eval: strings must be quoted
    # for field in fieldnames:
    #     setattr(record, field, eval(entries[field].get()))
    # db[key] = record
    import requests
    import json
    # recordNumber = entries['key'].get()
    data = {}

    target = 'http://khatangatao.com/api/entry/'
    headers = {"Authorization": "Bearer 56a4f78b7f4a6990d3ae6c223a73249b8765c0c1",
               "Content-Type": "application/json"}
    for field in fieldnames:
        data[field] = entries[field].get()

    data = json.dumps(data)
    print(data)

    r = requests.post(url=target, data=data, headers=headers)
    print(r.status_code)

def checkAvaibility():
    # todo распараллелить с основным потоком
    import subprocess
    reply = subprocess.run(['ping', '-c', '3', '-n', 'khatangatao.com'],
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           )
    # todo должно открыться окно с результатом проверки
    if reply.returncode == 0:
        showinfo(title='popup', message='Работает!')
    else:
        showinfo(title='popup', message='Не работает!')


window = makeWidgets()
window.mainloop()
