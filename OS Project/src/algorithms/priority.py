def priority_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    done = [False] * n
    time_line = []

    while completed < n:
        best = float('inf')
        position = -1
        for i, p in enumerate(processes):
            if not done[i] and p.arrival <= time:
                if p.priority < best:
                    best = p.priority
                    position = i

        if position == -1:
            time_line.append(("Idle", time, time + 1))
            time += 1
            continue

        p = processes[position]
        if p.start is None:
            p.start = time

        time_line.append((p.id, time, time + p.burst))

        time += p.burst
        p.completion = time
        done[position] = True
        completed += 1

    return processes, time_line


def calculate_metrics(processes):
    result = []
    total_wt = total_tat = total_rt = 0

    for p in processes:
        turn_around_time = p.completion - p.arrival
        waiting_time = turn_around_time - p.burst
        response_time = p.start - p.arrival

        total_wt += waiting_time
        total_tat += turn_around_time
        total_rt += response_time

        result.append((p.id, turn_around_time, waiting_time, response_time))

    n = len(processes)
    avg = (total_tat / n, total_wt / n, total_rt / n)
    return result, avg