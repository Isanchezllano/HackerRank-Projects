def runner_up(n, arr):
    score = []
    if n >= 2 and n <= 10:
        for i in arr:
            if i >= -100 and i <= 100:
                score.append(i)

    second= sorted(set(score), reverse=True)[1]

    return second