lg=0
slg=0
sm=999999
ssm=999999
print("Enter '0'(zero) to stop")
while 1:
    a=int(input("Enter a number : "))
    if a==0:
        break
    else:
        if a>lg:
            slg=lg
            lg=a
        elif a>slg:
            slg=a
        if a < sm:
            ssm = sm
            sm = a
        elif a < ssm:
            ssm = a
print("largest number",lg)
print("second largest number",slg)

print("small number",sm)
print("second smallest number",ssm)