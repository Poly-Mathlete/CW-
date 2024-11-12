from game2048.grid_2048 import create_grid
import pytest 


def test_create_grid():
    assert create_grid() == [[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]

