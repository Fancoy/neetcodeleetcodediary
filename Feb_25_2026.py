from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    num = len(my_list)
    return my_list[num-3:num]


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))


from typing import Tuple # this is to add type hints for tuples

def create_pair(name: str, age: int) -> Tuple[str, int]:
    ey = (name, age)
    return ey

# do not modify code below this line
print(create_pair("Alice", 25))
print(create_pair("Bob", 30))
print(create_pair("Charlie", 35))


from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    ane = set()
    for i in range (len(nums)):
        ane.add(nums[i])
    return ane


# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))


from typing import List

def count_unique_words(words: List[str]) -> int:
    setWords = set(words)
    return len(setWords)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))


from typing import List

def contains_duplicate(words: List[str]) -> bool:
    wordsSet = set(words)
    if(len(wordsSet) == len(words)):
        return False
    return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))


from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    a = {name: age}
    return a


def list_to_dict(words: List[str]) -> Dict[str, int]:
    a = {}
    for i in range (len(words)):
        a[words[i]] = i
    return a




# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))


your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}
print(your_dict)
print(your_dict["a"])
print('d' in your_dict)
your_dict["a"] = 4
print(your_dict)
