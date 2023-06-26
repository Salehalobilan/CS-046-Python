def signin(password):
    return lambda username : username + password
firstsec = signin("saleh")
secsec = signin(927319)
print(firstsec("faisal "))
print(secsec(11223344))