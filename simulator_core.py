import json

from optimizer import Optimizer
from partner_data_reader import PartnerDataReader
import pandas as pd
import matplotlib.pyplot as plt
import datetime


class SimulatorCore:
    def __init__(self, partners_to_involve_in_simulation, partners_to_read_data_from, today, pseudorandom_seed,
                 number_of_simulation_steps, per_click_cost):
        self.partners_to_involve_in_simulation = partners_to_involve_in_simulation
        self.partners_to_read_data_from = partners_to_read_data_from
        self.today = today
        self.pseudorandom_seed = pseudorandom_seed
        self.number_of_simulation_steps = number_of_simulation_steps
        self.per_click_cost = per_click_cost

    def next_day(self):
        yesterday_df = pd.DataFrame()
        log = {'strategy': 'random', 'days': []}
        products_seen_so_far = []
        products_excluded_yesterday = []
        accumulated_profit = 0

        rows = [[0, 0]]
        for x in range(self.number_of_simulation_steps):
            df = pd.DataFrame()

            if len(yesterday_df):
                products_seen_so_far = sorted(yesterday_df['product_id'].unique().tolist())

            # read data for each day for all partners in partners_to_involve_in_simulation
            for partner_id in self.partners_to_read_data_from:
                # add to dataframe
                df = (PartnerDataReader(partner_id, self.today).next_day()).append(df, ignore_index=True)
            print('==========================================================')
            print(f'Day {x + 1}: {self.today.strftime("%Y-%m-%d")}')
            print(f'No. of products excluded yesterday: {len(products_excluded_yesterday)}')

            # initialize optimization
            products_excluded_yesterday = Optimizer(yesterday_df, products_excluded_yesterday,
                                                    self.pseudorandom_seed).next_day()

            # filter dataset based on products_excluded_yesterday
            today_df = df[~df['product_id'].isin(products_excluded_yesterday)]
            yesterday_df = yesterday_df.append(today_df)

            sales_amount = today_df.loc[(today_df['sales_amount'] != -1)].sum()['sales_amount']
            number_of_clicks = today_df.loc[(today_df['product_id'] != -1)].count()['product_id']

            accumulated_profit = accumulated_profit + ((sales_amount * 0.22) - (number_of_clicks * self.per_click_cost))
            today_products = df['product_id'].tolist()
            products_actually_excluded = sorted(
                list(set(products_excluded_yesterday).intersection(set(today_products))))

            rows.append([x + 1, accumulated_profit])

            log['days'].append({'day': self.today.strftime('%Y-%m-%d'), 'productsSeenSoFar': products_seen_so_far,
                                'productsToExclude': products_excluded_yesterday,
                                'productsActuallyExcluded': products_actually_excluded})

            delta = datetime.timedelta(1)
            self.today += delta
            print('===========================END============================')

        for partner_id in self.partners_to_read_data_from:
            with open(f'logs/{partner_id}_log.json', 'w') as outfile:
                json.dump(log, sort_keys=False, indent=4, separators=(',', ': '), fp=outfile)

        accumulated_sustained_profit_dataframe = pd.DataFrame(rows, columns=['Days of simulation',
                                                                             'Accumulated sustained profit'])
        accumulated_sustained_profit_dataframe.plot(x='Days of simulation', y='Accumulated sustained profit',
                                                    label=self.partners_to_read_data_from[0])
        plt.show()
