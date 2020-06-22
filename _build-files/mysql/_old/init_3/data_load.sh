# csvロードの対応
# docker-compose＋MySQL8（8.0.18）で初期データをCSVロードしようとするとエラー
# LOAD DATA LOCAL INFILEを実行するとエラー
mysql -umysqluser -pmysqluser00 mydb --local-infile=1 -e "LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/data.csv' INTO TABLE m_sample FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"
