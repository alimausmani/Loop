
# num=int(input("please enter the number:"))
# a=1
# while a<=10:
#     print(num,"*",a,"=",num*a)
#     a=a+1

# i=1
# while i<=10:
#     print(2*i)
# #     i=i+1



num=int(input("enter any table:"))
a=1
if num>0:
    print(num,"*",a,"=",num*a)
    if num>1:
        print(num,"*",a+1,"=",num*a*2)
        if num>2:
            print(num,"*",a+2,"=",num*a*3)
            if num>3:
                print(num,"*",a+3,"=",num*a*4)
                if num>4:
                    print(num,"*",a+4,"=",num*a*5)
                    if num>5:
                       print(num,"*",a+5,"=",num*a*6)
                       if num>6:
                           print(num,"*",a+6,"=",num*a*7)
                           if num>7:
                               print(num,"*",a+7,"=",num*a*8)
                               if num>8:
                                   print(num,"*",a+8,"=",num*a*9)
                                   if num>9:
                                      print(num,"*",a+9,"=",num*a*10)   
                                   else:
                                        print("Wrong")
                               else:
                                    print("Nothing")  
                           else:
                               print("No")
                       else:
                           print("Prosess")
                    else:
                       print("no")
                else:
                   print("nothing")
            else:
               print("wrong")
        else:
           print("prosess")
    else:
       print("galat") 
else:
    print("nahi")                                                                     

                                  

