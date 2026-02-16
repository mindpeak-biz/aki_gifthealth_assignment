'''
Script file name:   main.py
Author:             Aki Iskandar
Email:              aki@mindpeak.biz 

Authored date:      Feb 12, 2026

Purpose:
This program parses an input file of prescription events (for a pharmacy system)  
and outputs a report for the total number of fills and total income for each patient 
(in aggregate, and not per DrugName). 
'''


import sys
from helpers import get_menu_option, execute_normal_flow
from pathlib import Path


# =======================================================================================
def main():
    # Get the parameter list, parameter count, and the script directory
    parameters = sys.argv[1:]
    parameter_count = len(parameters)
    script_dir = Path(__file__).resolve().parent

    # If there are no command line parameters, show the program menu
    if parameter_count == 0:
        get_menu_option(script_dir)
    # If there is only 1 parameter, it is expected to be the data filename.So run the expected default aggregate report.
    elif parameter_count == 1:
        file_name = parameters[0]
        execute_normal_flow(file_path_name=file_name, ran_from_menu=False, report_type="aggregate")
    # If there are more than a single command line parameter, terminate the program  
    else:
        print(f"Error: Invalid number of command line parameters.")
        print(f"Maximum of 1 expected (the data file name), but {parameter_count} were supplied. \nTerminating program.")
        sys.exit(0)
# =======================================================================================

if __name__ == "__main__":
    main()
