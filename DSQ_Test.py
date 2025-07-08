import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

  #QUEUE TEST
  def test_queue_empty_str(self):
    self.assertEqual('[ ]', str(self.__queue), 'Empty queue should print as "[ ]"')

  def test_queue_length_empty(self):
    self.assertEqual('0', str(len(self.__queue)), 'Empty queue length should print "0"')

  def test_queue_peek_empty(self):
    self.assertEqual('None', str(self.__queue.peek()), 'Empty queue should print "None" when peeking')

  def test_queue_dequeue_empty(self):
    self.assertEqual('None', str(self.__queue.dequeue()), 'Empty queue should print "None" when dequeued')

  def test_enqueue_empty_queue(self):
    self.__queue.enqueue(0)
    self.assertEqual('[ 0 ]', str(self.__queue), 'Queue should return "[ 0 ]"')

  def test_peek_queue_with_one_item(self):
    self.__queue.enqueue(0)
    self.assertEqual('0', str(self.__queue.peek()), 'Peek should return "0"')

  def test_enqueue_queue_with_one_item(self):
    self.__queue.enqueue(0)
    self.__queue.enqueue(1)
    self.assertEqual('[ 0, 1 ]', str(self.__queue), 'Queue should return "[ 0, 1 ]"')

  def test_peek_queue_with_two_items(self):
    self.__queue.enqueue(0)
    self.__queue.enqueue(1)
    self.assertEqual('0', str(self.__queue.peek()), 'Peek should return "0"')

  def test_enqueue_queue_with_two_items(self):
    self.__queue.enqueue(0)
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual('[ 0, 1, 2 ]', str(self.__queue), 'Queue should return "[ 0, 1, 2 ]"')

  def test_peek_queue_with_three_items(self):
    self.__queue.enqueue(0)
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.assertEqual('0', str(self.__queue.peek()), 'Peek should return "0"')

  def test_dequeue_queue_with_three_items(self):
    self.__queue.enqueue(0)
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.assertEqual('[ 1, 2 ]', str(self.__queue), 'Queue should return "[ 1, 2 ]"')

  def test_peek_queue_after_dequeue_queue_with_3_items(self):
    self.__queue.enqueue(0)
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.assertEqual('1', str(self.__queue.peek()), 'Peek should return "1"')

  def test_dequeue_queue_with_two_item(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.assertEqual('[ 2 ]', str(self.__queue), 'Queue should return "[ 2 ]"')

  def test_peek_queue_after_dequeue_queue_with_2_items(self):
    self.__queue.enqueue(0)
    self.__queue.enqueue(1)
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('2', str(self.__queue.peek()), 'Peek should return "2"')

  def test_dequeue_queue_one_item(self):
    self.__queue.enqueue(2)
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue), 'Queue should return [ ]')

  def test_dequeue_empty_queue(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue), 'Queue should return [ ]')

  def test_peek_empty_queue(self):
    self.assertEqual('None', str(self.__queue.peek()), 'Peek should return "None"')

  def test_length_1_item(self):
    self.__queue.enqueue(1)
    self.assertEqual('1', str(len(self.__queue)), 'Length should be 1')

  def test_length_2_item(self):
    self.__queue.enqueue(1)
    self.__queue.enqueue(1)
    self.assertEqual('2', str(len(self.__queue)), 'Length should be 2')

