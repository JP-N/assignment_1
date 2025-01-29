# echo.py

# JP Noga
# 1.28.25
# Assignment 1

# Echo - Function to imitate a real world echo
def echo(text:str, repetitions: int = 3) -> str:

    char_list = list(text[-repetitions:])

    for i in range(len(char_list)):
        print(*char_list, sep='')
        char_list.pop(0)

if __name__ == "__main__":
     text = input("Yell something at a mountain: ")
     print(echo(text))