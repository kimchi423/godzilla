# year1 = int(input("몇년부터"))
# # year2 = int(input("몇년까지"))
# if year1 % 4 == 0 and year1 % 400 == 0 or year1 % 100 != 0:
#     print(1)
# else:
#     print(0)
#
# elif year1 % 100 == 0 or year1 % 4 == 0:
#
# elif year1 % 400 == 0 and year1 % 4 == 0:
#     s = 1
a = int(input("몇별까지?"))
# for b in (5,a+1):
#     for c in (0,b):
#         print(b*"*")
for b in range(1,a+1):
    print((a-b)*" ",b * "*")




# for i in range(year1,year2+1):
