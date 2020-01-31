Modularized automation framework.  Can be used to setup and run multiple tools or a single tool.  
Has built in code for parsing arguments, error handling, and a simple interface for adding new tools.

Steps for adding an additional tool via a python module.  All examples are using the "CheckMissingFiles.py" example.
1. Copy the "SampleTool.py" file and rename it to your tool name "CheckMissingFiles.py"
2. Open your CheckMissingFiles.py file and rename the class from SampleTool to CheckMissingFiles
3. Update the class variables to include the required arg names, values, optional args, and optional args with values.
4. Change the __init__ constructor to load your arguments based on what's required, optional, etc.
5. Change the run() function to perform whatever logic you want to achieve.
6. If you need to do any asserts or other error logic or messaging, please use the "ErrorHandling.py" module.  There are multiple
   examples throughout the "Automator.py" file.
7. Open the "Automator.py" file and search for each instance of "ADDTOOL" comments.  
   7.1. Follow the instructions to add your usage
        examples (note:  Usage examples should be appended to the USAGE variable, not replace existing ones -- this allows for multiple 
        tools to extend the Automator object to have any number of optional functional tools).
   7.2. And an "elif self.tool_name == "checkmissingfiles":" statement along with the expressions to import your module, 
        create your object passing in the arg_parser and then run() the object.
8. Update the unit test file by first adding any new text you added to the Automator.USAGE string to the BASE_USAGE string.
9. Run the unit tests (should pass once you've updated the BASE_USAGE string).  Fix if needed.
10. At the bottom of the "UnitTest.py" file be sure to add your own unit tests.  Follow the example of the Sample tool as needed.
