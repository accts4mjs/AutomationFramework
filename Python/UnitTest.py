from HelperFunctions import my_tdd, my_call_python
import os

FILE_NAME = "Automator.py"

# Check usage
test = "CHECK USAGE - no args"
expected = "ERROR: '' invalid tool\n" \
            f"usage: {FILE_NAME} -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN " \
            "[<parmN_value>]]\nExamples:\n" \
            f"\t{FILE_NAME} -tool Sample -basedir <path> -filename <name> -version <file_version> -start " \
            "<start_date> -end <end_date>"
result = my_call_python(f"{FILE_NAME}")
my_tdd(result, expected, test)
test = "CHECK USAGE - invalid value"
expected = "ERROR: 'foobar' invalid tool\n" \
            "usage: Automator.py -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN [<parmN_value>]]\n" \
            "Examples:\n\tAutomator.py -tool Sample -basedir <path> -filename <name> -version <file_version> " \
            "-start <start_date> -end <end_date>"
result = my_call_python(f"{FILE_NAME} -tool foobar")
my_tdd(result, expected, test)
test = "CHECK USAGE - required arg"
expected = "ERROR: 'version' is a required argument\n" \
            "usage: Automator.py -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN [<parmN_value>]]\n" \
            "Examples:\n\tAutomator.py -tool Sample -basedir <path> -filename <name> -version <file_version> " \
            "-start <start_date> -end <end_date>"
result = my_call_python(f"{FILE_NAME} -tool sample -basedir . -filename")
my_tdd(result, expected, test)
test = "CHECK USAGE - missing value"
expected = "ERROR: 'basedir' requires a value\n" \
            "usage: Automator.py -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN [<parmN_value>]]\n" \
            "Examples:\n\tAutomator.py -tool Sample -basedir <path> -filename <name> -version <file_version> " \
            "-start <start_date> -end <end_date>"
result = my_call_python(f"{FILE_NAME} -tool sample -basedir -filename foo -version 10 -start 0 -end 1 -v")
my_tdd(result, expected, test)
test = "CHECK USAGE - invalid arg"
expected = "ERROR: 'v' is not a valid argument\n" \
            "usage: Automator.py -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN [<parmN_value>]]\n" \
            "Examples:\n\tAutomator.py -tool Sample -basedir <path> -filename <name> -version <file_version> " \
            "-start <start_date> -end <end_date>"
result = my_call_python(f"{FILE_NAME} -tool sample -basedir . -filename foo -version 10 -start 0 -end 1 -v")
my_tdd(result, expected, test)
test = "CHECK USAGE - value with no arg name"
expected = "ERROR: Arg value #7 'bar' not preceded by arg name.\n" \
            "usage: Automator.py -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN [<parmN_value>]]\n" \
            "Examples:\n\tAutomator.py -tool Sample -basedir <path> -filename <name> -version <file_version> " \
            "-start <start_date> -end <end_date>"
result = my_call_python(f"{FILE_NAME} -tool sample -basedir . -filename foo bar -version 10 -start 0 -end 1 -v")
my_tdd(result, expected, test)


# Check sample tool
test = "SAMPLE TOOL"
expected = "Hello World!\nbasedir = .\nfilename = foo\nversion = 10\nstart = 20200130\nend = 20200131"
result = my_call_python(f"{FILE_NAME} -tool Sample -basedir . -filename foo -version 10 -start 20200130 -end 20200131")
my_tdd(result, expected, test)
