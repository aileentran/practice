# input: string hh:mm:ssAM or hh:mm:ssPM
# output: hh:mm:ss in military time! 

# always valid input

# thoughts
# isolate AM or PM into variable
# if AM -> return hh:mm:ss as is 
# if PM -> convert hh into an int + 12 back into int and return hh:mm:ss


def timeConversion(s):
    meridian = s[-2:]
    hour = s[:2]
    
    if meridian == 'AM' and hour == '12':
        return f'00{s[2:-2]}'
    
    elif meridian == 'AM' or (meridian == 'PM' and hour == '12'):
        return s[:-2]
    
    else:    
        convert = int(hour) + 12
        convert = str(convert)

        return f'{convert}{s[2:-2]}'

# runtime: bc length of string is constant = O(1); slicing would normally be n but.. know length of string 
# runspace: w/out loops or variable input --> O(1)


print(timeConversion('07:05:45PM')) #19:05:45
print(timeConversion('07:05:45AM')) #07:05:45
print(timeConversion('12:40:22AM')) #00:40:22
print(timeConversion('12:45:54PM')) #12:45:54