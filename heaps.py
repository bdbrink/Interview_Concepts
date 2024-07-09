import heapq


def heap():
    # Creating a heap
    heap = []
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 7)
    heapq.heappush(heap, 1)
    
    return heap

def heap_parsing(heap):
    
    print("Heap after pushing elements:", heap)

    # Popping the smallest element
    smallest = heapq.heappop(heap)
    print("Smallest element (popped):", smallest)
    print("Heap after popping:", heap)

    # Peeking at the smallest element without removing it
    print("Smallest element (peeked):", heap[0])

    # Creating a heap from a list
    numbers = [5, 3, 7, 1, 9, 2]
    heapq.heapify(numbers)
    print("Heapified list:", numbers)

    # Getting the n smallest elements
    n_smallest = heapq.nsmallest(3, numbers)
    print("3 smallest elements:", n_smallest)

    # Getting the n largest elements
    n_largest = heapq.nlargest(2, numbers)
    print("2 largest elements:", n_largest)

heap = heap()
print(type(heap))
heap_parsing(heap)