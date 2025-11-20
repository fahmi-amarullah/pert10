# nama | Nomor Telpon
# ===================
# ari  | 0881267888
# Dina | 087677776

a = {} # dict kosong
a = {'ari': "0881267888", 'Dina':"087677776" } #kontak ari dan dina
print ("kontaknya ari =", a['ari']) #menampilkan kontaknya ari
a['riko'] = ("087654544") #mennambahkan kontak baru
a ['Dina'] = ("088999776") #mengganti nomor dina
print(a.keys()) #mennampilkan seluuruh nama
print(a.values()) #menampilkan semua nomor telpon
print(a.items()) #menampilkan semua item

nomor_dihapus = a.pop('Dina') #mmenghapus kontak dina
print(a) #output