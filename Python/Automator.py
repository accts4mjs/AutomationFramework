import sys
import os
from ErrorHandling import ErrorHandler as err


class Automator:
    FILE_NAME = os.path.basename(sys.argv[0])
    USAGE = f"usage: {FILE_NAME} -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN " \
            "[<parmN_value>]]\nNOTE: Argument values are not required.  I.e. Argument names can be used without a " \
            " value.  If using a value it must immediately follow the argument name and not start with '-'\n" \
            "Examples:\n" \
            f"\t{FILE_NAME} -tool SampleTool -basedir <path> -filename <name> -remove"

    def __init__(self):
        # Identify the full list of tools available (each tool will be in the tool dir of the <tool_name>.py format).
        # Then scan the argument list looking for the tool name and if it matches one of the tools, load it, initialize
        # it and run it.
        err.set_usage_message(self.USAGE)
        self.arg_list = sys.argv[1:]  # Skip script name, already stored
        err.set_script_call_string(f"{self.FILE_NAME} {' '.join(self.arg_list)}")
        self.tool_name = self.get_tool_name()
        self.tool_list = Automator.get_tool_list()

    def get_tool_name(self):
        num_args = len(self.arg_list)
        if num_args < 2:
            err.error_abort(f"ERROR: minimum # of args is 2, got '{num_args}'", True)

        if self.arg_list[0] == "-tool":
            if self.arg_list[1][0] != '-':  # A '-' would indicate another argument name, not a value
                name = self.arg_list[1]
                # Remove the tool flag and value from the arg_list (tool creation won't need it)
                self.arg_list.pop(0)
                self.arg_list.pop(1)
                return name
            else:
                err.error_abort(f"ERROR: Tool name has '-' in it '{self.arg_list[1]}'", True)
        else:
            err.error_abort(f"ERROR: Incorrect syntax: '{err.get_call_script_string()}'", True)

    @staticmethod
    def get_tool_list():
        # All tools should be stored in the 'Tools' dir that is a child of the current dir
        base_path = "./Tools"
        tool_list = []
        with os.scandir(base_path) as entries:
            for entry in entries:
                # Only store files that end in .py
                if entry.is_file() and entry.name.endswith(".py"):
                    tool_list.append(entry.name[:-3])  # Remove the '.py' from the end of the string
        return tool_list

    def run(self):
        # Check that the requested tool (tool_name) is in the Tools directory (tool_list).
        # Load the tool's module, get its class (same name as tool name), instantiate the class, initialize it, and
        # run it.
        if self.tool_name in self.tool_list:
            module = __import__(f"Tools.{self.tool_name}")
            tool_class = getattr(module, self.tool_name)
            tool_object = tool_class(f"{self.FILE_NAME} -tool {self.tool_name} {' '.join(self.arg_list)}",
                                     self.arg_list)
            tool_object.initialize()
            tool_object.run()
        else:
            err.error_abort(f"ERROR: '{self.tool_name}' invalid tool", True)


def main():
    the_automator = Automator()
    the_automator.run()


if __name__ == "__main__":
    main()
