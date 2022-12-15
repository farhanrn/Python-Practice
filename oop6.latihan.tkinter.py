import tkinter
# tiap kelas ada huruf besar didepannya
main_window = tkinter.Tk() #tk ini adalah bojek
print(main_window.__dict__)

label1 = tkinter.Label(main_window, text = 'label1')
label2 = tkinter.Label(main_window, text = 'label2')

tombol1 = tkinter.Button(main_window, text = "tombol 1")
tombol2 = tkinter.Button(main_window, text = "tombol 2")
# method positioning

# huruf kecil itu fungsi
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

#method menampolkan GUI
main_window.mainloop()
