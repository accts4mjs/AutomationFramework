import ArgParser as ap
import ErrorHandling as err


class SampleTool:
    REQUIRED_ARG_NAMES = ['tool', 'basedir', 'filename', 'version', 'start', 'end']
    REQUIRED_ARG_VALUES = ['tool', 'basedir', 'filename', 'version', 'start', 'end']  # Arg names that must have values
    OPTIONAL_ARG_NAMES = ['r', 'm']  # These are args that are usually flags.  No values.  May or may not be set.

    def __init__(self, my_args: ap.Parser):
        my_args.check_names_values_optionals(self.REQUIRED_ARG_NAMES, self.REQUIRED_ARG_VALUES, self.OPTIONAL_ARG_NAMES)

        # load argument information into object variables
        self.basedir = my_args.get_value('basedir')
        self.filename = my_args.get_value('filename')
        self.version = my_args.get_value('version')
        self.start = my_args.get_value('start')
        self.end = my_args.get_value('end')
        return

    def run(self):
        print("Hello World!")
        print(f"basedir = {self.basedir}")
        print(f"filename = {self.filename}")
        print(f"version = {self.version}")
        print(f"start = {self.start}")
        print(f"end = {self.end}")