from matrixclass import MyMatrix
import copy

def test_flipped_left_right():
    m = MyMatrix([[1, 2, 3],[4, 5, 6]])
    another_m = copy.deepcopy(m)
    another_m = m.flipped_left_right()
    assert(another_m == [[3, 2, 1], [6, 5, 4]])
    assert(m.matrix == [[1, 2, 3], [4, 5, 6]])

def test_flip_left_right():
    m_lr = MyMatrix([[1, 2, 3],[4, 5, 6]])
    m_lr.flip_left_right()
    assert(m_lr.matrix == [[3, 2, 1], [6, 5, 4]])

def test_transposed():
    m_tr = MyMatrix([[1, 2, 3],[4, 5, 6]])
    another_m_tr = copy.deepcopy(m_tr)
    another_m_tr = m_tr.transposed()
    assert(another_m_tr == [[1, 4], [2, 5], [3, 6]])
    assert(m_tr.matrix == [[1, 2, 3], [4, 5, 6]])

def test_transpose():
    m_tre = MyMatrix([[1, 2, 3],[4, 5, 6]])
    m_tre.transpose()
    assert(m_tre.matrix == [[1, 4], [2, 5], [3, 6]])

def test_size():
    m_si = MyMatrix([[1, 2, 3],[4, 5, 6]])
    assert(m_si.size() == (2, 3))
    m_si1 = MyMatrix([[],[]])
    assert(m_si1.size() == (2, 0))
    m_si2 = MyMatrix([])
    assert(m_si2.size() == (0, 0))
    m_si3 = MyMatrix([[]])
    assert(m_si3.size() == (1, 0))
    m_si4 = MyMatrix([[1, 2, 3]])
    assert(m_si4.size() == (1, 3))

def test_flipped_up_down():
    m_ed_ud = MyMatrix([[1, 2, 3],[4, 5, 6]])
    another_m_ed_ud = copy.deepcopy(m_ed_ud)
    another_m_ed_ud = m_ed_ud.flipped_up_down()
    assert(another_m_ed_ud == [[4, 5, 6], [1, 2, 3]])
    assert(m_ed_ud.matrix == [[1, 2, 3], [4, 5, 6]])

def test_flip_up_down():
    m_ud = MyMatrix([[1, 2, 3],[4, 5, 6]])
    m_ud.flip_up_down()
    assert(m_ud.matrix == [[4, 5, 6], [1, 2, 3]])

def test_repr():
    m = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(m.__repr__() == '1 2 3 \n4 5 6 ')
    m_1 = MyMatrix([[]])
    assert((m_1.__repr__() == 'Matrix is empty'))
    m_2 = MyMatrix([])
    assert((m_2.__repr__() == 'Matrix is empty'))
