def pearson_correlation(x: list[int|float], y: list[int|float]) -> float:
    x = list(map(float, x))
    y = list(map(float, y))

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    sx = sum([(xi - mean_x) ** 2 for xi in x])
    sy = sum([(yi - mean_y) ** 2 for yi in y])

    cov = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in
               zip(x, y)])

    corr = cov / (sx * sy) ** 0.5

    return corr

print(pearson_correlation([1, 2, 3, 4, 5], [2, 3, 5, 7, 11]))
print(pearson_correlation([0, 1, 2], [2, 4, 6]))
print(pearson_correlation([4, 5, 6], [6, 7, 8]))
