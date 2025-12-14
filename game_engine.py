# first we will define the function for removing common characters

def remove_char(l1,l2):

    for i in range(len(l1)):
        for j in range(len(l2)):

            if l1[i] == l2[j]:
                c = l1[i]

                l1.remove(c)
                l2.remove(c)

                l3 = l1 + ['*'] + l2

                return [l3,True]
            
    l3 = l1 + ['*'] + l2
    return [l3,False]

