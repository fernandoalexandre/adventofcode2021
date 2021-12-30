from copy import copy
import itertools

class dict_3d_map():
    def __init__(self) -> None:
        self.dmap = {}

    def __get_key(self, x: int, y: int, z: int):
        return f"{x}_{y}_{z}"

    def __get_state_repr(self, state: str) -> int:
        return int(state == "on")

    def _get_intersection(
        self,
        x_region: tuple,
        y_region: tuple,
        z_region: tuple,
        x_limit: tuple,
        y_limit: tuple,
        z_limit: tuple
    ):
        x_intersect = (x_limit[0] <= x_region[0] <= x_limit[1]) or (x_limit[0] <= x_region[1] <= x_limit[1])
        y_intersect = (y_limit[0] <= y_region[0] <= y_limit[1]) or (y_limit[0] <= y_region[1] <= y_limit[1])
        z_intersect = (z_limit[0] <= z_region[0] <= z_limit[1]) or (z_limit[0] <= z_region[1] <= z_limit[1])

        # Valid intersection
        if x_intersect and y_intersect and z_intersect:
            x_l = [x for x in range(x_limit[0], x_limit[1]+1)]
            x_r = [x for x in range(x_region[0], x_region[1]+1)]
            x_i = list(set(x_l) & set(x_r))

            y_l = [y for y in range(y_limit[0], y_limit[1]+1)]
            y_r = [y for y in range(y_region[0], y_region[1]+1)]
            y_i = list(set(y_l) & set(y_r))

            z_l = [z for z in range(z_limit[0], z_limit[1]+1)]
            z_r = [z for z in range(z_region[0], z_region[1]+1)]
            z_i = list(set(z_l) & set(z_r))
            return x_i, y_i, z_i
        else:
            return None, None, None


    def set_region(
        self,
        state: str,
        x_region: tuple,
        y_region: tuple,
        z_region: tuple,
        x_limit: tuple,
        y_limit: tuple,
        z_limit: tuple
    ) -> None:
        target_state = self.__get_state_repr(state)

        x_r, y_r, z_r = self._get_intersection(
            x_region,
            y_region,
            z_region,
            x_limit,
            y_limit,
            z_limit
        )

        if x_r is not None and len(x_r) > 0 and len(y_r) > 0 and len(z_r) > 0:
            for x in x_r:
                for y in y_r:
                    for z in z_r:
                        dkey = self.__get_key(x, y, z)
                        self.dmap[dkey] = target_state

    def set_region_unbound(
        self,
        state: str,
        x_region: tuple,
        y_region: tuple,
        z_region: tuple,
    ) -> None:
        target_state = self.__get_state_repr(state)

        x = x_region[0]
        while x <= x_region[1]:
            y = y = y_region[0]
            while y <= y_region[1]:
                z = z_region[0]
                while z <= z_region[1]:
                    dkey = self.__get_key(x, y, z)

                    if target_state == 0:
                        if dkey in self.dmap:
                            self.dmap.pop(dkey)
                    else:
                        self.dmap[dkey] = target_state
                    z += 1
                y += 1
            x += 1

    def get_state_count(
        self,
        x_region: tuple = None,
        y_region: tuple = None,
        z_region: tuple = None,
    ) -> int:
        if x_region is not None and y_region is not None and z_region is not None:
            result = 0
            for x in range(x_region[0], x_region[1]+1):
                for y in range(y_region[0], y_region[1]+1):
                    for z in range(z_region[0], z_region[1]+1):
                        dkey = self.__get_key(x, y, z)
                        if dkey in self.dmap and self.dmap[dkey] == 1:
                            result += 1
            return result
        else:
            return len(self.dmap.values())
