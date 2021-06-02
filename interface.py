from tkinter import *
from tkinter import ttk
import requests

API_KEY = 'ZTJkYWFkY2QtZjBkYi00NDM1LThmYjUtZWRhMmRkYzRhYjUzOmEzNDYyZWM0NGUxNDQ5NDc4MGIwNDViMzIwN2FjNTFm'
POST_AUTH = 'api/v1.1/authenticate'
URL = 'https://developers.lingvolive.com/'
GET_REQ = 'api/v1/WordList'


class Translator:
    def __init__(self, parameters):
        self.parameters = parameters

    def translate_word(self):
        headers_auth = {
            'Authorization': f'Basic {API_KEY}'
        }
        auth = requests.post(URL + POST_AUTH, headers=headers_auth)

        if auth.status_code == 200:

            headers_get = {
                'Authorization': f'Bearer {auth.text}'
            }
            res = requests.get(URL + GET_REQ, headers=headers_get, params=self.parameters).json()
            try:
                return res['Headings'][0]['Heading'].capitalize() + " : " + res['Headings'][0][
                    'Translation'].capitalize()

            except:
                return 'Ничего не найдено'
        else:
            return 'Error!!'


###-main_frame_logic-###
def pr():
    if language.get() == 1:
        output_text.delete('1.0', END)
        tr = Translator(parameters={
            'prefix': ent.get(),
            'srcLang': 1033,
            'dstLang': 1049,
            'pageSize': 4})
        res = tr.translate_word()
        output_text.insert('1.0', res)
    elif language.get() == 2:
        output_text.delete('1.0', END)
        tr = Translator(parameters={
            'prefix': ent.get(),
            'srcLang': 1049,
            'dstLang': 1033,
            'pageSize': 4})
        res = tr.translate_word()
        output_text.insert('1.0', res)


def clear():
    ent.delete(0, END)
    output_text.delete('1.0', END)


###-Main window-###

root = Tk()
root.iconbitmap('media/Python.ico')
root.title('Translator')
root['bg'] = '#BADBE3'
root.geometry('550x200+800+300')
root.resizable(0, 1)

menu_frame = Frame(root, background='#BADBE3', height=40)
menu_frame.place(width=550, height=25)

lbl = ttk.Label(root, text='Введите слово для перевода', background='#BADBE3')
lbl.place(width=170, height=25, x=3, y=28)

ent = Entry(root)
word = ent.get()
ent.place(width=200, height=25, x=200, y=28)

output_text = Text(root, padx=3, pady=3, wrap=WORD)
output_text.place(width=300, height=80, x=100, y=75)

btn = ttk.Button(root, text='Translate', command=pr)
btn.place(width=100, height=25, x=420, y=28)

btn_dlt = ttk.Button(root, text='Delete', command=clear)
btn_dlt.place(width=100, height=25, x=420, y=75)

lbl_translate = ttk.Label(root, text='Перевод', background='#BADBE3')
lbl_translate.place(width=70, height=25, x=3, y=75)

language = IntVar()
select_lang_1 = Radiobutton(menu_frame, text='Eng->Rus', variable=language, value=1, background='#BADBE3')
select_lang_2 = Radiobutton(menu_frame, text='Rus->Eng', variable=language, value=2, background='#BADBE3')
select_lang_1.place(x=3, y=1)
select_lang_2.place(x=80, y=1)

root.mainloop()
