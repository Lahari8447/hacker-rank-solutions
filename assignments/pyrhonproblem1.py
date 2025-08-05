from collections import defaultdict, deque


# Task Scheduler with Dependencies

def task_scheduler(tasks, dependencies):
    graph = defaultdict(list)
    in_degree = {task: 0 for task in tasks}

    for task, prereq in dependencies:
        graph[prereq].append(task)
        in_degree[task] += 1

    queue = deque([task for task in tasks if in_degree[task] == 0])
    result = []

    while queue:
        curr = queue.popleft()
        result.append(curr)

        for neighbor in graph[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == len(tasks):
        return result
    else:
        return None

# Merge Intervals

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged





# Bonus: interval_operations

def interval_operations(intervals, operation):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    if operation == 'merge':
        return merge_intervals(intervals)

    elif operation == 'intersect':
        start = max(i[0] for i in intervals)
        end = min(i[1] for i in intervals)
        return [[start, end]] if start <= end else []

    elif operation == 'gaps':
        gaps = []
        for i in range(1, len(intervals)):
            prev_end = intervals[i-1][1]
            curr_start = intervals[i][0]
            if curr_start > prev_end:
                gaps.append([prev_end, curr_start])
        return gaps

    else:
        return []

# Test Cases

print("\n*Task Scheduler Tests*")
tasks1 = ["A", "B", "C", "D"]
dependencies1 = [("B", "A"), ("C", "B"), ("D", "A")]
print("Test 1:", task_scheduler(tasks1, dependencies1))

tasks2 = ["X", "Y", "Z"]
dependencies2 = [("Y", "X"), ("Z", "Y"), ("X", "Z")]
print("Test 2:", task_scheduler(tasks2, dependencies2))

tasks3 = ["P", "Q", "R"]
dependencies3 = []
print("Test 3:", task_scheduler(tasks3, dependencies3))

tasks4 = ["compile", "test", "deploy", "build", "package"]
dependencies4 = [
    ("test", "compile"),
    ("deploy", "package"),
    ("package", "build"),
    ("build", "compile")
]
print("Test 4:", task_scheduler(tasks4, dependencies4))


print("\n*Merge Intervals Tests*")
print("Test 1:", merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print("Test 2:", merge_intervals([[1,4],[4,5]]))
print("Test 3:", merge_intervals([[1,4],[2,3]]))
print("Test 4:", merge_intervals([[1,2],[3,4],[5,6]]))
print("Test 5:", merge_intervals([[1,4],[2,5],[3,6]]))
print("Test 6:", merge_intervals([[6,7],[2,4],[5,9]]))
print("Test 7:", merge_intervals([[1,4]]))
print("Test 8:", merge_intervals([[2,3],[4,5],[6,7],[8,9],[1,10]]))

print("\n*Bonus Function Tests*")
print("Gaps:", interval_operations([[1,3],[6,9]], 'gaps'))         # [[3,6]]
print("Merge:", interval_operations([[1,3],[2,6]], 'merge'))       # [[1,6]]
print("Intersect:", interval_operations([[1,5],[2,6],[4,7]], 'intersect'))  # [[4,5]]