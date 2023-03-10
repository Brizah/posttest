import os
os.system ("cls")

def jumpsearch(arr, x) :

    n = len(arr)

    stop = int( n ** 0.5)
    prev = 0

    while arr [min(stop, n) -1 ] < 1:
        prev = stop
        stop += int (n ** 0.5)
        
        if prev >= n:
            return -1
        
    while arr[prev] < x:
        prev += 1

        if prev == min (stop, n):
            return prev

        return -1
    
arr =  ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
arr_sorted = sorted(arr)

index_Arsel = jumpsearch(arr_sorted, "Arsel")
index_Avivah = jumpsearch(arr_sorted, "Avivah")
index_Daiva = jumpsearch(arr_sorted, "Daiva")
index_Wahyu = jumpsearch(arr_sorted,"Wahyu")
index_Wibi = jumpsearch(arr_sorted, "Wibi")


x = input ("Masukkan Nama Data Yang Ingin Di Cari:")

result = jumpsearch(arr, x)

if result != -1:
    print (f"Elemen {x}, ditemukan di index {result}" )
else:
    print(f"Elemen {x} tidak ditemukan pada array")
