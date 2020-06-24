
#!/bin/sh
set -e

source ~/.profile

if [ "$#" -gt "0" ]; then
    if [ "$1" == "webapp" ]; then
        start=$(date +%s)

        python manage.py migrate --noinput
        # 画像などの静的コンテンツファイルを1箇所に集めるコマンドです。 nginxと共有するボリュームへコピーしたいため、コンテナ起動時に実行しています。
        python manage.py collectstatic --noinput --clear

        end=$(date +%s)

        # if [ ! -z "${SENTRY_AUTH_TOKEN}" -a ! -z "${SENTRY_ORG}" ]; then
        #     version=$(cut -d'=' -f 2 < ./config/__init__.py | tr -d "' ")
        #     sentry-cli releases deploys "DockerHubUpdateNotifier@${version}" new -e "${SENTRY_ENV:-prod}" -t $((now-start))
        # fi

        exec uwsgi uwsgi.ini

    elif [ "$1" == "batch" ]; then
        exec python scheduler.py batch

    else
        exec "$@"
    fi
fi
