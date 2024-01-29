def circles(circlePairs):
    def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    results = []

    for pair in circlePairs:
        x1, y1, r1, x2, y2, r2 = map(int, pair.split())
        distance = calculate_distance(x1, y1, x2, y2)
        radius_sum = r1 + r2
        radius_diff = abs(r1 - r2)

        if distance == 0:
            if r1 == r2:
                results.append("Concentric")
            else:
                results.append("Disjoint-Inside")
        elif distance == radius_sum or distance == radius_diff:
            results.append("Touching")
        elif distance < radius_sum and distance > radius_diff:
            results.append("Intersecting")
        elif distance > radius_sum:
            results.append("Disjoint-Outside")
        else:
            results.append("Disjoint-Inside")
    print(results)
    return results

# Example usage
circlePairs = ['3 0 10 5 0 3', '0 1 4 0 1 5']
circles(circlePairs)
