import os
import re
from datetime import datetime, date

import pandas as pd


# implementacja z pomocą Macieja Drzewieckiego

class PartnersDataSplitter:
    Vector = list
    DEFAULT_COLUMNS = ["sale", "sales_amount", "time_delay_for_conversion", "click_timestamp", "nb_clicks_1week",
                       "product_price", "product_age_group", "device_type", "audience_id", "product_gender",
                       "product_brand", "category_1", "category_2", "category_3", "category_4", "category_5",
                       "category_6", "category_7", "product_country", "product_id", "product_title",
                       "partner_id", "user_id"]

    def __init__(self, exclude_profiles: Vector = None, columns: Vector = None):
        self.exclude_profiles = exclude_profiles
        if columns:
            self.data_format = columns
        else:
            self.data_format = PartnersDataSplitter.DEFAULT_COLUMNS
        self.raw_dataset_df = None

    def load_dataset(self):
        self.raw_dataset_df = pd.read_csv("resources\\CriteoSearchData", sep='\t', header=None,
                                          names=self.data_format, dtype=str)

    def split_dataset_by_partners(self):
        if self.raw_dataset_df is None:
            self.load_dataset()
        i = 1
        for partner, data in self.raw_dataset_df.groupby('partner_id'):
            data.to_csv("resources/{}_dataset.csv".format(partner), sep='\t', index=False, header=None)
            i += 1
            print("{}/313 partner files created.".format(i))

    def split_dataset_by_partner__spec(self):
        # LAST PASSED 11.08.2020
        # test_parameter_for_Mr_Riegel_20201103
        # for partner_id C0F515F0A2D0A5D9F854008BA76EB537:
        #     24079
        # test_parameter_for_Mr_Riegel_20201103
        # for partner_id E3DDEB04F8AFF944B11943BB57D2F620:
        #     3090150
        # test_parameter_for_Mr_Riegel_20201103
        # for partner_id E68029E9BCE099A60571AF757CBB6A08:
        #     3852
        partners_selected_for_test_parameter_for_mr_riegel_20201103 = ["C0F515F0A2D0A5D9F854008BA76EB537",
                                                                       "E3DDEB04F8AFF944B11943BB57D2F620",
                                                                       "E68029E9BCE099A60571AF757CBB6A08"]

        if self.raw_dataset_df is None:
            self.load_dataset()
        df_groups_for_partners = self.raw_dataset_df.groupby("partner_id")
        for partner_id, df_group_for_partner in df_groups_for_partners:
            if partner_id in partners_selected_for_test_parameter_for_mr_riegel_20201103:
                test_parameter_for_mr_riegel_20201103 = df_group_for_partner.shape[0]
                print("test_parameter_for_mr_riegel_20201103 for partner_id " + partner_id + " :",
                      test_parameter_for_mr_riegel_20201103)

    def timestamps_to_sorted_dates(self):
        # sortowanie tylko po dniu, zeby przyspieszyc proces, stad kolumna tymczasowa days_since_year_begin
        all_files = [filename for filename in os.listdir("resources") if
                     re.compile("^[0-9a-fA-F]+_dataset.csv$").search(filename)]
        already_sorted = list(map(lambda directory: directory[7:],
                                  [directory for directory in os.listdir("resources") if
                                   re.compile("sorted_[0-9a-fA-F]+_dataset.csv").search(directory)]))
        not_sorted_files = set(all_files) - set(already_sorted)
        i = 0
        for filename in not_sorted_files:
            i += 1
            partner_dataset = pd.read_csv("resources/{}".format(filename), sep='\t', header=None,
                                          names=self.data_format, dtype=str)
            partner_dataset['days_since_year_begin'] = 0
            k = 0
            for j in range(len(partner_dataset['click_timestamp'])):
                k += 1
                partner_dataset['click_timestamp'][j] = datetime.fromtimestamp(
                    int(partner_dataset['click_timestamp'][j]))
                days_passed = abs(
                    date(partner_dataset['click_timestamp'][j].year, 1, 1) - partner_dataset['click_timestamp'][
                        j].date())
                partner_dataset['days_since_year_begin'][j] = days_passed.days
                print("calcualted days for {}/{} rows.".format(k, len(partner_dataset['click_timestamp'])))
            print("Got days column calculated")
            partner_dataset = partner_dataset.sort_values(by='days_since_year_begin')
            del partner_dataset['days_since_year_begin']
            partner_dataset.to_csv("resources/sorted_{}".format(filename), sep='\t', index=False, header=None)
            print("Processed {}. {}/{} files.".format(filename, i, len(not_sorted_files)))

    # w podzielonych plikach partnerów brakowało pierwszego wiersza z nazwami kolumn, ta funkcja je dodaje
    def add_column_headers(self):
        csv_files = os.listdir("resources/sorted")

        headers = ["sale", "sales_amount", "time_delay_for_conversion", "click_timestamp", "nb_clicks_1week",
                   "product_price", "product_age_group", "device_type", "audience_id", "product_gender",
                   "product_brand", "category_1", "category_2", "category_3", "category_4", "category_5",
                   "category_6", "category_7", "product_country", "product_id", "product_title",
                   "partner_id", "user_id"]

        for file in csv_files:
            csv = pd.read_csv("resources/sorted/" + file, sep='\t')
            data_frame = pd.DataFrame(csv.values, columns=headers)
            data_frame.to_csv("resources/sorted/" + file, sep=',', index=None)
