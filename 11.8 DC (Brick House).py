if __name__ == '__main__':
    n = int(input())
    largelength = 5
    for _ in range(n):
        small, large, length = [int(i) for i in input().split()]
        exact = False
        if largelength < length:
            for g in range(large+1):
                if g * largelength == length:
                    exact = True
                    break
                elif g * largelength != length:
                    for p in range(small+1):
                        if (g * largelength) + p == length:
                            exact = True 
                            break
                else:
                    exact = False
        else:
            for g in range(small+1):
                if g == length:
                    exact = True
                    break
                else:
                    exact = False
        if exact == False:
            print("false")
        else:
            print("true")       
