from dateutil import tz
from info.models import *
import pytz
from datetime import timezone, datetime

# Ossクラスのテーブルに登録
Oss.objects.create(oss_id="1", oss_name="Apache httpd")

# Infoクラスのテーブルに登録
oss_id = "1"  # Apache httpdのid
version = "2.4.29"  # バージョン
released = date(2017, 10, 23)  # リリース日
now = datetime.now().replace(tzinfo=tz.tzlocal())  # 現在時刻(JST)
registrated = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)  # タイムゾーン情報を落とす

Info.objects.create(oss_id=oss_id, version=version, released=released, registrated=registrated)  # SQLでいうところのInsert
