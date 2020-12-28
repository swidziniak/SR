import pandas as pd


class PartnersProfiles:
    def __init__(self, partner_id):
        self.partner_id = partner_id

    def get_per_click_cost(self):
        # df = pd.read_csv(
        #     'resources/sorted/sorted_' + self.partner_id + '_dataset.csv')
        df = pd.read_csv(self.partner_id + '.csv')

        sales_amount = df.loc[(df['sales_amount'] != -1)].sum()['sales_amount']
        number_of_clicks = df.count()['sales_amount']

        # wartość średniego kosztu kliknięcia w kampanii danego reklamodawcy jest ilorazem 12% sumarycznej wartości
        # sprzedaży w całej kampanii danego reklamodawcy (partnera) i liczby wszystkich kliknięć w tej kampanii:
        per_partner_average_click_cost = (sales_amount * 0.12) / number_of_clicks

        return per_partner_average_click_cost
