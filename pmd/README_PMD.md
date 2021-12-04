**Instructions to run PMD script**
1) Clone projects you want to analyze to a local project directory(manually or using the clone script) and build them for best results
2) Update path in getPmdData.sh to point the local project directory
3) Update metrics_directory in pmd_automation.py to point to the temp directory where the pmd results should get stored
4) Run the script to get an excel file of pmd metrics with code smells listed for all of the projects in the local project directory


Note: Update rules.xml for more  rules if needed. Right now, the script is using pmd default design rules to detect code smells