# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions


Hashing functions allow us to convert a string key into number, with predictable output. For example, if 'blue' hashes to the number 3, it should always hash to the number 3 every time, so that we know where it should be placed.


2. Collision resolution


Collisions occur when 2 different keys hash to the same number. The idea of the hashtable is that each key cooresponds to a unique value, so when collisions occur they must be resolved somehow. One way to do this is with a linked list. Instead of a single entry, each entry in the hashtable is a node in a linked list. If a collision occurs, we can simply chain it onto the head of the list


3. Performance of basic hash table operations


Hashtable operations should ideally be O(1), or constant time. In a table with a lot of collisions, it will take additional time. In a worst-case scenario, where all of the keys have collided at a single index, it could be linear time O(n).

The hashing function itself will be linear, O(n) since it is looping over each character, but since the number of letters in a key is not the same as the number of inputs (which is what we are measuring with big O notation), it can be ignored in most circumstances.

4. Load factor


The load factor is a measure of how full the hashtable is. How many things are currently being stored in the hashtable divided by its capacity. Although, theoretically with a linked list implementation, capacity is limitless, the more things that are stored in the table without increasing capacity increases the probability of collisions and creates a less efficient hashtable.


5. Automatic resizing


Automatic resizing takes into account the current load factor and doubles (or even halves) the size of the hashtable when it reaches a predetermined threshold. A resizing method must also then replace all the values in the newly sized table. Since hashing funtions take into account the remainder of the division of the calculated hash and the length of the table, changing the size of the hashtable will change some hashes. This is good since it means less collisions, but it also means a resizing function will need to take care to replace every value in a newly calculated position.


6. Various use cases for hash tables


Hashtables have a large variety of applications. They are useful to store associations between things (perhaps a cipher) rather than just a jumbled list like an array. They can also save time in looping/recursive functions which may need to compute the same values repeatedly. Store them once, then you need only reference the answer after that. Hashtables can also be used to hold frequency data, how often a word or number appears in a given data set.


We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request

- ✅ ex1
- ✅ ex2
- ✅ ex3
- ✅ ex4
- ex5