import random
import copy
class Hat:
    def __init__(self, **ball_colors):
        self.contents = [k for k,v in ball_colors.items() for i in range(v)]
    
    def draw(self, numBalls):
        if numBalls >= len(self.contents):
            return self.contents
        else:
            draw_index = sorted(random.sample(range(len(self.contents)), numBalls), reverse = True)
            return [self.contents.pop(i) for i in draw_index]


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments:int):
    n = 0
    for i in range(num_experiments):
        cpHat = copy.deepcopy(hat)
        tmp_draw = cpHat.draw(num_balls_drawn)
        result = all([tmp_draw.count(k) >= v for k,v in expected_balls.items()])
        if result:
            n += 1
    return n/num_experiments
