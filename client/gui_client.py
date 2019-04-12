#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement a GUI for viewing and updating blog
"""
from tkinter import *
from tkinter.messagebox import showerror, showinfo
import threading
import logging

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
            entries[field].delete(0, END)
            entries[field].insert(0, r.json().get(field, ''))
            print(entries[field].get())
    elif r.status_code == 404:
        showerror(title='Error', message='Такой статьи нет!')



def updateRecord():
    import requests
    import json
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
    executeInNewThread(pingCheck())

def checkHomePage():
    import requests
    target = 'http://khatangatao.com/'
    headers = {"Authorization": "Bearer 56a4f78b7f4a6990d3ae6c223a73249b8765c0c1"}
    r = requests.get(target, headers=headers)
    print(r.status_code)


def pingCheck():
    import subprocess
    # print(threading.current_thread().getName(), 'Starting')
    logging.debug('Starting')
    reply = subprocess.run(['ping', '-c', '3', '-n', 'khatangatao.com'],
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           )
    if reply.returncode == 0:
        showinfo(title='popup', message='Работает!')
    else:
        showinfo(title='popup', message='Не работает!')

    # print(threading.current_thread().getName(), 'Exiting')
    logging.debug('Exiting')


def executeInNewThread(function):
    """Multithreading"""
    th = threading.Thread(name='pingCheck', target=function)
    th.start()
    print(th)
    # th.join()


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)


window = makeWidgets()
window.mainloop()
