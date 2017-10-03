

def isEmpID(id):
    '''
    Employee ID is 6 characters in Length
    '''
    if len(id) != 6:
        return False
    return True


def isStoreID(id):
    '''
    Store ID is 3-6 characters in Length
    Note: The function when called with id, checks if the length is between (exclusive) 3 and (inclusive) 6 and returns true if condition is satisfied else false which is the default return policy
    '''
    if 3 < len(id) <= 6:
        return True
    return False


validEmpID = False
validStoreID = False
while not (validEmpID and validStoreID): # Both has to be True to exit the loop, Otherwise the condition continues to go to True.
    if not validEmpID:
        print('Enter Employee ID:')
        empID = input()
        validEmpID = isEmpID(empID)
        if not validEmpID:
            print('Invalid Employee ID\nTry Again...\n')
            continue
    print('Enter Store ID:')
    strID = input()
    validStoreID = isStoreID(strID)
    if not validStoreID:
        print("Invalid Store ID\nTry Again!...\n")
        continue
