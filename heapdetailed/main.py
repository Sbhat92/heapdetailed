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
    if item == len(heap):
        return heap
    if item < 0:
        return heap
    left_child = 2*item + 1
    temp = heap[item]
    heap[item] = heap[left_child]
    heap[left_child] = temp
    return heap
    

def swap_right_child(heap,item):
    if item == len(heap):
        return heap
    if item < 0:
        return heap
    left_child = 2*item + 2
    temp = heap[item]
    heap[item] = heap[left_child]
    heap[left_child] = temp
    return heap

def move_up(heap, startpos, pos):
    newitem = heap[pos]    
    while pos > startpos:
        parent = (pos - 1) // 2
        parent_value = heap[parent]
        if newitem < parent_value:
            swap_parent(heap,pos)
            continue
        break
    return heap
    

def move_down(heap, pos):
    endpos = len(heap)
    startpos = pos   

    if startpos >= endpos:
        return heap
    
    left_child = 2*startpos+1
    right_child = left_child + 1
    if left_child<endpos:
        if heap[left_child] < heap[right_child] and heap[startpos]> heap[left_child]:
            swap_left_child(startpos)
            move_down(heap,left_child)
            
    if right_child < endpos:    
        if heap[left_child] > heap[right_child] and heap[startpos]> heap[right_child]:
            swap_right_child(startpos)
            move_down(heap,right_child)
    

    
    
    