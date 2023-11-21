import b1Parse, b2Parse
import pandas as pd

def main():
    invoices = b1Parse.read_data1()
    chics_list, constant_customers_list = b2Parse.read_data2()

    print("Processed data")

    invoice_df = pd.DataFrame(invoices, columns=["date", "day",
        "customer",
        "working_hours",
        "income",
        "outcome",
        "notes",
        "self_salary",
        "tools_salary",
        "car",
        "worker",
        "worker_salary"])

    cc_df = pd.DataFrame(constant_customers_list, columns=["name", "period"])
    chics_df = pd.DataFrame(chics_list, columns=["name", "date", "amount"])


    invoice_df.to_csv("processed_data/invoice.csv", index=False)
    cc_df.to_csv("processed_data/const_customers.csv", index=False)
    chics_df.to_csv("processed_data/chics.csv", index=False)

if __name__ == '__main__':
    main()