import pandas as pd
import numpy as np
import datetime


class PartnerDataReader:
    def __init__(self, partner_id, today):
        self.partner_id = partner_id
        self.today = today

    def next_day(self):
        df = pd.read_csv('resources/sorted/sorted_' + self.partner_id + '_dataset.csv')
        print(self.partner_id)
        date_time = self.today.strftime("%Y-%m-%d")
        print(date_time)

        print((df['click_timestamp'].astype(str).str.contains(date_time)))
        new_df = df.loc[(df['click_timestamp'].astype(str).str.contains(date_time))]
        return new_df
