#!/usr/bin/env python3

from typing import List


##########
## Moon ##
##########

class Moon:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x, self.y, self.z = x, y, z
        self.vel_x, self.vel_y, self.vel_z = 0, 0, 0

    def update_positions(self) -> None:
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def potential_energy(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self) -> int:
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    def total_energy(self) -> int:
        return self.potential_energy() * self.kinetic_energy()

    def __str__(self) -> str:
        result = f"pos=<x={self.x:3}, y={self.y:3}, z={self.z:3}>, "
        result += f"vel=<x={self.vel_x:3}, y={self.vel_y:3}, z={self.vel_z:3}>"
        return result
# endclass Moon


#############
## Jupiter ##
#############

class Jupiter:
    def __init__(self, fname: str) -> None:
        self.fname = fname
        self.moons = self.read_input_file(fname)

    def read_input_file(self, fname: str) -> List[Moon]:
        li = []
        with open(fname) as f:
            for line in f:
                line = line.rstrip("\n").replace("<", "").replace(">", "")
                parts = [int(part.split("=")[-1]) for part in line.split(", ")]
                li.append(Moon(*parts))
            #
        #
        return li

    def total_energy(self) -> int:
        return sum(moon.total_energy() for moon in self.moons)

    def update_velocities(self) -> None:
        size = len(self.moons)    # should be 4
        for i in range(0, size-1):
            moon_a = self.moons[i]
            for j in range(i+1, size):
                moon_b = self.moons[j]
                if moon_a.x < moon_b.x:
                    moon_a.vel_x += 1
                    moon_b.vel_x -= 1
                if moon_a.x > moon_b.x:
                    moon_a.vel_x -= 1
                    moon_b.vel_x += 1
                #
                if moon_a.y < moon_b.y:
                    moon_a.vel_y += 1
                    moon_b.vel_y -= 1
                if moon_a.y > moon_b.y:
                    moon_a.vel_y -= 1
                    moon_b.vel_y += 1
                #
                if moon_a.z < moon_b.z:
                    moon_a.vel_z += 1
                    moon_b.vel_z -= 1
                if moon_a.z > moon_b.z:
                    moon_a.vel_z -= 1
                    moon_b.vel_z += 1
            # endfor
        # endfor
    # enddef

    def update_positions(self) -> None:
        for moon in self.moons:
            moon.update_positions()

    def start_simulation(self, stop_iter=-1) -> None:
        cnt = -1
        while True:
            cnt += 1
            if cnt > 0:
                self.update_velocities()
                self.update_positions()
            print(f"After {cnt} step(s):")
            print(self)
            print("total energy in the system: {}".format(self.total_energy()))
            print()
            if stop_iter != -1:
                if cnt >= stop_iter:
                    break
        #

    def __str__(self) -> str:
        sb = []
        for moon in self.moons:
            sb.append(moon.__str__())
            sb.append("\n")
        #
        return "".join(sb).rstrip("\n")
# endclass Jupiter


def test_1(fname: str) -> None:
    """
    Sum of total energy: 36 + 45 + 80 + 18 = 179.
    """
    j = Jupiter(fname)
    j.start_simulation(stop_iter=10)


def test_2(fname: str) -> None:
    """
    Sum of total energy: 290 + 608 + 574 + 468 = 1940.
    """
    j = Jupiter(fname)
    j.start_simulation(stop_iter=100)


def start(fname: str) -> None:
    j = Jupiter(fname)
    j.start_simulation(stop_iter=1_000)


def main() -> None:
    # test_1("example1.txt")
    # test_2("example2.txt")

    start("input.txt")

##############################################################################

if __name__ == "__main__":
    main()
