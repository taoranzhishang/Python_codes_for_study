'''
%d字符，%s字符串，%d整数，%f浮点数，%e科学计数，%g
'''
print("pass is %c" % 'x')
print("pass is %c" % ('y'))
print("我有%d所房子" % 1.2)  # 格式要匹配，否则会异常
'''
默认小数点后6位,超出后四舍五入
'''
print("%f" % 1.2)
print("%f" % 1.23)
print("%f" % 1.234)
print("%f" % 1.2345)
print("%f" % 1.23456)
print("%f" % 1.234567)
print("%f" % 1.2345675)
'''
宽度为10，默认右对齐，-左对齐
'''
print("%10f" % 1.2)
print("%10f" % 1.23)
print("%10f" % 1.234)
print("%10f" % 1.2345)
print("%10f" % 1.23456)
print("%10f" % 1.234567)
print("%10f" % 1.2345675)
print("%-10f" % 1.2)
print("%10.4f" % 1.2345675)  # 宽度为10，小数点后4位
print("%010.5f" % 1.2345675)  # y右对齐，左边0填充，默认空格填充
'''
%%转义字符为一个%，%%%表示一个%字符，另一个没有转义不输出
'''
