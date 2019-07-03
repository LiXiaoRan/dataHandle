from pyecharts import Line
from pyecharts.engine import create_default_environment
import numpy as np

attr = ["1138", "1224", "4039", "4720", "7920", "11143", "27770", "34546", "81306", "82168", "265214", "281903",
        "325729", "415641", "875713"]
v1 = [0.427, 0.497, 0.517, 0.499, 0.563, 0.571, 1.403, 1.604, 4.008, 3.331, 11.769, 10.088, 8.215, 30.318, 60.233]
v2 = [0.783, 1.277, 4.576, 3.521, 6.269, 9.302, 43.222, 56.075, 147.704, 133.559, 567.381, 576.936, 482.167, 701.026,
      1441.697]
v3 = [5.7, 7.818, 57.718, 15.527, 20.976, 54.476, 387.546, 608.485, 1424.669, 1137.779, 1752.594, 5050.39, 2503.36,
      1547.2, 13273.716]
v4 = [2.144, 2.438, 7.547, 7.771, 13.851, 19.577, 53.117, 110.352, 190.145, 169.213, 506.433, 550.266, 635.331, 959.54,
      1840.998]
v5 = [0.562, 1.304, 5.292, 2.237, 3.778, 6.321, 79.1, 192.091, 191.263, 280.63, 488.67, 562.091, 498.26, 1728.517,
      3958.762]

line = Line("变化趋势")
line.add("gpu", attr, v1)
line.add("cpu", attr, v2)
line.add("yifan hu", attr, v3)
line.add("openord", attr, v4)
line.add("FA2", attr, v5)
line.render()

# env = create_default_environment("html")
# env.render_chart_to_file(line, path='line.html')
