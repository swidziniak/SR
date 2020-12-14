import numpy as np
import pandas as pd
import random


class Optimizer:
    def __init__(self, dataset, pseudorandom_seed):
        # get list of products_ids from dataset
        self.pseudorandom_seed = pseudorandom_seed
        self.products = dataset['product_id'].tolist()


    def get_excluded_products_pseudorandomly(self):
        dummy_list_of_potentially_excluded_products = self.products

        dummy_list_of_potentially_excluded_products = list(dummy_list_of_potentially_excluded_products)
        dummy_list_of_potentially_excluded_products.sort()
        dummy_how_many_products = round(len(dummy_list_of_potentially_excluded_products) / 3.1)
        random.seed(self.pseudorandom_seed)
        excluded_products = random.sample(dummy_list_of_potentially_excluded_products, dummy_how_many_products)
        return excluded_products

    def next_day(self):
        return self.get_excluded_products_pseudorandomly()