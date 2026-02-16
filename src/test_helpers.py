from pathlib import Path
import pytest
from helpers import execute_normal_flow 


file_path = 'sample_data.txt'
ran_from_menu = False


@pytest.fixture(autouse=True)
def setup_before_each_test():
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / "sample_data.txt"
    yield 


def test_aggregate_report_output_for_mark(capsys):
    report_type = "aggregate"
    execute_normal_flow(file_path, ran_from_menu, report_type)
    captured = capsys.readouterr()
    assert "Mark: 2 fills $9 income" in captured.out

def test_aggregate_report_output_for_nick(capsys):
    report_type = "aggregate"
    execute_normal_flow(file_path, ran_from_menu, report_type)
    captured = capsys.readouterr()
    assert "Nick: 0 fills $0 income" in captured.out

def test_aggregate_report_output_for_john(capsys):
    report_type = "aggregate"
    execute_normal_flow(file_path, ran_from_menu, report_type)
    captured = capsys.readouterr()
    assert "John: 0 fills -$1 income" in captured.out

def test_drug_group_report_output_for_mark(capsys):
    report_type = "grouped_by_drug"
    execute_normal_flow(file_path, ran_from_menu, report_type)
    captured = capsys.readouterr()
    assert "Mark (Drug: b): 2 fills $9 income" in captured.out

def test_drug_group_report_output_for_nick(capsys):
    report_type = "grouped_by_drug"
    execute_normal_flow(file_path, ran_from_menu, report_type)
    captured = capsys.readouterr()
    assert "Nick (Drug: a): 0 fills $0 income" in captured.out

def test_drug_group_report_output_for_john(capsys):
    report_type = "grouped_by_drug"
    execute_normal_flow(file_path, ran_from_menu, report_type)
    captured = capsys.readouterr()
    assert "John (Drug: e): 0 fills -$1 income" in captured.out