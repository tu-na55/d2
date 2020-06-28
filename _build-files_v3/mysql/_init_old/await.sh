# ${DB_HOST}や${DB_USERNAME}...等は適切に書き換えてください。コンテナにmysqlコマンドがインストールされている必要があります
MYSQLCMDBASE="mysql --host=${DB_HOST} --port=${DB_PORT:-3306} -ns --user=${DB_USERNAME} --password=${DB_PASSWORD} --database=${DB_DATABASE}"

# 接続できるまで待機する
for i in `seq 1 20`
do
  $MYSQLCMDBASE -w --connect-timeout=1000 -e "SELECT 'OK';"
  if [ $? -eq 0 ]; then
    break
  fi
  if [ $i -eq 20 ]; then
    echo "Failed to access ${DB_HOST}:${DB_PORT:-3306}"
    exit 1
  fi
  sleep 3
done
