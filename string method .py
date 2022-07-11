#Python string method

st1= 'my seLF chaiTanya'
print(st1.capitalize())


#Center Method

st2='My self chaitanya'
print(st2.center(24,'*'))


#Case fold

st3='pytHOn'
print(st3.casefold())

#Count

st4= "python is awesome, is it?"
substring="is"
print(st4.count(substring))

#ex 2

st5="python is awesome,is it?"
substring="is"
print(st5.count(substring,8,25))


#without start and end parameters

text="Python is easy to learn."

result=text.endswith('to learn')  #returns false
print(result)

result=text.endswith('to learn.')    #returns true
print(result)

result=text.endswith('Python is easy to learn.')   #returns true
print(result)


#


















