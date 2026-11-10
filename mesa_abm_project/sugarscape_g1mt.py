"""
Sugarscape with Traders (SugarscapeG1mt) — Final Course Model (Session 20)
Source: Complexity Explorer (Santa Fe Institute) — "Agent-Based Models with Python: An Introduction to Mesa"
Reference: Epstein, J. M., & Axtell, R. (1996). Growing Artificial Societies: Social Science from the Bottom Up.

Targeted fixes applied for standalone local execution outside Google Colab:
1. Removed hard dependency on `google.colab.drive` and hardcoded `/content/drive/MyDrive/sugar-map.txt` path;
   now resolves `sugar-map.txt` relative to this file (with fallback to current directory or Colab path).
2. Guarded `geometric_mean(list_of_prices)` against empty price lists (`len == 0`) on steps without trades,
   returning `np.nan` cleanly without emitting NumPy `Mean of empty slice` RuntimeWarnings.
3. Unpacked `self.grid.coord_iter()` items compatibly across Mesa 1.1.x `(content, (x, y))` and
   Mesa 1.2.x / 2.x `(content, x, y)`.
"""

import math
from pathlib import Path
import mesa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


# =====================================================================
# Helper Functions (Sessions 12, 18, 19)
# =====================================================================

def get_distance(pos_1, pos_2):
    """
    Calculate the Euclidean distance between two positions.
    Used in Trader.move().
    """
    x1, y1 = pos_1
    x2, y2 = pos_2
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx**2 + dy**2)


def flatten(list_of_lists):
    """
    Helper function for model datacollector for trade price.
    Collapses agent price list into one list.
    """
    return [item for sublist in list_of_lists for item in sublist]


def geometric_mean(list_of_prices):
    """
    Find the geometric mean of a list of prices.
    Returns np.nan if no trades occurred in the current step.
    """
    if len(list_of_prices) == 0:
        return np.nan
    return float(np.exp(np.log(list_of_prices).mean()))


def get_trade(agent):
    """
    For agent reporters in DataCollector.
    Returns list of trade partners for Trader agents and None for other agents.
    """
    if type(agent) == Trader:
        return agent.trade_partners
    else:
        return None


# =====================================================================
# Resource Classes (Sessions 3, 5, 6, 8)
# =====================================================================

class Sugar(mesa.Agent):
    """
    Sugar:
    - contains an amount of sugar
    - grows 1 amount of sugar at each turn (Growback rule G1)
    """

    def __init__(self, unique_id, model, pos, max_sugar):
        super().__init__(unique_id, model)
        self.pos = pos
        self.amount = max_sugar
        self.max_sugar = max_sugar

    def step(self):
        """
        Sugar growth function, adds one unit of sugar each step until max amount.
        """
        self.amount = min([self.max_sugar, self.amount + 1])


class Spice(mesa.Agent):
    """
    Spice:
    - contains an amount of spice
    - grows 1 amount of spice at each turn (Growback rule G1)
    """

    def __init__(self, unique_id, model, pos, max_spice):
        super().__init__(unique_id, model)
        self.pos = pos
        self.amount = max_spice
        self.max_spice = max_spice

    def step(self):
        """
        Spice growth function, adds one unit of spice each step until max amount.
        """
        self.amount = min([self.max_spice, self.amount + 1])


# =====================================================================
# Trader Agent (Sessions 3, 7, 9–17)
# =====================================================================

