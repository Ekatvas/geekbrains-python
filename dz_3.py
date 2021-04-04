"""
Номера функций соответсвуют номерам заданий
"""
def func_1(a, b):
    if b!=0:
        return a/b
    else:
        return

def func_2(**kwargs):
    string=''
    for val in kwargs.values():
        string+=val
        string+=' '
    return string

def func_3(a, b, c):
    some_list = [a, b, c]

    # Если все элементы int или float
    if all(map(lambda x: isinstance(x, (int, float)), some_list)):
        some_list.remove(min(a, b, c))
        result=some_list[0]+some_list[1]
        return result
    else:
        return

def func_4(x, y):
    if isinstance(x, (int, float)) and isinstance(y, int) and y<0:
        y=-y
        i=1
        result=1/x
        while i<y:
            result=result/x
            i+=1
        return result
    else:
        return

def func_5():
    some_list=[]
    result=0
    while not '#' in some_list:
        string=input('Введите числа через пробел: ')
        some_list=string.split()
        for item in some_list:
            try:
                result+=int(item)
            except:
                pass
        print(f'Сумма чисел: {result}')

def func_6():
    string=input('Введите слова: ')
    return string.title()


if __name__ == '__main__':
    dev=func_1(6, 3)
    print(dev)

    info=func_2(
        name='Ekaterina',
        second_name='Vasilyeva',
        date='27.01.1997',
        email='email@mail.ru',
        mobile='89999999999'
    )
    print(info)

    res=func_3(10, 7, 8)
    print(res)

    result=func_4(2, -3)
    print(result)

    s=func_6()
    print(s)
