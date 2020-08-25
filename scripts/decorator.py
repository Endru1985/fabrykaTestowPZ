#DEKORATORY

#przykład 1

def regular_function():
    print('this is a regular function')

def decor(function):
    def inside():
        print('decorate function')
        return function()
    return inside

new_function = decor(regular_function)
new_function()

#przykład 2

def decor(function):
    def inside():
        print('decorate function')
        return function()
    return inside

@decor
def regular_function():
    print('this is a regular function')

#przykład 3

from datetime import datetime

def say_hello():
    print('hello my friend')

def run(function):
    def wrapper():
        if 6 <= datetime.now().hour < 22: #jeżeli podana godzina będzie spoza zakresu 6 - 22 to wtedy wynik 2
            function()
        else:
            print('hour out of range')
    return wrapper()

run(say_hello)


#WYJĄTKI:

#try:
    #wait = WebDriverWait(driver,5)
    #wait.until(ec.visibility_of_element_located((By.Id, 'test')))
    #print('iframe found)

#except TimeoutException:
    #print('there is no iframe')