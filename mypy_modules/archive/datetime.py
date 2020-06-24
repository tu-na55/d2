from datetime import datetime, timedelta, timezone
import calendar

# init
JST = timezone(timedelta(hours=+9), 'JST')

datetime.now(JST)

##############################
# self._joined_args = ' '.join(map(str,
#   [datetime.datetime.now(), [args]:'] + list(args)
# ))
##############################
# logging.debug('debug %s %s', 'date', 'test')

# def create_date(year=2020, month=1, day=9, hour=14, minute=0, second=29):

#     dt_test = datetime.date(year, month, day, hour, minute, second)
#     datetime_today = datetime.date.today()
#     datetime_now = datetime.datetime.now()

#     # to str
#     print(datetime_today.strftime('%Y-%m-%d'))
#     print(datetime_now.strftime('%Y-%m-%d %H:%M:%S'))

#     # 文字列（日付）をdateオブジェクトに変換する。
#     tstr = '2012-12-29'
#     tdate = datetime.datetime.strptime(tstr, '%Y-%m-%d')
#     odate = datetime.date(tdate.year, tdate.month, tdate.day)

#     # 文字列（日時）をdatetimeオブジェクトに変換する。
#     tstrdt = '2017-12-01 23:06:19'
#     tdatetime = datetime.datetime.strptime(tstrdt, '%Y-%m-%d %H:%M:%S')

##############################

# def get_datetime_now():
#     """プログラム実行時点での日時を計算する。
#     @return datetime_now (datetime.datetime): プログラム実行時点での日時
#     """

#     datetime_now = datetime.datetime.now()
#     print("year=%s month=%s day=%s week()=%s" %
#     (current_datetime.year,
#      current_datetime.month,
#      current_datetime.day,
#      current_datetime.weekday(),)

#     return datetime_now
##############################


# def get_monday(time):
#     """指定する日時が含まれる週の月曜日を計算する。
#     @Args time (datetime.datetime): 指定する日時
#     @return result (datetime.date): 指定する日時が含まれる週の月曜日
#     """
#     time_date=time.date()
#     weekday=time_date.weekday()
#     delta=datetime.timedelta(days=weekday)
#     result=time_date - delta
#     return result

##############################

# """
# 月初を取得する
# """
# def get_firstdate(y, m):
#     return datetime.date(y, m, 1)

# fdate=get_firstdate(2019, 6)
##############################


# """
# 月末を取得する
# """
# def get_lastdate(y, m):
#     _, days=calendar.monthrange(y, m)
#     firstdate=get_firstdate(y, m)
#     lastdate=firstdate + datetime.timedelta(days=days - 1)
#     return lastdate

# ldate=get_lastdate(2019, 6)
##############################


# """
# 月初の週始まり（日曜日）を取得する
# """
# def get_first_sunday(y, m):
#     firstdate=get_firstdate(y, m)
#     from_date=firstdate - datetime.timedelta(days=firstdate.weekday() + 1)
#     return from_date

# fsunday=get_first_sunday(2019, 6)
##############################


# """
# 月末の週終わり（土曜日）を取得する
# """
# def get_last_saturday(y, m):
#     lastdate=get_lastdate(y, m)
#     to_date=lastdate + datetime.timedelta(days=lastdate.weekday())
#     return to_date

# fsaturday=get_last_saturday(2019, 6)
# 7. 24H以上の時間の取り扱い
# (14).24H以上の時刻をdatetimeに変換する
# datetime.datetimeのhourに 24以上の数値を渡すとエラーになります。

# ValueError: hour must be in 0..23
# このケースでは、timedeltaを使って分数を計算をして、日付に加算することで対応します。
##############################


# """
# 24H以上の時刻をdatetimeに変換する
# """
# def over24Hdatetime(year, month, day, hour, minute):

#     # to minute
#     minutes=int(hour) * 60 + int(minute)

#     dt=datetime.datetime(year=year, month=month, day=day)
#     dt += datetime.timedelta(minutes=minutes)

#     return dt

# dt14=over24Hdatetime(2019, 6, 9, 49, 19)
##############################

# """
# 時刻同士の引き算（分数に換算する。）
# """
# def get_minutes(fromdt, todt):
#     # 2つのdatetimeの差は、timedeltaオブジェクト
#     # timedelta には、days, seconds, microsecondsの３つのプロパティがある。
#     return (todt - fromdt).seconds / 60

# fromdt=datetime.datetime.strptime('2019-06-09 09:00', '%Y-%m-%d %H:%M')
# todt=datetime.datetime.strptime('2019-06-09 17:30', '%Y-%m-%d %H:%M')

# minutes=get_minutes(fromdt, todt)
