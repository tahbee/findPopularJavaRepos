#!/bin/bash
for path in /Users/melissaheredia/metrics-workspace/projects/*;
do
  file_name="$(basename -s .csv $path)"
  $HOME/pmd-bin-6.39.0/bin/run.sh pmd -d $path -R rules.xml -f csv -cache cache/cache.txt > metrics/file_name.csv ;
done