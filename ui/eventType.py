EVENT_TIMER = 'timer'  # 计时器事件，每隔1秒发送一次
EVENT_LOG = 'log'
EVENT_ERR = 'error'


# ----------------------------------------------------------------------
def test():
    """检查是否存在内容重复的常量定义"""
    check_dict = {}

    global_dict = globals()

    for key, value in global_dict.items():
        if '__' not in key:  # 不检查python内置对象
            if value in check_dict:
                check_dict[value].append(key)
            else:
                check_dict[value] = [key]

    for key, value in check_dict.items():
        if len(value) > 1:
            print(u'存在重复的常量定义:' + str(key))
            for name in value:
                print(name)
            print('')

    print(u'测试完毕')


# 直接运行脚本可以进行测试
if __name__ == '__main__':
    test()
