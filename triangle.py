from typing import Union

class Triangle:
    def __init__(self, l1: Union[int, float], 
                 l2: Union[int, float], 
                 l3: Union[int, float]):
                
        self.l1:  Union[int, float] = l1
        self.l2:  Union[int, float] = l2
        self.l3:  Union[int, float] = l3

        self._all_sides: list[float] = [self.l1, self.l2, self.l3]

        # Checks if all the params are int or float. If not, assert raises Exception.
        #----------------------------------------------------------------------------
        correct_params: bool = all([isinstance(param, (float, int)) 
                                    for param 
                                    in self._all_sides])

        assert correct_params, "Parameters must be integer or float!"
        
        # Checks if all the params are bigger than 0. If not, assert raises Exception.
        #----------------------------------------------------------------------------
        positive_params: list[Union[int, float]] = [num 
                                                    for num 
                                                    in self._all_sides 
                                                    if num > 0]
        
        assert len(self._all_sides) == len(positive_params), "Params must be bigger than 0." 

        
    def describe(self) -> str:
        '''
        Compares all sides of the triangle, then correspondingly to the value 
        returns what kind of triangle is the object.
        '''

        _largest_side:  float = max(self._all_sides)
        _total:         float = self.l1 + self.l2 + self.l3
        
        is_triangle:    bool = _largest_side < _total
        is_equilateral: bool = (self.l1 == self.l2) and (self.l2 == self.l3)
        is_isosceles:   bool = ((self.l1 == self.l2)
                               or (self.l2 == self.l3)
                               or (self.l1 == self.l3))

        triangle_type: str

        if not is_triangle:
            triangle_type = "It's not a triangle." 

        elif is_equilateral:
            triangle_type = "It's a equilateral triangle."
        
        elif is_isosceles:
            triangle_type = "It's a isosceles triangle."
        
        else:
            triangle_type = "It's a scalene triangle."

        return triangle_type


    def __str__(self) -> str:
        "Upon calling a Triangle object -> Prints out sides."

        return f"L1:{self.l1}\nL2:{self.l2}\nL3:{self.l3}"


if __name__ == '__main__':

    print("Welcome to Bermuda!\n")
    print("Give me lengths of 3 sides and I give you a triangle.\n")
    
    while True:

        try:
            first_side:  float = float(input("Enter the value of first side: \n"))
            second_side: float = float(input("Enter the value of second side: \n"))
            third_side:  float = float(input("Enter the value of third side: \n"))

            queried_triangle: Triangle = Triangle(first_side, second_side, third_side)

            print("The sides are: \n")
            print(queried_triangle)
            print("\n")
            print(queried_triangle.describe())

            break

        except (ValueError, NameError):
            print("""\nERROR:
    The value of a side must be decimal or fraction!
    Not permited:
    - symbols
    - letters\n""")



    
