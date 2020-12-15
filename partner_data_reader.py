import pandas as pd


class PartnerDataReader:
    def __init__(self, partner_id, today):
        self.partner_id = partner_id
        self.today = today

    def next_day(self):
        df = pd.read_csv(
            'resources/sorted/sorted_' + self.partner_id + '_dataset.csv')
        df['click_timestamp'] = pd.to_datetime(df['click_timestamp']).dt.strftime("%m/%d/%Y")
        date_time2 = self.today.strftime("%m/%d/%Y")

        new_df = df.loc[(df['click_timestamp'] == date_time2)]
        return new_df
