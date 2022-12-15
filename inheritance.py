# basic si

# turunan

class Ojek():
    def __init__(self,nama,transmisi,daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah
    
    def cek_id_abang(self):
        print("Nama :",self.nama,'\nmotor :',self.transmisi,'\ndaerah :', self.daerah)


# inheritance
class Gojek(Ojek): # diwariskan, bisa ditambahkan fungsi baru 
    def cek_id_abang(self):
       print("cek aplikasi gojek")

ojek1= Ojek('mario','manual','bandung') # ini punyanya ojek aja
ojek2= Gojek('jasom','auto','tasikmalaya') # ini punyanya Gojek

ojek1.cek_id_abang()
ojek2.cek_id_abang()
