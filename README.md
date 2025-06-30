# Quicksort Algorithm Implementation and Analysis

This repository contains the implementation and analysis of the Quicksort algorithm as part of the MSCS 532 – Algorithms & Data Structures course assignment at the University of the Cumberlands. It includes both deterministic and randomized versions of Quicksort, empirical performance analysis, and a detailed report.

## Overview

- **Assignment 5**: Focuses on Quicksort implementation, theoretical analysis, and empirical comparison of deterministic and randomized versions.
- **Author**: Mohit Gokul Murali
- **Instructor**: Dr. Brandon Bass
- **Date**: June 29, 2025

## Files

- `assignment5_QuickSort_Implementation.py`: Contains the Python implementation of deterministic and randomized Quicksort with example usage and edge case testing.
- `assignment5_QuickSort_Analysis.py`: Performs empirical analysis, benchmarking running times and generating performance plots for various input sizes and distributions.
- `report.md`: A comprehensive report in Markdown format, including theoretical analysis, results, and visualizations, adhering to APA 7 standards.

## Setup

### Prerequisites
- Python 3.x
- Required libraries:
  - `numpy` (for numerical operations)
  - `matplotlib` (for plotting)
- Install dependencies using:
  ```bash
  pip install numpy matplotlib
  ```

### Clone the Repository
```bash
git clone https://github.com/your-username/quicksort-assignment.git
cd quicksort-assignment
```

## Usage

1. **Run Implementation**:
   - Execute `assignment5_QuickSort_Implementation.py` to test the Quicksort implementations:
     ```bash
     python3 assignment5_QuickSort_Implementation.py
     ```
   - Expected output includes sorted arrays and edge case results.

2. **Run Analysis**:
   - Execute `assignment5_QuickSort_Analysis.py` to perform benchmarks and generate plots:
     ```bash
     python3 assignment5_QuickSort_Analysis.py
     ```
   - This generates performance data and saves plots as `random_plot.png`, `sorted_plot.png`, `reverse_plot.png`, and `equal_plot.png` in the current directory.

3. **View Report**:
   - Open `report.md` in a Markdown viewer (e.g., VS Code, GitHub) or convert to PDF for submission.
   - Insert the generated plots into the report as instructed in the file.

## Notes
- Ensure all plot files (`random_plot.png`, `sorted_plot.png`, `reverse_plot.png`, `equal_plot.png`) are in the same directory as `report.md` when viewing or submitting.
- The analysis tests array sizes 100, 500, and 1000 with random, sorted, reverse-sorted, and all-equal distributions.
- For optimal performance on all-equal inputs, consider using the latest `assignment5_QuickSort_Analysis.py` version with three-way partitioning (available from the assignment instructions).

## License
This project is for academic purposes only. No commercial use is intended.
