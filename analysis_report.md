## Provide a detailed analysis of the time complexity for both the deterministic and randomized selection algorithms.

### Deterministic:
- First step is diving the input data into groups of 5, which takes O(n) time to iterate and identify the groups.
- Secondly, finding the median, to do that we sort which take O(5 log 5) = O(1) times per group. Since we have n/5 groups, we conclude to say, O(n) time is taken. Now, we need to recursively select the median of these n/5 medians. That again will take O(n/5).
- As we know from quicksort operation, partitioning takes O(n) time.
- As we saw on the algorithm, the final recursive call will only happen on one particular subset. We can be sure that 30% of the elements will be discarded in each recursive step which concludes: 7n/10 elements.
- Summing them all:
  
  \[
  T(n) = O(n) + T(n/5) + T(7n/10)
  \]
  
  \[
  T(n) = O(n)
  \]

**Worst-case time complexity:** O(n)

### Randomized:
- Starts off with partitioning again, which takes O(n) time. After we partition, only one of the subsets will be called recursively.
- On an average case, partition will split the array into two equal halves but this is not guaranteed because of randomness.
- This would end up in the expected time complexity of:

  \[
  T(n) = O(n)
  \]

**Worst case:** The algorithm might choose the worst pivot, similar to the quicksort problem, which would end up in time complexity of O(n²).

---

## Explain why the deterministic algorithm achieves \(O(n)\) time complexity in the worst case, while the randomized algorithm achieves \(O(n)\) time complexity in expectation.

### Deterministic Algorithm:
- As mentioned in the previous section, the determination of the pivot makes a big difference. As provided above, the equation will still stand even when the worst-case input is provided:

  \[
  T(n) = O(n) + T(n/5) + T(7n/10)
  \]

  Therefore, the deterministic algorithm achieves O(n) time complexity in the worst case.

### Randomized Algorithm:
- In expected scenarios, a random pivot could split the input into two equal halves and continuing to do for the rest of the partitions results in O(n) time.
- In the worst case, if the random pivot happens to be the worst choice because of bad luck, this could result in a situation similar to quicksort, with O(n²) time complexity.

---

## Empirical Comparison

### Randomized vs Deterministic in different scenarios:

Provided values are in microseconds. 

| Algorithm           | Random           | Sorted           | Reverse sorted   |
|---------------------|------------------|------------------|------------------|
| Deterministic       | 190275           | 60636            | 149962           |
| Randomized          | 641              | 766              | 676              |

**Conclusion**: Based on this empirical analysis, it looks like randomized select provides a much faster results compared to deterministic. This is majorly contributed to the fact that the pivot is chosen in random. .

---

## Discuss the space complexity and any additional overheads associated with both algorithms.

- **Median of Medians**:
  - Overall space complexity is O(n) for the auxiliary space.

- **Quickselect**:
  - Although it does not need an additional array, the recursive depth in the worst case could result in O(n) space.

---

## Part 2: Data Structures
## Basic Operations of Data Structures

### Arrays and Matrices

| Operation   | Time Complexity |
|-------------|------------------|
| Insertion   | \(O(1)\)         |
| Deletion    | \(O(1)\)         |
| Access      | \(O(1)\)         |

### Stack & Queue Operations

| Operation     | Time Complexity |
|---------------|------------------|
| Push          | \(O(1)\)         |
| Pop           | \(O(1)\)         |
| Peek          | \(O(1)\)         |
| Enqueue       | \(O(1)\)         |
| Dequeue       | \(O(1)\)         |

### Linked List Operations

| Operation     | Time Complexity |
|---------------|------------------|
| Insertion     | \(O(n)\)         |
| Deletion      | \(O(1)\) (head) / \(O(n)\) (last) |
| Search        | \(O(n)\)         |

---

## Discuss the trade-offs between using arrays versus linked lists for implementing stacks and queues.

- **Arrays**:
  - Fixed size and resizing is expensive.
  - Accessing an element is O(1) based on the index.
  
- **Linked Lists**:
  - No fixed size, can expand dynamically.
  - Takes O(n) for access since traversal is required.
  - More memory overhead due to pointers.

---

## Compare the efficiency of different data structures in specific scenarios.

- **Fast Access**: 
  - Arrays are optimal for retrieving values by index due to O(1) access time.
  
- **Insertions/Deletions**:
  - Linked lists are better for frequent insertions and deletions, especially at the head, as these operations are O(1).

---

## Practical Applications of Data Structures

- **Doubly Linked List**:
  - Useful for browser navigation where users can go back and forth between pages.

- **Matrices**:
  - Ideal for representing a chessboard with rows and columns.

- **Stacks**:
  - Used in IDEs for undo/redo operations with LIFO behavior.

- **Queues**:
  - Perfect for task scheduling, like how priority queues are implemented.

---

## Highlight scenarios where one data structure may be preferred over another due to factors like memory usage, speed, and ease of implementation.

- **Memory Usage**: 
  - Arrays are more efficient as they avoid the additional memory overhead of pointers in linked lists.

- **Speed**: 
  - Arrays, stacks, and queues are generally faster, with O(1) performance in most operations.

- **Functionality**:
  - Stacks are ideal for LIFO functionality, while queues are preferred for FIFO tasks like scheduling.

