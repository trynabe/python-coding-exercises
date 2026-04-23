'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab12-list-interleaving
*/
'''

# YOUR CODE HERE
def list_interleaving(list1, list2):
    result = []
    
    while len(list1) > 0 or len(list2) > 0:
        
        if len(list1) > 0:
            result.append(list1.pop(0))
            
        if len(list2) > 0:
            result.append(list2.pop(0))
            
    return result

n1 = int(input())
n2 = int(input())

list1 = []
for _ in range(n1):
    list1.append(input())

list2 = []
for _ in range(n2):
    list2.append(input())

interleaved_list = list_interleaving(list1, list2)
print(interleaved_list)