import sys
import os
import importlib
from ErrorHandling import ErrorHandler as err


class Automator:
    FILE_NAME = os.path.basename(sys.argv[0])
    USAGE_NOTE = "NOTE: Argument values are not required.  I.e. Argument names can be used without a value.\n" \
                 "\tIf using a value it must immediately follow the argument name and not start with '-'"
    USAGE_EXAMPLE = f"Example:\n\t{FILE_NAME} -tool SampleTool -basedir <path> -filename <name> -version " \
                    "<file_version> -start <start_date> -end <end_date>"
    DEFAULT_USAGE = f"-tool <tool_name> [-parm1 [<parm1_value>] .. -parmN [<parmN_value>]]"

    def __init__(self):
        # Identify the full list of tools available (each tool will be in the tool dir of the <tool_name>.py format).
        # Then scan the argument list looking for the tool name and if it matches one of the tools, load it, initialize
        # it and run it.
        err.set_file_name(self.FILE_NAME)
        err.set_note(self.USAGE_NOTE)
        err.set_example(self.USAGE_EXAMPLE)
        err.set_usage_message(self.DEFAULT_USAGE)
        self.arg_list = sys.argv[1:]  # Skip script name, already stored
        err.set_script_call_string(f"{self.FILE_NAME} {' '.join(self.arg_list)}")
        self.tool_name = self.get_tool_name()
        self.tool_list = Automator.get_tool_list_from_tools_dir()

    def get_tool_name(self):
        num_args = len(self.arg_list)
        err.assert_abort(num_args >= 2, f"ERROR: minimum # of args is 2, got '{num_args}'", True)

        if self.arg_list[0] == "-tool":
            # Check next arg and see if it is a value or another arg name
            if self.arg_list[1][0] != '-':  # A '-' would indicate another argument name, not a value
                name = self.arg_list[1]
                # Remove the tool flag and value from the arg_list (tool creation won't need it)
                self.arg_list.pop(0)
                self.arg_list.pop(0)  # 0 again because you just popped the previous 0 item.
                return name
            else:
                err.error_abort(f"ERROR: Tool name has '-' in it '{self.arg_list[1]}'", True)
        else:
            err.error_abort(f"ERROR: Incorrect syntax: '{err.get_call_script_string()}'", True)

    @staticmethod
    def get_tool_list_from_tools_dir():
        # All tools should be stored in the 'Tools' dir that is a child of the current dir
        base_path = "Tools"
        tool_list = []
        with os.scandir(base_path) as entries:
            for entry in entries:
                # Only store files that end in .py and ignore abstract ToolParent class
                if entry.is_file() and entry.name.endswith(".py") and entry.name != "ToolParent.py":
                    tool_list.append(entry.name[:-3])  # Remove the '.py' from the end of the string
        return tool_list

    def run(self):
        # Check that the requested tool (tool_name) is in the Tools directory (tool_list).
        # Load the tool's module, get its class (same name as tool name), instantiate the class, and run it.
        if self.tool_name in self.tool_list:
            module = importlib.import_module(f"Tools.{self.tool_name}")
            tool_class = getattr(module, self.tool_name)
            tool_object = tool_class(f"{self.FILE_NAME} -tool {self.tool_name} {' '.join(self.arg_list)}",
                                     self.arg_list)
            tool_object.run()
        else:
            err.error_abort(f"ERROR: '{self.tool_name}' invalid tool", True)


def main():
    the_automator = Automator()
    the_automator.run()


if __name__ == "__main__":
    main()
