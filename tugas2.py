# Arguments

def myname(fname):
    print(fname + " Refsnes")


# Pass by Reference
def add_list(dlist, aplist):
    dlist.append(aplist)


# Arbitary

def teman(*teman):
    print("Teman -1 " + teman[0])
    print("Teman -2 " + teman[1])
    print("Teman terakhir " + teman[-1])


# Keyword

def teman2(t1="jon", t2="puan", t3="rocky"):
    print("Teman Terakhir : " + t3)


# Lambda


def absurd(a, b): return (a*b)


def main():
    nama = input("Nama Anda :")
    myname(nama)
    default_list = [1, 2, 3, 4, 5]
    print("Berikut List yang sudah ada : " + str(default_list))
    list2 = int(input("Tambahkan List : "))
    add_list(default_list, list2)
    print("List sekarang : " + str(default_list))
    teman_in = str(input("Masukkan nama teman Anda: "))
    teman(teman_in, "joko", "widowo", "prabowi")
    print("teman yang lain")
    teman2()
    perkalian_absurd = absurd(len(teman_in), len(nama))
    print("Panjang karakter nama depan * nama teman : " + str(perkalian_absurd))


if __name__ == "__main__":
    main()
