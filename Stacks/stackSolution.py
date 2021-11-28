
alphabet = ['E', 'A', 'C', 'B', 'D']


save = alphabet.pop() # D
saveLetter = []
saveLetter.append(save) # D


saveAnother = []
save = alphabet.pop() # B
saveAnother.append(save) # B

save = alphabet.pop() # C
saveLetter.append(save) # D, C

save = alphabet.pop() # A
saveAnother.append(save) # B, A

saveMore = []
save = alphabet.pop() # E
saveMore.append(save) # E

# Now load them back up again!
save = saveAnother.pop() # A
alphabet.append(save) # A
save = saveAnother.pop() # B
alphabet.append(save) # A, B
save = saveLetter.pop() # C
alphabet.append(save) # A, B, C
save = saveLetter.pop() # D
alphabet.append(save) # A, B, C, D
save = saveMore.pop() # E
alphabet.append(save) # A, B, C, D

print(alphabet)

 # to make sure it worked!
