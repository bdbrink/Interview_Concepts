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

# Example usage
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 7
print(max_sum_subarray(arr, k))
