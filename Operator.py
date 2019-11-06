class Operator():
    def zeros(self,_height,_width):
        row_arr = []
        arr = []

        for i in range(_width):
            row_arr.append(0)
        for i in range(_height):
            arr.append(row_arr.copy())
        
        return arr