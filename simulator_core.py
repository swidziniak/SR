from partner_data_reader import PartnerDataReader
from per_partner_simulator import PerPartnerSimulator
import pandas as pd
import datetime


class SimulatorCore:
    def __init__(self, partners_to_involve_in_simulation, partners_to_read_data_from, today, pseudorandom_seed, number_of_simulation_steps):
        self.partners_to_involve_in_simulation = partners_to_involve_in_simulation
        self.partners_to_read_data_from = partners_to_read_data_from
        self.today = today
        self.pseudorandom_seed = pseudorandom_seed
        self.number_of_simulation_steps = number_of_simulation_steps

    def next_day(self):
        # orczytanie danych o kolejnym dniu na podstawie partner_data_reader(partners_to_read_data_from)
        last_day_excluded_products = []
        # excluded_products = []
        for x in range(self.number_of_simulation_steps):
            df = pd.DataFrame()
            # read data for each day for all partners in partners_to_involve_in_simulation
            for partner_id in self.partners_to_read_data_from:
                # add to dataframe
                df = (PartnerDataReader(partner_id, self.today).next_day()).append(df, ignore_index=True)
            print("Day", x+1, ":")
            print("Initial dataset length:", len(df["click_timestamp"]))
            # filter dataset based on last_day_excluded_products
            df = df[~df['product_id'].isin(last_day_excluded_products)]
            print("Dataset length without excluded products from day before:", len(df["click_timestamp"]))
            # initialize optimalisation for partners
            for partner_id in self.partners_to_involve_in_simulation:
                last_day_excluded_products = PerPartnerSimulator(partner_id, self.today, df, self.pseudorandom_seed).next_day()
            delta = datetime.timedelta(1)
            self.today += delta
            print("Number of excluded products: ", len(last_day_excluded_products))






