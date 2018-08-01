from math import sqrt, log, exp, inf
import random, time
from functools import reduce
import operator
from util import *
from gui import GUI
from edge import canny


class Path(list):
    def draw(self, img: np.ndarray, color=None):
        if img.ndim == 2:
            newimg = img.repeat(3).reshape(*(img.shape + 3)) * 255
        else:
            newimg = img

        if color is None:
            l = len(self)
            color = np.concatenate([np.linspace(0, 150, l).reshape(-1, l),
                                    255 * np.ones([2, l])]).T[None, :, :]
            color = cv2.cvtColor(color.astype(np.uint8), cv2.COLOR_HSV2BGR).reshape(l, 3)
        else:
            color = np.array(color)

        if color.ndim == 1:
            for coord in self:
                newimg[coord] = color
        else:
            for coord, c in zip(self, color):
                newimg[coord] = c
        return newimg


def quad_neighbor(r, c):
    """四方向邻居"""
    return (r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)


def diag_neighbor(r, c):
    return (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1), (r + 1, c + 1)


def oct_neighbor(r, c):
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a != 0 or b != 0:
                yield r + a, c + b


def findpath(img, r, c):
    h, w = img.shape

    def get_true_neighbor(neighbor_list):
        l = []
        for i in neighbor_list:
            if 0 <= i[0] < h and 0 <= i[1] < w and img[i]:
                l.append(i)
        return l

    def addpath(r, c):
        path = []
        while 1:
            img[r, c] = 0
            path.append((r, c))
            quad_nei = get_true_neighbor(quad_neighbor(r, c))
            if len(quad_nei) >= 1:
                # random choose one direction
                r, c = quad_nei[0]
            else:
                diag_nei = get_true_neighbor(diag_neighbor(r, c))
                if len(diag_nei) >= 1:
                    r, c = diag_nei[0]
                else:
                    break
        return path

    oct_nei = get_true_neighbor(oct_neighbor(r, c))
    img[r, c] = 0
    if len(oct_nei) == 1:
        path = [(r, c)] + addpath(*oct_nei[0])
    elif len(oct_nei) >= 2:
        path = [(r, c)] + addpath(*oct_nei[0])
        path2 = addpath(*oct_nei[1])
        path = list(reversed(path2)) + path
    else:
        path = [(r, c)]

    return Path(path)


class PathList:
    """
    path: 连续不断的一段笔画
    solution: 笔画首末节点编号的集合, 为len(pathlist) * 2的数组, 表示一个规划方案
    node编号: a, b = divmod(node, 2), a表示path编号, b为0/1表首/末节点
    """
    def __init__(self, edgeimg):
        edgecopy = edgeimg.copy()
        shape = edgeimg.shape
        paths = []
        for i in range(shape[0]):
            for j in range(shape[1]):
                if edgecopy[i, j] == 1:
                    paths.append(findpath(edgecopy, i, j))
        self.pathlist = list(filter(lambda x: len(x) > 1, paths))
        self.solution = []
        for i in range(len(self.pathlist)):
            self.solution.append((i * 2, i * 2 + 1))

    def __getitem__(self, item):
        if np.issubdtype(type(item), np.integer):
            a, b = divmod(item, 2)
            return self.pathlist[a][b and -1]
        elif type(item) == tuple:
            return self.pathlist[item[0]][item[1] and -1]
        else:
            raise IndexError(f'index must be int or tuple, not {item}')

    def __len__(self):
        return len(self.pathlist)

    def distance(self, node1, node2):
        if node1 >> 1 == node2 >> 1:
            return 0
        else:
            c1, c2 = self[node1], self[node2]
            return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

    def swap_diff(self, sol, p1, p2):
        # after - before
        # i->x, j->y, [..., a, x, ..., y, b, ...]
        # a1x0 + y1b0 -> a1y1 + x0b0
        def getitem(idx):
            if idx == -1 or idx == len(self):
                return 0, 0
            else:
                return sol[idx]

        a, x, y, b = lmap(getitem, [p1 - 1, p1, p2, p2 + 1])
        return (a[1] and (self.distance(a[1], y[1]) - self.distance(a[1], x[0]))) + \
               (b[0] and (self.distance(x[0], b[0]) - self.distance(y[1], b[0])))

    def tot_dist(self, sol=None):
        if sol is None:
            sol = self.solution
        lastidx = sol[0][1]
        dist = 0
        for i in range(1, len(self)):
            idx = sol[i]
            dist += self.distance(lastidx, idx[0])
            lastidx = idx[1]
        return dist

    def greedy(self):
        newsol = [(0, 1)]
        visited_idx = [0, 0] + [1] * (len(self) - 1) * 2
        curidx = 1
        for _ in range(len(self) - 1):
            best_next = 0
            best_dist = inf
            for i, flag in zip(np.array(self.solution).flatten(), visited_idx):
                if flag:
                    d = self.distance(i, curidx)
                    if d < best_dist:
                        best_next = i
                        best_dist = d
            curidx = best_next ^ 1
            newsol.append((best_next, curidx))
            visited_idx[best_next] = 0
            visited_idx[curidx] = 0
        return newsol

    def tolist(self):
        ret = []
        for idx in self.solution:
            start = idx[0]
            # [(x1, y1), ...]
            p = self.pathlist[start >> 1]
            if idx[0] & 1 == 1:
                p = list(reversed(p))
            ret += list(reduce(operator.add, p))
            ret += [-1, -1]
        return ret



