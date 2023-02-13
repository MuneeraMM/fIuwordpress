import re
def isWordPress(str):
    def isValidDomain(str):
        #Regex to check valid.
        #Domain name.
        regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
        #compile the Regex
        p = re.compile(regex)
        #if the string is empty
        #return false
        if (str == None):
            return False
        #Return ifthe string
        #matched the regex
        if (re.search(p, str)):
            return ("It is a valid domain")   
        else:
            return ("It is not a valid domain")
    # #test cases:
    
    str1="youtube.com"
    print(isValidDomain(str1))
    # str3 = "Tripadvisor.com"
    # print(isValidDomain(str3))

    # str4 = "sonymusic.com"
    # print(isValidDomain(str4))
str1="youtube.com"

if(isWordPress("http://str/wp-admin")):
    print("Yes")
else:
    print("No")


# isWordPress(str10)
# str11 = "sonymusic.com"
# isWordPress(str11)