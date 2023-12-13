#return index of element in array or -1 if element doesnt exist in the array
#Preprocessing: O(nlogn) to sort the array
#Time Complexity is O(log n)
#Space Compleixty is O(1)
def bin_search(array, element):
    low = 0
    high = len(array) - 1


    while low <=high:
        mid = (low + high) // 2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            low = mid+1
        else:
            high = mid-1
    return -1

print(bin_search([1,2,3,10,11],11))

    

