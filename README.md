## Description
This is a command-line program written in Python. It ingests an input file as a stream, parses the rows as they are encountered to create instances of patients, stores them in two separate dictionaries, and then **renders** reports to the terminal (i.e., stdout).  

---

## Tech Stack
* **Python** has been selected as the programming language to implement the solution for the coding assignment.
* The only dependency to be installed other than Python is **pytest** (for unit tests).
* **uv** was used for generating the project and should be used for running it (refer to the last section 'Running the code' for instructions on how to run the project and the unit tests).
* **Alternatively**, and more easily, a Python virtual environment can be set up (since pytest needs to be installed). When the virtual environment is created and activated, the project can be started by typing: `python main.py` (from within the `src` directory).
* No databases were used since the processing is all in-memory and the output goes directly to standard out (i.e., the terminal). 

---

## Assumptions 
* A `PatientName` was given instead of a `PatientID` for illustrative purposes. Typically, a patient ID would be used for this type of project.
* The sample output provided in the assignment instructions seems to be ordered by the number of fills in **descending** order instead of the order in which 'create' prescription events occurred in the sample data. However, this could be by accident since, in many programming languages, hash structures do not guarantee the order of the items within them.
* Despite the small sample data provided in the instructions as input for the assignment, I realize that the input (in real life) can be **arbitrarily** long.

## Thought Process
As per the instructions, this is a fairly simple project. There are a number of ways to design the solution, as well as ways to test it. Additionally, the instructions made it clear not to have a single method that processes the file and outputs the report. While there are many ways to go overboard—adding superfluous features or functionality that were not requested—I have added a reasonable amount of features that serve to:
* Make the project easier to run (for instance, a menu has been added to allow the user to make certain selections).
* Add sorting to the project, since it is reasonable to assume this would be a useful feature.
* Control the way the program sorts the data (i.e., the patient instances within the main dictionary structures).
* Add a second type of report (i.e., per patient drug) which is a bit more granular than the requested aggregate report. The user can choose **which** type of report to run.
* Add the ability for the **user** to specify a text file as input for either of the two reports.
* Since in a real-life scenario the data can be arbitrarily long, I have implemented the ingestion of the file as a stream so that the host machine's memory is not exhausted (as may be the case if a file that was too large to read in all at once was supplied). 

**Note:** A more detailed description of the thought process, architectural decisions, trade-offs, and program organization can be given during the walk-through portion of the interview. 

## Architecture Decisions
To demonstrate the ability to break a program into logical units for reusability and extensibility, and to show the proper selection and usage of data structures—all without over-engineering—the program has been spread across multiple files. Just the right types and amount of data structures have been utilized. They are enumerated in the 'Data structures used' and 'Code organization / Project structure' sections below. 

## Trade-offs
* I chose to validate the data file before processing it. Typically, it is preferable for the system to validate the input file before processing. This strategy requires parsing and traversing the file twice (once to validate, and another time to process). However, this is often well worth the processing cost because—while the processing in this case is fairly light—it is usually more difficult to undo processing (such as for when a database or microservices are involved) if there is something wrong with the data. 
* I have written a minimum set of unit tests. While near 100% test coverage is often the goal in software development, they are time-consuming to write. However, I have written six unit tests for the most critical parts of the project, using the sample data as the **test** fixture. 
* While lists (i.e., arrays) could also have been used to hold the patient instances, I've elected to use **dictionaries** since they are typically preferred for searching (to modify specific object properties) and ordering (when producing the reports).  
* Environment variables are typically used to provide a way to feed values into a program to control how it works. However, a good compromise for this project was to place the control variables in an easy-to-access location (the top portion of the `helpers.py` file) instead of using environment variables. This also prevents the hard-coding of values—such as **controlling** how the program sorts and altering the monetary values for income per fulfilled prescription and the cost of returns. 

## Data Structures Used 
The main data structures utilized were:
* **Python dictionaries** (similar to Ruby's Hashes), which serve to hold patient instances.
* **Custom classes** representing **enumerations** (for things such as prescription events and different possible sort types).
* **Custom classes** representing a patient, used to create instances of patients.
* **A custom class**, comprised only of **class-based** methods, to **assist** with the sorting of the dictionaries.

## Code Organization / Project Structure
The project is comprised of four Python files and one input text file:
* `main.py` => The program's main entry point. It is purposefully a light file that imports other modules for classes, enumerations, **logic**, etc. 
* `patient.py` => Contains the two primary classes to represent a patient, as well as two enumerations and a utility class. Note: though the two patient base classes are similar, **inheritance** was purposefully not used since the classes are used for different purposes. 
* `helpers.py` => This file contains virtually all of the program's **logic**.
* `test_helpers.py` => Contains six unit tests which rely on the `sample_data.txt` file as the fixture.
* `sample_data.txt` => The data input file for feeding the program prescription events. 

---

## Running the Code (using `uv`)
1. Install **uv** on the host system.
2. Clone the project **repository** from GitHub: `https://github.com/mindpeak-biz/aki_gifthealth_assignment`
3. `cd` into the `aki_gifthealth_assignment` directory.
4. Run the project: `uv run src/main.py src/sample_data.txt` 
5. To run the unit tests: `uv run pytest -v`

**Note:** **Omitting** the `.txt` file will activate a **menu** for the user to select what they'd like to do—including running another input file (**provided** the file exists in the same directory as the `main.py` file).

## Running the Code (using a Python virtual environment and `pip`)
1. Clone the project repository.
2. `cd` into the `aki_gifthealth_assignment` directory.
3. Create a Python virtual environment within the project's root directory: `python -m venv venv`
4. Activate the virtual enviraonment: `source venv/bin/activate` 
5. Install the dependencies: `pip install -r requirements.txt` (to install **pytest**).
6. `cd` into the `src` directory.
7. Run the project: `python main.py sample_data.txt` 
8. To run the unit tests: `python -m pytest -v`

---

Thank you,

Aki Iskandar