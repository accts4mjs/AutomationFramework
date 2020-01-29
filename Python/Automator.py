import ArgParser as ap
import sys
import ErrorHandling as err

class Automator:
    def __init__(self):
        # Create the arg parser object with the sys.args list of arguments
        self.arg_parser = None
        return

    def init(self, arg_list):
        self.arg_parser = ap.Parser(arg_list)
        self.tool_list = self.arg_parser.get_function_names()

    def run(self):
        if len(self.tool_list) == 0:
            err.error_abort("No tools chosen")

        for tool in self.tool_list:
            if tool['name'] == "Sample":
                import SampleTool as st
                tool_object = st.Sample_Tool()
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