def count_substring(string, sub_string):

    count = 0
    
    for i in range(0, len(string)-len(sub_string)+1):
        n = 0
        for j in range(0,len(sub_string)):
                        
                if sub_string[j] != string[i+j]:
                        break
                else: 
                        n += 1      
        if n == len(sub_string):
                count +=1
                
       
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)