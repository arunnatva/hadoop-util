#!/bin/bash


if [[ $# -lt 2 ]];then
  echo -e "\n Usage : Pass two arguments to the script (1) alias (2) provider path\n"
  exit 0
fi
echo "Alias : $1"
echo "Provider : $2"
java -cp `hadoop classpath`:../lib/decrypt.jar com.hortonworks.util.DecryptionUtilDriver "$1" "$2"
