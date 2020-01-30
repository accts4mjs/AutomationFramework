import sys
import os
import ArgParser as ap
import ErrorHandling as err

class Automator:
    FNAME = os.path.basename(sys.argv[0])
    USAGE = f"usage: {FNAME} -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN " \
            "[<parmN_value>]]\nExamples:\n" \
            f"\t{FNAME} -tool Sample -basedir <path> -filename <name> -version <file_version> -start " \
            f"<start_date> -end <end_date>"

    def __init__(self):
        # Create the arg parser object with the sys.args list of arguments
        self.arg_parser = None
        return

    def init(self, arg_list):
        self.arg_parser = ap.Parser(arg_list)
        self.tool_list = self.arg_parser.get_function_names()

    def run(self):
        if len(self.tool_list) == 0:
            err.error_abort("No tools chosen", Automator.USAGE)

        for tool in self.tool_list:
            if tool['name'] == "Sample":
                import SampleTool as st
                tool_object = st.Sample_Tool(self.arg_parser)
                tool_object.run()
            else:
                err.error_continue(f"'{tool.name}' invalid tool")
        return


def main():
    the_automator = Automator()
    the_automator.init(sys.argv)
    the_automator.run()


if __name__ == "__main__":
    main()
