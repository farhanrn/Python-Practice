print('Teknik looping')

nama_band = ['Payung Teduh',
            'Fourtwenty',
            'Dialog Dini Hari',
            'Mr. Sojaya',
            'Paraheyana']

kumpulan_lagu = ['akad',
        'zona nyaman',
        'Rumahku',
        'Sang filusuf',
        'Sindoro']

# enumerate
for index,band in enumerate(nama_band):
    print(index,':',band)

# zip

for band, lagu in zip(nama_band,kumpulan_lagu):
    print(band,'Menyanyikan lagu yang berjudul:',lagu)

# set
playlist = {'baby baby', 'ada apa dengan cinta', 'cenat cenut', 'jaran goyang', 'gorgon', 'kuda','kucing'}
for lagu in sorted(playlist):
    print(lagu)

# dictionary 
playlis2 = {'Payung Teduh':'akad',
            'Fourtwenty':'zona nyaman',
            'Dialog Dini Hari':'Rumahku',
            }
for i,v in playlis2.items():
    print(i,'lagunya :',v)


