from tools import constant as constant, utils as utils
import os
import matplotlib.pyplot as plt
import numpy as np

Count = [[0] * 12 for i in range(12)]
Coordinate = [[0] * 2 for i in range(12)]


def build_count_list(data):
    del data[0]
    for line in data:
        line_list = line.split(',')
        for i in range(1, 12):
            for j in range(i+1, 13):
                if line_list[i] == line_list[j] and line_list[i] == "T":
                    Count[i-1][j-1] += 1
    return 0


def circle_xy(r=20, side_num=12):
    theta = np.linspace(0, 2*np.pi, side_num, False)
    x = r*np.sin(theta)
    x = np.append(x, x[0])
    y = r*np.cos(theta)
    y = np.append(y, y[0])
    return x, y


def draw_graph(x, y, count, value):
    product = 1
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set(title="Relationship", aspect='equal')
    for i in range(1, 12):
        for j in range(i+1, 13):
            c_x = [x[i-1], x[j-1]]
            c_y = [y[i-1], y[j-1]]
            if count[i-1][j-1] > value*2:
                plt.plot(c_x, c_y, lw=3, color='black')
            elif count[i-1][j-1] > value:
                plt.plot(c_x, c_y, lw=1, color='black')
    x = np.delete(x, 12, 0)
    y = np.delete(y, 12, 0)
    for i, j in zip(x, y):
        plt.text(i, j, "product" + str(product), ha='center', va='bottom', fontsize=10)
        product += 1


if __name__ == '__main__':
    print('start')
    data = utils.read_file(os.path.join(constant.data_files_path, constant.cust_prod_dat_name))
    build_count_list(data)
    x, y = circle_xy()
    draw_graph(x, y, Count, 4482)

    plt.show()
    print("end")
