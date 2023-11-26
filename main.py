import b1Parse, b2Parse
import pandas as pd

def main():
    # read and process xls file and convert tables into lists of tuples
    invoices = b1Parse.read_data1()
    chics_list, constant_customers_list = b2Parse.read_data2()

    print("Processed data")


    # convert lists of tuples into dataframes
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

    # save data into csv files
    invoice_df.to_csv("processed_data/invoice.csv", index=False)
    cc_df.to_csv("processed_data/const_customers.csv", index=False)
    chics_df.to_csv("processed_data/chics.csv", index=False)

if __name__ == '__main__':
    main()
    dataset["kpi"] = dataset.apply(lambda r: 1 if r["working_hours"] == 0 else r["income"]/(r["working_hours"]*100), axis=1)