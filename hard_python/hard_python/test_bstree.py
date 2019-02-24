import pytest
from .bstree import BSTree

@pytest.fixture
def tree_balanced():
    tree = BSTree()
    tree.set(5, 'five')
    tree.set(3, 'three')
    tree.set(7, 'seven')
    tree.set(4, 'four')
    tree.set(2, 'two')
    tree.set(6, 'six')
    tree.set(8, 'eight')
    tree.set(1, 'one')
    tree.set(9, 'nine')
    tree.set(0, 'nothing')
    tree.set(0, 'zero')
    return tree

def test_set(tree_balanced):
    assert tree_balanced._count == 10

def test_get(tree_balanced):
    assert tree_balanced.get(5) == 'five'
    assert tree_balanced.get(7) == 'seven'
    assert tree_balanced.get(3) == 'three'
    assert tree_balanced.get(4) == 'four'
    assert tree_balanced.get(0) == 'zero'

def test_remove(tree_balanced):
    tree_balanced.remove(0)
    assert tree_balanced._count == 9
    tree_balanced.remove(2)
    assert tree_balanced._count == 8
    tree_balanced.remove(8)
    assert tree_balanced._count == 7
    tree_balanced.remove(7)
    assert tree_balanced._count == 6
    tree_balanced.remove(5)
    assert tree_balanced._count == 5


    assert tree_balanced.root.key == 6
    assert tree_balanced.get(5) == None
    assert tree_balanced.get(7) == None
    assert tree_balanced.get(3) == 'three'
    assert tree_balanced.get(4) == 'four'
    assert tree_balanced.get(1) == 'one'
    assert tree_balanced.get(9) == 'nine'


