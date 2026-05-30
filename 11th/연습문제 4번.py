def merge(A, left, mid, right):
    sorted = [0] * (right - left + 1)

    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i += 1
        else:
            sorted[k] = A[j]
            j += 1
        k += 1

    if i > mid:
        sorted[k:k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]

    A[left:right+1] = sorted