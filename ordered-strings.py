selfish = 'me me me'

#print(selfish)
#print(selfish[0])

abcd = '01234567'
# print(abcd[1:4]) #[start:stop]

# print(abcd[0:6:2]) #[start:stop:stepover] Default stepover is 1

print(abcd[::1]) #if we not specify start and stop, it will default start from 0 and ends at last index.

print(abcd[-1]) #-ve index means starts from back

print(abcd[::-1]) #-ve index means starts from back and Here we will get reverse of the string 

print(abcd[::-2]) 