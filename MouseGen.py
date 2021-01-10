def func1(arg1, arg2):
    var3 = func4()
    var20 = func5(arg2, var3)
    var21 = (var20 ^ -1617433874) & arg2 | var3
    var22 = -285 + arg1 - var21 | var3
    if var3 < var3:
        var23 = (336 | 555629899 & var21) & 406
    else:
        var23 = var20 & arg1 & var21 | -375299622
    var24 = var21 + (var3 ^ -873) - arg2
    var25 = ((var21 ^ arg2) - arg1) - var3
    var26 = arg2 + var21 | var24 - arg1
    var27 = -919 ^ var26
    var28 = arg1 - var20
    if var20 < var22:
        var29 = var28 | 129
    else:
        var29 = var3 - 148 + var25
    var30 = var21 | var27
    result = (var27 - var21 + var30 + var26 ^ (((var27 | var22 | var30) ^ arg2 & var3 - var27) & var26)) - var28
    return result
def func5(arg4, arg5):
    var6 = 0
    for var19 in func6(arg4, arg5):
        var6 += var19 & arg5
    return var6
def func6(arg7, arg8):
    var9 = -454 + ((858174544 & arg7) - -681)
    yield var9
    var10 = (arg7 - var9 ^ -635498561) | arg7
    yield var10
    var11 = arg8 ^ var9 ^ var10 & arg8
    yield var11
    var12 = arg7 & (var11 & var11)
    yield var12
    var13 = 493 & var11 ^ -107
    yield var13
    var14 = ((var11 & -551) + 872) ^ var10
    yield var14
    var15 = var13 + var9
    yield var15
    var16 = var15 + arg8
    yield var16
    var17 = var12 ^ 684 + var12
    yield var17
    var18 = (var16 | (arg8 & arg7)) + var14
    yield var18
def func4():
    func2()
    result = len([(i | 6) ^ (-6 + 7) for i in (-6 | 7 + -6 for i in range(32))])
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : -8
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 7'
    print 'arg_number: 31'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
