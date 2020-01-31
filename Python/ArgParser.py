import os
from ErrorHandling import ErrorHandler as err


class Parser:
    def __init__(self, arg_list):
        self.arg_pairs = {}
        self.arg_names = []
        script_name = os.path.basename(arg_list.pop(0))
        arg_string = " "
        arg_string = arg_string.join(arg_list)

        index = 0  # Already popped the script name from position 0 in the list
        num_args = len(arg_list)
        try:
            while index < num_args:
                # Format of arg list should be [-<arg_name> [<arg_value>] .. -<arg_name> [<arg_value>]]
                # Every arg name must start with '-'.  Arg values cannot start with '-'.  Arg values must follow an
                # arg name.
                # NOTE:  All arg names and arg values will be stored as lower case to make them case independent
                if arg_list[index][0] == "-":
                    self.arg_names.append(arg_list[index][1:].lower())  # Strip the '-' from the arg name
                    if index+1 < num_args and [index+1][0] != "-":
                        # Capture arg name and arg value (arg values do not start with '-')
                        self.arg_pairs[arg_list[index][1:].lower()] = arg_list[index+1].lower()
                        index += 1  # Skip the arg value in the iteration of arg names and arg values
                else:
                    # Reaching this condition means either the list started with an arg value or the list
                    # had two arg values in a row.  Both conditions are incorrect.
                    err.error_abort(f"ERROR: Arg value #{index+1} not preceded by arg name.\n{script_name}"
                                    f" {arg_string}", True)
        except IndexError:
            err.error_abort(f"ERROR: Incorrect argument list.\n{script_name} {arg_string}", True)

    def get_value(self, arg_name):
        # Although caller should use lower case, go ahead and force it lower to be case independent
        lower_name = arg_name.lower()
        if lower_name in self.arg_pairs:
            return self.arg_pairs[lower_name]
        else:
            return ""
