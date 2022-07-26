# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
l1 = [1,3,3,1]

ans = isPalindrome(l1)
 
if (ans):
    print("same")
else:
    print("Not same")