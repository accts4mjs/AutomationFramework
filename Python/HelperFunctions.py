import subprocess


def my_tdd(actual, expected, test_name):
    state = "FAIL"
    result = False
    # print("'" + actual + "' '" + expected + "'")
    if str(actual) == str(expected):
        state = "PASS"
        result = True

    print(f"{test_name} - {state}")
    return result


def my_call_python(call_string):
    result = subprocess.check_output(f"python {str(call_string)}", stderr=subprocess.STDOUT,
                                     universal_newlines=True).strip()
    return result
