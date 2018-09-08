# -*- coding: utf-8 -*-

# 파이썬의 유효범위는 함수를 기준으로 생성됩니다.
a = 1
def scope1():
    a = 2
    print("scope1 is called. a is {0}.".format(a))
# 함수 밖의 a는 전역변수, 함수 안의 a는 지역변수입니다.
scope1() # a is 2
print("global a is {}.".format(a)) # global a is 1


def scope2():
    print("scope2 is called. a is {0}.".format(a))
scope2() # a is 1
# 파이썬에서는 가장 가까운 변수를 찾을 때까지 한 단계씩 범위를 넓혀나갑니다.
# 범위는 4가지로 구분할 수 있습니다.
# 1. Local: 함수의 내부
# 2. Enclosing Function Local: 함수를 감싸고 있는 바깥 함수
# 3. Global: 함수 영역이 아닌 모듈 영역
# 4. Built-in: 내장 영역


b = 10
c = 11
def scope3_outer():
    b = 20
    def scope3():
        d = 30
        print("scope3 is called. b is {0}, c is {1}, d is {2}.".format(b,c,d))
    scope3()
scope3_outer() # b is 20, c is 11, d is 30
# scope3에서 b는 Enclosing Function Local, c는 Global, d는 Local변수입니다.


def scope4():
    a = a + 5
    print("scope4 is called. a is {0}.".format(a))
scope4() # UnboundLocalError: local variable 'a' referenced before assignment
# 변수의 값을 탐색할 때는 위의 네 가지 범위를 순서로 탐색하지만,
# 변수의 값을 변경하려고 할 때는 가장 가까운 범위(Local범위)에서 변수를 찾고 해당 범위에 변수가 없을 때 에러를 발생시킵니다.


def scope5():
    global a
    a = a + 5
    print("scope5 is called. a is {0}.".format(a))
scope5() # a is 6
# 함수의 내부에서 전역변수의 값을 변경하려면 'global'키워드를 적어줌으로써 전역변수를 가리킨다는 것을 알려줘야 합니다.

e = 40
def scope7():
    e = 50
    def scope6():
        nonlocal e
        print("scope6 is called. e is {0}.".format(e))
        e = 51
    scope6() # e is 50
    print("scope7 is called. e is {0}".format(e)) # e is 51
scope7()
print("global e is {}.".format(e)) # e is 40
# Local범위가 아닌 가장 가까운 범위의 변수를 참조하려면 'nonlocal'키워드를 적어줍니다.('nonlocal'은 버전 3.0 이상에서만 지원한다고 합니다.)
# scope6에서 'nonlocal'로 참조되는 e는 scope7에서 정의된 변수입니다.
# scope6에서 e를 51로 변경했으므로 scope7에서의 e의 값은 51입니다.
# 전역 변수 e는 그대로 유지됩니다.

# 전역 변수 e가 51이 아닌 40으로 유지되는 이유는 파이썬의 변수가 렉시컬 스코프를 가지기 때문입니다.
# 함수가 호출될 떄의 시점이 아니라 함수가 정의될 때의 시점에서 변수를 참조하므로
# 전역변수 e는 scope7을 호출했을 때 시점이 아닌 40으로 정의되었을 때의 시점에서 참조됩니다.
