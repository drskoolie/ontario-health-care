# -*- coding: utf-8 -*-

def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (data/p0-raw) into
        cleaned data ready to be analyzed (saved in data/p1-interim).
    """

if __name__ == '__main__':
    input_filepath = 'data/p0-raw/public-accounts/detailed-2021-22_2022-09-22.csv'
    output_filepath = 'data/p1-interim/public-data.csv'
    main(input_filepath, output_filepath)
