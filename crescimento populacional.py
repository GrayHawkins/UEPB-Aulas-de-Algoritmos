paisA = 80000
paisB = 200000
anos = 0
while paisA < paisB:
    paisA += paisA*0.03
    paisB += paisB*0.015
    anos += 1
    
print(f"número de anos: {anos}")