import sys
from pathlib import Path
from patient import PatientAggregate, Patient, PatientUtility, SortBy, PrescriptionEvent


# Program variables
patient_drug_dict = {} # this is the dictionary for the bonus output (granular instead of default aggregated report data)
patient_aggregated_dict = {} # this is the dictionary for the requested output
income_per_prescription_filled = 5
loss_per_return = 1
total_loss_per_return = income_per_prescription_filled + loss_per_return
sort_by = SortBy.DECREASING_FILLS # this is the default sort, and can be modified and the program re-run.


def execute_normal_flow(file_path_name, ran_from_menu, report_type):
    # ran_from_menu is a boolean which controls whether the report header is printed 
    # as well as whether the program ends or loops back to the menu
    file_exists = check_file_exists(file_path_name, ran_from_menu)
    if file_exists:
        validate_input_file(file_path_name)
        process_validated_file(file_path_name)
        if report_type == "aggregate":
            print_patient_aggregate_report(ran_from_menu, sort_by)
        else:
            print_patient_drug_report(ran_from_menu, sort_by)


def get_menu_option(script_dir):
    selection = ''
    print("\nWelcome to RX Report")
    while selection not in ['4','q']:  
        print("\nPlease select a menu option.")
        print("(select option 4, or press 'q' to quit)")
        print("--------------------------------------------------")
        print("1. Run aggregate report using the default data file (sample_data.txt)")
        print("2. Run aggregate report specifying a data filename.")
        print("3. Run report (grouped by drug) specifying a data filename.")
        print("4. Quit program")
        selection = input("\nSelection: ")
        selection = selection.strip().lower()
        if selection in ['4','q']: 
            print(f"\nThank you for using RX Report. Goodbye.\n")
            sys.exit()
        elif selection == '1':
            report_type = "aggregate"
            file_path = f"{script_dir}/sample_data.txt"
            execute_normal_flow(file_path, True, report_type)
        elif selection == '2':
            report_type = "aggregate"
            file_name = input("\nEnter data filename: ").strip().lower()
            file_path = f"{script_dir}/{file_name}"
            execute_normal_flow(file_path, True, report_type)
        elif selection == '3':
            report_type = "grouped_by_drug"
            file_name = input("\nEnter data filename: ").strip().lower()
            file_path = f"{script_dir}/{file_name}"
            execute_normal_flow(file_path, True, report_type)
        else:
            print(f"\nInvalid selection. Please try again.")


def check_file_exists(file_name, ran_from_menu):
    script_root = Path(__file__).resolve().parent
    file_path = script_root / file_name
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        error_message = f"Error: The file {file_path} was not found."
        if not ran_from_menu:
            error_message += "\nTerminating program.\n"
            print(error_message)
            sys.exit(0)
        else:
            print(error_message + "\n")
            return False
    return True


def validate_input_file(file_path):
    try:
        line_count = 1
        valid_prescription_events = list({event.value for event in PrescriptionEvent})
        with open(file_path, 'r', encoding='utf-8') as file_stream:
            for line in file_stream:
                word_array = line.strip().split(' ')
                word_count = len(word_array)
                valid_event = word_array[2].lower() in valid_prescription_events
                if word_count != 3 or valid_event == False:
                   print(f"Error: Invalid input file (line {line_count}).\nTerminating program.")
                   sys.exit(0)
                line_count += 1
    except Exception as e:
        print(e)
        sys.exit(0)


def add_patient_to_patient_drug_dict(patient_drug_key, patient_name, drug):
    if patient_drug_key not in patient_drug_dict:
        patient = Patient(patient_name, drug)
        patient_drug_dict[patient_drug_key] = patient


def add_patient_to_patient_aggregated_dict(patient_aggregate_key, patient_name, drug):
    if patient_aggregate_key not in patient_aggregated_dict:
        patient = PatientAggregate(patient_name)
        patient.add_prescription(drug)
        patient_aggregated_dict[patient_aggregate_key] = patient
    else:
        patient_aggregated_dict[patient_aggregate_key].add_prescription(drug)


