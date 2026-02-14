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


# =======================================================================================
def main():
    # Get the parameter list, and parameter count
    parameters = sys.argv[1:]
    parameter_count = len(parameters)
    # If there are no command line parameters, show the program menu
    if parameter_count == 0:
        get_menu_option()
    # If there is only 1 parameter, it is expected to be the data filename
    elif parameter_count == 1:
        report_type = "aggregate"
        file_path = f"data/{parameters[0]}" 
        execute_normal_flow(file_path, False, report_type)
    # If there are more than a single parameter, terminate the program  
    else:
        print(f"Error: Invalid number of command line parameters.")
        print(f"Maximum of 1 expected, but {parameter_count} were supplied. \nTerminating program.")
        sys.exit(0)
# =======================================================================================

if __name__ == "__main__":
    main()
