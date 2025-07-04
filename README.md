# Automated Test Case and Mutation Generation Framework

This project provides an automated pipeline to generate test cases for any Python script, create mutants for mutation testing, and assess the effectiveness of generated test cases by checking whether they can “kill” the mutants. It ensures improved code quality and higher test coverage.

## 🚀 Project Setup

### 1. Clone the repo:
```git clone https://github.com/Ammarkarimi/Mutant-and-Test-Case-Generation```

---

### 2. Requirements
- Install dependencies:
```pip install -r requirements.txt```

---

## ⚒️ How It Works

### 1. Place Your Python Script

- Write the Python code you wish to test inside the main directory.
- Name your file as: ```script_number.py```

---

### 2. Configure `main.ipynb`

- Open the `main.ipynb` notebook.
- In the main cell, modify: ```script_<number>.py```

---

### 3. Generate Test Cases

- Run the notebook cell.
- The system generates initial test cases for the selected script.
- Test cases are cleaned and displayed to the user.
- You’ll be prompted: _Are you satisfied with these test cases, or do you want to generate more?_
- If you want more tests, continue the generation loop until satisfied.

---

### 4. Generate Mutants
- Once you’re happy with the test cases, the system automatically generates mutants:
  - All types of mutants are created.
  - Mutants continue being generated until the user confirms satisfaction.

---

### 5. Mutation Testing
- The mutants are run against the generated test cases:
  - A mutant is killed if test cases detect its presence (i.e. tests fail as expected).
  - A mutant survives if test cases pass despite the mutation.
- If mutants survive:
  - More test cases are generated and added.
  - The process repeats until all mutants are killed.

---

### 6. . Save Results
- When all mutants are killed:
  - The final test cases are saved into: ```script_<number>_output.py```

---

### 7. Check Coverage
- After saving the test cases:
  - Code coverage analysis is performed to measure how well the test cases exercise your original code.
 
---

## 👨‍💻 Developed By

**Mohammed Ammar Karimi**<br>
💼 [LinkedIn](https://www.linkedin.com/in/mohammed-ammar)<br>
🌐 [Website](https://ammarkarimi.vercel.app/)<br>
📫 [Email](ammarkarimi9898@gmail.com)<br>