def process_validated_file(file_path):
    # This function creates 2 data structures for patient prescriptions:
    # patient_drug_dict => this is for tracking patient-drug prescriptions (so we can produce a granular report)
    # patient_aggregated_dict => this is for aggregating all prescriptions per patient (for the aggregate report)
    patient_drug_dict.clear()
    patient_aggregated_dict.clear()
    with open(file_path, 'r', encoding='utf-8') as file_stream:
        for line in file_stream:
            word_array = line.strip().lower().split(' ')
            patient_name = word_array[0]
            drug_name = word_array[1]
            prescription_event = word_array[2]
            patient_drug_key = f"{patient_name}_{drug_name}"
            patient_aggregate_key = f"{patient_name}"
            if prescription_event == PrescriptionEvent.CREATED.value:
                # patient_drug_dict
                add_patient_to_patient_drug_dict(patient_drug_key, patient_name, drug_name)
                # patient_aggregated_dict
                add_patient_to_patient_aggregated_dict(patient_aggregate_key, patient_name, drug_name)
            elif prescription_event == PrescriptionEvent.FILLED.value:
                # modify patient record in patient_drug_dict
                if patient_drug_key in patient_drug_dict:
                    patient_drug_dict[patient_drug_key].increment_income_to_pharmacy(income_per_prescription_filled)
                    patient_drug_dict[patient_drug_key].increment_fills()
                # modify patient record in patient_aggregated_dict
                if patient_aggregate_key in patient_aggregated_dict and drug_name in patient_aggregated_dict[patient_aggregate_key].created_prescriptions:
                    patient_aggregated_dict[patient_aggregate_key].increment_total_income_to_pharmacy(income_per_prescription_filled)
                    patient_aggregated_dict[patient_aggregate_key].increment_total_fills()
            elif prescription_event == PrescriptionEvent.RETURNED.value:
                # modify patient record in patient_drug_dict
                if patient_drug_key in patient_drug_dict:
                    patient_drug_dict[patient_drug_key].decrement_income_to_pharmacy(total_loss_per_return)
                    patient_drug_dict[patient_drug_key].decrement_fills()
                # modify patient record in patient_aggregated_dict
                if patient_aggregate_key in patient_aggregated_dict and drug_name in patient_aggregated_dict[patient_aggregate_key].created_prescriptions:
                    patient_aggregated_dict[patient_aggregate_key].decrement_total_income_to_pharmacy(total_loss_per_return)
                    patient_aggregated_dict[patient_aggregate_key].decrement_total_fills()
            else:
                # This branch should never be reached if the data file was validated. 
                # However, it's here for added safety. Logging may be a good idea here.
                pass


def sort_patient_dicts():
    pass


def print_patient_drug_report(ran_from_menu, sort_by):
    # Print report header if this function was called from the get_menu_option function
    if ran_from_menu:
        print("\nRX Report (by patient-drug)\n--------------------------")
    # sort the dictionary
    util = PatientUtility
    if sort_by == SortBy.ALPHABETICAL:
        processed_patient_drug_dict = util.sort_patient_drug_alphabitical(patient_drug_dict)
    elif sort_by == SortBy.DECREASING_INCOME:
        processed_patient_drug_dict = util.sort_patient_drug_by_decreasing_income(patient_drug_dict)
    elif sort_by == SortBy.DECREASING_FILLS:
        processed_patient_drug_dict = util.sort_patient_drug_by_decreasing_fills(patient_drug_dict)
    else:
        processed_patient_drug_dict = patient_drug_dict
    for key, patient in processed_patient_drug_dict.items():
        print(patient)
    print()


def print_patient_aggregate_report(ran_from_menu, sort_by):
    # Print report header if this function was called from the get_menu_option function
    if ran_from_menu:
        print("\nRX Report (aggregated)\n--------------------------")
    # sort the dictionary
    util = PatientUtility
    if sort_by == SortBy.ALPHABETICAL:
        processed_patient_aggregated_dict = util.sort_aggregate_patient_alphabitically(patient_aggregated_dict)
    elif sort_by == SortBy.DECREASING_INCOME:
        processed_patient_aggregated_dict = util.sort_aggregate_patient_by_decreasing_income(patient_aggregated_dict)
    elif sort_by == SortBy.DECREASING_FILLS:
        processed_patient_aggregated_dict = util.sort_aggregate_patient_by_decreasing_fills(patient_aggregated_dict)
    else:    
        processed_patient_aggregated_dict = patient_aggregated_dict
    for key, patient in processed_patient_aggregated_dict.items():
        print(patient)
    print()


def add_numbers(a: int, b: int) -> int:
    return a + b