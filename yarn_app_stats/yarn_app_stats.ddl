DROP TABLE IF EXISTS YARN_APP_STATS;
CREATE TABLE IF NOT EXISTS YARN_APP_STATS (
id string
,name string
,queue string
,yarn_user string
,applicationType string
,state string
,elapsedTime string
,memorySeconds bigint
,vcoreSeconds bigint
,startedTime string
,finishedTime string
,finalStatus string
,trackingUrl string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|'
;