################

  #STACK TEST
  def test_stack_empty_str(self):
    self.assertEqual('[ ]', str(self.__stack), 'Empty stack should print as "[ ]"')

  def test_stack_length_empty(self):
    self.assertEqual('0', str(len(self.__stack)), 'Empty stack length should print "0"')

  def test_stack_peek_empty(self):
    self.assertEqual('None', str(self.__stack.peek()), 'Empty stack should print "None" when peeking')

  def test_stack_pop_empty(self):
    self.assertEqual('None', str(self.__stack.pop()), 'Empty stack should print "None" when dequeued')

  def test_push_empty_stack(self):
    self.__stack.push(0)
    self.assertEqual('[ 0 ]', str(self.__stack), 'Stack should return "[ 0 ]"')

  def test_peek_stack_with_one_item(self):
    self.__stack.push(0)
    self.assertEqual('0', str(self.__stack.peek()), 'Peek should return "0"')

  def test_push_stack_with_one_item(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.assertEqual('[ 1, 0 ]', str(self.__stack), 'Stack should return "[ 1, 0 ]"')

  def test_peek_stack_with_two_items(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.assertEqual('1', str(self.__stack.peek()), 'Peek should return "1"')

  def test_push_stack_with_two_items(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual('[ 2, 1, 0 ]', str(self.__stack), 'Stack should return "[ 2, 1, 0 ]"')

  def test_peek_stack_with_three_items(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.__stack.push(2)
    self.assertEqual('2', str(self.__stack.peek()), 'Peek should return "2"')

  def test_pop_stack_with_three_items(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.assertEqual('[ 1, 0 ]', str(self.__stack), 'Stack should return "[ 1, 0 ]"')

  def test_peek_stack_after_popping_stack_with_3_items(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.assertEqual('1', str(self.__stack.peek()), 'Peek should return "1"')

  def test_stack_after_popping_2_items(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ 0 ]', str(self.__stack), 'Stack should return "[ 0 ]"')

  def test_peek_stack_after_popping_with_2_items(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('0', str(self.__stack.peek()), 'Peek should return "0"')

  def test_pop_stack_so_its_empty(self):
    self.__stack.push(0)
    self.__stack.push(1)
    self.__stack.push(2)
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack), 'Stack should return "[ ]"')

  def test_pop_empty_stack(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack), 'Stack should return "[ ]"')

  def test_peek_empty_stack(self):
    self.assertEqual('None', str(self.__stack.peek()), 'Peek should return "None"')

  def test_length_1_item(self):
    self.__stack.push(1)
    self.assertEqual('1', str(len(self.__stack)), 'Length should be 1')

  def test_length_2_item(self):
    self.__stack.push(1)
    self.__stack.push(1)
    self.assertEqual('2', str(len(self.__stack)), 'Length should be 2')


  ### DEQUE TESTS
  def test_deque_empty_str(self):
    self.assertEqual('[ ]', str(self.__deque), 'Deque should return "[ ]"')

  def test_deque_empty_len(self):
    self.assertEqual('0', str(len(self.__deque)), 'Length should return "0"')

  def test_deque_peek_front_empty(self):
    self.assertEqual('None', str(self.__deque.peek_front()), 'Peek should return "None"')

  def test_deque_peek_back_empty(self):
    self.assertEqual('None', str(self.__deque.peek_back()), 'Peek should return "None"')

  def test_deque_push_front_1_item_onto_empty(self):
    self.__deque.push_front(0)
    self.assertEqual('[ 0 ]', str(self.__deque), 'Deque should return "[ 0 ]"')

  def test_deque_push_back_1_item_onto_empty(self):
    self.__deque.push_back(0)
    self.assertEqual('[ 0 ]', str(self.__deque), 'Deque should return "[ 0 ]"')

  def test_deque_peek_front_1_item(self):
    self.__deque.push_front(0)
    self.assertEqual('0', str(self.__deque.peek_front()), 'Peek should return "0"')

  def test_deque_peek_back_1_item(self):
    self.__deque.push_front(0)
    self.assertEqual('0', str(self.__deque.peek_back()), 'Peek should return "0"')

  def test_deque_push_front_2_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.assertEqual('[ 1, 0 ]', str(self.__deque), 'Deque should return "[ 1, 0 ]"')

  def test_deque_peek_front_2_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.assertEqual('1', str(self.__deque.peek_front()), 'Deque should return "1"')

  def test_deque_peek_back_2_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.assertEqual('0', str(self.__deque.peek_back()), 'Deque should return "0"')

  def test_deque_push_back_2_items(self):
    self.__deque.push_back(0)
    self.__deque.push_back(1)
    self.assertEqual('[ 0, 1 ]', str(self.__deque), 'Deque should return "[ 0, 1 ]"')

  def test_deque_pop_front_of_2_items(self):
    self.__deque.push_front(0)
    self.__deque.push_back(1)
    self.__deque.pop_front()
    self.assertEqual('[ 1 ]', str(self.__deque), 'Deque should return "[ 1 ]"')

  def test_deque_pop_back_of_2_items(self):
    self.__deque.push_front(0)
    self.__deque.push_back(1)
    self.__deque.pop_back()
    self.assertEqual('[ 0 ]', str(self.__deque), 'Deque should return "[ 0 ]"')

  def test_deque_push_front_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('[ 2, 1, 0 ]', str(self.__deque), 'Deque should return "[ 2, 1, 0 ]"')

  def test_deque_push_back_3_items(self):
    self.__deque.push_back(0)
    self.__deque.push_back(1)
    self.__deque.push_back(2)
    self.assertEqual('[ 0, 1, 2 ]', str(self.__deque), 'Deque should return "[ 2, 1, 0 ]"')

  def test_deque_pop_front_once_with_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_front()
    self.assertEqual('[ 1, 0 ]', str(self.__deque), 'Deque should return "[ 1, 0 ]"')

  def test_deque_pop_back_once_with_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_back()
    self.assertEqual('[ 2, 1 ]', str(self.__deque), 'Deque should return "[ 2, 1 ]"')

  def test_deque_pop_front_twice_with_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('[ 0 ]', str(self.__deque), 'Deque should return "[ 0 ]"')

  def test_deque_pop_back_twice_with_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.assertEqual('[ 2 ]', str(self.__deque), 'Deque should return "[ 2 ]"')

  def test_deque_pop_front_3_times_with_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque), 'Deque should return "[ ]"')

  def test_deque_pop_back_3_times_with_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque), 'Deque should return "[ ]"')

  def test_deque_peek_front_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('2', str(self.__deque.peek_front()), 'Deque should return "2"')

  def test_deque_peek_back_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('0', str(self.__deque.peek_back()), 'Deque should return "0"')

  def test_deque_length_3_items(self):
    self.__deque.push_front(0)
    self.__deque.push_front(1)
    self.__deque.push_front(2)
    self.assertEqual('3', str(len(self.__deque)), 'Length should be 3')

if __name__ == '__main__':
  unittest.main()

