#-------------------------------number vs number-----------------------------------
# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
#
# plt.scatter(x,y,color='red',label='sample visualization')
# plt.xlabel("input data")
# plt.ylabel('output data')
# plt.legend()
# plt.show()

"""Below program is to do plot with different colors"""

# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
#
# plt.scatter(x,y,c=x,label='sample visualization')
# plt.xlabel("input data")
# plt.ylabel('output data')
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
#
# plt.scatter(x,y,c=x,label='sample visualization',cmap="rainbow")
# plt.xlabel("input data")
# plt.ylabel('output data')
# plt.colorbar()
# plt.legend()
# plt.show()


"""Different visualization with different marker"""
"""To join the marked points"""

# import matplotlib.pyplot as plt
#
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]
#
# plt.plot(x,y,label='sample visualization',color='Red',marker='o')
# plt.xlabel("input data")
# plt.ylabel('output data')
# plt.legend()
# plt.show()

#------------------------ category vs number-----------------------------------------

"""Different visualization with number and category"""
"""To create a bar chart"""

# import matplotlib.pyplot as plt
#
# x = ['csk','rcb','kkr','mi']
# y = [5,1,3,5]
#
# plt.bar(x,y,label='sample visualization')
# plt.legend()
# plt.show()

#-----------------------------number only--------------------------------------------
"""Different visualization with some usage"""

# import matplotlib.pyplot as plt
#
# x = [1,20,30,400,500,5000,-1000]
#
# plt.boxplot(x)
# plt.xlabel("input data")
# plt.show()
#
