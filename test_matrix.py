from matrixclass import MyMatrix
import copy
#def test_repr():
#    m = MyMatrix([[1,2,3],[4,5,6]])
#    assert(repr(m) == " 1 2 3\n")

def test_flipped_left_right():
    m = MyMatrix([[1,2,3],[4,5,6]])
    another_m = copy.deepcopy(m)
    another_m = m.flipped_left_right()
    assert(another_m == [[3, 2, 1], [6, 5, 4]])
    assert(m.matrix == [[1, 2, 3], [4, 5, 6]])

def test_flip_left_right():
    m = MyMatrix([[1,2,3],[4,5,6]])
    m.flip_left_right()
    assert(m.matrix == [[3, 2, 1], [6, 5, 4]])

def test_transposed():
    m = MyMatrix([[1,2,3],[4,5,6]])
    another_m = copy.deepcopy(m)
    another_m = m.transposed()
    assert(another_m == [[1, 4], [2, 5], [3, 6]])
    assert(m.matrix == [[1, 2, 3], [4, 5, 6]])

def test_transpose():
    m = MyMatrix([[1,2,3],[4,5,6]])
    m.transpose()
    assert(m.matrix == [[1, 4], [2, 5], [3, 6]])

def test_size():
    m = MyMatrix([[1,2,3],[4,5,6]])
    assert(m.size() == (2,3))
    m = MyMatrix([[],[]])
    assert(m.size() == (2,0))

def test_flipped_up_down():
    m = MyMatrix([[1,2,3],[4,5,6]])
    another_m = copy.deepcopy(m)
    another_m = m.flipped_up_down()
    assert(another_m == [[4, 5, 6], [1, 2, 3]])
    assert(m.matrix == [[1, 2, 3], [4, 5, 6]])

def test_flip_up_down():
    m = MyMatrix([[1,2,3],[4,5,6]])
    m.flip_up_down()
    assert(m.matrix == [[4, 5, 6], [1, 2, 3]])

def test_repr():
    m = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(m.__repr__() == '1 2 3 \n4 5 6 ')
