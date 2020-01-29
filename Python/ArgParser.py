class Parser:
    def __init__(self, arg_list):
        self.function_list = []
        self.arg_pairs = []
        self.arg_names = []
        return

    def get_function_names(self):
        return self.function_list