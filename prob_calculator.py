
import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**all_item):
        self.contents = []
        for key, value in all_item.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, cant):
        draw_list = []
        if cant >= len(self.contents):
            return self.contents
        for j in range(cant):
            ball = self.contents.pop(random.randrange(len(self.contents)))
            draw_list.append(ball)
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    Count=0
    for k in range(num_experiments):
        copyhat = copy.deepcopy(hat)
        t_list = copyhat.draw(num_balls_drawn)
        success = True
        for key,value in expected_balls.items():
            if t_list.count(key) < value:
                success = False
                break
        if success:
            Count += 1
    return Count/num_experiments