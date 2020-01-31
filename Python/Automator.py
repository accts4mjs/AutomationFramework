import sys
import os
import ArgParser as ap
from ErrorHandling import ErrorHandler as err


class Automator:
    FILE_NAME = os.path.basename(sys.argv[0])
    # ADDTOOL:  Add an example of using your tool with any required or optional parameters.
    #   Each new tool usage line should start with f"\t{FILE_NAME} -tool <your_tool_name> ..
    USAGE = f"usage: {FILE_NAME} -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN " \
            "[<parmN_value>]]\nExamples:\n" \
            f"\t{FILE_NAME} -tool Sample -basedir <path> -filename <name> -version <file_version> -start " \
            f"<start_date> -end <end_date>"

    def __init__(self):
        # Create the arg parser object with the sys.args list of arguments.  This will be used by each tool
        # module to generate the options and data it will need.
        err.set_usage_message(self.USAGE)
        self.arg_parser = ap.Parser(sys.argv)
        self.tool_name = self.arg_parser.get_value("tool")
        return

    def run(self):
        # ADDTOOL: This is where you will add your tool creation and call for a new tool.
        #   Follow the "Sample" example (used for unit test of framework).  Import the module file,
        #   create the tool object and pass it the arg_parser, then run the tool.
        #   NOTE: All names and values are stored lower case.  Be sure to do comparisons with lower case.
        if self.tool_name == "sample":
            import SampleTool as st
            tool_object = st.SampleTool(self.arg_parser)
            tool_object.run()
        else:
            err.error_abort(f"ERROR: '{self.tool_name}' invalid tool", True)

        return


def main():
    the_automator = Automator()
    the_automator.run()


if __name__ == "__main__":
    main()
