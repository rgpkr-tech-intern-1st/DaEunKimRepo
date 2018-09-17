class Human:

    def __init__(self, name='kde', age=25):
        self.name = name
        self.age = age

    def __enter__(self):
        '''__enter__()
        with의 suite가 실행되기 전에 먼저 호출됩니다.
        __enter__()가 리턴한 값은 with [expression] as [variable]에서 variable로 넘어옵니다.
        '''
        print(self.__enter__.__doc__)
        return self

    def __exit__(self, err_type, err_value, err_traceback):
        '''__exit__()
        with의 suite가 모두 실행되고 나서 __exit__(type, value, traceback)이 호출됩니다.
        suite에서 에러가 발생하지 않을 경우 suite 내용이 모두 실행되고 __exit__의 파라미터는 모두 None으로 들어옵니다.
        에러가 발생하면 suite는 중단되고 __exit__의 파라미터로 에러에 관한 정보가 들어옵니다.
        object's info: {0}, {1}
        err type: {2}
        err value: {3}
        err traceback: {4}
        '''
        print(self.__exit__.__doc__.format(self.name, self.age, err_type, err_value, err_traceback))

    def get_info(self):
        return self.name, self.age


class Person(Human):

    def __init__(self, name, age):
        super().__init__(name, age)

    def __enter__(self):
        print(super().__enter__.__doc__)
        return self

    def __exit__(self, err_type, err_value, err_traceback):
        print(super().__exit__.__doc__.format(self.name, self.age, err_type, err_value, err_traceback))

    def get_info(self):
        return super().get_info()


def with_no_exception():
    '''with Human() as h's suite executes.
    __enter__()가 호출되고 나서 with의 내부(suite)가 실행됩니다.
    h는 __enter__()에서 리턴한 인스턴스입니다.
    '''
    with Human() as h:
        print(with_no_exception.__doc__)
        name, age = h.get_info()
        print(f'''h's name is {name}, h's age is {age}
        ''')


def with_exception():
    '''with Person() as p's suite executes.
    '''
    with Person('jadu', 1) as p:
        name, age = p.get_info()
        print(with_exception.__doc__)
        raise Exception('exception raises!')
        print(f'''p's name is {name}, p's age is {age}
        ''')


def with_nested():
    with Human() as kde:
        print(f'''with suite: {kde.get_info()}
        ''')
        with Person('jadu', 1) as jadu:
            print(f'''nested with suite: {jadu.get_info()}
            ''')
            raise Exception('exception raises again!')


print('---------------------- with문의 동작 ---------------------')
with_no_exception()
print('-------------- with문에 Exception이 발생할 때 -------------')
with_exception()
print('------------------ with문이 중첩될 때 -------------------')
with_nested()