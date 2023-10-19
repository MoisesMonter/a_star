from asyncio import run
from decouple import config
from table import in_Table
# from a_star import Node
text = ["selecione um valor: ","Valor menor ou igual a 0, novamente","valor não numérico, novamente"]





class new_table:
    def __init__(self,table = None,start = None,end = None):
        self.table = table
        self.start = start
        self.end = end

class Main():
    
    def __init__(self,info):
        self.info = info

    def mapping(self):
        if info == None:
            self.info = new_table()


    def main(self,info = None):
        if info == None:
            info = new_table()

        aux = int(input("Informações:\nLer um texto(0)\nCriar tabela(1)\nsair(-1):\n"))
        if aux < 0:
            return -1
        elif aux == 0:
            self.info.table = in_Table({}).read_map() 
            print(self.info.table)
            self.printing()
        else:
            info.table = self.run()




    def run(self,x = None, y = None):
        print("\nDgite a quantidade de linhas(Ex: 10)")
        while x is not int: 
            try:    
                x = int(input(text[0]))
                if int(x) > 0:
                    break
                else:
                    print(text[1],end=' ')
            except:
                print(text[2],end=' ')

        print("Dgite a quantidade de linhas(Ex: 10)\n")
        while y is not int: 
            try:    
                y = int(input(text[0]))
                if int(y) > 0:
                    break
                else:
                    print(text[1],end=' ')
            except:
                print(text[2],end=' ')
        self.info.table = in_Table().created_map(x,y)
        self.printing()
        self.block()

    def printing(self):
        max_x = max(coord[0] for coord in self.info.table) + 1
        max_y = max(coord[1] for coord in self.info.table) + 1
        print(max_x,max_y)

        matrix = [[' ' for _ in range(max_x)] for _ in range(max_y)]
        
        
        for coord, value in self.info.table.items():
            x, y = coord
            matrix[y][x] = value

        print(matrix)
        for row in matrix:
            print(' '.join(row))
            
    def block(self,x = None,y = None):
        print("Digite local da parede (-1 para encerrar)\n")
        x,y = int(input("x:")),int(input("y: "))
        if x >=0 or y >=0:
            self.info.table = in_Table(self.info.table).create_block(x,y)
            self.printing()
            self.block()
    
    def start(self):
        pass

    def end(self):
        pass
if __name__ == "__main__":
    info = new_table()
    Main(info).main()