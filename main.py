def swap_parent(heap,item):
    if item == 0:
        return heap

    if item < 0:
        return heap
    parent = (item-1)//2
    temp = heap[item]
    heap[item] = heap[parent]
    heap[parent] = temp

    return heap

def swap_left_child(heap,item):
    pass

def swap_right_child(heap,item):
    pass