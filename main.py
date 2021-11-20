import csv
import re
import numpy as np
import matplotlib.pyplot as plt


def paint_cpu(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
        x = []
        y = []
        count = 0
        for line in reader:
            if line[1] == 'all':
                count += 1
                x.append(count)
                y.append(100 - float(line[10]))

        return x, y


def paint_cpu_len(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
        x = []
        y = []
        count = 0
        for line in reader:
            count += 1
            x.append(count)
            y.append(int(line[1]))
        print(x)
        print(y)
        return x, y


def main():
    paint_cpu("cpu.csv")

    plt.style.use('seaborn-whitegrid')  # стиль графика

    # создаем рисунок fig и 1 график на нём
    fig, ax1 = plt.subplots()
    ax1.set_title("Утилизация CPU")
    ax1.set_xlabel("Продолжительность теста, мин")
    ax1.set_ylabel("Утилизация CPU, %", color='green')
    x, y = paint_cpu("cpu.csv")
    ax1.plot(x, y, color='green')
    ax1.legend()

    ax2 = ax1.twinx()
    ax2.set_ylabel("Длина очереди CPU", color='blue')

    x1, y = paint_cpu_len("cpu_len.csv")
    ax2.plot(x, y, color='blue')
    ax2.legend()

    plt.show()


if __name__ == "__main__":
    main()







