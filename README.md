# Data Structures with Towers of Hanoi
An implementation of fundamental data structures (**stacks, queues, deques**) with both array-based and **linked-list**-based backends, featuring a recursive Tower of Hanoi solver and **delimiter** validation tool.

## Overview

This project demonstrates the adapter pattern by implementing stacks and queues using a common deque interface, with interchangeable array-based and linked-list-based implementations. The Tower of Hanoi solver showcases exponential recursive algorithms, while the delimiter checker provides a practical stack application.

## Project Components

### Core Data Structures
- **Array_Deque**: Circular array implementation with dynamic resizing
- **Linked_List_Deque**: Doubly-linked list with sentinel nodes
- **Stack**: LIFO structure using deque adapter
- **Queue**: FIFO structure using deque adapter

### Applications
- **Tower of Hanoi**: Recursive puzzle solver with performance timing
- **Delimiter_Check**: Balanced bracket/parentheses validator
- **Comprehensive Testing**: 50+ unit tests covering edge cases

## Key Features

### Adapter Pattern Implementation
```python
# Stack and Queue both use the same deque interface
class Stack:
    def __init__(self):
        self.__dq = get_deque()  # Factory method
    
    def push(self, val):
        self.__dq.push_front(val)  # Stack uses front
    
class Queue:
    def __init__(self):
        self.__dq = get_deque()  # Same factory
    
    def enqueue(self, val):
        self.__dq.push_back(val)  # Queue uses back
```

### Performance Characteristics

| Structure | Operation | Array-Based | Linked-List-Based |
|-----------|-----------|-------------|-------------------|
| Stack/Queue | push/enqueue | Amortized O(1)* | O(1) |
| Stack/Queue | pop/dequeue | O(1) | O(1) |
| Stack/Queue | peek | O(1) | O(1) |
| Deque | All operations | Amortized O(1)* | O(1) |

*Array operations are O(n) when resizing occurs

### Tower of Hanoi - Exponential Algorithm
**Time Complexity**: O(2^n)
```python
def Hanoi_rec(n, source, auxiliary, destination):
    if n == 0:
        destination.push(source.pop())
    else:
        Hanoi_rec(n-1, source, destination, auxiliary)
        destination.push(source.pop())
        Hanoi_rec(n-1, auxiliary, source, destination)
```

## Usage Examples

### Tower of Hanoi
```bash
python Hanoi.py  # Solves 3-disk puzzle with timing
```

### Delimiter Validation
```bash
python Delimiter_Check.py source_file.py
# Output: "The file contains balanced delimiters."
```

### Testing
```bash
python DSQ_Test.py  # Run comprehensive unit tests
```

## Implementation Highlights

### Array_Deque Design
- **Circular Buffer**: Efficient use of array space with wraparound indexing
- **Dynamic Growth**: Doubles capacity when full (amortized O(1) performance)
- **Front/Back Pointers**: Enable O(1) operations at both ends

### Linked_List_Deque Design  
- **Sentinel Nodes**: Eliminate edge cases for empty lists
- **Bidirectional Links**: Enable efficient front and back operations
- **No Resizing**: Consistent O(1) performance for all operations

### Design Philosophy
**No Exception Strategy**: Operations return `None` for invalid states rather than raising exceptions, enabling cleaner flow control and natural empty-checking patterns.

## Testing Strategy

### Comprehensive Coverage
- **Boundary Testing**: Empty, single-element, and multi-element scenarios
- **Growth Testing**: Array deque expansion under load
- **Integration Testing**: Stack/queue behavior with both deque implementations
- **Algorithm Validation**: Hanoi solutions verified against known results

### Test Categories
1. **Empty Structure Tests**: Verify behavior with no elements
2. **Single Element Tests**: Edge cases with minimal data
3. **Multi-Element Tests**: Standard operations with various sizes
4. **Performance Tests**: Timing validation for exponential algorithms

## Technical Insights

This project illustrates several important computer science concepts:

1. **Adapter Pattern**: How different implementations can share common interfaces
2. **Amortized Analysis**: Why occasional expensive operations can still yield efficient overall performance
3. **Exponential Algorithms**: Real-world example of O(2^n) time complexity
4. **Trade-offs**: Memory vs. time complexity in different implementations

The design demonstrates how careful abstraction enables code reuse while maintaining performance characteristics appropriate for different use cases.
