## Part 0: Intialization
import pandas as pd

input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
df_accounts = pd.read_csv(input_filepath)
df_accounts = df_accounts.rename(columns={' Amount ': 'Amount'})
df_accounts.columns = df_accounts.columns.str.lower()
df_accounts['amount']  = pd.to_numeric(df_accounts['amount'].str.replace('[^\-.0-9]', '', regex=True), errors='coerce')
df_accounts.drop(df_accounts[df_accounts['amount'] < 0].index, inplace=True)
df_accounts.dropna(axis='rows', inplace=True)

def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (data/p0-raw) into
        cleaned data ready to be analyzed (saved in data/p1-interim).
    """
    input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
    df_accounts = pd.read_csv(input_filepath)
    df_accounts = df_accounts.rename(columns={' Amount ': 'Amount'})
    df_accounts.columns = df_accounts.columns.str.lower()
    df_accounts['amount']  = pd.to_numeric(df_accounts['amount'].str.replace('[^\-.0-9]', '', regex=True), errors='coerce')
    """
    Delete negative valued columns

    In 2021-2022 there was only one negative row, here are its details:

               amount            ministry            category               payment detail                           recipient statutory additional detail
    8731 -259956709.0  Ministry Of Health  Statutory Payments  Ontario Government Pharmacy  Less: Distribution And Cash Sales   No Value          No Value

    It was deleted, not sure what was going on with that. Either it was mislabeled, so we need to make it positive. Or something else was going on.

    """
    df_accounts.drop(df_accounts[df_accounts['amount'] < 0].index, inplace=True)
    df_accounts.dropna(axis='rows', inplace=True)

if __name__ == '__main__':
    input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
    output_filepath = 'data/p1-interim/public-accounts.csv'
    main(input_filepath, output_filepath)
