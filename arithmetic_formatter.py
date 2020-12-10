import operator

def arithmetic_arranger(l: list, result = False) -> str:
    ops = {"+": operator.add, "-": operator.sub}

    if len(l) > 5:
        return "Error: Too many problems."
    
    if any(['*' in i for i in l]) or any(['/' in j for j in l]):
        return "Error: Operator must be '+' or '-'."
    
    tmp_list = [op.split() for op in l]
    
    if not all([d[0].isdigit() and d[2].isdigit() for d in tmp_list]):
        return "Error: Numbers must only contain digits."
    
    if not all([len(d[0]) <= 4 and len(d[2]) <= 4 for d in tmp_list]):
        return "Error: Numbers cannot be more than four digits."
    
    len_max = []
    
    for i in tmp_list:
        if int(i[0]) > int(i[2]):
            len_max.append(len(i[0]))
        else:
            len_max.append(len(i[2]))
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for j,k in enumerate(tmp_list):
        line1 += f"{k[0].rjust(len_max[j] + 2)}    "
        line2 += f"{k[1]}{k[2].rjust(len_max[j] + 1)}    "
        line3 += f"--{len_max[j]*'-'}    "
        if result:
            total = str(ops[k[1]](int(k[0]), int(k[2])))
            line4 += f"{total.rjust(len_max[j] + 2)}    "
    arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + "\n" + line3.rstrip()

    if result:
        return arranged_problems + "\n" + line4.rstrip()
    else:
        return arranged_problems

