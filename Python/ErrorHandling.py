class ErrorHandler:
    filename = "<script_name>"
    note = ""
    example = ""
    base_usage = ""
    usage_message = ""
    script_call_string = ""

    def __init__(self):
        pass

    @classmethod
    def build_usage_message(cls):
        cls.usage_message = f"usage: {cls.filename} {cls.base_usage}"
        if cls.note != "":
            cls.usage_message += f"\n{cls.note}"
        if cls.example != "":
            cls.usage_message += f"\n{cls.example}"

    @classmethod
    def set_usage_message(cls, usage):
        cls.base_usage = usage
        cls.build_usage_message()

    @classmethod
    def set_file_name(cls, filename):
        cls.filename = filename
        cls.build_usage_message()

    @classmethod
    def set_note(cls, note):
        cls.note = note
        cls.build_usage_message()

    @classmethod
    def set_example(cls, example):
        cls.example = example
        cls.build_usage_message()

    @classmethod
    def set_script_call_string(cls, call_string):
        cls.script_call_string = call_string

    @classmethod
    def get_script_call_string(cls):
        return cls.script_call_string

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
