laporan_minuman = [
    {
        'nama': 'kopi',
        'harga': '11000',
        'terjual': '10',
        'modal_satuan': 6000,
    },
    {
        'nama': 'teh_ES',
        'harga': '6000',
        'terjual': '12',
        'modal_satuan': '3500',
    },
    {
        'nama': 'jus',
        'harga': '10000',
        'terjual': '7',
        'modal_satuan': '6000',
    },
]  # tidak ada yg perlu dibuah dsn

# isi list makanan dan untuk nama, harga, terjual, modal satuan bebas tetapi diinput melalui terminal (cukup 2 makanan)
laporan_makanan = []  # format makanan samad dengan minuman
"""
format makanan
{
        'nama': '',
        'harga': '',
        'terjual': '',
        'modal_satuan': ,
}
"""
total_semua_penjualan = 0
total_semua_keuntungan_penjualan = 0
special_value = 0
penjualan = {
    'minuman': laporan_minuman,
    'makanan': laporan_makanan,
    'summary': {
        'total_penjualan': {
            'makanan': '',
            'minuman': '',
            'semua': ''
        },
        'keuntungan_penjualan': {
            'makanan': '',
            'minuman': '',
            'semua': '',
        },
        # juga tidak ada yg perlu diubah dsn
        'special_case': total_semua_penjualan+total_semua_keuntungan_penjualan+special_value+10000
    }
}

# lakukan programn didalam fungsi ini


def main():

    global laporan_minuman, laporan_makanan, total_semua_penjualan, total_semua_keuntungan_penjualan, penjualan, special_value
    special_value = 2003
    print("Semangat Upgrading, Machine Learning Semangat")
    laporan_makanan_dict = dict()
    for i in range(2):
        nama_makanan = input("Masukkan nama makanan : ")
        harga_makanan = int(input("Harga makanan : "))
        jumlah_makanan = int(input("Jumlah makanan : "))
        modal_makanan = int(input("Modal makanan : "))
        laporan_makanan_dict = {'nama': nama_makanan, 'harga': harga_makanan,
                                'terjual': jumlah_makanan, 'modal_satuan': modal_makanan}
        laporan_makanan.append(laporan_makanan_dict)

    penjualan['summary']['total_penjualan']['makanan'] = penjualan['makanan'][0]['terjual'] + \
        penjualan['makanan'][1]['terjual']
    print("Penjualan makanan")
    print(penjualan['summary']['total_penjualan']['makanan'])
    penjualan['summary']['total_penjualan']['minuman'] = int(penjualan['minuman'][0]['terjual']) + \
        int(penjualan['minuman'][1]['terjual']) + \
        int(penjualan['minuman'][2]['terjual'])
    print("Penjualan minuman")
    print(penjualan['summary']['total_penjualan']['minuman'])
    penjualan['summary']['total_penjualan']['semua'] = int(penjualan['summary']['total_penjualan']['makanan']) +\
        int(penjualan['summary']['total_penjualan']['minuman'])
    print("Penjualan total")
    print(penjualan['summary']['total_penjualan']['semua'])

    penjualan['summary']['keuntungan_penjualan']['makanan'] = (penjualan['makanan'][0]['terjual']*(penjualan['makanan'][0]['harga']-penjualan['makanan'][0]['modal_satuan'])) + \
        (penjualan['makanan'][1]['terjual']*(penjualan['makanan'][1]
                                             ['harga']-penjualan['makanan'][1]['modal_satuan']))
    print("Keuntungan Makanan")
    print(penjualan['summary']['keuntungan_penjualan']['makanan'])
    penjualan['summary']['keuntungan_penjualan']['minuman'] = int(penjualan['minuman'][0]['terjual'])*(int(penjualan['minuman'][0]['harga']) - int(penjualan['minuman'][0]['modal_satuan'])) + \
        int(penjualan['minuman'][1]['terjual'])*(int(penjualan['minuman'][1]
                                                     ['harga'])-int(penjualan['minuman'][1]['modal_satuan'])) + int(penjualan['minuman'][2]['terjual'])*(int(penjualan['minuman'][2]
                                                                                                                                                             ['harga'])-int(penjualan['minuman'][2]['modal_satuan']))
    print("Keuntungan Minuman")
    print(penjualan['summary']['keuntungan_penjualan']['minuman'])

    penjualan['summary']['keuntungan_penjualan']['semua'] = int(penjualan['summary']['keuntungan_penjualan']['makanan']) + \
        int(penjualan['summary']['keuntungan_penjualan']['minuman'])
    print('laporan_makanan')
    print(penjualan['makanan'])
    print('laporan_minuman')
    print(penjualan['minuman'])
    # juga tidak ada yg perlu diubah dsn
    print("total_semua_penjualan")
    total_semua_penjualan = penjualan['summary']['total_penjualan']['semua']
    print(total_semua_penjualan)
    # juga tidak ada yg perlu diubah dsn
    print("total_semua_keuntungan_penjualan")
    total_semua_keuntungan_penjualan = penjualan['summary']['keuntungan_penjualan']['semua']
    print(total_semua_keuntungan_penjualan)
    # perlu sedikit penambahan
    penjualan.update({"summary": {"special_case": total_semua_penjualan +
                                  total_semua_keuntungan_penjualan+special_value+10000}})
    special_case = penjualan['summary']['special_case']
    print("Special Case")
    print(special_case)


if __name__ == "__main__":
    main()
