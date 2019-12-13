import matplotlib.pyplot as plt

fig5 = plt.figure(constrained_layout=True)
widths = [2, 2, 1]
heights = [2, 2, 1]
spec5 = fig5.add_gridspec(ncols=3, nrows=3, width_ratios=widths,
                          height_ratios=heights)
for row in range(3):
    for col in range(3):
        ax = fig5.add_subplot(spec5[row, col])

plt.show()