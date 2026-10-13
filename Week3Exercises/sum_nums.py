num=int(input("Type a number."))
sonuc=0
gauss=num * (num+1)/2
n=1
for i in range(1,num+1):
    sonuc=sonuc+i
if sonuc==gauss:
    print("Equal")
if sonuc!=gauss: 
    print("Not Equal")   