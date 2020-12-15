import simulator_core
import datetime

from partners_profiles import PartnersProfiles


class SimulationExecutor:
    def __init__(self, partners_to_involve_in_simulation, partners_to_read_data_from, number_of_simulation_steps, npm,
                 pseudorandom_seed):
        # init values from configuration file
        self.number_of_simulation_steps = number_of_simulation_steps
        self.npm = npm
        self.pseudorandom_seed = pseudorandom_seed
        self.partners_to_read_data_from = partners_to_read_data_from
        for partner in partners_to_read_data_from:
            if partner not in partners_to_involve_in_simulation:
                partners_to_involve_in_simulation.append(partner)
        self.partners_to_involve_in_simulation = partners_to_involve_in_simulation

        per_click_cost = PartnersProfiles("C0F515F0A2D0A5D9F854008BA76EB537").get_per_click_cost()

        start_date = datetime.date(2020, 9, 30)
        simulator_core.SimulatorCore(self.partners_to_involve_in_simulation, self.partners_to_read_data_from,
                                     start_date, self.pseudorandom_seed, self.number_of_simulation_steps,
                                     per_click_cost).next_day()