class Trader(mesa.Agent):
    """
    Trader:
    - has a metabolism of sugar and spice
    - harvest and trade sugar and spice to survive
    """

    def __init__(self, unique_id, model, pos, moore=False, sugar=0,
                 spice=0, metabolism_sugar=0, metabolism_spice=0,
                 vision=0):
        super().__init__(unique_id, model)
        self.pos = pos
        self.moore = moore
        self.sugar = sugar
        self.spice = spice
        self.metabolism_sugar = metabolism_sugar
        self.metabolism_spice = metabolism_spice
        self.vision = vision
        self.prices = []
        self.trade_partners = []

    def get_sugar(self, pos):
        """Used in self.get_sugar_amount() and self.eat()."""
        this_cell = self.model.grid.get_cell_list_contents(pos)
        for agent in this_cell:
            if type(agent) is Sugar:
                return agent
        return None

    def get_sugar_amount(self, pos):
        """Used in self.move() as part of self.calculate_welfare()."""
        sugar_patch = self.get_sugar(pos)
        if sugar_patch:
            return sugar_patch.amount
        return 0

    def get_spice(self, pos):
        """Used in self.get_spice_amount() and self.eat()."""
        this_cell = self.model.grid.get_cell_list_contents(pos)
        for agent in this_cell:
            if type(agent) is Spice:
                return agent
        return None

    def get_spice_amount(self, pos):
        """Used in self.move() as part of self.calculate_welfare()."""
        spice_patch = self.get_spice(pos)
        if spice_patch:
            return spice_patch.amount
        return 0

    def get_trader(self, pos):
        """Helper function used in self.trade_with_neighbors()."""
        this_cell = self.model.grid.get_cell_list_contents(pos)
        for agent in this_cell:
            if isinstance(agent, Trader):
                return agent

    def is_occupied_by_other(self, pos):
        """Helper function part 1 of self.move() and self.trade_with_neighbors()."""
        if pos == self.pos:
            # Agent's own position is considered unoccupied as agent can stay there
            return False
        this_cell = self.model.grid.get_cell_list_contents(pos)
        for a in this_cell:
            if isinstance(a, Trader):
                return True
        return False

    def calculate_welfare(self, sugar, spice):
        """
        Helper function for part 2 of self.move() and self.trade().
        Cobb-Douglas functional form; starting on p. 97 of Growing Artificial Societies.
        """
        m_total = self.metabolism_sugar + self.metabolism_spice
        return sugar**(self.metabolism_sugar / m_total) * spice**(
            self.metabolism_spice / m_total)

    def is_starved(self):
        """Helper function for self.maybe_die()."""
        return (self.sugar <= 0) or (self.spice <= 0)

    def calculate_MRS(self, sugar, spice):
        """
        Helper function for self.trade() and self.maybe_sell_spice().
        Determines what trader agent needs and can give up (p. 101).
        """
        return (spice / self.metabolism_spice) / (sugar / self.metabolism_sugar)

    def calculate_sell_spice_amount(self, price):
        """Helper function for self.maybe_sell_spice() which is called from self.trade()."""
        if price >= 1:
            sugar = 1
            spice = int(price)
        else:
            sugar = int(1 / price)
            spice = 1
        return sugar, spice

    def sell_spice(self, other, sugar, spice):
        """Used in self.maybe_sell_spice(); exchanges sugar and spice between traders."""
        self.sugar += sugar
        other.sugar -= sugar
        self.spice -= spice
        other.spice += spice

    def maybe_sell_spice(self, other, price, welfare_self, welfare_other):
        """Helper function for self.trade()."""
        sugar_exchanged, spice_exchanged = self.calculate_sell_spice_amount(price)

        # Assess new sugar and spice amount - what if change did occur
        self_sugar = self.sugar + sugar_exchanged
        other_sugar = other.sugar - sugar_exchanged
        self_spice = self.spice - spice_exchanged
        other_spice = other.spice + spice_exchanged

        # Double check to ensure agents have resources
        if ((self_sugar <= 0) or
            (other_sugar <= 0) or
            (self_spice <= 0) or
            (other_spice <= 0)):
            return False

        # Trade criteria #1 - are both agents better off?
        both_agents_better_off = (
            (welfare_self < self.calculate_welfare(self_sugar, self_spice)) and
            (welfare_other < other.calculate_welfare(other_sugar, other_spice)))

        # Trade criteria #2 - is their MRS not crossing?
        mrs_not_crossing = self.calculate_MRS(
            self_sugar, self_spice
        ) > other.calculate_MRS(other_sugar, other_spice)

        if not (both_agents_better_off and mrs_not_crossing):
            return False

        # Criteria met, execute trade
        self.sell_spice(other, sugar_exchanged, spice_exchanged)
        return True

    def trade(self, other):
        """
        Helper function used in trade_with_neighbors().
        other is a Trader agent object.
        """
        assert self.sugar > 0
        assert self.spice > 0
        assert other.sugar > 0
        assert other.spice > 0

        mrs_self = self.calculate_MRS(self.sugar, self.spice)
        mrs_other = other.calculate_MRS(other.sugar, other.spice)

        welfare_self = self.calculate_welfare(self.sugar, self.spice)
        welfare_other = other.calculate_welfare(other.sugar, other.spice)

        if math.isclose(mrs_self, mrs_other):
            return

        # Calculate price (geometric mean of both agents' MRS)
        price = math.sqrt(mrs_self * mrs_other)

        if mrs_self > mrs_other:
            # self is a sugar buyer, spice seller
            sold = self.maybe_sell_spice(other, price, welfare_self, welfare_other)
            if not sold:
                return
        else:
            # self is a spice buyer, sugar seller
            sold = other.maybe_sell_spice(self, price, welfare_other, welfare_self)
            if not sold:
                return

        # Capture data
        self.prices.append(price)
        self.trade_partners.append(other.unique_id)

        # Continue trading recursively until no mutually beneficial trade remains
        self.trade(other)

    # -----------------------------------------------------------------
    # Main Trader Actions (Rule M, Consumption, Rule T)
    # -----------------------------------------------------------------

    def move(self):
        """
        Function for trader agent to identify optimal move for each step in 4 parts:
        1 - identify all possible moves
        2 - determine which move maximizes welfare
        3 - find closest best option
        4 - move
        """
        # 1. Identify all possible moves (Von Neumann neighborhood up to self.vision, including center)
        neighbors = [i
                     for i in self.model.grid.get_neighborhood(
                         self.pos, self.moore, True, self.vision
                     ) if not self.is_occupied_by_other(i)]

        # 2. Determine which move maximizes welfare
        welfares = [
            self.calculate_welfare(
                self.sugar + self.get_sugar_amount(pos),
                self.spice + self.get_spice_amount(pos))
            for pos in neighbors
        ]

        # 3. Find closest best option
        max_welfare = max(welfares)
        candidate_indices = [i for i in range(len(welfares))
                             if math.isclose(welfares[i], max_welfare)]
        candidates = [neighbors[i] for i in candidate_indices]

        min_dist = min(get_distance(self.pos, pos) for pos in candidates)
        final_candidates = [pos for pos in candidates
                            if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02)]
        self.random.shuffle(final_candidates)

        # 4. Move Agent
        self.model.grid.move_agent(self, final_candidates[0])

    def eat(self):
        """Harvest all sugar and spice in current cell, then deduct metabolism."""
        sugar_patch = self.get_sugar(self.pos)
        if sugar_patch:
            self.sugar += sugar_patch.amount
            sugar_patch.amount = 0
        self.sugar -= self.metabolism_sugar

        spice_patch = self.get_spice(self.pos)
        if spice_patch:
            self.spice += spice_patch.amount
            spice_patch.amount = 0
        self.spice -= self.metabolism_spice

    def maybe_die(self):
        """Function to remove Traders who have consumed all their sugar or spice."""
        if self.is_starved():
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)

    def trade_with_neighbors(self):
        """
        Function for trader agents to decide who to trade with in three parts:
        1 - identify neighbors who can trade
        2 - trade
        3 - collect data
        """
        neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
            self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
        ]

        if len(neighbor_agents) == 0:
            return

        for a in neighbor_agents:
            if a:
                self.trade(a)
        return


