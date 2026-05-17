# Level-3-Python

# Task 1: Basic File Encryption & Decryption using Python
# Project Overview

This project is a Python-based File Encryption and Decryption application developed to securely encrypt and decrypt text or file contents using the Fernet encryption algorithm from the cryptography library.

The application allows users to select files for encryption or decryption through a menu-driven command-line interface. Encrypted files are converted into unreadable secure data, while decrypted files are restored back to their original form using a secret key.

This project demonstrates practical implementation of cybersecurity concepts, secure file handling, encryption techniques, and Python programming fundamentals.

# Features

* Encrypt files securely using Fernet encryption
* Decrypt encrypted files back to original form
* Automatic secret key generation
* Secure key storage using secret.key
* User-friendly menu-driven interface
* Separate encrypted and decrypted output files
* Error handling for invalid files and keys
* Beginner to Intermediate level cybersecurity project
  
# Concepts Used

* File Encryption & Decryption
* Symmetric Encryption
* Fernet Encryption Algorithm
* File Handling
* Binary File Operations
* Functions
* Loops (while)
* Conditional Statements (if-elif-else)
* Exception Handling (try-except)
  
# Objectives

* Allow users to select files for encryption or decryption
* Encrypt file contents securely
* Save encrypted data into a new file
* Decrypt encrypted files back into original format
* Generate and manage encryption keys securely
* Handle invalid file and decryption errors
  
# Error Handling Implemented

File not found handling
Invalid encryption key handling
Corrupted encrypted file handling
Invalid user input handling

# Learning Outcomes

Through this project, I learned:

* Fundamentals of cryptography
* Secure file encryption and decryption
* Working with the Fernet encryption algorithm
* File handling in Python
* Binary file operations
* Exception handling techniques
* Real-world cybersecurity implementation

# Future Improvements

* GUI-based application using Tkinter
* Password-protected encryption
* Multiple file encryption support
* Folder encryption support
* Advanced AES encryption implementation
* Drag-and-drop file support
  
# Acknowledgement

This project helped me gain practical knowledge of file encryption, cybersecurity concepts, cryptography libraries, and secure file handling techniques. It also improved my understanding of real-world data protection methods and Python programming.



# Task 2: N-Queens Problem using Backtracking in Python
# Project Overview

The N-Queens Problem is a classic problem in computer science and artificial intelligence. The objective is to place N queens on an N × N chessboard such that no two queens attack each other.

In chess, a queen can attack:

Horizontally (same row)
Vertically (same column)
Diagonally

This project uses the Backtracking Algorithm to find a valid arrangement of queens on the chessboard while satisfying all constraints.

The project demonstrates recursion, backtracking, constraint satisfaction, and problem-solving techniques in Python.

# Objectives

* Represent the chessboard using a 2D array
* Place queens safely using backtracking
* Ensure no two queens attack each other
* Handle row, column, and diagonal constraints
* Develop recursive and logical problem-solving skills

# Features

* Dynamic N × N chessboard generation
* Solves N-Queens problem using Backtracking
* Displays valid queen arrangement
* Efficient recursive solution
* Safe position checking
* Beginner-friendly AI and DSA project
* User input for board size

# Concepts Used

* Backtracking Algorithm
* Recursion
* 2D Arrays (Lists) 
* Constraint Satisfaction
* Conditional Statements (if)
* Loops (for, while)
* Problem Solving Logic
  
# How the Program Works
* The user enters the value of N.
* The program creates an empty chessboard using a 2D array.
* Queens are placed column by column.
* Before placing a queen, the program checks:
* Row safety
* Upper diagonal safety
* Lower diagonal safety
* If the position is safe:
* The queen is placed.
* The algorithm recursively moves to the next column.
* If no valid position exists:
* Backtracking removes the previously placed queen.
* Another position is tried.
* When all queens are placed, the final board is displayed.
  
# Constraints Handled

The program ensures:

* No two queens are in the same row
* No two queens are in the same column
* No two queens are in the same diagonal

# Time Complexity
O(N!)

Because multiple possible queen placements are checked recursively.

# Challenges Solved

* Designing efficient recursive logic
* Implementing backtracking correctly
* Checking diagonal conflicts accurately
* Managing dynamic chessboard size
* Constraint satisfaction handling

# Learning Outcomes

Through this project, I learned:

* Backtracking algorithm implementation
* Recursive problem-solving techniques
* Constraint satisfaction logic
* Chessboard representation using 2D arrays
* Optimization and decision-making algorithms
* Real-world AI and DSA concepts

# Future Improvements

* Display all possible solutions
* GUI-based chessboard visualization
* Animated backtracking visualization
* Performance optimization for large N values
* User-friendly graphical interface

# Acknowledgement

This project helped me strengthen my understanding of recursion, backtracking algorithms, problem-solving techniques, and constraint satisfaction concepts. It also improved my logical thinking and algorithmic design skills through practical implementation.



Completing above both projects has been a valuable learning experience and an important step toward improving my software development and cybersecurity skills. 





