# ss_spider

ss_spider是一个基于shadowsocks的自动获取并更新网络免费服务器地址密码的脚本，服务器来源为ishadow，在进行好配置之后运行脚本即可更新shadowsocks的密码。

配制方法：
1. 在ss中添加三个服务器
2. 将 main.py 中 old_path 修改为自己的ss目录
3. 将 main.py 中 old['configs'] 后的[1][2][3]修改为自己ss配置文件中us，jp，sg的顺序，顺序从0开始
4. 运行main.py更新密码
