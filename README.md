# Algo-Race: Sorting Visualizer
An interactive, concurrent algorithm visualization engine that benchmarks sorting efficiency in real-time to visually demostrate Time Complexity (Big-O) differences
between O(n²) and O(n log n) algorithms using asynchronous execution loops and DOM manipulation.

## The Algorithms
- Quick Sort (O(n log n)): The industry standard. Uses a pivot-based divide and conquer strategy
- Merge Sort (O(n log n)): A stable sorter that recursively splits and merges lists.
- Bubble Sort (O(n²)): The naive approach. Swaps adjacent elements repeatedly.
- Selection Sort (O(n²)): Scans the list to find the minimum element. Highly inefficient.

## Key Features
- Concurrent Execution: All algorithms run simultaneously using async/await patterns.
- Audio Sonification: Generates Web Audio API tones based on value height.
- Interactive Controls: Adjust race speed and dataset size (10-100 items) dynamically.
- Billingual Support: Full English/Spanish (Latam) localization engine.

## Tech Stack
- Frontend: HTML5, CSS3 (Grid/Flexbox)
- Logic: JavaScript (ES6+ Classes)
- Rendering: HTML5 Canvas API

## Live Demo
**[Click Here to start the race](https://lushosly.github.io/algo-race/)**

**_Tip: Cmd ⌘ + Click (macOS) or Ctrl + Click (Windows/Linux) to open in a new tab._**
=================================== **Developer** =================================

Luis J. Rodriguez Espinal

Software Engineer | AI & Automation
