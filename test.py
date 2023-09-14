
smallest = None
biggest = None
        
while True:
    nums = input("Enter a number:")
    if nums == 'done':
        break
    try:
        num = float(nums)
    except:
        print('invalid input')
        continue
        
    if smallest is None or num < smallest:
        smallest = num
        
    elif biggest is None or num > biggest:
        biggest = num
        

print("Maximum Is", int(biggest))
print("Minimum Is", int(smallest))