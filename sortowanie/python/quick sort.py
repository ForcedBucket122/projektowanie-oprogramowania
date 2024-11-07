tablica = [8,2,1,9,5]
print(tablica)

def podziel(tab, start, end):
    pivot= tab[end]
    low = start
    high = end -1

    while True:
        while low <= high and tab[low]<=pivot:
            low+=1
        
        while low <= high and tab[high]>=pivot:
            high-=1

        if low <=high:
            tab[low],tab[high] = tab[high],tab[low]
        else:
            break
    
    tab[end], tab[low] = tab[low], tab[end]
    return low

def sort(tab, start, end):
    if start<end:
        pivot = podziel(tab, start, end)
        sort(tab,start,pivot-1)
        sort(tab,pivot+1,end)
        print(tab)

sort(tablica, 0, len(tablica)-1)
print(tablica)