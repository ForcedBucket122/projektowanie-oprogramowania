using System;

class babelkowe
{
    static void Main()
    {
        
        int[] array= new int[6];
        for(int i = 0; i < 6; i++)
        {
            Console.Write("Podaj liczbe: ");
            int liczba = int.Parse(Console.ReadLine());
            array[i] = liczba;
        }
        BubbleSort(array);

        Console.WriteLine("Posortowana tablica:");
        foreach (int item in array)
        {
            Console.Write(item + " ");
        }
    }

    static void BubbleSort(int[] array)
    {
        int n = array.Length;
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (array[j] > array[j + 1])
                {
                    // Zamiana miejscami
                    Console.WriteLine(String.Join(", ", array));
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }
}

