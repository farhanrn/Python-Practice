data = "Ini adalah string"
print(data)
print(type(data))

# 1. cara buat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo gais, apakabar ini pake single quote tbh'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('Mari solat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("c:\\user\\Ucup")

# tab
print("Ucup otong")
print("ucup\totong, jauhan")

# backspace
print("ucup \botong, jadi deketan")

#newline
print("Baris pertama.\nbaris kedua.") # LF _> line feed -> unix, linux macos
print("baris pertama.\rbaris kedua.") # CR -> carriage return _> commodore, acorn
print("baris pertama.\r\nbaris kedua") # CRLF -> carriage return -> dipakai buat windows

# 3. string literal atau raw

# hati-hati 
print('C:\nnew folder') #akan salah folder

# menggunakan raw string
print(r'C:\new folder')

#multiline literal string
print("""
Nama : Ucup
Kelas: 3 SD
""")

#multiline literal string dan raw
print(r"""
Nama : Ucup
Kelas: 3 SD\new normal
website : www.ucup.com/newID
""")







