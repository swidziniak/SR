import pandas as pd


class PartnerDataReader:
    def __init__(self, partner_id, today):
        self.partner_id = partner_id
        self.today = today

    def next_day(self):
        # df = pd.read_csv(
        #     'resources/sorted/sorted_' + self.partner_id + '_dataset.csv')
        df = pd.read_csv(self.partner_id + '.csv')

        # normal date format (537)
        df['click_timestamp'] = pd.to_datetime(df['click_timestamp']).dt.strftime('%Y-%m-%d')
        # unix timestamp (887)
        # df['click_timestamp'] = pd.to_datetime(df['click_timestamp'], unit='s').dt.strftime('%Y-%m-%d')
        date = self.today.strftime('%Y-%m-%d')

        new_df = df.loc[(df['click_timestamp'] == date)]
        return new_df
