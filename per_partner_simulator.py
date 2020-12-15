from optimizer import Optimizer


class PerPartnerSimulator:
    def __init__(self, dataset, last_day_excluded_products, pseudorandom_seed):
        self.dataset = dataset
        self.pseudorandom_seed = pseudorandom_seed
        self.last_day_excluded_products = last_day_excluded_products

    def next_day(self):
        return Optimizer(self.dataset, self.last_day_excluded_products, self.pseudorandom_seed).next_day()

