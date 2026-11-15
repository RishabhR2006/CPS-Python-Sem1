# Computational Problem Solving (CPS) — Python, Semester 1

Programs written for the **Computational Problem Solving** course in Semester 1 of B.Tech CSE at Amrita Vishwa Vidyapeetham, Bengaluru.
They go from first steps (input, output, conditions) to recursion, searching and sorting, matrices, a stack and file handling.

## Contents

| Folder | Programs | Concepts |
|---|---|---|
| [`01-basics`](01-basics) | hello world, voting eligibility, positive / negative / zero, odd or even, largest of three, sums of even and odd digits, lambda, number patterns | input and output, `if`/`elif`/`else`, loops, nested loops |
| [`02-recursion`](02-recursion) | factorial, Fibonacci, sum of natural numbers, palindrome check | base case and recursive case |
| [`03-searching`](03-searching) | linear search (loop and recursive), binary search, sorting and searching a matrix by row sum | searching a list, divide and conquer |
| [`04-sorting`](04-sorting) | insertion sort, selection sort, bubble vs selection vs insertion sort | in-place sorting, comparing algorithms |
| [`05-lists-and-matrices`](05-lists-and-matrices) | rotate a list, matrix addition, scalar multiplication, transpose | lists of lists, nested loops |
| [`06-stack`](06-stack) | menu-driven stack of garment records | push, pop, display |
| [`07-file-handling`](07-file-handling) | character, word and line statistics in text files; saving records with `pickle` | reading text files, binary files |
| [`08-practice-questions`](08-practice-questions) | ATM withdrawal simulator | dictionaries, functions, a larger problem |

## How to run

You only need Python 3; no extra packages.

```
cd 04-sorting
python bubble_selection_insertion_sort.py
```

Output:

```
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
```

Many programs ask for input while they run (for example `01-basics/odd_or_even.py` asks for a number).
The file-handling programs read a text file from the folder you run them in (`Paragraph.txt`, `Notice.txt` or `report.txt`), so create one with a few lines of text first.
