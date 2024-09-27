using System;

class QuickSort
{
    public static void Sort(int[] array, int left, int right)
    {
        if (left < right)
        {
            int pivot = Partition(array, left, right);

            if (pivot > 1)
                Sort(array, left, pivot - 1);

            if (pivot + 1 < right)
                Sort(array, pivot + 1, right);
        }
    }

    private static int Partition(int[] array, int left, int right)
    {
        int pivot = array[left];
        while (true)
        {
            while (array[left] < pivot)
                left++;

            while (array[right] > pivot)
                right--;

            if (left < right)
            {
                if (array[left] == array[right]) return right;

                int temp = array[left];
                array[left] = array[right];
                array[right] = temp;
            }
            else
            {
                return right;
            }
        }
    }

    static void Main(string[] args)
    {
        int[] array = { 29, 10, 14, 37, 13 };
        Sort(array, 0, array.Length - 1);

        Console.WriteLine("Posortowana tablica:");
        foreach (int item in array)
        {
            Console.Write(item + " ");
        }
    }
}
