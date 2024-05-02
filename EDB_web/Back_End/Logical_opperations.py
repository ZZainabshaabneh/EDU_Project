# Explain what is the logical operations
print("________________________________________________________________________")
print("The logical operation ")
print("We will study three type of logical operations which is (and - or - not)")
print("________________________________________________________________________")
end = 0

print("(and) operator, means there are two cases, if both cases logically true >> true, either >> false ")
print("(or) operator, means there are two cases, if one of cases logically true >> true, either >> false ")
print("(not) operator, means there a case, if it is logically true >will reversed> false, either >> true ")
print("Now try to answer Right and Wrong to understand the logical operation")
print("________________________________________________________________________")

while end == 0:

    number_1 = int(input("pleas inter the square of 5"))
    logical_operator = str(input("please choose a logical operator"))
    number_2 = int(input("pleas inter the square of 10"))
    if logical_operator == 'and':
        if number_1 == 25 and number_2 == 100:
            print(f"If square of {number_1} = 25 'and' square of {number_2} = 100: |True| ")
        else:
            print("False, in order to get true, 'and' operation should see both condition are correct")
    elif logical_operator == 'or':
        if number_1 == 25 or number_2 == 100:
            print(f"If square of {number_1} = 25 'or' square of {number_2} = 100: |True| ")
        else:
            print("False, in order to get true, 'or' operation should see one of condition are correct")
    elif logical_operator == 'not':
        if not (number_1 == 25 and number_2 == 100):
            print(f"If square of {number_1} = 25 'and' square of {number_2} = 100: |false| ")
        else:
            print("'not' operation will reverse real answer, so now it is true")
    else:
        print("this is not operation try again")
    print("________________________________________________________________________")
    end = int(input("to continue press 0, to end press 1"))