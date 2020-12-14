import pandas as pd

class PartnersProfiles:
    def __init__(self, partner_id):
        self.partner_id = partner_id


    def getPerClickCost(self):
        df = pd.read_csv(
            'D:/Ala/Studia/Informatyka/IV rok/VII SEMESTR/Systemy rekomendacyjne/dataset/sorted_' + self.partner_id + '_dataset.csv')

        salesAmount = df.loc[(df['SalesAmountInEuro'] != -1)].sum()['SalesAmountInEuro']

        numberOfClicks = df.count()['SalesAmountInEuro']

        return (salesAmount * 0.12)/numberOfClicks