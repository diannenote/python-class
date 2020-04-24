class Test:
    a=30
    b='python'
    
# 1.__name__ 이부분은 현재 모듈의 이름을 가지는 내장 변수 입니다. 
# 2.__main__ 은 해당 코드가 메인 코드로 사용되었을때를 의미합니다.
# 3.구현한 코드가 다른 파이썬 코드에 의해서 모듈로 import 될 경우도 있고, 
#   파이썬 인터프리터에 의해서 직접 실행될 경우도 있는데 이 코드는 
#   인터프리터에 의해서 직접 실행될 경우에만 실행하도록 하고 싶은 
#   코드 블럭이 있는 경우에 사용한다. 

if __name__ == '__main__':   
   t=Test()             # Test 객체 생성

print(t.a)
print(t.b)