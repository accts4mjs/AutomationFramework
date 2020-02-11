from HelperFunctions import tdd as ut_tdd, call_python as ut_call_python

FILE_NAME = "Automator.py"
USAGE = f"usage: {FILE_NAME} -tool <tool_name> [-parm1 [<parm1_value>] .. -parmN " \
        "[<parmN_value>]]\n" \
        "NOTE: Argument values are not required.  I.e. Argument names can be used without a value.\n" \
        "\tIf using a value it must immediately follow the argument name and not start with '-'\n" \
        f"Example:\n\t{FILE_NAME} -tool SampleTool -basedir <path> -filename <name> -version <file_version>" \
        " -start <start_date> -end <end_date>"

###########################################
# Check usage
###########################################
test = "CHECK USAGE - no args"
expected = f"ERROR: minimum # of args is 2, got '0'\n{USAGE}"
result = ut_call_python(f"{FILE_NAME}")
# print(f"{expected}\n"); print(result); ut_tdd(result, expected, test); exit(0)
ut_tdd(result, expected, test)

test = "CHECK USAGE - invalid value"
expected = f"ERROR: 'foobar' invalid tool\n{USAGE}"
result = ut_call_python(f"{FILE_NAME} -tool foobar")
ut_tdd(result, expected, test)

test = "CHECK USAGE - required arg"
# Updated USAGE because rest of tests use SampleTool
USAGE = f"usage: {FILE_NAME} -tool SampleTool -basedir <value> -filename <value> -version <value> -start <value> -end " \
        f"<value> [-r] [-m] [-foo <value>]\n" \
        "NOTE: Argument values are not required.  I.e. Argument names can be used without a value.\n" \
        "\tIf using a value it must immediately follow the argument name and not start with '-'\n" \
        f"Example:\n\t{FILE_NAME} -tool SampleTool -basedir <path> -filename <name> -version <file_version>" \
        " -start <start_date> -end <end_date>"
expected = f"ERROR: 'version' is a required argument\n{USAGE}"
result = ut_call_python(f"{FILE_NAME} -tool SampleTool -basedir . -filename")
ut_tdd(result, expected, test)

test = "CHECK USAGE - missing value"
expected = f"ERROR: 'basedir' requires a value\n{USAGE}"
result = ut_call_python(f"{FILE_NAME} -tool SampleTool -basedir -filename foo -version 10 -start 0 -end 1 -v")
ut_tdd(result, expected, test)

test = "CHECK USAGE - invalid arg"
expected = f"ERROR: 'v' is not a valid argument\n{USAGE}"
result = ut_call_python(f"{FILE_NAME} -tool SampleTool -basedir . -filename foo -version 10 -start 0 -end 1 -v")
ut_tdd(result, expected, test)

test = "CHECK USAGE - value with no arg name"
expected = f"ERROR: Arg value #7 'bar' not preceded by arg name.\n{USAGE}"
result = ut_call_python(f"{FILE_NAME} -tool SampleTool -basedir . -filename foo bar -version 10 -start 0 -end 1 -v")
ut_tdd(result, expected, test)

test = "CHECK USAGE - optional arg with missing required value"
expected = f"ERROR: 'foo' requires a value\n{USAGE}"
result = ut_call_python(f"{FILE_NAME} -tool SampleTool -basedir . -filename bar -version 10 -start 0 -end 1 -foo")
ut_tdd(result, expected, test)

###########################################
# Check SampleTool
###########################################
test = "SAMPLE TOOL - no optional args"
expected = "Hello World!\nbasedir = .\nfilename = foo\nversion = 10\nstart = 20200130\nend = 20200131\n" \
           "remove = False\nfoo = None"
result = ut_call_python(
    f"{FILE_NAME} -tool SampleTool -basedir . -filename foo -version 10 -start 20200130 -end 20200131")
ut_tdd(result, expected, test)

test = "SAMPLE TOOL - '-r' optional arg"
expected = "Hello World!\nbasedir = .\nfilename = foo\nversion = 10\nstart = 20200130\nend = 20200131\n" \
           "remove = True\nfoo = None"
result = ut_call_python(f"{FILE_NAME} -tool SampleTool -basedir . -filename foo -version 10 -start 20200130 "
                        "-end 20200131 -r")
ut_tdd(result, expected, test)

test = "SAMPLE TOOL - '-r' and '-foo bar' optional args"
expected = "Hello World!\nbasedir = .\nfilename = foo\nversion = 10\nstart = 20200130\nend = 20200131\n" \
           "remove = True\nfoo = bar"
result = ut_call_python(f"{FILE_NAME} -tool SampleTool -basedir . -filename foo -version 10 -start 20200130 "
                        "-end 20200131 -r -foo bar")
ut_tdd(result, expected, test)
