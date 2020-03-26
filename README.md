# MapReduce

The mapper.py function is modified to use regular expression to search for a specific word pattern. To use the regular expression, just change the input argument in the py_runner.sh file in the mapper function line.

1. For example, count word contain "oo", change py_runner.sh file to:

<<<<<<< HEAD
=======
```
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
#!/bin/bash

/etc/bootstrap.sh
THIS_DIR=/usr/local/hadoop

if [ -n "$1" ];
then SUB_DIR="$1/" 
fi

<<<<<<< HEAD
'''diff
=======
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
${THIS_DIR}/bin/hadoop dfsadmin -safemode leave
${THIS_DIR}/bin/hadoop fs -mkdir -p ${THIS_DIR}/sample
${THIS_DIR}/bin/hdfs dfs -put ${THIS_DIR}/py/${SUB_DIR}sample/* ${THIS_DIR}/sample
${THIS_DIR}/bin/hadoop jar \
${THIS_DIR}/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-file ${THIS_DIR}/py/${SUB_DIR}mapper.py \
<<<<<<< HEAD
<<<<<<< HEAD
+-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py 1 oo"\
=======
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py 1 oo"\
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
=======
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py oo*"\
>>>>>>> dbb5fa312c67f9f047e7c394e448176b9e106e6e
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
<<<<<<< HEAD
'''
=======
```
<<<<<<< HEAD
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
The first argument 1 means to use rule 1, the second argument means search "oo" with rule 1. Output will be:
=======
Output will be:
>>>>>>> dbb5fa312c67f9f047e7c394e448176b9e106e6e

foo 6

2. For example, begin with "f" and end with "o"

py_runner.sh file:

<<<<<<< HEAD
=======
```
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
#!/bin/bash

/etc/bootstrap.sh
THIS_DIR=/usr/local/hadoop

if [ -n "$1" ];
then SUB_DIR="$1/" 
fi

<<<<<<< HEAD
'''diff
=======
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
${THIS_DIR}/bin/hadoop dfsadmin -safemode leave
${THIS_DIR}/bin/hadoop fs -mkdir -p ${THIS_DIR}/sample
${THIS_DIR}/bin/hdfs dfs -put ${THIS_DIR}/py/${SUB_DIR}sample/* ${THIS_DIR}/sample
${THIS_DIR}/bin/hadoop jar \
${THIS_DIR}/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-file ${THIS_DIR}/py/${SUB_DIR}mapper.py \
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py ^f.*o$"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
<<<<<<< HEAD
'''
=======
```
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef

Output will be:

foo 6

3. For example, count word with 1 capital letter.

py_runner.sh file:

<<<<<<< HEAD
=======
```
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
#!/bin/bash

/etc/bootstrap.sh
THIS_DIR=/usr/local/hadoop

if [ -n "$1" ];
then SUB_DIR="$1/" 
fi

<<<<<<< HEAD
'''diff
=======
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
${THIS_DIR}/bin/hadoop dfsadmin -safemode leave
${THIS_DIR}/bin/hadoop fs -mkdir -p ${THIS_DIR}/sample
${THIS_DIR}/bin/hdfs dfs -put ${THIS_DIR}/py/${SUB_DIR}sample/* ${THIS_DIR}/sample
${THIS_DIR}/bin/hadoop jar \
${THIS_DIR}/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-file ${THIS_DIR}/py/${SUB_DIR}mapper.py \
-mapper "${THIS_DIR}/py/${SUB_DIR}mapper.py [A-Z]{1}"\
-file ${THIS_DIR}/py/${SUB_DIR}reducer.py    \
-reducer "${THIS_DIR}/py/${SUB_DIR}reducer.py ${*:2}" \
-input ${THIS_DIR}/sample/* \
-output ${THIS_DIR}/py-output
${THIS_DIR}/bin/hdfs dfs -cat ${THIS_DIR}/py-output/*
<<<<<<< HEAD
'''
=======
```

<<<<<<< HEAD
>>>>>>> 1b1aae75823f3fd7dc7b77d4b981f7c693baf9ef
The first argument 3 means to use rule 3;
the second argument means how many capital letter is required, here it is 1

=======
>>>>>>> dbb5fa312c67f9f047e7c394e448176b9e106e6e
Output will be:

(Actually it is empty, because no word in the data has any capital letter)
