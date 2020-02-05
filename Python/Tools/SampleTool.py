import ErrorHandling as err
import Tools.ToolParent as tp


# ADDTOOL: Copy this entire file and rename it to the name of your tool.  Then rename the "SampleTool" class to the
#   name of your tool as well.  Update the 3 class ARG variables with the list of required arg names, arg names that
#   will have values and any optional arg_names.
class SampleTool(tp.ToolParent):
    REQUIRED_ARG_NAMES = ['basedir', 'filename', 'version', 'start', 'end']
    # Arg names that must have values.  May be the complete set of REQUIRED_ARG_NAMES or may be a subset
    REQUIRED_ARG_VALUES = ['basedir', 'filename', 'version', 'start', 'end']
    # These are args that are usually flags (do not require values, but may have them).  May or may not be set
    OPTIONAL_ARG_NAMES = ['r', 'm', 'foo']
    OPTIONAL_ARG_VALUES = ['foo']  # These are args that are optional but do require a value if set

    def __init__(self, script_call_string, arg_list):
        my_args.check(self.REQUIRED_ARG_NAMES, self.REQUIRED_ARG_VALUES, self.OPTIONAL_ARG_NAMES,
                      self.OPTIONAL_ARG_VALUES)

        # load argument information into object variables
        self.basedir = my_args.get_value('basedir')
        self.filename = my_args.get_value('filename')
        self.version = my_args.get_value('version')
        self.start = my_args.get_value('start')
        self.end = my_args.get_value('end')
        if my_args.optional_arg_set('r'):
            self.remove = True
        else:
            self.remove = False
        if my_args.optional_arg_set('foo'):
            self.foo = my_args.get_value('foo')
        else:
            self.foo = None
        return

    def run(self):
        print("Hello World!")
        print(f"basedir = {self.basedir}")
        print(f"filename = {self.filename}")
        print(f"version = {self.version}")
        print(f"start = {self.start}")
        print(f"end = {self.end}")
        print(f"remove = {self.remove}")
        print(f"foo = {self.foo}")