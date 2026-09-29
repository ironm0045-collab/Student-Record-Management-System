from academic_engine import calculate_academic_performance

def run_tests():
    print("Testing academic calculation engine...")

    # Case 1: All clear with good scores
    marks_pass = {"Math": 80, "Physics": 70, "CS": 90}
    tot, pct, res = calculate_academic_performance(marks_pass)
    assert tot == 240, f"Expected 240, got {tot}"
    assert pct == 80.0, f"Expected 80.0, got {pct}"
    assert res == "Pass", f"Expected Pass, got {res}"
    print(" -> Passing condition check: OK")

    # Case 2: One subject below 40 should result in Fail
    marks_fail = {"Math": 30, "Physics": 70, "CS": 80}
    _, _, res_fail = calculate_academic_performance(marks_fail)
    assert res_fail == "Fail", f"Expected Fail, got {res_fail}"
    print(" -> Subject cutoff failure check: OK")

    # Case 3: Empty marks handling
    empty_tot, empty_pct, empty_res = calculate_academic_performance({})
    assert empty_tot == 0 and empty_pct == 0.0 and empty_res == "N/A"
    print(" -> Empty input fallback check: OK")

    print("All unit checks passed successfully.\n")

if __name__ == "__main__":
    run_tests()