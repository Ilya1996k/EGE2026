def get_cluster():
    cluster = [s.pop(0)]
    for i in cluster:
        for j in s[::]:
            if dist(i, j) < 1:
                cluster.append(j)
                s.remove(j)
    return cluster

clusters = []
while len(s) > 0:
    clusters.append(get_cluster())
clusters = [i for i in clusters if len(i) >= 20]
