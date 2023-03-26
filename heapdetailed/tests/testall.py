# from heapdetailed import swap_parent, swap_left_child, swap_right_child, move_up, move_down

def test_swap_parent():
    assert swap_parent([1,5,34,3],1) == [1,5,34,3]

def test_swap_left_child():
    assert swap_left_child([1,5,34,3],1) == [1,3,34,5]

def test_swap_right_child():
    assert swap_right_child([1,5,34,3,5,6,7],2) == [1,5,6,3,5,34,7]

