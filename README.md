1.运行说明，可按以下命令执行

`python webtest.py -w <inputweb> -t <inputtime> -p <port> -d <delay> -c <Det> `

如 `python .\webtest.py -d 60 -w 114.114.114.114 -p 53 -c 23 -t 03：15`（这也是程序的默认值）

其中**inputweb**为输入的网址，**port**为端口，**inputtime**为每天测试断网时间，**Det**为连续检测网络失败后重启的次数，**delay**为两次检测的间隔。

也可以用添加环境的方式（环境变量优先级高于指令），环境变量分别为**Timed_inputweb，Timed_inputtime，Timed_port，Timed_delay，Timed_det**
