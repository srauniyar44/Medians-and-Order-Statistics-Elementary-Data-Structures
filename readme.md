# Assignment 6: Medians, Order Statistics & Elementary Data Structures

This repository contains Python implementations and analysis for two core algorithmic and data structure topics:

## 📌 Part 1: Selection Algorithms

### ✅ Implemented Algorithms
- **Deterministic Selection (Median of Medians)**: Finds the k-th smallest element in worst-case linear time.
- **Randomized Quickselect**: Finds the k-th smallest element in expected linear time.

### 📁 File: `median_selection.py`
- `median_of_medians(arr, k)`: Deterministic algorithm
- `randomized_select(arr, k)`: Randomized algorithm

---

## 📌 Part 2: Elementary Data Structures

### ✅ Implemented Data Structures
- **Arrays and Matrices** (insert, delete, access)
- **Stacks and Queues** (array-based implementation)
- **Singly Linked Lists** (insert, delete, traverse)

### 📁 Files:
- `array_stack_queue.py`: Contains Array, Stack, and Queue implementations
- `linked_list.py`: Contains Singly Linked List implementation

---

## 📈 Performance & Analysis

Refer to `report.md` for:
- Time and space complexity analysis
- Empirical comparisons and test cases
- Practical use-case discussions

---

## 💻 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/assignment6-selection-datastructures.git
cd assignment6-selection-datastructures

# Run selection algorithms
python3 median_selection.py

# Run data structures
python3 array_stack_queue.py
python3 linked_list.py
