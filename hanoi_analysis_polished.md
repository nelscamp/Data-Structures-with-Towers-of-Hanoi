# Data Structures Performance Analysis

## Stack and Queue Performance Analysis

### Time Complexity

**Array_Deque-based implementations:**
- `__str__()`: O(n) - must traverse all elements
- `push()/enqueue()`: **Amortized O(1)** - occasionally O(n) when growth occurs
- `pop()/dequeue()`: O(1) - direct access to front/back
- `peek()`: O(1) - direct access without removal
- `__len__()`: O(1) - maintained size counter

**Linked_List_Deque-based implementations:**
- `__str__()`: O(n) - must traverse all elements  
- `push()/enqueue()`: O(1) - sentinel nodes enable direct access
- `pop()/dequeue()`: O(1) - direct access to front/back
- `peek()`: O(1) - direct access without removal
- `__len__()`: O(1) - maintained size counter

### Design Decision: No Exception Handling

**Advantages:**
- `pop()` returning `None` on empty structures provides natural flow control
- Eliminates need for explicit empty checks before operations
- Enables `pop()` as both operation and condition check
- Simplifies client code by avoiding exception handling

**Justification:** This design choice enhances usability without limiting functionality. Users can check for `None` returns rather than catching exceptions, leading to cleaner, more readable code.

## Deque Performance Analysis

### Array_Deque
- `__str__()`, `__grow()`: O(n) - linear operations
- `push_front()`, `push_back()`: **Amortized O(1)** - growth triggers O(n)
- `pop_front()`, `pop_back()`, `peek_front()`, `peek_back()`: O(1)

### Linked_List_Deque  
- `__str__()`: O(n) - requires full traversal
- All other operations: O(1) - sentinel-based direct access

### Empty vs Single-Element Distinction
Both implementations use `self.__size` counter:
- Empty: `self.__size == 0`
- Single element: `self.__size == 1`

### Array Growth Strategy
**Why double instead of increment by one?**
- **Amortized Analysis**: Doubling ensures amortized O(1) insertion time
- **Performance**: Reduces frequency of expensive growth operations
- **Trade-off**: Higher memory usage for significantly better time complexity

## Tower of Hanoi Analysis

### Performance Characteristics
**Time Complexity**: O(2^n) - exponential growth

**Observation**: Each recursive call spawns two additional calls, creating exponential branching. The runtime doubles with each additional disk, representing our first encounter with exponential time complexity.

**Recursive Structure**: T(n) = 2 × T(n-1) + 1, where the constant represents moving one disk.

## Command-Line Integration Strategy

```python
def create_deque_structure(structure_type, implementation_type):
    """
    Factory method for command-line deque selection
    structure_type: 'stack', 'queue', 'deque'  
    implementation_type: 'array', 'linked'
    """
    if implementation_type == 'array':
        base_deque = Array_Deque()
    else:
        base_deque = Linked_List_Deque()
    
    if structure_type == 'stack':
        return Stack(base_deque)
    elif structure_type == 'queue':
        return Queue(base_deque)
    return base_deque
```

Usage: `python program.py stack array` or `python program.py queue linked`

## Testing Strategy

### Comprehensive Coverage
**Stack/Queue Tests**: Cover empty, single-element, and multi-element scenarios for all operations (push/pop, enqueue/dequeue, peek, length).

**Deque Tests**: Test all six operations (push/pop front/back, peek front/back) across empty, 1-element, 2-element, and 3+ element states to trigger growth mechanisms.

**Hanoi Testing**: Verified against known solutions for small n values, confirmed exponential timing behavior through empirical measurement.

**Delimiter_Check Testing**: Tested with files containing balanced and unbalanced delimiter combinations to verify correct parsing.