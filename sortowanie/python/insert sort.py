def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(arr)
        key = arr[i]
        j = i - 1
        # Przesuwamy elementy większe od key o jedno miejsce w prawo
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        

# Przykład użycia
lista = [5, 2, 9, 1, 5, 6]
insertion_sort(lista)
print(lista)
