**Instructions to run god class calculations script**
*The number of god classes for each repository should have already been found as a prerequisite to this script and this script should have been downloaded in local machine already*
1) Open terminal or anything equivalent to run the script.
2) Go to the directory of where the script is located. The command should start with cd with trailing whitespace followed by the name of directory(cd <DirectoryName>). For example, cd Desktop is the command to enter the Desktop directory.
3) Run the following command: python godClassCalc.py
3) Enter the number of the god classes found for each repository in the godClassMetricsInput array in god_class_calc.py. The numbers should be entered with comma and trailing space to separate each number.
4) Run the god_class_calc.py script to get metrics for the number of god classes found per repository for this tool.

Note: This script is meant to be run separately for the data from each static code analysis tool (i.e. once for PMD data, Jdeodorant data, and Embold data)
