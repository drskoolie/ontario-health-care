## Part 0: Intialization
import pandas as pd

input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
df_accounts = pd.read_csv(input_filepath)
df_accounts = df_accounts.rename(columns={' Amount ': 'Amount'})
df_accounts.columns = df_accounts.columns.str.lower()
df_accounts['Amount']

def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (data/p0-raw) into
        cleaned data ready to be analyzed (saved in data/p1-interim).
    """
    input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
    df_accounts = pd.read_csv(input_filepath)
    df_accounts = df_accounts.rename(columns={' Amount ': 'Amount'})
    df_accounts.columns = df_accounts.columns.str.lower()


if __name__ == '__main__':
    input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
    output_filepath = 'data/p1-interim/public-accounts.csv'
    main(input_filepath, output_filepath)
