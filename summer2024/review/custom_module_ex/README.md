This directory includes two files:
- 'custom_module': displays the digits of pi from the pi_module
- 'pi_module': defines digits of pi

The 'custom_module' file imports 'pi_module' to demonstrate how user's can import files amongst other files.

To import a file, the following syntax is required:
"import <insert the file name here>"
Ex. import pi_module

To use a custom variable from an imported file, the following syntax is required:
"<insert the file name here>.<name of variable>"
Ex. pi_module.pi

To use a custom function from an imported file, the following syntax is required:
"<insert the file name here>.<name of function>()"
Ex. pi_module.do_something()
