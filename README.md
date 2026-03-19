# 📁 Implementing a Binary Search
> A Python implementation of binary search, with path tracking to visualise exactly how the algorithm narrows down to its target.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Learning-Journey-orange)
![DSA](https://img.shields.io/badge/Topic-Algorithms-red?logo=python&logoColor=white)

## 📌 About

This project implements binary search from scratch, an algorithm that finds a value in a sorted list by repeatedly halving the search space rather than checking every element. A `path_to_target` list records every value inspected along the way, making the search process transparent and easy to trace. Built to understand how O(log n) search works and why it's dramatically faster than linear search on large datasets.

## 🧠 What I Learned

- **Binary search logic** — Maintaining `low` and `high` pointers that close in on the target, calculating `mid` each iteration and eliminating half the remaining search space based on whether the target is higher or lower
- **Floor division for the midpoint** — Using `(low + high) // 2` to always land on a valid integer index regardless of list size
- **Path tracking** — Appending the value at each midpoint to path_to_target before any comparison, producing a step-by-step trace of the algorithm's decisions
- **Why sorted input matters** — Understanding that binary search only works on sorted lists because it assumes values to the right are larger and values to the left are smaller — a wrong assumption on unsorted data silently breaks the algorithm
- **O(log n) vs O(n)** — Recognising that while linear search checks up to n elements, binary search checks at most `log₂(n)` — on a list of 1,000,000 items, that's the difference between up to 1,000,000 checks and at most 20
- **Returning multiple values as a tuple** — Returning both `path_to_target` and a result string together, unpacking naturally when printed

## 🛠️ Technologies Used
| Tool/Library | Purpose |
|--------------|---------|
| Python 3.x | Core Language |

## 💡 How It Works

The algorithm keeps a `low` and `high` boundary and checks the midpoint each iteration:
```
List:  [1, 2, 3, 4, 5]   Target: 3

Step 1: mid = index 2 → value 3 ✅ found!
path_to_target = [3]

List:  [1, 2, 3, 4, 5, 9]   Target: 4

Step 1: mid = index 2 → value 3, target is higher → search right half
Step 2: mid = index 4 → value 5, target is lower  → search left half
Step 3: mid = index 3 → value 4 ✅ found!
path_to_target = [3, 5, 4]
```

**Example output:**
```
binary_search([1, 2, 3, 4, 5], 3)
# ([3], 'Value found at index 2')

binary_search([1, 2, 3, 4, 5, 9], 4)
# ([3, 5, 4], 'Value found at index 3')

binary_search([1, 3, 5, 9, 14, 22], 10)
# ([], 'Value not found')
```

## 🚀 Future Improvements

- [ ] Add a step counter to display how many comparisons were made alongside the path
- [ ] Compare performance against a linear search on large lists to visualise the O(log n) advantage
- [ ] Extend to search a list of dictionaries by a specific key
- [ ] Implement a recursive version and compare it to the iterative approach

## 📂 Project Structure

```
binary-search/
│
├── BinarySearchAlgorithm.py    # binary_search function with example usage
└── README.md
```

*Part of my Python learning journey 🐍 — moving from data structures into algorithms with O(log n) search*
