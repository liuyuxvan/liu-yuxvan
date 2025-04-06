import heapq
import math


def dijkstra(n: int, edges: list, start: int) -> list:
    """
    堆优化的Dijkstra算法模板
    :param n: 节点总数（节点编号从0开始）
    :param edges: 边列表，格式为 [(u, v, w), ...]，表示u到v的边权为w
    :param start: 起点编号
    :return: 起点到所有节点的最短距离列表，不可达时为math.inf
    """
    # 1. 构建邻接表
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))  # 有向图

    # 2. 初始化距离数组
    INF = math.inf
    dist = [INF] * n
    dist[start] = 0

    # 3. 优先队列（最小堆）
    heap = []
    heapq.heappush(heap, (0, start))  # (distance, node)

    # 4. 松弛操作
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:  # 跳过旧记录
            continue
        for v, w in adj[u]:
            if (new_dist := dist[u] + w) < dist[v]:
                dist[v] = new_dist  # 更新最短距离
                heapq.heappush(heap, (new_dist, v))  # 新记录入堆
    return dist


# =================== 示例用法 ===================
if __name__ == "__main__":
    # 示例1：有向图
    n = 5
    edges = [
        (0, 1, 4), (0, 2, 1),
        (1, 3, 1), (2, 1, 2), (2, 3, 5), (3, 4, 3)
    ]
    start = 0
    dist = dijkstra(n, edges, start)
    print("从起点出发的最短距离：")
    for i in range(n):
        print(f"节点{i}: {dist[i] if dist[i] != math.inf else '不可达'}")

    # 示例2：无向图（需将边双向添加）
    n = 3
    edges = [(0, 1, 2), (1, 0, 2), (1, 2, 3), (2, 1, 3), (0, 2, 5)]
    start = 0
    dist = dijkstra(n, edges, start)
    print("\n无向图结果：")
    for i in range(n):
        print(f"节点{i}: {dist[i]}")