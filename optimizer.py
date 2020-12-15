import random


class Optimizer:
    def __init__(self, last_day_dataset, last_day_excluded_products, pseudorandom_seed=12):
        # get list of products_ids from dataset
        self.pseudorandom_seed = pseudorandom_seed
        self.last_day_dataset = last_day_dataset
        self.last_day_excluded_products = last_day_excluded_products

    def get_excluded_products_pseudorandomly(self, products, how_many_ratio=20):
        dummy_list_of_potentially_excluded_products = products

        dummy_list_of_potentially_excluded_products = list(dummy_list_of_potentially_excluded_products)
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / how_many_ratio)
        random.seed(self.pseudorandom_seed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products, dummy_how_many_products)

        return excluded_products

    def next_day(self):
        if len(self.last_day_dataset):
            print('\nOPTIMISED:')
            yesterday_optimised_products = list(self.last_day_dataset['product_id'].unique())
            self.last_day_excluded_products = self.last_day_excluded_products + list(
                set(yesterday_optimised_products) - set(self.last_day_excluded_products))

            today_excluded_products = self.get_excluded_products_pseudorandomly(self.last_day_excluded_products)
            # today_excluded_products = products to exclude
            print(f'Number of products excluded today: {len(today_excluded_products)}')
            today_excluded_products.sort()

            return today_excluded_products
        else:
            return []
