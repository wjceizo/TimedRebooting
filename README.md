# TimedRebooting

Timed reboot in case of disconnection

1. webtest.py -w inputweb -t inputtime | 如webtest.py -w 114.114.114.114 -t 15:30
3. 默认的host为114.114.114.114，默认的时间为03:15,默认间隔60分钟。一天24小时均断网就会重启。
