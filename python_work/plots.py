import matplotlib.pyplot as plt

# plot using matplotlib
'''
plt.plot(range(10))
plt.show()
'''

# plot of chemistry data
'''
time = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]

plt.plot(time, co2, 'b--')

plt.xlabel('Time (decade)')
plt.ylabel('CO2 concentration (ppm)')
plt.title('CO2 concentration vs time')
plt.show()
'''

# add a second line to the example above
'''
time = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
plt.plot(time, co2, 'b--', time, temp, 'r--')

plt.savefig("figure2.pdf")
'''

# reuse previous example with different axes
'''
time = range(7)
co2 = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

fig, ax1 = plt.subplots()
ax1.plot(time, co2, 'b--')
ax1.set_ylabel("[CO2]")

ax2 = ax1.twinx()
ax2.plot(time, temp, 'r--')
ax2.set_ylabel("Temp (degC)")

plt.show()
'''

# plot two graphs side by side

plt.subplot(1, 3, 1)
x = range(0, 10, 1)
plt.plot(x)
plt.subplot(1, 3, 2)
y = range(10, 0, -1)
plt.plot(y)

plt.subplot(1, 3, 3)

z = [4] * 10

plt.plot(z)

plt.show()
