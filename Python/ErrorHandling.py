class ErrorHandler:
    usage_message = ""

    def __init__(self, usage):
        ErrorHandler.usage_message = usage

    @classmethod
    def set_usage_message(cls, usage):
        cls.usage_message = usage

    @classmethod
    def error_continue(cls, message, usage=False):
        print(f"{message}")
        if usage:
            print(cls.usage_message)
        return

    @classmethod
    def error_abort(cls, message, usage=False):
        print(f"{message}")
        if usage:
            print(cls.usage_message)
        exit(0)

    @classmethod
    def assert_abort(cls, test, message, usage=False):
        if not test:
            print(f"{message}")
            if usage:
                print(cls.usage_message)
            exit(0)

    @classmethod
    def assert_continue(cls, test, message, usage=False):
        if not test:
            print(f"{message}")
            if usage:
                print(cls.usage_message)
        return
