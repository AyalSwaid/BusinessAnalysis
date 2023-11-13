import datetime
import re

AR_name = "الاسم"
def parse_const_cust_data(line, index):
    name = line[index["name"]]
    if name != "":
        period = line[index[period]]
        return (name, period)
    return None

def parse_chic_data(line, chic_index):
    if line[chic_index["name"]] == "" and line[chic_index["date"]] == "" and line[chic_index["amount"]] == "":
        return None
    
    name = line[chic_index["name"]] if line[chic_index["name"]] != "" else "UNKNOWN"
    
    date_nums = re.findall(r'\d+', line[chic_index["date"]])
    if len(date_nums) < 3:
        date = f"{date_nums[0]}-{date_nums[1]}-{datetime.datetime.now().year}" 
    else:
        date = f"{date_nums[0]}-{date_nums[1]}-{date_nums[2]}" 
    
    amount = float(line[chic_index["amount"]]) if line[chic_index["amount"]] != "" else 0

    return (name, date, amount)

def read_data2():
    chic_index = {"name": 0, "date": 1, "amount": 2} # these indices doesnt include first index
    constant_index = {"name": 13, "period": 14}
    
    
    chics_list = []
    constant_customers_list = []
    
    lines = open("../data2.csv").read().split('\n')
    line_num = 0
    for line in lines:
        if len(line) < 14:
            break
        # print(len(line))
        line_num += 1
        line = line.split(",")

        if line_num > 4:
            chic_data = parse_chic_data(line, chic_index)
            chics_list.append(chic_data)

        # if line_num > 2:
            # const_customer_data = parse_const_cust_data(line, constant_index)
            # 
            # if const_customer_data is not None:
            #     constant_customers_list.append(const_customer_data)
            print(chic_data)
    return chics_list, constant_customers_list

    print(lines)
