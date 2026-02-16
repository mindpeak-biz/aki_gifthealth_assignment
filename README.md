## Project Description
Coming ...

---

## Tech stack
* Python has been selected as the programming language to implement the solution for the coding assignment.
* The only dependency, to be installed other than Python, is pytest (for unit tests).
* uv was used for generating the project, and should be used for running the project (refer to the last section 'Running the code' for instructions on how to run the project and how to run the unit tests)
* alertnatively, and more easily, a Python virtual environment can be set up (since pytest needs to be installed). When the virtual environment is created and activated the project can be started by typing: python main.py (from within the src directory)
* No databases were used since the processing is all in memory and the output goes to directly to standard out (i.e. the terminal) 

---

## Assumptions 
* A PatientName was given instead of a PatientID for illustrative purposes.  Typically a patient id would be used for this type of project.
* The sample output provided in the assingment instructions seems to be ordered by the number of fills in decending order instead of the order in which 'create' prescription events occurred in the sample data. However, this could be by accident since in many programming languages hash structures do not guarantee the order of the items within them.
* Despite the small sample data provided in the instructions, as input to the program for the assignment, I realize that the the input (in real life) can be arbitrarilly long.

## Thought process
As per the instructions, this is a fairly simple project. There are a number of ways to design the solution, as well as there are ways to test the solution. Additionally, the instructions made it clear to not have a single method process that processes the file and outputs the report. There are many ways to go overboard - adding superfluous features / functionality that were not asked for. 

## Architecture decisions
For the purposes of demonstrating knowledge of being able to break the program up into logical units for reusability and extensibility, and to show the proper selection and usage of datastructures - all without over-engineering - .

## Tradeoffs
* I chose to validate the data file before processing it. This is because it is typically preferable for the system to validate the input file before it processes it. This strategy requires parsing and traversing the file twice (once to validate, and another time to process it). However, it is very often the case that this is well worth the processing cost because - while the processing in this case is fairly light - it is usually more difficult to undo processing (such as for when a database or microservices are involved) if there is something wrong with the data in the file. 
* I have written a minimum set of unit tests. While near 100% test coverage is often the goal in software development, they are time consuming to write (unfortunately, too much time for an assignment). However, I have written 6 unit tests for the most important part of the project to test - using the sample data as the text fixture.   

## Data structures used 
This is a small program and so there are not many data structures that were used. The main datastructures utilized were:
* Python dictionaries (these are like Ruby's Hashes), which serve to hold patient instances.
* Custom classes to represent enumerations (for things such as prescription events, and the different possible sort types).
* Custom classes to represent a patient. These are used to created instances of patients.
* A custom class, comprised only of class based methods, to assiste with the sorting of the dictionaries.

## Code organization / Project structure
The project is comprised of 4 Python files, and one input / text file. The 5 files are as follows:
* main.py => this is where the program's main entry point is. It is purposefully a light file which imports the other files / modules for the classes, enumerations, locic, etc. 
* patient.py => this file contains the two primary classes to represent a patient for the program, as well as 2 enumerations and a utility class for working with the two primary classes. Note: though the two patient base classes are similar, inheritence was purposefully not used since the classes are fundamentally used for different purposes. 
* helpers.py => this file contains virtually all of the program's logic resides.
* test_helpers.py => this file contains 6 unit tests, which rely on the sample_data.txt file as the fixture.
* sample_data.txt => this is the data input file for feeding the program prescription events. 

---

## Running the code (using uv)
1. Install uv on the host system
2. Clone the project repositoty from Github: https://github.com/mindpeak-biz/aki_gifthealth_assignment
3. cd into the aki_gifthealth_assignment/src directory
4. Run the project: uv run main.py sample_data.txt 
5. To run the unit tests for the project: uv run pytest -v
Note: ommiting the txt file will activate a memu for the user to select what they'd like to do - including running another input file (frovided the file exists in the same directory as the main.py file)


## Running the code (using a Python virtual environment and pip)
1. Clone the project repositoty from Github: https://github.com/mindpeak-biz/aki_gifthealth_assignment
2. cd into the aki_gifthealth_assignment directory
3. Create a Python virtual environment within the project's root directory
4. Run: pip install -r requirements.txt (this is so you can install PyTest to run the unit tests)
5. cd into the src directory
6. Run the project: python main.py sample_data.txt 
7. To run the unit tests for the project: python -m pytest -v
Note: ommiting the txt file will activate a memu for the user to select what they'd like to do - including running another input file (frovided the file exists in the same directory as the main.py file)

