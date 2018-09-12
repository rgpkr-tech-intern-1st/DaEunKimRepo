# -*- coding: utf-8 -*-
print("""
----------------------------------------------------------
파이썬에서는 가장 가까운 변수를 찾을 때까지 한 단계씩 범위를 넓혀나갑니다.
범위는 4가지로 구분할 수 있습니다.

1. Local: 함수의 내부
2. Enclosing Function Local: 함수를 감싸고 있는 바깥 함수
3. Global: 함수 영역이 아닌 모듈 영역
4. Built-in: 내장 영역
-----------------------------------------------------------
""")
a = 1


def scope1():
    """A. scope1 밖의 a는 전역변수, scope1 안의 a는 지역변수입니다.

    scope1 is called.
    a is {0}.
    """
    a = 2
    print(scope1.__doc__.format(a))


scope1()


def scope2():
    """B. scope2 내부에 a가 지역변수로 정의되지 않다면 scope2는 전역변수 a를 참조합니다.

    scope2 is called.
    a is {0}.
    """
    print(scope2.__doc__.format(a))


scope2()


b = 10
c = 11


def scope3_outer():
    """C. scope3에서 b는 Enclosing Function Local, c는 Global, d는 Local변수입니다.

    global b is {0}
    global c is {1}
    scope3 is called."""
    global b
    global c
    print(scope3_outer.__doc__.format(b, c), end="")
    b = 20

    def scope3():
        """
        b is {0}.
        c is {1}.
        d is {2}.
        """
        d = 30
        print(scope3.__doc__.format(b, c, d))

    scope3()


scope3_outer()


def scope4():
    """D. scope4에서 변수를 변경할 때는 local범위에서 변수를 찾고 해당 범위에 변수가 없을 때 에러를 발생시킵니다.

    scope4 is called.
    UnboundLocalError: local variable 'a' referenced before assignment
    """
    print(scope4.__doc__)


scope4()


def scope5():
    """E. scope5 내부에서 전역변수의 값을 변경하려면 'global'키워드를 적어줌으로써 전역변수를 가리킨다는 것을 알려줘야 합니다.

    scope5 is called.
    a is {0}.
    """
    global a
    a = a + 5
    print(scope5.__doc__.format(a))


scope5()


e = 40

print("""F. Local범위가 아닌 가장 가까운 범위의 변수를 참조하려면 'nonlocal'키워드를 적어줍니다.""")
print("""G. 'nonlocal'은 버전 3.0 이상에서만 지원한다고 합니다.""")


def scope7():
    """
    scope7 is called.
    """
    print("""H. scope6에서 'nonlocal'로 참조되는 e는 scope7에서 정의된 변수입니다.""")
    print("""I. scope6에서 e를 51로 변경했으므로 scope7에서의 e의 값은 51입니다.""")

    e = 50

    def scope6():
        """
        scope6 is called.
        e is {0}.
        """
        nonlocal e
        print(scope6.__doc__.format(e), end="")
        e = 51

    print(scope7.__doc__.format(e), end="")
    scope6()
    print("""
    scope7's e is {0}
    """.format(e))


scope7()




print("""J. 전역 변수 e는 그대로 유지됩니다.
    global e is {0}.
    """.format(e))


print("""K. 전역 변수 e가 51이 아닌 40으로 유지되는 이유는 파이썬의 변수가 렉시컬 스코프를 가지기 때문입니다.
함수가 호출될 떄의 시점이 아니라 함수가 정의될 때의 시점에서 변수를 참조하므로
전역변수 e는 scope7을 호출했을 때 시점이 아닌 40으로 정의되었을 때의 시점에서 참조됩니다.""")
