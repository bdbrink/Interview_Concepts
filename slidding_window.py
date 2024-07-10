def max_sum_subarray(arr, k):
    n = len(arr)
    print(n)
    if n < k:
        return None
    
    # Compute sum of first window
    window_sum = sum(arr[:k])
    print(window_sum)
    max_sum = window_sum
    
    # Slide the window and update max_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 7
print(f"calculating the max sumb of the subarray up to {k}")
print(max_sum_subarray(arr, k))

def smallest_subarray_with_sum(arr, target_sum):
    n = len(arr)
    window_sum = 0
    start = 0
    min_length = float('inf')

    for end in range(n):
        window_sum += arr[end]
        
        while window_sum >= target_sum:
            min_length = min(min_length, end - start + 1)
            window_sum -= arr[start]
            start += 1
    
    return min_length if min_length != float('inf') else 0

arr = [4, 2, 2, 7, 8, 1, 2, 8, 10]
target_sum = 8
print(smallest_subarray_with_sum(arr, target_sum))