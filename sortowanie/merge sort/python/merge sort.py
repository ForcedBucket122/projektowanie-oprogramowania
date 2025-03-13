tab = [8, 2, 1, 9, 5]
print(tab)


def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        R = tab[mid:]
        print("L: ", L);
        print("R: ", R)
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1

        print("_PO: ", tab)


mergeSort(tab)
print(tab)