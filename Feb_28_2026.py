from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    a = []
    for key, value in age_dict.items():
        a.append(key)
    return a

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    a = []
    for key, value in age_dict.items():
        a.append(value)
    return a

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))


from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    a = {}
    for ch in (word):
        if(ch in a):
            a[ch] += 1
            continue
        a[ch] = 1
    return a
        
            






# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))


from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for key in keys:
        if key not in my_dict:
            continue
        del my_dict[key]
    return my_dict




# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))


from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    values = list(age_dict.values())
    return values

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))


def read_and_print_input() -> None:
    usr = input("Reading one line of text into a string: ")
    print(usr)
read_and_print_input()
read_and_print_input()



def read_integer() -> int:
    usr = int(input())
    return usr

def read_float() -> float:
    ust = float(input())
    return ust
# do not modify below this line
print(read_integer())
print(read_integer())
print(read_integer())

print(read_float())
print(read_float())
print(read_float())


from typing import List

def read_integers() -> List[int]:
    usr = input()
    str_list = usr.split(",")
    int_list = []
    for key in str_list:
        int_list.append(int(key))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())


def add_two_numbers() -> int:
    a = input()
    a_list = a.split(",")
    a_int_list = []
    for key in a_list:
        a_int_list.append(int(key))
    return a_int_list[0] + a_int_list[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())


def divide_numbers(a: int, b: int) -> None:
    try:
        print(a / b)
    except:
        print("An error occurred!")



# do not modify below this line
divide_numbers(10, 2)
divide_numbers(12, 3)
divide_numbers(2, 0)


def divide_numbers(a: str, b: str) -> None:
    try:
        a_new = int(a)
        b_new = int(b)
        print(a_new / b_new)
    except Exception as error:
        print("An error occurred:", error)





# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")


def divide_numbers(a: str, b: str) -> None:
    try:
        num1 = int(a)
        num2 = int(b)
        result = num1 / num2
        print(result)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")


