# Progression Outcome Histogram

This Python program evaluates student progression outcomes based on their credit scores and visualizes the results using a histogram. It also stores the outcomes in a text file for record-keeping.

## Features
- Accepts user input for credit at pass, defer, and fail.
- Validates input against predefined valid marks.
- Determines progression outcomes: **Progress, Trailer, Retriever, Exclude**.
- Saves results to a text file (`Progression Outcome Report.txt`).
- Displays a histogram visualization using the **graphics.py** library.

## Requirements
- Python 3
- `graphics.py` (For histogram visualization)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/progression-histogram.git
   ```
2. Navigate to the project directory:
   ```bash
   cd progression-histogram
   ```
3. Install required dependencies (if any):
   ```bash
   pip install graphics.py
   ```

## Usage
1. Run the script:
   ```bash
   python progression.py
   ```
2. Enter the required credit values as prompted.
3. The program will evaluate the progression and store the outcome.
4. After multiple entries, it generates a **histogram**.
5. View stored results in `Progression Outcome Report.txt`.

## Example Input/Output
```
Please enter your credits at pass: 100
Please enter your credit at defer: 20
Please enter your credit at fail: 0
Progress (module trailer)
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: q
```

## License
This project is open-source and available under the MIT License.



