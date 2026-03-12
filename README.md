# Heap Sort Algorithm Implementation

Name: Evans Mutuma 
Registration Number: EB3/67266/23

## Project Description

This project implements the Heap Sort algorithm without using built-in sorting functions.
The program sorts a list of integers and records the number of comparisons and swaps.

## How Heap Sort Works

Heap Sort first converts the list into a Max Heap. 
The largest element is always located at the root. 
The root element is swapped with the last element and removed from the heap.
The heap is then rebuilt until all elements are sorted.

## Time Complexity

Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)

## Space Complexity

Heap Sort uses O(1) auxiliary memory because sorting is done in-place.

## Experiment

The algorithm was tested with the following input sizes:

1
2
3
4
5
10
250
999
9999
89786
789300
1,780,000

Results show that runtime grows approximately proportional to n log n.
