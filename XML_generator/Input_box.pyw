# Created By: Mikołaj Oleisński 12.2021

import pandas as pd
from os.path import exists
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showerror


def build_xml(path: str, file_name: str):
    df = pd.read_excel(path, converters={"O_PESEL": str,  'KOD TERYTORIALNY': str})
    try:
        df = df[["O_PESEL", 'KOD TERYTORIALNY', 'Z_PROBKA_DATA_POBRANIA']]
    except KeyError:
        showerror("Błąd", "Niewłaściwy plik Excel")
        return
    df["Z_PROBKA_DATA_POBRANIA"] = df["Z_PROBKA_DATA_POBRANIA"].dt.date
    num_lines = sum(1 for line in open('template.txt'))

    with open('template.txt') as template:
        body = []
        head = [next(template) for x in range(3)]
        for position, line in enumerate(template):
            if position == num_lines - 4:  # 4 bo num_lines liczy od 1 + 3 od head
                tail = line
            else:
                body.append(line)

    output = open(file_name + ".xml", "w")
    for index, row in df.iterrows():
        # wpisuje naglowek xml
        if index == 0:
            for line in head:
                output.write(line)
        # po naglowku wpisuje w pentli tresc xml pacjenta
        for line in body:
            if line.startswith('  <nfz:zestaw-wyk-bad-poz id'):
                updated_line = line.replace('id-zest-wyk-bad-poz="1"', f'id-zest-wyk-bad-poz="{index+1}"')
            elif line.startswith('        <nfz:ident'):
                updated_line = line.replace('id-osoby="61021207287"', f'id-osoby="{row[0]}"')
            elif line.startswith('        <nfz:adres'):
                updated_line = line.replace('teryt="2861011"', f'teryt="{row[1]}"')
            elif line.startswith('      <nfz:wyk-badanie '):
                updated_line = line.replace('data-wyk-badania="2021-12-01"', f'data-wyk-badania="{row[2]}"')
            else:
                updated_line = line
            output.write(updated_line)
        # dopisuje zakonczenie xml
        if index == len(df)-1:
            output.write(tail)
    output.close()


def select_file():
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*'))

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    # czy jest to plik excel
    if filename[-4:len(filename)] != 'xlsx':
        showinfo(
            title='Wybrany Plik',
            message=f'Nie wybrano pliku Excel')
        return

    # wyczyszczam entry box, wkładam ścieżkę i powiadamiam użytkownika co wybrał
    entry_path_entry.delete(0, END)
    entry_path_entry.insert(0, filename)
    if filename:
        showinfo(
            title='Wybrany Plik',
            message=filename)


def generate():
    path, file_name = entry_path_entry.get(), file_name_entry.get()
    if not path or not file_name or len(path) <= 4:
        canvas1.delete('all')
        drew_canvas()
        showerror("Błąd", "Brak nazwy lub ścieżki")
        return
    canvas1.delete('all')
    canvas1.create_text(160, 90, text="Generowanie pliku", font=("Purisa", 15))

    build_xml(path, file_name)
    if not exists(file_name + '.xml'):
        canvas1.delete('all')
        drew_canvas()
        return

    canvas1.delete('all')
    canvas1.create_text(150, 90, text="Generowanie zakończone", font=("Purisa", 15))


def drew_canvas():
    # wpisywanie ścieżki
    poziom_input, pion_input = 30, 40
    global entry_path_entry
    entry_path_entry = Entry(root, width=40)
    entry_path_box = canvas1.create_window(poziom_input, pion_input, window=entry_path_entry, anchor='nw')
    entry_path_label = canvas1.create_text(poziom_input + 60, pion_input - 10, text="Ścieżka do pliku Excel")

    # wpisywanie nazwy output
    poziom_output, pion_output = 30, 110
    global file_name_entry
    file_name_entry = Entry(root, width=40)
    file_name_box = canvas1.create_window(poziom_output, pion_output, window=file_name_entry, anchor='nw')
    file_name_label = canvas1.create_text(poziom_output + 50, pion_output - 10, text="Nazwa pliku xml")

    file_chooser = Button(root, text='Wybierz plik', command=select_file)
    canvas1.create_window(poziom_input + 120, pion_input + 35, window=file_chooser)

    make_xml = Button(text='Generuj xml', command=generate)
    canvas1.create_window(150, 180, window=make_xml)


root = Tk()
root.title('Generator XML')
canvas1 = Canvas(root, width=300, height=200)
canvas1.pack(fill='both')
drew_canvas()


root.mainloop()
