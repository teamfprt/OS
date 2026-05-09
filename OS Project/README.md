# Scheduling Algorithm Scenarios

Comparison of **Priority Scheduling** vs **Round Robin** across four process scenarios.

### Metrics

| Metric | Formula |
|---|---|
| TAT (Turnaround Time) | completion − arrival |
| WT (Waiting Time) | TAT − burst |
| RT (Response Time) | start − arrival |

---

## Scenario A — Basic Mixed Workload

| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1      | 0       | 5     | 2        |
| P2      | 1       | 3     | 1        |
| P3      | 2       | 4     | 3        |

**Quantum = 3**

### Priority Scheduling

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 5   | 0  | 0  |
| P2      | 7   | 4  | 4  |
| P3      | 10  | 6  | 6  |
| **AVG** | **7.33** | **3.33** | **3.33** |

**Gantt Chart:**

```
| P1 | P2 | P3 |
0    5    8    12
```

### Round Robin

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 11  | 6  | 0  |
| P2      | 5   | 2  | 2  |
| P3      | 10  | 6  | 4  |
| **AVG** | **8.67** | **4.67** | **2.00** |

**Gantt Chart:**

```
| P1 | P2 | P3 | P1 | P3 |
0    3    6    9    11   12
```

---

## Scenario B — Urgency Case

| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1      | 0       | 8     | 3        |
| P2      | 1       | 8     | 3        |
| P3      | 2       | 2     | 1        |

**Quantum = 3**

### Priority Scheduling

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 8   | 0  | 0  |
| P2      | 17  | 9  | 9  |
| P3      | 8   | 6  | 6  |
| **AVG** | **11.00** | **5.00** | **5.00** |

**Gantt Chart:**

```
| P1 | P3 | P2 |
0    8    10   18
```

### Round Robin

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 16  | 8  | 0  |
| P2      | 17  | 9  | 2  |
| P3      | 6   | 4  | 4  |
| **AVG** | **13.00** | **7.00** | **2.00** |

**Gantt Chart:**

```
| P1 | P2 | P3 | P1 | P2 | P1 | P2 |
0    3    6    8    11   14   16   18
```

---

## Scenario C — Fairness Case

| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1      | 0       | 10    | 1        |
| P2      | 0       | 10    | 2        |
| P3      | 0       | 10    | 3        |

**Quantum = 2**

### Priority Scheduling

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 10  | 0  | 0  |
| P2      | 20  | 10 | 10 |
| P3      | 30  | 20 | 20 |
| **AVG** | **20.00** | **10.00** | **10.00** |

**Gantt Chart:**

```
| P1 | P2 | P3 |
0    10   20   30
```

### Round Robin

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 26  | 16 | 0  |
| P2      | 28  | 18 | 2  |
| P3      | 30  | 20 | 4  |
| **AVG** | **28.00** | **18.00** | **2.00** |

**Gantt Chart:**

```
| P1 | P2 | P3 | P1 | P2 | P3 | P1 | ...
0    2    4    6    8    10   12   14  ...
```

---

## Scenario D — Possible Starvation Case

| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1      | 0       | 10    | 4        |
| P2      | 1       | 3     | 1        |
| P3      | 3       | 3     | 1        |
| P4      | 5       | 3     | 1        |

**Quantum = 3**

### Priority Scheduling

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 10  | 0  | 0  |
| P2      | 12  | 9  | 9  |
| P3      | 13  | 10 | 10 |
| P4      | 14  | 11 | 11 |
| **AVG** | **12.25** | **7.50** | **7.50** |

**Gantt Chart:**

```
| P1 | P2 | P3 | P4 |
0    10   13   16   19
```

### Round Robin

| Process | TAT | WT | RT |
|---------|-----|----|----|
| P1      | 19  | 9  | 0  |
| P2      | 5   | 2  | 2  |
| P3      | 6   | 3  | 3  |
| P4      | 10  | 7  | 7  |
| **AVG** | **10.00** | **5.25** | **3.00** |

**Gantt Chart:**

```
| P1 | P2 | P3 | P1 | P4 | P1 | P1 |
0    3    6    9    12   15   18   19
```