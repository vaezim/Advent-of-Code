import re
from math import sqrt


class GPU:
    def __init__(self, lines):
        self.particle_positions = {}  # (x,y,z) => [particle_index1, particle_index2, ...]
        self.destroyed_particles = set()
        self.particles = self._ProcessText(lines)  # [ [[x0,x1,x2],[v0,v1,v2],[a0,a1,a2]], ...]

    def GetClosestToCenterInLongRun(self):
        min_acc_mag = float("inf")
        min_acc_particle = float("inf")
        for i, part in enumerate(self.particles):
            acc_mag = self._GetMagnitude(part[2])
            if acc_mag < min_acc_mag:
                min_acc_mag = acc_mag
                min_acc_particle = i
        return min_acc_particle

    def SimulateCollision(self):
        iters = 10_000
        for _ in range(iters):
            # Move all particles
            for i in range(len(self.particles)):
                if i in self.destroyed_particles:
                    continue
                self._MoveParticle(i)
            # Remove collided particles
            remove_list = []
            for pos in self.particle_positions:
                particle_indices = self.particle_positions[pos]
                if len(particle_indices) == 1:
                    continue
                for index in particle_indices:
                    self.destroyed_particles.add(index)
                remove_list.append(pos)
            for item in remove_list:
                self.particle_positions.pop(item)
        return len(self.particles)-len(self.destroyed_particles)

    def _MoveParticle(self, index):
        # Remove from particle_positions
        init_pos = tuple(self.particles[index][0])
        self.particle_positions[init_pos].remove(index)
        # Apply acceleration to velocity
        a = self.particles[index][2]
        self.particles[index][1][0] += a[0]
        self.particles[index][1][1] += a[1]
        self.particles[index][1][2] += a[2]
        # Apply velocity to position
        v = self.particles[index][1]
        self.particles[index][0][0] += v[0]
        self.particles[index][0][1] += v[1]
        self.particles[index][0][2] += v[2]
        # Save new positions
        new_pos = tuple(self.particles[index][0])
        if self.particle_positions.get(new_pos) != None:
            self.particle_positions[new_pos].append(index)
        else:
            self.particle_positions[new_pos] = [index]

    def _GetMagnitude(self, vec):
        sum = 0
        for i in vec:
            sum += (i * i)
        return sqrt(sum)

    def _ProcessText(self, lines):
        particles = []
        for index, line in enumerate(lines):
            part = [[0,0,0],[0,0,0],[0,0,0]]
            nums = re.findall(r"-?\d+", line.strip())
            nums = list(map(lambda x: int(x), nums))
            part[0][0], part[0][1], part[0][2] = nums[0], nums[1], nums[2]
            part[1][0], part[1][1], part[1][2] = nums[3], nums[4], nums[5]
            part[2][0], part[2][1], part[2][2] = nums[6], nums[7], nums[8]
            particles.append(part)
            self.particle_positions[tuple(part[0])] = [index]
        return particles
