# Program classes

class PatientByDrugDict:
    """Object to track a patient's granular (by drug) fills and revenue generated for the pharmacy"""
    def __init__(self, name, drug=None):
        self.name = name.capitalize()
        self.drug = drug
        self.fills = 0
        self.income_to_pharmacy = 0

    def increment_income_to_pharmacy(self, amount):
        self.income_to_pharmacy += amount

    def decrement_income_to_pharmacy(self, amount):
        self.income_to_pharmacy -= amount

    def increment_fills(self):
        self.fills += 1

    def decrement_fills(self):
        self.fills -= 1

    def __str__(self):
        sign = ''
        if self.income_to_pharmacy < 0:
            sign = '-'
        return f"{self.name} (Drug: {self.drug}): {self.fills} fills {sign}${abs(self.income_to_pharmacy)} income"


class PatientAggregateDict:
    """Object to track a patient's aggregate fills and revenue generated for the pharmacy"""
    def __init__(self, name):
        self.name = name.capitalize()
        self.created_prescriptions = []
        self.total_fills = 0
        self.total_income_to_pharmacy = 0

    def add_prescription(self, drug):
        self.created_prescriptions.append(drug)

    def increment_total_income_to_pharmacy(self, amount):
        self.total_income_to_pharmacy += amount

    def decrement_total_income_to_pharmacy(self, amount):
        self.total_income_to_pharmacy -= amount

    def increment_total_fills(self):
        self.total_fills += 1

    def decrement_total_fills(self):
        self.total_fills -= 1

    def __str__(self):
        sign = ''
        if self.total_income_to_pharmacy < 0:
            sign = '-'
        return f"{self.name}: {self.total_fills} fills {sign}${abs(self.total_income_to_pharmacy)} income"
    

class PatientDictsUtility:
    @classmethod
    def sort_patient_drug_alphabitical(cls, patient_dict):
        return {k: patient_dict[k] for k in sorted(patient_dict)}
    
    @classmethod
    def sort_patient_drug_by_income_decreasing(cls, patient_dict):
        return dict(sorted(patient_dict.items(), key=lambda item: item[1].income_to_pharmacy, reverse=True))
    
    @classmethod
    def sort_aggregate_patient_alphabitically(cls, patient_dict):
        return {k: patient_dict[k] for k in sorted(patient_dict)}
    
    @classmethod
    def sort_aggregate_patient_by_income_decreasing(cls, patient_dict):
        return dict(sorted(patient_dict.items(), key=lambda item: item[1].total_income_to_pharmacy, reverse=True))