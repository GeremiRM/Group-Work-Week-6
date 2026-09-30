INCHES_PER_FOOT = 12 

def main(): 
    feet = float(input('Enter the number of feet: '))
    feet_to_inches(feet)
   
    
def feet_to_inches(feet): 
    inches = feet * INCHES_PER_FOOT
    print(f'{feet} feet = {inches:.2f} inches')

main()