import math

def minimizeMaxParcelLoad(initialParcels, additionalParcels):
    def check(max_load):
        capacity_to_absorb = 0
        for parcels in initialParcels:
            if parcels > max_load:
                return False
            capacity_to_absorb += (max_load - parcels)
        return capacity_to_absorb >= additionalParcels

    low = max(initialParcels)
    high = max(initialParcels) + additionalParcels
    ans = high

    while low <= high:
        mid = low + (high - low) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans