"""
Tugas dari Andra
Aksara, bisa tolong bantu mengurus beberapa data penjualan dari dataset oder.csv? Saya sedang rapat dan bahan ini ditunggu dalam pembahasan cabang supermarket kita. Berikut ya detailnya:

1. Median price yang dibayar customer dari masing-masing metode pembayaran.
2. Tentukan metode pembayaran yang memiliki basket size (rataan median price) terbesar.
3. Ubah freight_value menjadi shipping_cost dan cari shipping_cost termahal dari data penjualan tersebut menggunakan sort.
4. Untuk setiap product_category_name, berapa rata-rata weight produk tersebut dan standar deviasi mana yang terkecil dari weight tersebut,
5. Buat histogram quantity penjualan dari dataset tersebut untuk melihat persebaran quantity penjualan tersebut dengan bins = 5 dan figsize= (4,5)
6. Khusus poin 4, tolong diperhatikan lebih ya, Aksara karena hasil analisisnya akan digunakan kepala cabang dalam menyusun strategi free ongkir.

Kubalas email itu segera, OK! Hasilnya akan selesai sebelum makan siang ya. You can count on me, hehehe.

Perhatian: Semua string dinyatakan dalam kutipan "...".

 
"""



import pandas as pd
import matplotlib.pyplot as plt
order_df = ___("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Median price yang dibayar customer dari masing-masing metode pembayaran. 
median_price = order_df["___"].___(___["___"]).___
print(median_price)
# Ubah freight_value menjadi shipping_cost dan cari shipping_cost 
# termahal dari data penjualan tersebut menggunakan sort.
order_df.___(___={"___": "___"}, inplace=___)
sort_value = order_df.___(by="___", ascending=0)
print(sort_value)
# Untuk product_category_name, berapa  rata-rata weight produk tersebut 
# dan standar deviasi mana yang terkecil dari weight tersebut, 
mean_value = order_df["___"].___(___["___"]).___
print(mean_value.sort_values())
std_value = order_df["___"].___(___["___"]).___
print(std_value.sort_values())
# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity 
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
order_df[["___"]].___(figsize=(___, 5), bins=___)
plt.show()