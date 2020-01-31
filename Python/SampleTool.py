import ArgParser as ap
import ErrorHandling as err


class SampleTool:
    REQUIRED_ARG_NAMES = ['basedir', 'filename', 'version', 'start', 'end']
    REQUIRED_ARG_VALUES = ['basedir', 'filename', 'version', 'start', 'end']  # Use arg names that should have values
    OPTIONAL_ARG_NAMES = ['r', 'm']  # These are args that are usually flags.  No values, may or may not be set.

    def __init__(self, my_args: ap.Parser):
        my_args.check_names(self.REQUIRED_ARG_NAMES, self.OPTIONAL_ARG_NAMES)
        my_args.check_required_values_by_name(self.REQUIRED_ARG_VALUES)

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