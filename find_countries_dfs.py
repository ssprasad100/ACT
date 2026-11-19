#Find how many different countries exist on this map using DFS

def findcountr(A):
    rows = len(A)
    cols = len(A[0])

    visited = [[False] * cols for _ in range(rows)]

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    countries = 0

    for r in range(rows):
        for c in range(cols):
            if visited[r][c]:
                continue

            countries += 1
            color = A[r][c]

            stack = [(r, c)]
            visited[r][c] = True

            while stack:
                x, y = stack.pop()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if (0 <= nx < rows and
                        0 <= ny < cols):

                        if (not visited[nx][ny] and
                            A[nx][ny] == color):

                            visited[nx][ny] = True
                            stack.append((nx, ny))

    return countries
