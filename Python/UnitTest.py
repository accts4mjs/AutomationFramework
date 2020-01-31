from HelperFunctions import my_tdd, my_call_python
import os

# Check usage
test = "CHECK USAGE"
FILE_NAME = "Automator.py"
expected = "ERROR: '' invalid tool\n" \
            f"usage: {FILE_NAME} -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN " \
            "[<parmN_value>]]\nExamples:\n" \
            f"\t{FILE_NAME} -tool Sample -basedir <path> -filename <name> -version <file_version> -start " \
            "<start_date> -end <end_date>"
result = my_call_python(f"{FILE_NAME}")
my_tdd(result, expected, test)


# Check sample tool
test = "SAMPLE TOOL"
expected = "Hello World!\nbasedir = .\nfilename = foo\nversion = 10\nstart = 20200130\nend = 20200131"
result = my_call_python(f"{FILE_NAME} -tool Sample -basedir . -filename foo -version 10 -start 20200130 -end 20200131")
my_tdd(result, expected, test)
