nama = ["celio","shandy","farel","ghazali","vito","yuyun","adri"]

nama = ["celio",
        "shandy",
        "farel",
        "ghazali",
        "vito",
        "yuyun",
        "adri",
        "rizal",
        "adi",
        "ibnu"
]

print("sebelum: ")
print(nama)
print("")
print("sesudah:")

nama.insert(2,"afrizal")
print(nama)
nama[4]= "fufufafa"
print(nama)
del nama[2]
print(nama)
hapus = nama.pop(2)
print(nama)
print(hapus)


print(nama[0:2])
print(nama[1:9:1])

matkul = ["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]

data = nama+matkul

print("sebelum: ")
print(nama)
print("")
print("sesudah:")
print(data)

data = ["farel","celio"[1,2,["halo",23,2.3,True]]]
        
print(data[2][2][::-1])

print(data[::-1])

matkul = [1,2,3,4,[5,6,7,[2,3,4]]]
print(matkul[4])
print(matkul[4][1])
print(matkul[4][3][::-1])

matkul = [1,2,3,4]
for i in matkul:
    print(i)