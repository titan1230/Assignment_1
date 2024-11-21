import json
import random
import os
from typing import Literal

dbms = {
    "quiz_data": [
        {
            "question": "Which of the following is a type of database management system?",
            "options": [
                "Hierarchical",
                "Network",
                "Relational",
                "All of the above"
            ],
            "answer": "All of the above"
        },
        {
            "question": "What does SQL stand for?",
            "options": [
                "Structured Query Language",
                "Simple Query Language",
                "Structured Question Language",
                "None of the above"
            ],
            "answer": "Structured Query Language"
        },
        {
            "question": "Which of the following is a valid SQL command?",
            "options": [
                "SELECT",
                "INSERT",
                "UPDATE",
                "All of the above"
            ],
            "answer": "All of the above"
        },
        {
            "question": "What is a primary key?",
            "options": [
                "A unique identifier for a record in a table",
                "A key that is used to encrypt data",
                "A key that is used to decrypt data",
                "None of the above"
            ],
            "answer": "A unique identifier for a record in a table"
        },
        {
            "question": "Which SQL statement is used to extract data from a database?",
            "options": [
                "GET",
                "OPEN",
                "EXTRACT",
                "SELECT"
            ],
            "answer": "SELECT"
        },
        {
            "question": "Which SQL keyword is used to sort the result-set?",
            "options": [
                "SORT",
                "ORDER",
                "ORDER BY",
                "SORT BY"
            ],
            "answer": "ORDER BY"
        },
        {
            "question": "Which of the following is not a type of SQL join?",
            "options": [
                "INNER JOIN",
                "OUTER JOIN",
                "LEFT JOIN",
                "RIGHT JOIN"
            ],
            "answer": "OUTER JOIN"
        },
        {
            "question": "What is a foreign key?",
            "options": [
                "A key used to unlock foreign databases",
                "A key used to link two tables together",
                "A key used to encrypt data",
                "None of the above"
            ],
            "answer": "A key used to link two tables together"
        },
        {
            "question": "Which of the following is a NoSQL database?",
            "options": [
                "MySQL",
                "PostgreSQL",
                "MongoDB",
                "SQLite"
            ],
            "answer": "MongoDB"
        }
    ]
}

os = {
    "quiz_data": [
        {
            "question": "What is a critical section in an operating system?",
            "options": [
                "A part of the OS",
                "A section of memory",
                "A code segment where shared resources are accessed",
                "A disk sector"
            ],
            "answer": "A code segment where shared resources are accessed"
        },
        {
            "question": "Which scheduling algorithm is also known as First Come First Serve?",
            "options": [
                "Round Robin",
                "FCFS",
                "SJF",
                "Priority Scheduling"
            ],
            "answer": "FCFS"
        },
        {
            "question": "What is the purpose of virtual memory?",
            "options": [
                "To increase CPU speed",
                "To provide disk storage",
                "To simulate more RAM than physically available",
                "To prevent disk fragmentation"
            ],
            "answer": "To simulate more RAM than physically available"
        },
        {
            "question": "What is a process in an operating system?",
            "options": [
                "A program in execution",
                "A program in memory",
                "A program on disk",
                "A program in cache"
            ],
            "answer": "A program in execution"
        },
        {
            "question": "Which of the following is a non-preemptive scheduling algorithm?",
            "options": [
                "Round Robin",
                "Multilevel Queue",
                "Shortest Job Next",
                "Priority Scheduling"
            ],
            "answer": "Shortest Job Next"
        },
        {
            "question": "What is the main function of the command interpreter?",
            "options": [
                "To provide the interface between the user and the computer hardware",
                "To handle the files in the system",
                "To get and execute the next user-specified command",
                "To manage system resources"
            ],
            "answer": "To get and execute the next user-specified command"
        },
        {
            "question": "What is thrashing in an operating system?",
            "options": [
                "A high paging activity",
                "A high CPU activity",
                "A high disk activity",
                "A high memory activity"
            ],
            "answer": "A high paging activity"
        },
        {
            "question": "Which of the following is a synchronization tool?",
            "options": [
                "Thread",
                "Pipe",
                "Semaphore",
                "Socket"
            ],
            "answer": "Semaphore"
        },
        {
            "question": "What is the main purpose of an interrupt in an operating system?",
            "options": [
                "To provide a way to break the normal sequence of execution",
                "To provide a way to increase the speed of the CPU",
                "To provide a way to decrease the speed of the CPU",
                "To provide a way to handle memory management"
            ],
            "answer": "To provide a way to break the normal sequence of execution"
        },
        {
            "question": "What is the role of the page table in a virtual memory system?",
            "options": [
                "To map virtual addresses to physical addresses",
                "To map physical addresses to virtual addresses",
                "To store the contents of the virtual memory",
                "To store the contents of the physical memory"
            ],
            "answer": "To map virtual addresses to physical addresses"
        }
    ]
}

