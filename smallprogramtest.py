def phasecreator(nums):
    from itertools import permutations
    phasepossibilities=[]
    for value in permutations(nums, len(nums)):
        phasepossibilities.append(list(value))
    return phasepossibilities

phase_list=[5,6,7,8,9]
print(phasecreator(phase_list))
        
