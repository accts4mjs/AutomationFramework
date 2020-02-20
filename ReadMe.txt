Modularized automation framework.  Can be used to setup and run any number of tools.
Has built in code for parsing arguments, error handling, and a simple interface for adding new tools as described
below.

Steps for adding an additional tool via a python module.  All examples are using a "YourTool.py" example.
1. Copy the "SampleTool.py" file in the "Tools" dir and rename it to your tool name "YourTool.py"
2. Open the "YourTool.py" file and rename the class from SampleTool to YourTool
3. Update the class variables under the first "TODO" section to include any required arg names, values, optional args, and optional args with values.  NOTE:  Be sure to remove the SampleTool arg names and values.
4. In the second "TODO" section, change the __init__ constructor to load your arguments based on what's required, optional, etc
5. Change the validate_arguments() method to do any additional validation on your arguments.  The base class method will validate required arguments are there, arg names match your list from #3 above.  If you need to check for constraints on values for arguments or the right combination of optional args, you would do it in this method.
6. Change the run() function to perform whatever logic you want to achieve.
6. If you need to do any asserts or other error logic or messaging, please use the "ErrorHandling.py" module.  There
   are multiple examples throughout the "Automator.py" file.
7. At the bottom of the "UnitTest.py" file be sure to add your own unit tests.  Follow the example of the SampleTool
    as needed.
8. Run the unit tests (should pass once you've updated the BASE_USAGE string).  Fix if needed.
