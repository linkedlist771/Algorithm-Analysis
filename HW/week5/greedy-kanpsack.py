from typing import List, Dict
from logging import getLogger, basicConfig, INFO
logger = getLogger(__name__)


class GreedyKanpSackSolver:
    def __init__(self, item: Dict, capacity: int):
        self.item = item
        self.capacity = capacity
        self.item = item
        self.value = 0
        self.solution = {}

    def solve(self):
        item_value = self.item['value']
        item_weigh = self.item['weigh']
        item_name = self.item['name']
        item_value_per_weight = [_value/_weight for _value, _weight in zip(item_value, item_weigh)]
        # get the corresponding index after sort
        sorted_item_value_per_weight = sorted(item_value_per_weight, reverse=True)
        index = [item_value_per_weight.index(i) for i in sorted_item_value_per_weight]
        for idx in index:
            current_item_weigh = item_weigh[idx]
            if current_item_weigh <= self.capacity:
                self.capacity -= current_item_weigh
                self.value += item_value[idx]
                self.solution[item_name[idx]] = 1
            else:
                fraction = self.capacity / current_item_weigh
                self.value += item_value[idx] * fraction
                self.capacity = 0
                self.solution[item_name[idx]] = fraction
                break
        logger.info(f'The greedy kanpsack solver result has found its solution!')

    def get_solution(self):
        return self.solution.__str__()


if __name__ == "__main__":
    item = {
        'value': [60, 100, 120],
        'weigh': [10, 20, 30],
        'name': ['item1', 'item2', 'item3']
    }
    capacity = 50
    solver = GreedyKanpSackSolver(item, capacity)
    solver.solve()
    print(solver.get_solution())