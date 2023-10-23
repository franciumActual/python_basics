message = "hello world"
'''
print(message)  

print(len(message))

#called slicing
print("message[6] is:",message[6])

print("message[3:9] is:",message[3:9])

#a method is a function that belongs to a specific class
print(message.upper())
print(message.lower())


#these are case sensitive 
print(message.find('world'))
print(message.count('world'))


print(message.replace('world', 'universe'))
print(message.replace('world', 'universe', 0)) #does not print because 3rd param is set to 0
print(message.replace('world', 'universe', 1))




greeting = 'hello'
name = 'sandi'

greeting_message = greeting + ' ' + name

greeting_message_ref = f'{greeting} {name}. Welcome to our Company!'



print(greeting_message)
print(greeting_message_ref)

print(dir())
print(__file__)



print(dir(message))

'''