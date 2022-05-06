from typing import Union
import pytest
import triangle as t

@pytest.mark.parametrize(
   ('param_1', 'param_2', 'param_3','expected'),
   (
        pytest.param(3, 3, 3, "It's a equilateral triangle.", id='equilateral_case' ),
        pytest.param(1, 3, 3, "It's a isosceles triangle.", id='isosceles_case' ),
        pytest.param(1, 2, 3, "It's a scalene triangle.", id='scalene_case' )
   ),
)
def test_triangle_describe(param_1: Union[int, float],
                param_2: Union[int, float],
                param_3: Union[int, float],
                expected: str):
    assert t.Triangle(param_1, param_2, param_3).describe() == expected


@pytest.mark.parametrize(
    ('param_1', 'param_2', 'param_3'),
    (
        pytest.param(-3, 3, 3, id='negative_case'),
        pytest.param('i', '=', '$', id='non-numeric_case'),
    ),
)
def test_non_num_exceptions(param_1, param_2, param_3):
    
    with pytest.raises(Exception):
        t.Triangle(param_1, param_2, param_3)


def test_num_params_exceptions():
    
    with pytest.raises(TypeError):
        t.Triangle(1, 2)

    with pytest.raises(TypeError):
        t.Triangle(1, 2, 3, 4)
