# Custom Module Implementation

Note: use the math module if you are looking to calculate using pi. This is only an example of how to import custom programs.

This directory includes two files:
- 'import_custom': displays the digits of pi from the pi_module
- 'pi_module': defines digits of pi

The 'import_custom' file imports 'pi_module' to demonstrate how users can import Python files amongst other Python programs.

To import a file, the following syntax is required:
- import name_of_file
- Ex. import pi_module

To use a custom variable from an imported file, the following syntax is required:
- name_of_file.name_of_variable
- Ex. pi_module.pi

To use a custom function from an imported file, the following syntax is required:
- name_of_file.name_of_function()
- Ex. pi_module.do_something()
