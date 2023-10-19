from re import sub
from decouple import config

Way = config("Way", cast=bool) if config("Way") == "True" else config("Way")
Wall = config("Wall",cast=bool) if config("Wall") == "False" else config("Wall")

class in_Table:
    def __init__(self,table = {},x= None, y= None ) -> None:
        self.__table = table

    def read_map(self, text_info=None):
        info = None
        with open("text.txt") as table:
            old_info = table.readlines()
            new_info = [self.filtered(info) for info in old_info]
            
            x, y = self.len_map(new_info)
            self.created_map(x, y,True, new_info)
            
        return self.__table

    def len_map(self, info):
        linha = len(info[0])
        coluna = len(info)
        return linha, coluna

    def filtered(self, listed):
        information = sub(r'\n', ',', listed)
        new_information = sub(r'\s', '', information)
        end = new_information.split(',')
        return [int(item) for item in end if item]

    def created_map(self, end_x=10, end_y=10,cm = False, info=None, x=0, y=0):
        if x < end_x and y < end_y:
            if cm == True:
                if info[y][x] == 0:
                    self.__table[(x, y)] = Way
                else:
                    self.__table[(x, y)] = Wall
            else:
                self.__table[(x, y)] = Way
            self.created_map(end_x, end_y,cm, info, x + 1, y) if x + 1 < end_x else self.created_map(end_x, end_y,cm, info, 0, y + 1)
        return self.__table

    def create_block(self,x = None,y = None):
        if x == None or y == None:
            return self.__table
        else:
            self.__table[(x,y)] = Wall
            
            return self.__table


    def main(self):
        self.created_map()
        x = self.filtered('1,2,3,4\n,5,6,7,8,9')
        
        self.read_map(x)

# if __name__ == "__main__":
#     in_Table({}).read_map() 