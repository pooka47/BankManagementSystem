import re
def isIFSCValid(n1):
        if not((len(n1)==11) and (n1[:4].isupper()==True) and (n1[:4].isalpha()==True) and (n1[4]=='0') and (n1[5:].isalnum()==True) and (n1[5:].isupper()==True)):
            return False
        else:
            return True



def isBankNameValid(bn):
        for char in bn:
            if not((char.isalpha()==True) or (char.isspace()==True)):
                return False
        return True

def isCityNameValid(city):
        for char in city:
            if not((char.isalpha()==True) or (char.isspace()==True)):
                return False
        return True

def isAgeValid(age):
    if not(age.isdigit()==True and int(age)<100 and int(age)>18):
        return False
    return True

def isAadharValid(aadhar):
    if not(len(aadhar)==12 and aadhar.isdigit()==True):
        return False
    return True

def isGenderValid(gender):
    tup1=('Male','Female','Transgender','M','F','m','f','MALE','FEMALE','TRANSGENDER','male','female','transgender')
    if not(gender in tup1):
        return False
    return True


def isAccountTypeValid(acc_type):
    tup2=('SAVINGS','SALARY','CURRENT','FIXED DEPOSITS','FD','RD','current','salary','savings','rd','fd')
    if not(acc_type in tup2):
        return False
    return True


def isInitialBalanceValid(balance):
    if not(balance.isdigit()==True and int(balance)>0):
        return False
    return True

def isAddressValid(address):
    for char in address:
            if not((char.isalpha()==True) or (char.isspace()==True) or (char.isalnum()==True)):
                return False
    return True
    
def isAccountNumberValid(acc_no):
    len1=len(acc_no)
    for i in acc_no:
        if not((i.isdigit()==True) and (int(len1)>=11) and (int(len1)<=16)):
            return False
        return True
        


def isPanValid(n1):
        if not((len(n1)==10) and (n1[:5].isupper()==True) and (n1[:5].isalpha()==True) and (n1[5:9].isdigit()==True) and (n1[9].isalpha()==True) and (n1[9].isupper()==True)):
            return False
        else:
            return True

expr1='^\d{2}-\d{2}-\d{4}$'

def isDOBValid(dob):
        if not(re.match(expr1,dob)):
                return False
        else:
                return True


def isAccountHolderName(ac_nm):
        words=ac_nm.split()

        for i in words:
                if not i[0].isupper() or not i.isalpha():
                        return False
        return True       
 






