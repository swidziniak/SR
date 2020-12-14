from optimizer import Optimizer


class PerPartnerSimulator:
    def __init__(self, partner_id, today, dataset, pseudorandom_seed):
        self.partner_id = partner_id
        self.today = today
        self.dataset = dataset
        self.pseudorandom_seed = pseudorandom_seed

    def next_day(self):
        return Optimizer(self.dataset, self.pseudorandom_seed).next_day()