def random_choose2(N):
    # i, j = 0, 0
    # while i == j:
    j = random.randint(0, N-1)
    i = random.randint(0, j)
    # if i > j:
    #     i, j = j, i
    return i, j


def neighbor_swap2(sol, i, j):
    # i, j = random_choose2(len(sol))
    # assert type(sol) == list
    inv = np.flip(np.array(sol[i:j+1]).flatten(), 0).reshape(-1, 2).tolist()
    if i > 0:
        inv = sol[:i] + inv
    if j < len(sol) - 1:
        inv += sol[j+1:]
    return inv


def sa_start_temp(paths, P0=0.9, T0=10):
    # start temp estimate
    N = 200; M = 50; step = 50
    randsol = paths.solution
    Ta, pa = None, None
    T = T0
    while 1:
        acc = 0
        for _ in range(M):
            random.shuffle(randsol)
            for i in range(N):
                choose = random_choose2(len(paths))
                delta = paths.swap_diff(randsol, *choose)
                if delta < 0 or random.random() < exp(-delta / T):
                    acc += 1
        p = acc / (N * M)
        printd(p, T, end=';  ')
        if p > P0:
            break
        else:
            # 使用弦截法求解
            dT = (P0 - p) / (p - pa) * (T - Ta) if Ta else step
            if dT < 0:
                dT = step
            Ta, pa = T, p
            T += dT
    printd()
    return T


def simulated_annealing(paths: PathList):
    T0 = sa_start_temp(paths)
    print('T0 =', T0)
    sol = paths.solution
    solE = paths.tot_dist(sol)
    bestsol = sol
    bestE = solE
    T = T0
    n = 0
    while T > 1e-3:
        for _ in range(200):
            choose = random_choose2(len(sol))
            delta = paths.swap_diff(sol, *choose)
            if delta < 0 or random.random() < exp(-delta / T):
                sol = neighbor_swap2(sol, *choose)
                solE += delta
            if solE < bestE:
                bestsol, bestE = sol, solE

        T *= 0.995

        n += 1
        if n == 100:
            n = 0
            printd('temp:', T, ' E:', paths.tot_dist(sol))
    m1, m2 = 0, 0
    for j in range(len(paths)):
        for i in range(j):
            d = paths.swap_diff(sol, i, j)
            if d < 0:
                m1 += 1
            else:
                m2 += 1
    printd(m1, m2, m1 / (m1 + m2))
    return bestsol


def opt2(paths: PathList):
    def swap2_gen(n):
        for j in range(n):
            for i in range(j):
                yield i, j

    sol = paths.solution
    solE = paths.tot_dist(sol)

    while 1:
        canopt = False
        bestswap = (0, 0)
        bestd = 0
        down = 0
        ts = time.time()
        for i, j in swap2_gen(len(paths)):
            d = paths.swap_diff(sol, i, j)
            if d < bestd:
                bestswap = (i, j)
                bestd = d
                canopt = True
                down += 1
                break
        if not canopt:
            break
        else:
            sol = neighbor_swap2(sol, *bestswap)
            solE += bestd
            print('E:', solE, ' d<0:', down, ' time: {:.3f}'.format(time.time() - ts))

    return sol


if __name__ == '__main__':
    imgname = 'face.jpg'
    edgeimg = canny(imgname) // 255
    # edgeimg = cv2.imread('face edge.png')[:, :, 0] // 255
    paths = PathList(edgeimg)

    print('total path: ', len(paths))
    print('origin dist:', paths.tot_dist())
    greedy_sol = paths.greedy()
    print('greedy dist:', paths.tot_dist(greedy_sol))

    bestsol = simulated_annealing(paths)
    print('sa dist:', paths.tot_dist(bestsol))
    paths.solution = bestsol

    # bestsol = opt2(paths)
    # print('2-opt dist:', paths.tot_dist(bestsol))
    # paths.solution = bestsol

    gui = GUI(edgeimg.shape[:2], paths)