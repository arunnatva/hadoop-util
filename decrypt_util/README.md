### This Utility is written to decrypt the credentials given that the user has read access to the jceks file and the Alias.
### Making the source code of the utility available to everyone warrants that the jceks files are protected with utmost care and only developers of a given application should have read access to the jcecks file.

### The hdfs home directory of the service account associated with an application is the right place to store the jceks file

### The permissions should be 400 which will prevent anyone from reading the jceks file.

### The script to build the jar is in scripts/build.sh
### The script to run the jar is scripts/getpass.sh
