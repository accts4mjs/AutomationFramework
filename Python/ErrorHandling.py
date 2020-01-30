def error_continue(message):
    print(f"FAIL - {message}")
    return


def error_abort(message, usage = ""):
    print(f"FAIL - {message}")
    if usage:
        print(usage)
    exit(0)