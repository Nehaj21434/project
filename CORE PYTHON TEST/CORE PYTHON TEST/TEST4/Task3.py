# WAP to print following patterns
# **********
#         *
#        *
#      *
#     *
#    *
#   *
#  *
# *
# **********

n = 10   # number of stars in first and last row

for i in range(n):
    if i == 0 or i == n - 1:   # first and last row
        print("*" * n)
    else:                      # middle rows
        print(" " * (n - i - 1) + "*")
