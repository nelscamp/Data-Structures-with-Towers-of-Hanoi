from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__front = 0
    self.__back = 0
    self.__size = 0
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    if self.__size == 0:
      return '[ ]'
    elif self.__size == 1:
      return '[ ' + str(self.__contents[self.__front]) + ' ]'
    elif self.__size > 1:
      string_to_return = ''
      current = self.__front
      while current != self.__back:
        string_to_return = string_to_return + str(self.__contents[current]) + ', '
        current = (current + 1 + self.__capacity) % self.__capacity
      final_string = string_to_return + str(self.__contents[current])
      return '[ ' + final_string + ' ]'
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    old_data = self.__contents
    self.__contents = [None] * self.__capacity * 2
    current = self.__front
    for item in range(self.__size):
      self.__contents[item] = old_data[current]
      current = (current + 1) % self.__capacity
    self.__front = 0
    self.__back = self.__size-1
    self.__capacity *= 2
 

  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size >= self.__capacity:
      self.__grow()
    self.__front = (self.__front - 1 + self.__capacity) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1

    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return None
    else:
      val = self.__contents[self.__front]
      self.__front = (self.__front + 1 + self.__capacity) % self.__capacity
      self.__size -= 1
      return val
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
      return None
    else:
      return self.__contents[self.__front]
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size >= self.__capacity:
      self.__grow()
    self.__back = (self.__back + 1 + self.__capacity) % self.__capacity
    self.__contents[self.__back] = val
    self.__size += 1
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return None
    else:
      value = self.__contents[self.__back]
      self.__back = (self.__back - 1 + self.__capacity) % self.__capacity
      self.__size -= 1
      return value

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
      return None
    else:
      return self.__contents[self.__back]

#No main section is necessary. Unit tests take its place.
# if __name__ == '__main__':
#   dog = Array_Deque()

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
