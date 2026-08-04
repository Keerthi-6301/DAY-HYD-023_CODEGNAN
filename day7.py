'''
Usage of else with for -->the else keyword will only be executed when the loop is completely done without any break
'''
'''
#for with else...
work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day ==1:
        #print(day)
        current_streak = current_streak + 1 
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(f'longest streak is {longest_streak}')
            break
    else:
        current_streak = 0#streak breaks
else:
    print(f'Longest Stresk is{longest_streak}')
print("Execution done")    
#In this case when the entire loop execution is done we get result of
#else block
'''
'''
#for else with Notification scenario

#notifications = [0,0,1,0]
notifications = 
for notification in notifications:
    if notification == 1:
        print('Unread Notification')
        break
else:
    print('All Caught Up')
'''
'''
#try to take notifications from user -->list of integers
notifications = [0,0,0,1,0]
otifications = list(map(int,input("Enter the values --> 0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
        print('Unread Notification')
        break
else:
    print('All Caught Up')
    '''
'''
#while -->it relies on Condition,it will be completely executed until the
#condition is satisified...
'''
'''

Syntax while:

while <condition>:
    statement(s)....
    ......
    ......
'''
'''
while True:
    print("Yes")
'''
'''
#It runs an infinite loop we need to press Ctrl+C (Keyboard interrupt)

i = 1#initialised statement
while i<=10:
    print(i)
    i =i+1#counter
    '''
'''
#Get the counter from 10 to 1    
i = 10#initialised statement
while i>=1:
    print(i)
    i =i-1#decrement i-=1
 '''
'''
i = 0
while i<=10:
    print(10-i)
    i = i+ 1
'''



#banking scenario -->PIN authentication if more than 3 attempts
#Account located...

pin ="1234"
max_attempts = 3
current_attempt = 0
while current_attempt <=max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if entered_pin == pin:
        print("Login Successfully")
        #break
        #continue #it holds for this condition and skips to the next part of continue
    else:
        print("Entered PIN is wrong..Try again carefully")
        current_attempt +=1
else:
    print("Account Locked,try after 24hours...")        





    














