# =====================================================================
# Model Class (Sessions 3–8, 18–20)
# =====================================================================

class SugarscapeG1mt(mesa.Model):
    """
    Manager class to run Sugarscape with Traders (G1, M, T).
    """

    def __init__(self, width=50, height=50, initial_population=200,
                 endowment_min=25, endowment_max=50, metabolism_min=1,
                 metabolism_max=5, vision_min=1, vision_max=5, seed=None):
        super().__init__(seed=seed)
        self.width = width
        self.height = height
        self.initial_population = initial_population
        self.endowment_min = endowment_min
        self.endowment_max = endowment_max
        self.metabolism_min = metabolism_min
        self.metabolism_max = metabolism_max
        self.vision_min = vision_min
        self.vision_max = vision_max
        self.running = True

        # Initiate activation schedule
        self.schedule = mesa.time.RandomActivationByType(self)
        # Initiate Mesa MultiGrid (non-toroidal 50x50)
        self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)
        # Initiate DataCollector
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Trader": lambda m: m.schedule.get_type_count(Trader),
                "Trade Volume": lambda m: sum(len(a.trade_partners)
                    for a in m.schedule.agents_by_type[Trader].values()),
                "Price": lambda m: geometric_mean(
                    flatten([a.prices for a in m.schedule.agents_by_type[Trader].values()]))
            },
            agent_reporters={"Trade Network": lambda a: get_trade(a)}
        )

        # Read in landscape file (local sugar-map.txt with fallback to Colab path)
        local_map = Path(__file__).with_name("sugar-map.txt")
        colab_map = Path("/content/drive/MyDrive/sugar-map.txt")
        map_path = local_map if local_map.exists() else (
            Path("sugar-map.txt") if Path("sugar-map.txt").exists() else colab_map
        )
        sugar_distribution = np.genfromtxt(map_path)
        spice_distribution = np.flip(sugar_distribution, 1)

        agent_id = 0
        for item in self.grid.coord_iter():
            # Support both Mesa 1.1.x (content, (x, y)) and Mesa 1.2+/2.x (content, x, y)
            if len(item) == 2:
                _, (x, y) = item
            else:
                _, x, y = item

            max_sugar = sugar_distribution[x, y]
            if max_sugar > 0:
                sugar = Sugar(agent_id, self, (x, y), max_sugar)
                self.schedule.add(sugar)
                self.grid.place_agent(sugar, (x, y))
                agent_id += 1

            max_spice = spice_distribution[x, y]
            if max_spice > 0:
                spice = Spice(agent_id, self, (x, y), max_spice)
                self.schedule.add(spice)
                self.grid.place_agent(spice, (x, y))
                agent_id += 1

        for i in range(self.initial_population):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            # Growing Artificial Societies p. 108 initialization
            sugar = int(self.random.uniform(self.endowment_min, self.endowment_max + 1))
            spice = int(self.random.uniform(self.endowment_min, self.endowment_max + 1))
            metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max + 1))
            metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max + 1))
            vision = int(self.random.uniform(self.vision_min, self.vision_max + 1))

            trader = Trader(
                agent_id,
                self,
                (x, y),
                moore=False,
                sugar=sugar,
                spice=spice,
                metabolism_sugar=metabolism_sugar,
                metabolism_spice=metabolism_spice,
                vision=vision
            )
            self.grid.place_agent(trader, (x, y))
            self.schedule.add(trader)
            agent_id += 1

    def randomize_traders(self):
        """
        Helper function for self.step().
        Puts traders in randomized list for step function.
        """
        trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
        self.random.shuffle(trader_shuffle)
        return trader_shuffle

    def step(self):
        """
        Unique step function that does staged activation of sugar and spice
        and then randomly activates traders.
        """
        # 1. Step Sugar agents
        for sugar in self.schedule.agents_by_type[Sugar].values():
            sugar.step()

        # 2. Step Spice agents
        for spice in self.schedule.agents_by_type[Spice].values():
            spice.step()

        # 3. Step Trader agents (move, eat, maybe_die)
        trader_shuffle = self.randomize_traders()
        for agent in trader_shuffle:
            agent.prices = []
            agent.trade_partners = []
            agent.move()
            agent.eat()
            agent.maybe_die()

        # 4. Re-shuffle surviving traders and trade with neighbors
        trader_shuffle = self.randomize_traders()
        for agent in trader_shuffle:
            agent.trade_with_neighbors()

        self.schedule.steps += 1  # Important for data collector to track number of steps

        # 5. Collect model & agent level data
        self.datacollector.collect(self)

        # Remove None records from non-Trader (Sugar/Spice) agents to conserve memory
        agent_trades = self.datacollector._agent_records[self.schedule.steps]
        agent_trades = [agent for agent in agent_trades if agent[2] is not None]
        self.datacollector._agent_records[self.schedule.steps] = agent_trades

    def run_model(self, step_count=1000):
        for i in range(step_count):
            self.step()


if __name__ == "__main__":
    print("Running SugarscapeG1mt single simulation (1000 steps, seed=42)...")
    model = SugarscapeG1mt(seed=42)
    model.run_model(step_count=1000)

    results = model.datacollector.get_model_vars_dataframe()
    print("\n--- Model DataCollector Summary (First 5 & Last 5 Steps) ---")
    print(results.head())
    print(results.tail())
    print(f"\nSurviving Traders at step 1000: {int(results['Trader'].iloc[-1])} / {model.initial_population}")
    print(f"Geometric Mean Price (all steps): {results['Price'].dropna().mean():.4f}")
