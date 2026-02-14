## Project Description


---

## Tech stack
* This is a Python based project.
* The only dependency is pytest (for unit tests)
* uv was used for generating the project, and should be used for running the project (refer to the last section 'Running the code' for instructions on how to run the project and how to run the unit tests)
* No databases were used since the output goes to the terminal


---

## Assumptions 
* A PatientName was given instead of a PatientID for illustrative purposes.  Typically a patient id would be used for this type of project.
* The expected output is not ordered in any way. The sample output provided in the assingment instructions was not in alphabetical order, or ordered by income.
* Despite the small file that was supplied in the instructions for the assignment, the input file (in real life) can be arbitrarilly long. 

## Thought process
Coming ...

## Architecture decisions
Coming ...

## Tradeoffs
* I chose to validate the data file before processing it. This is because it is typically preferable for the system to validate the input file before it processes it. This strategy requires parsing and traversing the file twice (once to validate, and another time to process it). However, it is very often the case that this is well worth the processing cost because - while the processing in this case is fairly light - it is usually more difficult to undo processing (such as for when a database or microservices are involved) if there is something wrong with the data in the file. 
* I have written a minimum set of unit tests. While near 100% test coverage is often the goal in software development, they are time consuming to write (unfortunately, too much time for an assignment). However, I have written unit tests for the most important part of the project to test - using the sample data as the text fixture.   


## Data structures used 


## Code organization / Project structure

---

## Running the code