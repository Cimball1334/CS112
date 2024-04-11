#CS 112 _ 233 Python lab 7
#Author Craig Kimball
#Date 10/12/2021 11:30AM 

def test_alias(list1, list2):
    test_result = ''
    
    
    if(id(list2) == id(list1)):
        test_result = 'Alias. They refer to the same object in memory.'
    elif(list2 == list1):
        test_result = 'Not alias. AND They have same content.'
    else:
        test_result = 'Not alias. BUT They have different content.'
    
    list3 = list2[:len(list2)]
    
    return_list = [list1, list2, test_result,list3]
    print(return_list)
    print(id(return_list[0]))
    print(id(return_list[1]))
    print(id(return_list[2]))
    print(id(return_list[3]))

list1 = ['PA1','PA2','PA3','PA5']
list2 = ['PA1','PA2','PA3','PA6']
list3 = list1

test_alias(list1, list2)
test_alias(list1, list3)
