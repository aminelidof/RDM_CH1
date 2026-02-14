import numpy as np

class RDMEngine:
    def __init__(self, L):
        self.L = L
        self.point_loads = []  # Forces ponctuelles (kN)
        self.dist_loads = []   # Charges réparties (kN/m)

    def add_point_load(self, mag, pos):
        self.point_loads.append({"mag": mag, "pos": pos})

    def add_distributed_load(self, q):
        self.dist_loads.append(q)

    def solve(self):
        # 1. Calcul des réactions d'appuis
        # Somme des moments en A = 0
        m_point = sum(p["mag"] * p["pos"] for p in self.point_loads)
        m_dist = sum(q * (self.L**2 / 2) for q in self.dist_loads)
        
        Rb = (m_point + m_dist) / self.L
        Ra = sum(p["mag"] for p in self.point_loads) + sum(q * self.L for q in self.dist_loads) - Rb

        # 2. Génération des diagrammes
        x = np.linspace(0, self.L, 1000)
        V = np.zeros_like(x)
        M = np.zeros_like(x)

        for i, xi in enumerate(x):
            # Effort Tranchant T(x)
            val_v = Ra
            val_v -= sum(q * xi for q in self.dist_loads)
            val_v -= sum(p["mag"] for p in self.point_loads if xi >= p["pos"])
            V[i] = val_v

            # Moment Fléchissant M(x)
            val_m = Ra * xi
            val_m -= sum(q * (xi**2 / 2) for q in self.dist_loads)
            val_m -= sum(p["mag"] * (xi - p["pos"]) for p in self.point_loads if xi >= p["pos"])
            M[i] = val_m

        return x, V, M, (Ra, Rb)