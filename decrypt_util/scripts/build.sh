#!/bin/bash
javac -d ../ -cp `hadoop classpath` ../src/com/hortonworks/util/DecryptionUtilDriver.java
jar cvf ../lib/decrypt.jar ../com/hortonworks/util/DecryptionUtilDriver.class
