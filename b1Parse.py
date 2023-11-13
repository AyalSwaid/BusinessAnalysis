import pandas as pd
import re

# arabic words
AR_year = "عام"
AR_month = "شهر"
AR_week = "الاسبوع"
AR_date = "تاريخ"

AR_sunday = "الاحد"

def check_new_year(line):
    """
    If entering new year return the year as int else return None
    """
    for cell in line:
        reg = re.findall(AR_year + r' (\d+)', cell)
        if len(reg) > 0:
            return reg[0]
    return None


def check_new_month(line):
    """
    If entering new month return the year as int else return None
    """
    for cell in line:
        reg = re.findall(AR_month + r'.*?(\d+)', cell)
        if len(reg) > 0:
            return reg[0]
    return None


def check_new_week(line):
    """
    If entering new week return the year as int else return None
    """
    for cell in line:
        reg = re.findall(AR_week + r'.*(\d+)', cell)
        if len(reg) > 0:
            return True
    return False


def parse_line(line, year, month, day, curr_date):
    # date format: {d-m-y}
    date = (re.findall(r'(\d{1,2})\W+\d+\.?', line[0])[0] + f"-{month}-{year}") if line[0] != "" else curr_date
    day = day
    customer = line[2]
    working_hours = (int(line[3].split(':')[0]) + (float(line[3].split(':')[1])/60)) if line[3] != "" else 0
    
    # doing income
    reg_income = re.findall(r'/(\d+)/', line[4])
    if line[4] == "" or 'v' in line[4].lower():
        income = 0
    elif len(reg_income) > 0:
        income = float(reg_income[0])
    else:
        income = float(line[4])

    outcome = float(line[5]) if line[5] != "" else 0
    notes = line[6] 
    self_salary = float(line[7]) if line[7] != "" else 0
    tools_salary = float(line[8]) if line[8] != "" else 0
    car = float(line[9]) if line[9] != "" else 0
    worker = line[10]
    worker_salary = float(line[11]) if line[11] != "" else 0


    return (
        date,
        day,
        customer,
        working_hours,
        income,
        outcome,
        notes,
        self_salary,
        tools_salary,
        car,
        worker,
        worker_salary
    )


def read_data1():
    curr_year = 0
    curr_month = 0
    curr_day = ""
    curr_date = 0

    res_data = [] # list of tuples


    data = open('../data1.csv').read().split('\n')
    for line in data:
        line = line.split(',')[1::]

        # ignore short lines
        if len(line) < 12:
            continue

        #check new week and continue if true
        if check_new_week(line):
            continue

        # check if new year
        new_year = check_new_year(line)
        if new_year is not None:
            curr_year = new_year
            continue
        
        # check if new month
        new_month = check_new_month(line)
        if new_month is not None:
            curr_month = new_month
            continue
        
        # get data from a normal line
        if AR_date in line[0]: # this line has columns names
            continue
        elif not ((line[0] == "") and (line[2] == "")): # this line contains data TODO: may contain a bug
            if line[1] != "":
                curr_day = line[1]
            line_data = parse_line(line, curr_year, curr_month, curr_day, curr_date)
            curr_date = line_data[0]
            res_data.append(line_data)

            # print(line_data)
    return res_data