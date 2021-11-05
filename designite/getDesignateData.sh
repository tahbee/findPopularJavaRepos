#!/bin/bash
for path in /Users/melissaheredia/metrics-workspace/projects/*;

# /Users/melissaheredia/.m2/repository/DesigniteJava/DesigniteJava/CommunityEdition/DesigniteJava.jar
do
  file_name="$(basename -s .csv $path)"
  java -jar  /Users/melissaheredia/.m2/repository/DesigniteJava/DesigniteJava/1.1.2/DesigniteJava-1.1.2.jar -i /Users/melissaheredia/metrics-workspace/projects/$file_name -o /Users/melissaheredia/metrics-workspace/designite/$file_name
done