$ cat yarn_appstats.sh
#!/bin/bash


CSV_FILENAME=$(cat ../conf/dev-app.conf | grep output_file | cut -d'=' -f2)

CSVFILE_PATH="$HOME""/""$CSV_FILENAME"
echo "$CSVFILE_PATH"

### INVOKE THE PYTHON CODE TO EXTRACT YARN APP STATS INTO CSV FILE
/opt/anaconda3/envs/pyenv/bin/python ../src/extract_yarn_app_stats.py ../conf/dev-app.conf

### COPY DATA INTO HDFS FILE
CSV_HDFS_PATH="/user/$USER/""$CSV_FILENAME"
hadoop fs -put -f "$CSVFILE_PATH" "$CSV_HDFS_PATH"

### LOAD DATA INTO HIVE STAGING TABLE
/bin/beeline -u "$HIVE_CON" -e "TRUNCATE TABLE YARN_APP_STATS_STG"
/bin/beeline -u "$HIVE_CON" -e "LOAD DATA INPATH '""$CSV_HDFS_PATH""' INTO TABLE YARN_APP_STATS_STG"

### LOAD DATA FROM STAGING TO FINAL TABLE
/bin/beeline -u "$HIVE_CON" -e "INSERT INTO TABLE YARN_APP_STATS_STG SELECT * FROM YARN_APP_STATS"
/bin/beeline -u "$HIVE_CON" -e "INSERT OVERWRITE TABLE YARN_APP_STATS SELECT DISTINCT * FROM YARN_APP_STATS_STG"
