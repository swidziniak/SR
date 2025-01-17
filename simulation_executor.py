import simulator_core
import datetime
from partner_data_reader import PartnerDataReader


class SimulationExecutor:
    def __init__(self, partners_to_involve_in_simulation, partners_to_read_data_from, number_of_simulation_steps, npm,
                 pseudorandom_seed):
        self.number_of_simulation_steps = number_of_simulation_steps
        self.npm = npm
        self.pseudorandom_seed = pseudorandom_seed
        self.partners_to_read_data_from = partners_to_read_data_from

        for partner in partners_to_read_data_from:
            if partner not in partners_to_involve_in_simulation:
                partners_to_involve_in_simulation.append(partner)
        self.partners_to_involve_in_simulation = partners_to_involve_in_simulation

        # per_click_cost = PartnerDataReader("C306F0AD20C9B20C69271CC79B2E0887").get_per_click_cost()
        per_click_cost = PartnerDataReader("C0F515F0A2D0A5D9F854008BA76EB537").get_per_click_cost()

        # C0F515F0A2D0A5D9F854008BA76EB537
        start_date = datetime.date(2020, 9, 30)
        # C306F0AD20C9B20C69271CC79B2E0887
        # start_date = datetime.date(2020, 8, 3)
        simulator_core.SimulatorCore(self.partners_to_involve_in_simulation, self.partners_to_read_data_from,
                                     start_date, self.pseudorandom_seed, self.number_of_simulation_steps,
                                     per_click_cost).next_day()
