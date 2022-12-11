print("Registration and Login system using Python, file handling\n")
print("Enter 1 for Registration")
print("Enter 2 for Login")
n=int(input())
# Check conditions for UserID
def check_email(mail):
    email=list(map(str,mail))
    at,dot=0,0
    if "@" in email:             
        at=email.index("@")        
        if "." in email:           
            dot=email.index(".")   

    rule1,rule2,rule3,rule4,rule5=0,0,0,0,0
    
    if dot>at:                  
        rule1=1
    else:
        print("\n@ should appear first and then .")
        return 0

    if at>0:                       
        rule2=1
    else:
        print("\nMake sure atleast one charecter before @")
        return 0

    if dot-at-1 > 1:               
        rule3=1
    else:
        print("\nMake sure the atleast one char between @ and .")
        return 0
        
    if not email[0].isdigit():    
        rule4=1
    else:
        print("\nMake sure that UserID doesn't start with number")
        return 0

    if email[0] not in '[@_!#$%^&*()<>?/\|}{~:]':
        rule5=1                    
    else:
        print("\nMake sure that UserID doesn't start with special charecter")
        return 0
        
    if rule1==1 and rule2==1 and rule3==1 and rule4==1 and rule5==1:
        return 1                   
# Check conditions for Password
def check_password(pw):
    password=pw
    length=len(password)

    rule1,rule2,rule3,rule4,rule5=0,0,0,0,0

    if length>=5 and length<=16:         # make sure that password length is between 5 and 16
        rule1=1
    else:
        print("make sure that password length atleast 5 and atmost 16")
        return 0
        
    for i in password:
        if i in '[@_!#$%^&*()<>?/\|}{~:]':  
            rule2=1
        if i.isdigit():                     
            rule3=1
        if i.isupper():                     
            rule4=1
        if i.islower():                     
            rule5=1
    
    if rule2==0:
        print("Make sure password contains a special char")
        return 0
        
    if rule3==0:
        print("Make sure password contains a number")
        return 0
    
    if rule4==0:
        print("Make sure password contains an Uppercase letter")
        return 0
        
    if rule5==0:
        print("Make sure password contains an Lowercase letter")
        return 0

    if rule1==1 and rule2==1 and rule3==1 and rule4==1 and rule5==1:        
        return 1                           
# After verifying the userid and password save the values in a file
def registration():
    print("\nPlease Enter UserID: ")
    mail=input()
    cm=check_email(mail)
    file1 = open('users.txt', 'r')
    Lines = file1.readlines()
    flag=0

    for line in Lines:
        up=list(map(str,line.split()))
        if up[0]==mail:
            flag=1
    if flag==1:
        print("UserID already Exists,Please try with a different UserID")
        return
    if cm==1 and flag==0:
        print("\nPlease Enter Password")
        password1=input()
        pm=check_password(password1)       
        
        if pm==1:
            print("\nPlease Re-enter Password")
            password2=input()
            if password1==password2:
                details=mail+" "+password1+"\n"          
                with open("users.txt", 'a') as file1:   # if userid and pasword are ok then save it in file
                    file1.write(details) 
                print("\nRegistration Successful")
            else:
                print("\nPassword1 and Password2 are not matching, kindly try again later")
                
        else:
            print("\nKindly Register Again")
            
    else:
        print("\nPlease try again ")
        registration()
# If only userid matches and password doesnt then show old password from file or create new password
def onlyuser(uid,line,password):
    print("\nOnly UserID correct and password is wrong")
    print("\nChoose any one of following actions")
    print("Enter 1 for Forgot password")
    print("Enter 2 to create new password")
    n=int(input())
    if n==1:
        print("\nThe original password for userid",uid,"is:",password)
    if n==2:
        print("\nPlease enter new password for userId",uid)
        new_pass=input()
        np=check_password(new_pass)
        if np==1:
            print("\nPlease enter new password again")
            new_pass1=input()
            if new_pass==new_pass1:
                
                print("\nNew password updated")
                with open('users.txt', 'r') as file:
                    data = file.readlines()

                data[line] = uid+" "+new_pass+"\n"
  
                with open('users.txt', 'w') as file:
                    file.writelines(data)
            else:
                print("\nNew password1 and new password2 are not matching, please try again later")
        else:
            print("\nPlease try later")
# Get userid and password from user and search in the file if they exist or not            
def login():
    print("\nPlease Enter UserID: ")
    mail=input()
    print("\nPlease Enter Password")
    password=input()
    
    file1 = open('users.txt', 'r')
    Lines = file1.readlines()
    flag,useronly,count,line_no=0,0,0,0

    for line in Lines:
       up=list(map(str,line.split()))
       if up[0]==mail and up[1]==password:
           print("\nLogged Successfully")
           flag=1
           break 
       if up[0]==mail and up[1]!=password:
           useronly=1
           line_no=count
           pwd=up[1]
       count=count+1
       up=[]
    
    if flag==0 and useronly==0:
        print("\nUsername and Password not found, Please make new registration")
        registration()
    if flag==0 and useronly==1:
        onlyuser(mail,line_no,pwd)

if n==1:
    print("Rules for UserId:")
    print("1 @ should appear first and then . \n2 Atleast one character before @ \n3 Atleast one character between @ and .\n4 It should not start with numbers or special character")
    print("\nRules for Password:")
    print("1 password length should be atleast 5 to 16 characters\n2 Should contain atleast one special character\n3 Should contain atleast one number\n4 Should contain one uppercase character\n5 Should contain one lowercase character ")
    registration()
if n==2:
    login()

