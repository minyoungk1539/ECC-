def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)

        merge(A, left, mid, right)

def merge(A, left, mid, right):
    sorted_arr = []

    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted_arr.append(A[i])
            i += 1
        else:
            sorted_arr.append(A[j])
            j += 1

    while i <= mid:
        sorted_arr.append(A[i])
        i += 1

    while j <= right:
        sorted_arr.append(A[j])
        j += 1

    for k in range(len(sorted_arr)):
        A[left + k] = sorted_arr[k]