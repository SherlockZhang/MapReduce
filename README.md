# MapReduce

The mapper.py function is modified to use regular expression to search for a specific word pattern. To use the regular expression, just change the input argument in the py_runner.sh file in the mapper function line.

1. For example, count word contain "oo", change py_runner.sh file to:


```
#!/bin/bash

/etc/bootstrap.sh
THIS_DIR=/usr/local/hadoop

if [ -n "$1" ];
then SUB_DIR="$1/" 
fi


${THIS_DIR}/bin/hadoop dfsadmin -safemode leave
${THIS_DIR}/bin/hadoop fs -mkdir -p ${THIS_DIR}/sample
${THIS_DIR}/bin/hdfs dfs -put ${THIS_DIR}/py/${SUB_DIR}sample/* ${THIS_DIR}/sample
${THIS_DIR}/bin/hadoop jar \
${THIS_DIR}/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-file ${THIS_DIR}/py/${SUB_DIR}mapper.py \
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py oo*"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
```

Output will be:

foo 6

2. For example, begin with "f" and end with "o"

py_runner.sh file:

```
#!/bin/bash

/etc/bootstrap.sh
THIS_DIR=/usr/local/hadoop

if [ -n "$1" ];
then SUB_DIR="$1/" 
fi


${THIS_DIR}/bin/hadoop dfsadmin -safemode leave
${THIS_DIR}/bin/hadoop fs -mkdir -p ${THIS_DIR}/sample
${THIS_DIR}/bin/hdfs dfs -put ${THIS_DIR}/py/${SUB_DIR}sample/* ${THIS_DIR}/sample
${THIS_DIR}/bin/hadoop jar \
${THIS_DIR}/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-file ${THIS_DIR}/py/${SUB_DIR}mapper.py \
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py oo*"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
```

Output will be:

foo 6

3. For example, count word with 1 capital letter.

py_runner.sh file:

```
#!/bin/bash

/etc/bootstrap.sh
THIS_DIR=/usr/local/hadoop

if [ -n "$1" ];
then SUB_DIR="$1/" 
fi


${THIS_DIR}/bin/hadoop dfsadmin -safemode leave
${THIS_DIR}/bin/hadoop fs -mkdir -p ${THIS_DIR}/sample
${THIS_DIR}/bin/hdfs dfs -put ${THIS_DIR}/py/${SUB_DIR}sample/* ${THIS_DIR}/sample
${THIS_DIR}/bin/hadoop jar \
${THIS_DIR}/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-file ${THIS_DIR}/py/${SUB_DIR}mapper.py \
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py oo*"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
```

Output will be:

(Actually it is empty, because no word in the data has any capital letter)
