## Part 0: Intialization
import pandas as pd

input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
df_accounts = pd.read_csv(input_filepath)
df_accounts = df_accounts.rename(columns={' Amount ': 'Amount'})
df_accounts.columns = df_accounts.columns.str.lower()
df_accounts['amount']  = pd.to_numeric(df_accounts['amount'].str.replace('[^\-.0-9]', '', regex=True), errors='coerce')

df_accounts[df_accounts['amount'] < 0]


def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (data/p0-raw) into
        cleaned data ready to be analyzed (saved in data/p1-interim).
    """
    input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
    df_accounts = pd.read_csv(input_filepath)
    df_accounts = df_accounts.rename(columns={' Amount ': 'Amount'})
    df_accounts.columns = df_accounts.columns.str.lower()
    df_accounts['amount']  = pd.to_numeric(df_accounts['amount'].str.replace('[^\-.0-9]', '', regex=True), errors='coerce')


if __name__ == '__main__':
    input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
    output_filepath = 'data/p1-interim/public-accounts.csv'
    main(input_filepath, output_filepath)
