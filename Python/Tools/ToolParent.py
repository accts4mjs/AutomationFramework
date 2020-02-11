from abc import ABC, abstractmethod
from ErrorHandling import ErrorHandler as err


class ToolParent(ABC):
    def __init__(self, arg_list):
        self.arg_pairs = {}
        self.arg_names = []

        index = 0
        num_args = len(arg_list)
        try:
            while index < num_args:
                # Format of arg list should be [-<arg_name> [<arg_value>] .. -<arg_name> [<arg_value>]]
                # Every arg name must start with '-'.  Arg values are optional.  Arg values cannot start with '-'.
                # Arg values must follow an arg name.
                # NOTE:  All arg names and arg values will be stored as lower case to make them case independent
                if arg_list[index][0] == "-":
                    arg_name_without_dash = arg_list[index][1:].lower()  # [1:] notation means char 1 forward (0 based)
                    # All arg names are stored in arg_names list
                    self.arg_names.append(arg_name_without_dash)

                    # If there are more args, do a quick look ahead to see if next item is another arg name (will start
                    # with '-') or if it's an arg value (no '-').  Store arg value and arg name in arg_pairs.
                    next_arg_index = index + 1
                    if next_arg_index < num_args and arg_list[next_arg_index][0] != "-":
                        self.arg_pairs[arg_name_without_dash] = arg_list[next_arg_index].lower()
                        index += 1  # Skip the arg value in the iteration of arg names and arg values
                    index += 1  # Move to the next arg name
                else:
                    # Reaching this condition means either the list started with an arg value or the list
                    # had two arg values in a row.  Both conditions are incorrect.
                    # index + 3 is used because 0 = script name, 1 = '-tool', 2 = tool name.
                    err.error_abort(f"ERROR: Arg value #{index+3} '{arg_list[index]}' not preceded by arg name.",
                                    True)
        except IndexError:
            err.error_abort(f"ERROR: Incorrect argument list.\n{err.get_call_script_string()}", True)

    def get_value(self, arg_name):
        # Although caller should use lower case, go ahead and force it lower to be case independent
        lower_name = arg_name.lower()
        if lower_name in self.arg_pairs:
            return self.arg_pairs[lower_name]
        else:
            raise Exception(f"ERROR: '{arg_name}' does not have a value pair")

    @abstractmethod
    def validate_arguments(self, name_list, value_name_list, optional_name_list, optional_value_list):
        # Make all names lower case (do not change values)
        for local_list in (name_list, value_name_list, optional_name_list, optional_value_list):
            index = 0
            while index < len(local_list):
                local_list[index] = local_list[index].lower()
                index += 1

        for name in name_list:
            err.assert_abort(name in self.arg_names, f"ERROR: '{name}' is a required argument", True)
        for name in value_name_list:
            err.assert_abort(name in self.arg_pairs, f"ERROR: '{name}' requires a value", True)
        # Optional name list is a bit trickier.  Need to remove all required names first then compare
        # each optional name to the optional list.  I.e. are the non-required names in the list 'allowed'
        # by the optional list?
        remaining_names = []
        for name in self.arg_names:
            if name not in name_list:
                remaining_names.append(name)
        for name in remaining_names:
            err.assert_abort(name in optional_name_list, f"ERROR: '{name}' is not a valid argument", True)
            # Is a valid optional arg.  If also in optional_value_list then it must have a value
            if name in optional_value_list:
                err.assert_abort(name in self.arg_pairs, f"ERROR: '{name}' requires a value", True)

    def optional_arg_set(self, optional_arg):
        return optional_arg.lower() in self.arg_names

    def set_err_usage(self, required_arg_names, required_arg_values, optional_arg_names, optional_arg_values):
        pass
