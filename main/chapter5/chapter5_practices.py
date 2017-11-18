import calendar
import datetime
import time

'''
    python时间相关操作：http://www.cnblogs.com/fengfenggirl/archive/2013/05/20/python_time.html
'''


def show_timestruct_utc(t):
    print('年：', t.tm_year)
    print('月：', t.tm_mon)
    print('日：', t.tm_mday)
    print('小时：', t.tm_hour)
    print('分钟', t.tm_min)
    print('秒', t.tm_sec)
    print('星期：', t.tm_wday)
    print('一年的第 %s 天' % t.tm_yday)
    print('是否夏时令：', t.tm_isdst)


print(time.time())
# 浮点时间转化为直观时间
t = time.time()  # 浮点时间
print(t)
print(time.ctime(t))

# 直观时间转化为浮点时间
t = time.time()  # 浮点时间
ct = time.ctime(t);  # 直观时间
utct = time.strptime(ct)  # 直观时间转化为UTC时间
tt = time.mktime(utct)  # UTC时间转化为浮点时间
print(t, ct, utct, tt)
show_timestruct_utc(utct)
show_timestruct_utc(time.gmtime())

# 获取当前时区的当前时间，可以传入毫秒值计算得出对应的时间
print("localtime: ", time.localtime())

# 格式化时间
lt = time.localtime()
fotmattedTime = time.strftime("%b %d %a %H:%M:%S %Y %s", lt)
fotmattedTime_Full = time.strftime("%B %D %A %H:%M:%S %Y %s", lt)
print(fotmattedTime)
print(fotmattedTime_Full)

# CPU时钟时间clock()，它反映了程序运行的实际时间，使用它做性能测试更准确
# for i in range(5):
#     print(time.time(), '\t', time.clock())
#     a = i * 3.14
#     for j in range(4000000):
#         a += j - 1;
# for i in range(5):
#     print(time.time(), '\t', time.clock())
#     print("sleep ", i)
#     time.sleep(i)

# 日期和时间管理--datetime
print(datetime.time(18, 20, 56))  # 构造时间
print(datetime.time.min, datetime.time.max, datetime.time.resolution)

# 日期由date表示，today()可以获得今天的日期，其中的年、月、日都可以替换
d = datetime.date(1998, 2, 5)  # 构造日期
print(d)
today = datetime.date.today()
print(today)
print(today.replace(day=22))  # 替换日
print(today.replace(month=1))  # 替换月
print(today.replace(year=1))  # 替换年

# 时间段datedelta，datedelta可以表示星期、日、小时、分钟、秒、毫秒、微秒
print(datetime.timedelta(days=1))  # 一天
# 利用时间段可以很方便的进行时间和日期运算
today = datetime.date.today()
print("今天", today)
oneDay = datetime.timedelta(days=1)  # 一天
yesterday = today - oneDay;
print("昨天", yesterday)
tommorrow = today + oneDay
print("明天", tommorrow)
print("时间差", yesterday - tommorrow)

# datetime实例都可以用getattr()解析
now = datetime.datetime.now()
items = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']
for attr in items:
    print('%12s: %s' % (attr, getattr(now, attr)))

# 可以使用date和time结合成一个datetime
t = datetime.time(20, 10, 15)
d = datetime.date.today()
dt = datetime.datetime.combine(d, t)
print(dt)

'''
    Calendar处理日期，管理面向年、月、周的时间。
    Calendar定义了三个类Calendar、TextCalendar和HTMLCalendar
    利用TextCalendar的prmonth()可以生成一个格式化的日历
'''
c = calendar.TextCalendar(calendar.SUNDAY)  # 入参：日历的第一列
c.prmonth(2017, 9)

'''
    利用HTMLCalendar和formatmonth()也可以生成这样的日历，只是有一些HTML标签，保存成HTML,在浏览器下打开就可以看到了
    HTMLCalendar在处理一些重复性日期时比较方便，假设公司每个月第二周的周二要开一次会议，现在要计算今天这一年开会的日期
'''
for month in range(1, 13):
    c = calendar.monthcalendar(2017, month)
    firstWeek = c[0]
    secondWeek = c[1]
    thirdWeek = c[2]
    if firstWeek[calendar.TUESDAY]:  # 如果第0个星期有星期二，第1个星期二就该开会
        meetingdate = secondWeek[calendar.TUESDAY]
    else:
        meetingdate = thirdWeek[calendar.TUESDAY]
    print('%5s: %2s' % (calendar.month_abbr[month], meetingdate))

# 字符串时间转成数值型时间
a = '2011-09-28 10:00:00'
pattern = '%Y-%m-%d %H:%M:%S'
print(time.mktime(time.strptime(a, pattern)))
