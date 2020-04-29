from src import objective_fn
import math


class sphere_fn(objective_fn):

    def __init__(self, dims):
        super(sphere_fn, self).__init__(dims)
        self.domain = (-math.inf, math.inf)


    def get_minima(self):
        minima_2d_coords = (0, 0)  # minima val is -1
        return self.eval_fn(minima_2d_coords)


    def eval_fn(self, params):
        f = 0
        try:
            if len(params) != self.dims:
                raise Exception('Dimensions not matching params')
            for param in params:
                f = f + (param ** 2)
            return f
        except Exception as error:
            print('Exception in sphere_fn.eval_fn: ', repr(error))


    def graph_fn(self):
        pass


    def is_defined_only_for_2d(self):
        return False