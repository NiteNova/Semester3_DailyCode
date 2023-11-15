# https://lmcodequestacademy.com/problem/factorial
if __name__ == '__main__':
    cases = int(input())

    def factorial(num):
        return_value = 1
        for i in range(num):
            return_value = return_value * (i+1)
        return return_value
    
    for _ in range(cases):
        user_input = int(input())
        print(factorial(user_input))

# https://lmcodequestacademy.com/problem/caught-speeding
if __name__ == '__main__':
    cases = int(input())
    
    for _ in range(cases):
        driver = input()
        stuff = driver.split(" ")
        if stuff[1] == "true":
            bday = True
        else:
            bday = False
        if bday == True:
            speed_reduction = 5
        else:
            speed_reduction = 0
        speed = int(stuff[0])

        if speed <= (60+speed_reduction):
            print("no ticket")
        elif speed >= (61+speed_reduction) and speed <= (80+speed_reduction):
            print("small ticket")
        elif speed >= (81+speed_reduction):
            print("big ticket")
