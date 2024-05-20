This directory includes two files:
- 'custom_module': displays the digits of pi from the pi_module
- 'pi_module': defines digits of pi

The 'custom_module' file imports 'pi_module' to demonstrate how users can import Python files amongst other Python programs.

To import a file, the following syntax is required:
- import name_of_file
- Ex. import pi_module

To use a custom variable from an imported file, the following syntax is required:
- name_of_file.name_of_variable
- Ex. pi_module.pi

To use a custom function from an imported file, the following syntax is required:
- name_of_file.name_of_function()
- Ex. pi_module.do_something()
