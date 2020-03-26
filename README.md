# MapReduce

The mapper.py function is modified to support those three rules with generic values. To use each rules, just change the input argument in the py_runner.sh file in the mapper function line.

1. First selection cretiron: count word with certain string. For example, count word contain "oo", change py_runner.sh file to:

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
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py 1 oo"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
```
The first argument 1 means to use rule 1, the second argument means search "oo" with rule 1. Output will be:

foo 6

2. Second selectin cretion: count word begin with one letter and end with another letter. For example, begin with "f" and end with "o"

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
+-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py 2 f o"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
```

The first argument 2 means to use rule 2; 
the second argument means to search word starts with "f";
the third argument means to search word ends with "o". 

Output will be:

foo 6

3. Third cretiron: count word with certain number of capital letter. For example, count word with 1 capital letter.

y_runner.sh file:

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
+-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py 3 1"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
```

The first argument 3 means to use rule 3;
the second argument means how many capital letter is required, here it is 1

Output will be:

(Actually it is empty, because no word in the data has any capital letter)
