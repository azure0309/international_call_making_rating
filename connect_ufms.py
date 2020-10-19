import cx_Oracle as cx
ip = '10.21.64.190'
port = 1521
service_name = 'UFMS'
username = 'UNI_TRAFFIC'
password = '123456oracle'
dsn = cx.makedsn(ip, port, service_name=service_name)
connection = cx.connect(username, password, dsn)
