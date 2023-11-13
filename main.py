import b1Parse, b2Parse


def main():
    invoices = b1Parse.read_data1()
    chics_list, constant_customers_list = b2Parse.read_data2()

    print("DONE")


if __name__ == '__main__':
    main()