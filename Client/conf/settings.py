import os

# 远端接收数据的服务器
Params = {
    "server": "127.0.0.1",
    "Port": 8000,
    'url': '/assets/report/',
    'request_timeout': 20,
}

# 日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')