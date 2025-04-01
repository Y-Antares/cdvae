from ase.io import read
from ase import Atoms
 
structure = read('your_structure.cif')
 
n_atoms = len(structure)
for i in range(n_atoms):
    for j in range(i + 1, n_atoms):
        # 计算两个原子之间的距离
        distance = structure.get_distance(i, j)
        # 检查键长是否小于1.0
        if distance < 1.0:
            error_found = True
 
if error_found:
    print("wrong structure")