#Cannot get this to run
#from thinkpython.com

def str_fill(i, len):
    return str(i).zfill(len)


def are_reversed(i, j):
    return str_fill(i, 2) == str_fill(j, 2)[::-1]

def num_instances(diff, flag=False):
    
    daughter = 0
    count = 0
    
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count+1
            if flag:
                print(daughter, mother)
            if mother >120:
                break
            daughter += 1
    return count


def check_diffs():
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n>0:
            print(diff, n)
        diff += 1


print("Diff # instances")

check_diffs()

print("Daughter Mother")
num_instances(18, True)
