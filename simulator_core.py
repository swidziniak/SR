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
        last_day_excluded_products = []
        yesterday_df = pd.DataFrame()
        accumulated_profit = 0

        rows = [[0, 0]]
        for x in range(self.number_of_simulation_steps):
            df = pd.DataFrame()
            # read data for each day for all partners in partners_to_involve_in_simulation
            for partner_id in self.partners_to_read_data_from:
                # add to dataframe
                df = (PartnerDataReader(partner_id, self.today).next_day()).append(df, ignore_index=True)
            print('==========================================================')
            print(f'Day {x + 1}: {self.today.strftime("%d/%m/%Y")}')
            if len(yesterday_df) > 0:
                print('Yesterday dataset length:', len(yesterday_df['product_id'].unique()))
            else:
                print('Yesterday dataset length: 0')

            print(f'Number of last day excluded products: {len(last_day_excluded_products)}')

            # initialize optimization for partner
            last_day_excluded_products = Optimizer(yesterday_df, last_day_excluded_products,
                                                   self.pseudorandom_seed).next_day()
            # filter dataset based on last_day_excluded_products
            today_df = df[~df['product_id'].isin(last_day_excluded_products)]
            yesterday_df = yesterday_df.append(today_df)

            print('Initial dataset length:', len(df['product_id'].unique()))
            print('Dataset length without excluded products from day before:', len(yesterday_df["product_id"].unique()))

            sales_amount = today_df.loc[(today_df['sales_amount'] != -1)].sum()['sales_amount']

            number_of_clicks = today_df.loc[(today_df['product_id'] != -1)].count()['product_id']

            accumulated_profit = accumulated_profit + ((sales_amount * 0.22) - (number_of_clicks * self.per_click_cost))
            # profit_per_day = sales_amount * 0.22 - number_of_clicks * self.per_click_cost

            rows.append([x + 1, accumulated_profit])

            delta = datetime.timedelta(1)
            self.today += delta
            print('===========================END============================')

        accumulated_sustained_profit_dataframe = pd.DataFrame(rows, columns=['Days of simulation', 'Accumulated sustained profit'])
        accumulated_sustained_profit_dataframe.plot(x='Days of simulation', y='Accumulated sustained profit', label=self.partners_to_read_data_from[0])
        plt.show()
