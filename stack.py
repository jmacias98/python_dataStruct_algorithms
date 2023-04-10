'''
This program implements stack algorithm without using linked-list concept.
It will store full names and phone numbers and print them in ascending order.
'''
# Creating a stack
def create_stack():
    stack = []
    return stack

# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("Pushed Item: " + item)

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "Stack is Empty"
    return stack.pop()
    
phones = create_stack() # create phone numbers stack
names = create_stack() # create names stack

push(names, str("Jesus Macias")) # pushing names into stack
push(names, str("John Elway"))
push(names, str("Eli Manning"))
push(names, str("Tom Brady"))
push(names, str("Lamar Jackson"))
push(names, str("Josh Allen"))

print("\nPopped Item: " + pop(names)) # pop last item 
print("\nStack After Popping Element: " + str(names)) # print stack 
names.sort()
print("\nSorted Stack:\n", names,"\n") # print sorted stack

push(phones, str("8007459917")) # pushing phone numbers into stack
push(phones, str("8324569665"))
push(phones, str("5678761668"))
push(phones, str("7732021761"))
push(phones, str("8749899112"))
push(phones, str("6308979678\n"))

print("\nPopped Item: " + pop(phones)) # pop last item
print("\nStack After Popping Element: " + str(phones)) # print stack
phones.sort()
print("\nSorted Stack:\n", phones) # print sorted phones numbers

'''
OUTPUT:
Pushed Item: Jesus Macias
Pushed Item: John Elway
Pushed Item: Eli Manning
Pushed Item: Tom Brady
Pushed Item: Lamar Jackson
Pushed Item: Josh Allen

Popped Item: Josh Allen

Stack After Popping Element: ['Jesus Macias', 'John Elway', 'Eli Manning', 'Tom Brady', 'Lamar Jackson']

Sorted Stack:
 ['Eli Manning', 'Jesus Macias', 'John Elway', 'Lamar Jackson', 'Tom Brady']

Pushed Item: 8007459917
Pushed Item: 8324569665
Pushed Item: 5678761668
Pushed Item: 7732021761
Pushed Item: 8749899112
Pushed Item: 6308979678


Popped Item: 6308979678


Stack After Popping Element: ['8007459917', '8324569665', '5678761668', '7732021761', '8749899112']

Sorted Stack:
 ['5678761668', '7732021761', '8007459917', '8324569665', '8749899112']
'''