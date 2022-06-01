# If you wish you can import any modules from the standard library
# Do not use modules that are not in the standard library
from __future__ import print_function


def processData(lines):
    '''Modify this function to process `lines` as indicated
    in the question. At the end, return a list containing
    the appropriate values

    Please create appropriate classes, and use appropriate
    data structures as necessary.

    Do not print anything in this function.

    Submit this entire program (not just this function)
    as your answer
    '''

    ret_value = []

    max_salary=int(lines[0].split(',')[3].strip())
    new_string=''
    dept_list=set()
    for elem in lines:
        dept=elem.split(',')[2].strip()
        dept_list.add(dept)

    #creating two separate list for eng dept and testing department
    engg_list=[]
    testing_list=[]
    for elem in lines:
        d=elem.split(',')[2].strip()
        if(d=='Testing'):
            testing_list.append(elem)
        else:
            engg_list.append(elem)

    #Assuming salary of first employee to be the maximum salary od each department
    max_salary_testing=int(testing_list[0].split(',')[3].strip())
    max_salary_engg=int(engg_list[0].split(',')[3].strip())
    for each in testing_list:
        temp_salary=int(each.split(',')[3].strip())
        if(temp_salary >= max_salary_testing):
            max_salary_testing=temp_salary
            depart=each.split(',')[2].strip()
            emp_id=each.split(',')[0].strip()
            ret_value.append(str(depart) + " : " + str(emp_id))


    for each in engg_list:
        temp_salary_engg=int(each.split(',')[3].strip())
        if (temp_salary_engg >= max_salary_engg):
            max_salary_engg = temp_salary_engg
            depart = each.split(',')[2].strip()
            emp_id = each.split(',')[0].strip()
            ret_value.append(str(depart) + " : " + str(emp_id))


    #print(ret_value)
    return (ret_value)

def run():
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.append(line)

        ret_value = processData(lines)
        #print(ret_value)
        with open('output.txt', 'w') as fout:
            for s in ret_value:
                print(s, file=fout)


if __name__ == '__main__':
    run()
