if __name__ == '__main__':
    n = int(input()) 
    init_list = []
    for i in range(n):
        sep = []
        commands = input()
        if commands.find("insert") != -1:
            sep = commands.split(" ")
            pos = int(sep[1])
            num = int(sep[2])
            init_list.insert(pos, num)
        elif commands.find("print") != -1:
            print(init_list)
        elif commands.find("remove") != -1:
            sep = commands.split(" ")
            num = int(sep[1])
            init_list.remove(num)
                    

            
