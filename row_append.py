import os
import pandas as pd
import csv

# przez datasplitter brakowalo pierwszej linijki z nazwami kolumn, ten plik ja dodaje
# zrobione wspolnie z Maciejem Anglartem

csv_files = os.listdir("resources/sorted")

row_contents = ["sale", "sales_amount", "time_delay_for_conversion", "click_timestamp", "nb_clicks_1week",
                       "product_price", "product_age_group", "device_type", "audience_id", "product_gender",
                       "product_brand", "category_1", "category_2", "category_3", "category_4", "category_5",
                       "category_6", "category_7", "product_country", "product_id", "product_title",
                       "partner_id", "user_id"]

for name in csv_files:
    print(name)

print(len(csv_files))
for file in csv_files:
    Cov = pd.read_csv("resources/sorted/" + file, sep='\t')
    Frame = pd.DataFrame(Cov.values, columns=['sale', 'sales_amount', 'time_delay_for_conversion', 'click_timestamp', 'nb_clicks_1week',
                       'product_price', 'product_age_group', 'device_type', 'audience_id', 'product_gender',
                       'product_brand', 'category_1', 'category_2', 'category_3', 'category_4', 'category_5',
                       'category_6', 'category_7', 'product_country', 'product_id', 'product_title',
                       'partner_id', 'user_id'])
    Frame.to_csv("resources/sorted/" + file, sep=',', index=None)
