from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val, 0)
  
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.remove_element_at(0)

  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.get_element_at(0)

  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    self.__list.append_element(val)
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.remove_element_at(len(self.__list) - 1)

  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.get_element_at(len(self.__list) - 1)

# Unit tests make the main section unneccessary.
# if __name__ == '__main__':
#   dog = Linked_List_Deque()

#   dog.push_front(2)
#   print(dog, len(dog), 'fpush 2')

#   dog.push_front(5)
#   print(dog, len(dog), 'fpush 5')

#   dog.push_front(7)
#   print(dog, len(dog), 'fpush 7')

#   val = dog.peek_front()
#   print(val, 'fpeek 7')

#   dog.pop_front()
#   print(dog, len(dog), 'fpop 7')

#   dog.push_front(3)
#   print(dog, len(dog), 'fpush 3')

#   dog.push_front(9)
#   print(dog, len(dog), 'fpush 9')

#   val = dog.peek_back()
#   print(val, 'bpeek 2')

#   dog.pop_back()
#   print(dog, 'bpop 2')

#   dog.push_back(21)
#   print(dog, 'bpush 21')