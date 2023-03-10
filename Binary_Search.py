def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif isinstance(arr[mid], list):
            result = binary_search(arr[mid], 0, len(arr[mid])-1, x)
            if result != -1:
                return [mid, result]
            else:
                return binary_search(arr, mid+1, high, x)
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
x = input("Masukkan data yang ingin dicari: ")

result = binary_search(arr, 0, len(arr)-1, x)

if isinstance(result, list):
    print(x, "ditemukan pada indeks", str(result[0]), "kolom", str(result[1]))
elif result != -1:
    print(x, "ditemukan pada indeks", str(result))
else:
    print(x, "tidak ditemukan dalam list")