dsa = {
    "quiz_data": [
        {
            "question": "What is the time complexity of binary search?",
            "options": [
                "O(n)",
                "O(log n)",
                "O(n log n)",
                "O(n^2)"
            ],
            "answer": "O(log n)"
        },
        {
            "question": "What data structure is used for implementing recursion?",
            "options": [
                "Queue",
                "Stack",
                "Heap",
                "Tree"
            ],
            "answer": "Stack"
        },
        {
            "question": "Which sorting algorithm is the fastest for large datasets?",
            "options": [
                "Bubble Sort",
                "Merge Sort",
                "Quick Sort",
                "Insertion Sort"
            ],
            "answer": "Quick Sort"
        },
        {
            "question": "What is the worst-case time complexity of Quick Sort?",
            "options": [
                "O(n)",
                "O(n log n)",
                "O(n^2)",
                "O(log n)"
            ],
            "answer": "O(n^2)"
        },
        {
            "question": "Which data structure is used to implement a priority queue?",
            "options": [
                "Array",
                "Linked List",
                "Heap",
                "Stack"
            ],
            "answer": "Heap"
        },
        {
            "question": "What is the space complexity of Depth First Search (DFS)?",
            "options": [
                "O(V)",
                "O(E)",
                "O(V + E)",
                "O(1)"
            ],
            "answer": "O(V)"
        },
        {
            "question": "Which algorithm is used to find the shortest path in a graph?",
            "options": [
                "Kruskal's Algorithm",
                "Prim's Algorithm",
                "Dijkstra's Algorithm",
                "Floyd-Warshall Algorithm"
            ],
            "answer": "Dijkstra's Algorithm"
        },
        {
            "question": "What is the time complexity of inserting an element in a binary search tree?",
            "options": [
                "O(1)",
                "O(log n)",
                "O(n)",
                "O(n log n)"
            ],
            "answer": "O(log n)"
        },
        {
            "question": "Which data structure is used for breadth-first search (BFS)?",
            "options": [
                "Stack",
                "Queue",
                "Heap",
                "Tree"
            ],
            "answer": "Queue"
        },
        {
            "question": "What is the time complexity of accessing an element in an array?",
            "options": [
                "O(1)",
                "O(log n)",
                "O(n)",
                "O(n^2)"
            ],
            "answer": "O(1)"
        }
    ]
}

class Quiz:
    
    def __init__(self, variation: Literal["dsa", "dbms", "os"]):
        valid_types = {"dsa", "dbms", "os"}
        
        if variation.lower().strip() not in valid_types:
            raise ValueError("Invalid quiz type!")
        
        self.quiz_data = []
        self.score = 0
        self.current_question = 0
        self.type = variation.lower().strip()

    def load_quiz_data(self):
        quiz_name = "dsa" if self.type == "dsa" else "dbms" if self.type == "dbms" else "os"
        
        quiz_data = dsa["quiz_data"] if self.type == "dsa" else dbms["quiz_data"] if self.type == "dbms" else os["quiz_data"]
            
        selected_data = random.sample(quiz_data, 5)
        random.shuffle(selected_data)
        self.quiz_data = selected_data
    
    def start_quiz(self):

        self.load_quiz_data()
        
        while self.current_question < 5:
            question = self.quiz_data[self.current_question]
            print(f"{self.current_question + 1}> {question['question']}")
            
            for i, option in enumerate(question['options'], 1):
                print(f"{i}. {option}")
            
            answer = input("Enter your answer: ")
            
            if not answer.isdigit() or int(answer) not in range(1, 5):
                print("Invalid Answer!")
                continue
            
            answer = int(answer)
            
            if question["options"][answer - 1] == question['answer']:
                self.score += 1
            
            self.current_question += 1
            
        print(f"Quiz Completed! Your score is {self.score}/5")
        self.current_question = 0