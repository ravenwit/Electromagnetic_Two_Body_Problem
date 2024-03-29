import numpy as np
import matplotlib.pyplot as plt

RK4 = 1
RK12 = 2
RK6 = 3

F_i = []
a = []
b = []
c = []


def Butcher_tableau(method):
    global a
    global b
    global c
    global F_i
    if method == 1:
        c = np.array([0, 1 / 2, 1 / 2, 1])
        a = np.array([
            [0, 0, 0, 0],
            [1 / 2, 0, 0, 0],
            [0, 1 / 2, 0, 0],
            [0, 0, 1, 0]
        ])
        b = np.array([1 / 6, 1 / 3, 1 / 3, 1 / 6])
    elif method == 2:
        c = np.array([0, 0.2, 5 / 9, 5 / 6, 1 / 3, 1, 67801993 / 100920496, 44758598 / 155021585, 9 / 16, 5 / 6,
                      172135849 / 181636255, 36851109 / 672327007, 20592542 / 242584693,
                      30120495 / 113415896, 1 / 2, 210568577 / 286712394, 96134905 / 105052617, 172135849 / 181636255,
                      5 / 6, 44758598 / 155021585, 67801993 / 100920496, 1 / 3, 5 / 9, 1 / 5, 1])
        a = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1 / 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [-35 / 162, 125 / 162, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5 / 24, 0, 5 / 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [29 / 150, 0, 11 / 50, -2 / 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1 / 10, 0, 0, 2 / 5, 1 / 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [37074941 / 358681667, 0, 0, 33585619 / 270735842, 257720006 / 533392767, -44020349 / 1135920344, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [25230124 / 203405979, 0, 0, 0, 98101881 / 451976942, 65957727 / 4798468366, -6070937 / 91831493, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [24737624 / 270423075, 0, 0, 0, 0, -3736153 / 686353106, 19485332 / 286247261, 50525157 / 123716602, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [60247834 / 676931571, 0, 0, 0, 0, 4275247 / 855856941, 36672659 / 92161292, 16731755 / 39099261,
             -38981915 / 450596697, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [27288061 / 392584475, 0, 0, 0, 0, 365006343 / 2826287155, 141373675 / 92356644, 163264999 / 282526613,
             -51629527 / 54272901, 142621687 / 349326099, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [32856654 / 738581809, 0, 0, 0, 0, -14162705 / 3722356397, 25582922 / 2391931811, 51119620 / 2438724161,
             -25704425 / 1102503257, 4688654 / 1780957031, 3117485 / 988194642, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0],
            [10458484 / 537465835, 0, 0, 0, 0, 0, 0, 0, 296227 / 4365826774, -383576 / 8924609019, 146141 / 8286564037,
             12646113 / 193405084, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [31431986 / 151965127, 0, 0, 0, 0, 0, 0, 0, 8107993 / 486102169, -20936474 / 2380493097,
             11794237 / 3402097500, -152083614 / 176581783, 102389113 / 112682442, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [11253958 / 551864565, 0, 0, 0, 0, 0, 0, 0, 42975146 / 494268647, -4474701 / 233483414, 6268097 / 956043048,
             15766372 / 159663323, 117183268 / 21888493765, 28144139 / 93450007, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [89861716 / 393422115, 0, 0, 0, 0, 0, 0, 0, -190920249 / 382830190, 37407972 / 277422485,
             -15879177 / 409829375, -24748163 / 19414396, 49033497 / 34070828, -135425641 / 632808015,
             100437343 / 104818503, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [329422004 / 164527983, 0, 0, 0, 0, 0, 0, 0, 159202720 / 77020477, 152179118 / 243885337,
             -35567233 / 769381099, -466749240 / 52741619, 161194222 / 20819195, -453082123 / 770078291,
             -26419211 / 23869100, -79543028 / 85573473, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [121929017 / 38856942, 0, 0, 0, 0, 365006343 / 2826287155, 141373675 / 92356644, 163264999 / 282526613,
             439144222 / 81009727, 13186261 / 56948547, 25264555 / 332737891, -401683667 / 32464540,
             2492304541 / 252908789, 47761777 / 555943912, -75613337 / 13377144, -248933559 / 128117530,
             -36061621 / 280957460, 0, 0, 0, 0, 0, 0, 0, 0],
            [155993079 / 112744303, 0, 0, 0, 0, 4275247 / 855856941, 36672659 / 92161292, 16731755 / 39099261,
             -164168531 / 125993596, 855875317 / 1294246651, -43179215 / 298694538, -509694778 / 73171449,
             235461367 / 35364726, -82607643 / 49466432, 119839851 / 58058089, -108798317 / 161243854,
             -1216233 / 1051933279, -11104923 / 2041128862, 0, 0, 0, 0, 0, 0, 0],
            [30575399 / 32142801, 0, 0, 0, 98101881 / 451976942, 65957727 / 4798468366, -6070937 / 91831493, 0,
             58237611 / 382433426, -87760066 / 259844263, -9942595 / 515625276, -123996494 / 33670977,
             101639181 / 32144170, -92687960 / 250195241, -4868661 / 94541843, -870114 / 1048803305,
             240782 / 86054719017, 3179847 / 75963145, 24618431 / 88211465, 0, 0, 0, 0, 0, 0],
            [37074941 / 358681667, 0, 0, 33585619 / 270735842, 257720006 / 533392767, -44020349 / 1135920344, 0,
             -120527899 / 274980832, 0, -58596715 / 268009592, -47102449 / 1508075769, 0, 0, 0, 0, 0, 0,
             47102449 / 1508075769, 58596715 / 268009592, 120527899 / 274980832, 0, 0, 0, 0, 0],
            [29 / 150, 0, 11 / 50, -2 / 25, 0, 0, 14340957 / 145703507, -31420077 / 159971156, 0, 103497843 / 237131315,
             22131167 / 339115870, 0, 0, 0, 0, 0, 0, -22131167 / 339115870, -103497843 / 237131315,
             31420077 / 159971156, -14340957 / 145703507, 0, 0, 0, 0],
            [-35 / 162, 125 / 162, 0, 0, -2 / 3, 0, -82382086 / 210859561, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             82382086 / 210859561, 2 / 3, 0, 0, 0],
            [1 / 5, 0, -40 / 243, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40 / 243, 0, 0],
            [157084639 / 106730534, 63 / 80, 91 / 216, 0, 7 / 24, 0, 100146079 / 287280186, 70568068 / 307486745,
             129515617 / 22367050, 72807936 / 173937191, 51739211 / 168509742, -123960914 / 26447765,
             207695632 / 66235459, 222633283 / 158870770, -234969570 / 42495271, -108932901 / 127684936,
             28937867 / 279388356, -46373597 / 330121299, -72807936 / 173937191, -70568068 / 307486745,
             -100146079 / 287280186, -7 / 24, -91 / 216, -63 / 80, 0]
        ])
        b = np.array([1 / 42, 3 / 128, 1 / 32, 0, 1 / 24, 0, 1 / 20, 1 / 20, 0, 1, 1 / 14, 0, 38532146 / 278385263,
                      119008733 / 551291285, 128 / 525, 119008733 / 551291285, 38532146 / 278385263, -1 / 14,
                      -1 / 10, -1 / 20, 1 / 20, -1 / 24, -1 / 32, -3 / 128, 1 / 42])
    elif method == 3:
        root21 = np.sqrt(21)
        c = np.array([0, 1, 1 / 2, 2 / 3, (7 - root21) / 14, (7 + root21) / 14, 1])
        a = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [3 / 8, 1 / 8, 0, 0, 0, 0, 0],
            [8 / 27, 2 / 27, 8 / 27, 0, 0, 0, 0],
            [3 * (3 * root21 - 7) / 392, 8 * (7 - root21) / 392, 48 * (7 - root21) / 392, 3 * (21 - root21) / 392, 0, 0,
             0],
            [-5 * (231 + 51 * root21) / 1960, -40 * (7 + root21) / 1960, -320 * root21 / 1960,
             3 * (21 + 121 * root21) / 1960, 392 * (6 + root21) / 1960, 0, 0],
            [15 * (22 + 7 * root21) / 180, 120 / 180, 40 * (7 * root21 - 5) / 180, -63 * (3 * root21 - 2) / 180,
             -14 * (49 + 9 * root21) / 180, 70 * (7 - root21) / 180, 0]
        ])
        b = np.array([9 / 180, 0, 64 / 180, 0, 49 / 180, 49 / 180, 9 / 180])
    for i in range(0, len(b)):
        F_i.append(0)
    return a, b, c


def __func_y1(y1, y2, t, **kwargs):
    return y2


def __func_y2(y1, y2, t, **kwargs):
    q = 1.15
    w = 0.9
    omega0 = 2.0 / 3.0
    return -q * y2 - np.sin(y1) + w * np.cos(omega0 * t)
    # return -q * y2 - np.sin(y1)
    # return (-(np.pi ** 2) / 4) * (y1)


LS = 137


def sum_velocity(velocities):
    summed = np.array([0, 0, 0])
    for velocity in velocities:
        summed = (summed + velocity) / (1 + (np.dot(summed, velocity)) / LS ** 2)
    return summed


# def F1(func, y1, y2, t, step, **kwargs):
#     global F_i
#     for i in range(len(b)):
#         F_i[i] = 0
#     for i in range(len(b)):
#         F_i[i] = np.array(func((y1 + step * sum_velocity([a[i][j] * F_i[j] for j in range(len(a))])),
#                                sum_velocity([y2, step * sum_velocity([a[i][j] * F_i[j] for j in range(len(a))])]),
#                                t + step * c[i], **kwargs))


def F(func, y1, y2, t, step, **kwargs):
    global F_i
    for i in range(len(b)):
        F_i[i] = 0
    for i in range(len(b)):
        F_i[i] = np.array(step * func((y1 + sum([a[i][j] * F_i[j] for j in range(len(a))])),
                                      (y2 + sum([a[i][j] * F_i[j] for j in range(len(a))])),
                                      t + step * c[i], **kwargs))


def F3(func, y1, y2, y3, t, step, **kwargs):
    global F_i
    for i in range(len(b)):
        F_i[i] = 0
    for i in range(len(b)):
        F_i[i] = np.array(step * func((y1 + sum([a[i][j] * F_i[j] for j in range(len(a))])),
                                      (y2 + sum([a[i][j] * F_i[j] for j in range(len(a))])),
                                      (y3 + sum([a[i][j] * F_i[j] for j in range(len(a))])),
                                      t + step * c[i], **kwargs))


def get_func(y10, y20, t0, step, points, method):
    Butcher_tableau(method)
    t = [t0]
    y1 = [y10]
    y2 = [y20]
    for k in range(points):
        F(__func_y1, y1[-1], y2[-1], t[-1], step)
        y1.append(y1[-1] + sum([b[i] * F_i[i] for i in range(len(b))]))
        F(__func_y2, y1[-1], y2[-1], t[-1], step)
        y2.append(y2[-1] + sum([b[i] * F_i[i] for i in range(len(b))]))
        t.append(t[-1] + step)

    return t, y1, y2


def get_single_point(last_y1, last_y2, last_t, func_y1, func_y2, step, method, **kwargs):
    Butcher_tableau(method)

    F(func_y1, last_y1, last_y2, last_t, step, **kwargs)
    y1 = last_y1 + sum([b[i] * F_i[i] for i in range(len(b))])
    F(func_y2, last_y1, last_y2, last_t, step, **kwargs)
    y2 = last_y2 + sum([b[i] * F_i[i] for i in range(len(b))])
    t = last_t + step

    return t, y1, y2


def get_single_point3(last_y1, last_y2, last_y3, last_t, func_y1, func_y2, func_y3, step, method, **kwargs):
    Butcher_tableau(method)

    F3(func_y1, last_y1, last_y2, last_y3, last_t, step, **kwargs)
    y1 = last_y1 + sum([b[i] * F_i[i] for i in range(len(b))])
    F3(func_y2, last_y1, last_y2, last_y3, last_t, step, **kwargs)
    y2 = last_y2 + sum([b[i] * F_i[i] for i in range(len(b))])
    F3(func_y3, last_y1, last_y2, last_y3, last_t, step, **kwargs)
    y3 = last_y3 + sum([b[i] * F_i[i] for i in range(len(b))])
    t = last_t + step

    return t, y1, y2, y3

# def get_single_point(last_y1, last_y2, last_t, func_y1, func_y2, step, method, **kwargs):
#     Butcher_tableau(method)
#
#     F(func_y1, last_y1, last_y2, last_t, step, **kwargs)
#     y1 = last_y1 + step * sum_velocity([b[i] * F_i[i] for i in range(len(b))])
#     F(func_y2, last_y1, last_y2, last_t, step, **kwargs)
#     y2 = sum_velocity([last_y2, step * sum_velocity([b[i] * F_i[i] for i in range(len(b))])])
#     t = last_t + step
#
#     return t, y1, y2


if __name__ == '__main__':
    t, y1, y2 = get_func(0, 1, 0, 0.1, 100, 1)
    t_m2, y1_m2, y2_m2 = get_func(0, 1, 0, 0.1, 100, 2)
    t_m3, y1_m3, y2_m3 = get_func(0, 1, 0, 0.1, 100, 3)
    # plt.plot(t, y1, color='#591919', linewidth=2, label='Theta(4)', marker='o', markersize=1)
    # plt.plot(t, y2, color='#38aac4', linewidth=2, label='Angular velocity(4)', marker='+', markersize=1)
    # plt.plot(t_m2, y1_m2, color='#34bc54', linewidth=2, label='Theta(12)', marker='o', markersize=1)
    # plt.plot(t_m2, y2_m2, color='#b8d13c', linewidth=2, label='Angular velocity(12)', marker='+', markersize=1)
    plt.xlabel('Theta(y1)')
    plt.ylabel('Angular velocity(y2)')
    plt.plot(y1, y2, label='RK4', marker='o', markersize=1)
    plt.plot(y1_m2, y2_m2, label='RK12', marker='o', markersize=1)
    plt.plot(y1_m3, y2_m3, label='RK6', marker='o', markersize=1)
    plt.legend()
    plt.show()
