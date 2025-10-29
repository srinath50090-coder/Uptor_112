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

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import alpha

# x = np.random.randint(1,101,100)
# y = np.random.randint(2,201,100)

# plt.scatter(x,y,c=y,label='sample visualization',cmap="rainbow")
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
# plt.plot(x,y,label='sample visualization',color='Red',marker='*')
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
# plt.bar(x,y,label='sample visualization',alpha=0.5,color = 'blue',edgecolor = 'black',linewidth=3, align='center')
# plt.legend()
# plt.show()

#-----------------------------number only--------------------------------------------
"""Different visualization with some usage"""
# import numpy as np
# import matplotlib.pyplot as plt
#
# X = np.arange(-3.0, 3.0, 0.1)
# Y = np.array([70,10,18,98])
# x = np.concatenate((X,Y))
#
# plt.boxplot(x)
# plt.xlabel("input data")
# plt.show()

