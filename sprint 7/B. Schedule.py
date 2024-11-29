def parse_time(t):
    if '.' in t:
        h, m = map(int, t.split('.'))
    else:
        h = int(t)
        m = 0
    return h * 60 + m


def format_time(minutes):
    h = minutes // 60
    m = minutes % 60
    if m == 0:
        return str(h)
    else:
        return f"{h}.{m:02}"


def max_non_overlapping_lessons(n, lessons):
    lessons = [(parse_time(start), parse_time(end)) for start, end in lessons]
    lessons.sort(key=lambda x: [x[1], x[0]])

    selected_lessons = []
    last_end_time = 0

    for start, end in lessons:
        if start >= last_end_time:
            selected_lessons.append((start, end))
            last_end_time = end

    result = [str(len(selected_lessons))]
    for start, end in selected_lessons:
        result.append(f"{format_time(start)} {format_time(end)}")
    return result


n = int(input())
lessons = [input().split() for _ in range(n)]

result = max_non_overlapping_lessons(n, lessons)
print("\n".join(result))
