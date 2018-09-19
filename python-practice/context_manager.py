class Human:

    def __init__(self, name='kde', age=25):
        self.name = name
        self.age = age

    def __enter__(self):
        '''__enter__()
        with의 suite가 실행되기 전에 먼저 호출됩니다.
        __enter__()가 리턴한 값은 with [expression] as [variable]에서 variable로 넘어옵니다.
        variable의 타입은 {0}입니다.
        '''
        print(self.__enter__.__doc__.format(type(self)))
        return self

    def __exit__(self, err_type, err_value, err_tb):
        '''__exit__()
        with의 suite가 모두 실행되고 나서 __exit__(type, value, traceback)이 호출됩니다.
        suite에서 에러가 발생하지 않을 경우 suite 내용이 모두 실행되고 __exit__의 파라미터는 모두 None으로 들어옵니다.
        에러가 발생하면 suite는 중단되고 __exit__의 파라미터로 에러에 관한 정보가 들어옵니다.
        object's info: {0}
        err type: {1}
        err value: {2}
        err traceback: {3}
        '''
        print(self.__exit__.__doc__.format(type(self), err_type, err_value, err_tb))

    def get_info(self):
        '''
        get_info: {0}객체의 정보를 출력합니다.
        name is {1}.
        age is {2}.
        '''
        pass


class Person(Human):

    pass


def with_no_exception():
    '''with Human() as human's suite executes.
        __enter__()가 호출되고 나서 with의 내부(suite)가 실행됩니다.
        human은 __enter__()에서 리턴한 인스턴스입니다.
    '''
    with Human() as human:
        print(with_no_exception.__doc__)
        print(human.get_info.__doc__.format(type(human), human.name, human.age))


def with_exception():
    '''with Person() as person's suite executes.
        __enter__()가 호출되고 나서 with의 내부(suite)가 실행됩니다.
        person은 __enter__()에서 리턴한 인스턴스입니다.
    '''
    with Person('jadu', 1) as person:
        print(with_exception.__doc__)
        print(person.get_info.__doc__.format(type(person), person.name, person.age))
        raise Exception('exception raises!')


def with_nested():
    with Human() as kde:
        print(kde.get_info.__doc__.format(type(kde), kde.name, kde.age))
        with Person('jadu', 1) as jadu:
            print(jadu.get_info.__doc__.format(type(jadu), jadu.name, jadu.age))
            raise Exception('exception raises again!')


print('---------------------- with문의 동작 ---------------------')
with_no_exception()
print('-------------- with문에 Exception이 발생할 때 --------------')
with_exception()
print('------------------ with문이 중첩될 때 ---------------------')
with_nested()
