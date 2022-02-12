# import sys
# input_ = []
# for _ in range(9):
#     input_.append(int(sys.stdin.readline().rstrip()))

# for i in range(len(input_)):
#     for j in range(i+1, len(input_)):
#         if (input_[i] + input_[j]) == (sum(input_) - 100):
#             n = input_[i]
#             m = input_[j]
#             input_.remove(n)
#             input_.remove(m)
#             break

# for i in sorted(input_):
#     print(i)

# import sys
# tall = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
# tall.sort()
# for i in range(len(tall)):
#   for j in range(i+1, len(tall)):
#     for k in range(j+1, len(tall)):
#       for a in range(k+1, len(tall)):
#         for b in range(a+1, len(tall)):
#           for c in range(b+1, len(tall)):
#             for d in range(c+1, len(tall)):
#               if tall[i] + tall[j] + tall[k] + tall[a] + tall[b] + tall[c] + tall[d] == 100:
#                 print(tall[i])
#                 print(tall[j])
#                 print(tall[k])
#                 print(tall[a])
#                 print(tall[b])
#                 print(tall[c])
#                 print(tall[d])
#                 sys.exit(0)

import sys
input_ = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
total = sum(input_)
for i in range(len(input_)):
    for j in range(i+1, len(input_)):
        if (input_[i] + input_[j]) == (total - 100):
            n = input_[i]
            m = input_[j]
            input_.remove(n)
            input_.remove(m)
            break

for i in sorted(input_):
    print(i)