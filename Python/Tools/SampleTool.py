from ErrorHandling import ErrorHandler as err
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
        super().__init__(arg_list)  # Always call parent constructor
        super().set_err_usage(self.REQUIRED_ARG_NAMES, self.REQUIRED_ARG_VALUES, self.OPTIONAL_ARG_NAMES,
                      self.OPTIONAL_ARG_VALUES)
        self.validate_arguments(self.REQUIRED_ARG_NAMES, self.REQUIRED_ARG_VALUES, self.OPTIONAL_ARG_NAMES,
                      self.OPTIONAL_ARG_VALUES)

        # load argument information into object variables
        try:
            self.basedir = self.get_value('basedir')
            self.filename = self.get_value('filename')
            self.version = self.get_value('version')
            self.start = self.get_value('start')
            self.end = self.get_value('end')
            if self.optional_arg_set('r'):
                self.remove = True
            else:
                self.remove = False
            if self.optional_arg_set('foo'):
                self.foo = self.get_value('foo')
            else:
                self.foo = None
        except Exception as e:
            err.error_abort(e, True)
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

    def validate_arguments(self, name_list, value_name_list, optional_name_list, optional_value_list):
        # Call parent validation first (generic but useful validation)
        super().validate_arguments(name_list, value_name_list, optional_name_list, optional_value_list)

        # Now perform validation as needed for this custom tool
