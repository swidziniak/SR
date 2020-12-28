import random


class Optimizer:
    def __init__(self, yesterday_df, products_excluded_yesterday, pseudorandom_seed=12):
        self.pseudorandom_seed = pseudorandom_seed
        self.yesterday_df = yesterday_df
        self.products_excluded_yesterday = products_excluded_yesterday

    def get_excluded_products_pseudorandomly(self, products, how_many_ratio=20):
        dummy_list_of_potentially_excluded_products = products

        dummy_list_of_potentially_excluded_products = list(dummy_list_of_potentially_excluded_products)
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / how_many_ratio)
        random.seed(self.pseudorandom_seed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products, dummy_how_many_products)

        return excluded_products

    def next_day(self):
        if len(self.yesterday_df):
            yesterday_products_optimized = list(self.yesterday_df['product_id'].unique())
            self.products_excluded_yesterday = self.products_excluded_yesterday + list(
                set(yesterday_products_optimized) - set(self.products_excluded_yesterday))

            products_excluded_today = self.get_excluded_products_pseudorandomly(self.products_excluded_yesterday)
            print(f'No. of products excluded today: {len(products_excluded_today)}')
            products_excluded_today.sort()

            return products_excluded_today
        else:
            return []
