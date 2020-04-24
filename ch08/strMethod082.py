print ("---------------------------------------------------------------------")
print ("---  문자열 포매팅  튜플을 이용한 포매팅                             --")
print ("---  포맷팅 문자 : 문자열 내에 존재하는 %                            --")
print ("---  포맷팅을 활용한 문자열 변환:포맷팅 문자를 포함하는 문자열 % 튜플 --")
print ("----------------------------------------------------------------------")
print ()
print ('version2 방식  : name = %s, age = %s' % ('강미리', '24'))
print ('version3 방식  : name = {}, age = {}' .format('강종찬', '34'))
print ('version3(index) 방식  : name = {1}, age = {0}' .format('고두빈', '19'))
letter = '''
안녕하세요 %s님,
오늘 밤 파티에 참석해 주실 수 있나요?
그럼..
고수진 드림'''
name = '권순규'
print (" ---- 111 letter % name ------" , letter %name)
print (" ============================================")
names = ['김기전', '김동인', '김승률', '김영준','김원겸']
for name in names:
    print  (" letter % name " , letter % name)
    print  ('-' * 40)
    print  ()
    
print ("--------------------------------------------------------")
print ("-----  문자열 포매팅  튜플을 이용한 포매팅            ----")
print ("-----  사전(Dictionary)을 이용한 포매팅               ----")
print ("-----  사전형태이기 때문에 순서가 바뀌어도 괜찮음      ----")
print ("-----  주소 항목은 % 앞에 없기 때문에 무시            ----")
print ("--------------------------------------------------------")
print ('%(이름)s -- %(전화번호)s' %{'이름':'김의환', '전화번호':1234})
print ('%(이름)s -- %(전화번호)s' %{'전화번호':5678, '이름':'김진호'})
print ('%(이름)s -- %(전화번호)s' %{'전화번호':2345, '이름':'마재현', '주소':'안시성'})