def error_continue(message):
    print(f"FAIL - {message}")
    return


def error_abort(message):
    print(f"FAIL - {message}")
    exit(0)