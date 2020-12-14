import simulator_core
import datetime


class SimulationExecutor:
    def __init__(self, partners_to_involve_in_simulation, partners_to_read_data_from, number_of_simulation_steps, npm, pseudorandom_seed):
        # init values from configuration file
        self.number_of_simulation_steps = number_of_simulation_steps
        self.npm = npm
        self.pseudorandom_seed = pseudorandom_seed
        self.partners_to_read_data_from = partners_to_read_data_from
        for partner in partners_to_read_data_from:
            if partner not in partners_to_involve_in_simulation:
                partners_to_involve_in_simulation.append(partner)
        self.partners_to_involve_in_simulation = partners_to_involve_in_simulation

        start_date = datetime.date(2020, 8, 3) + datetime.timedelta(days=1)
        simulator_core.SimulatorCore(self.partners_to_involve_in_simulation, self.partners_to_read_data_from, start_date, self.pseudorandom_seed, self.number_of_simulation_steps).next_day()


test = SimulationExecutor(["1BB44E9DB5ABBD9F9A64B475291DC555", "2F13BB7176EBE22D37B5AFB3C814FE12"], ["2F13BB7176EBE22D37B5AFB3C814FE12", "1BB44E9DB5ABBD9F9A64B475291DC555"], 3, 0, 12)