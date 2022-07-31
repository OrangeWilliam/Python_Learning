def foo(a):
    print("初始值a：", a)
    b = yield a
    print("传递值b：", b)
    c = yield a+b
    print("传递值c：", c)


rg=foo(1)
print(next(rg))
print(rg.send(2))
print(rg.send(99))
