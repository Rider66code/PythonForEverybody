str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
output=''
temp=''
for word in str1.split():
    temp=word.strip("!")
    if temp=='false':
        output='False. You aren’t you?'
        print(output)
    elif temp=='true':
        output='True! You are you!'
        print(output)
        break
    else:
        output='Neither true nor false!'
        print(output)
