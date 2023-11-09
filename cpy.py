        
        # get data from a normal line
        if AR_date in line[0]: # this line has columns names
            continue
        elif not ((line[0] == "") and (line[2] == "")): # this line contains data TODO: may contain a bug
            if line[1] != "":
                curr_day = line[1]
            line_data = parse_line(line, curr_year, curr_month, curr_day, curr_date)
            curr_date = line_data[0]
            if not (line_data[0] == res_data[-1][0] and line_data[2] == "" and res_data[-1][2] == ""):
                res_data.append(line_data)

        print(line_data)


def main():