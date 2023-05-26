def achimsp144s(board):

    # rows -> 42
    # columns -> 60

    pos = [
        (2, 2), (2, 3), (2, 28), (2, 29), (3, 2), (3, 3), (3, 28), (3, 29),
        (4, 20), (4, 21), (5, 19), (5, 22), (6, 20), (6, 21), (7, 16), (8, 15), (8, 17),
        (9, 14), (9, 18), (10, 14), (10, 17), (11, 14), (11, 17), (12, 13), (12, 17),
        (13, 14), (13, 16), (14, 15), (15, 10), (15, 11), (16, 9), (16, 12), (17, 10), (17, 11),
        (18, 2), (18, 3), (18, 28), (18, 29), (19, 2), (19, 3), (19, 28), (19, 29),
        (23, 32), (23, 33), (23, 58), (23, 59), (24, 32), (24, 33), (24, 58), (24, 59),
        (25, 50), (25, 51), (26, 49), (26, 52), (27, 50), (27, 51), (28, 46), (29, 45), (29, 47),
        (30, 44), (30, 48), (31, 44), (31, 47), (32, 44), (32, 47), (33, 43), (33, 47),
        (34, 44), (34, 46), (35, 45), (36, 40), (36, 41), (37, 39), (37, 42), (38, 40), (38, 41),
        (39, 32), (39, 33), (39, 58), (39, 59), (40, 32), (40, 33), (40, 58), (40, 59)
    ]

    for y, x in pos:
        board[y][x] = 1

    return board


def anura(board):

    # rows -> 31
    # columns -> 54

    pos = [
        (1, 10), (1, 22), (2, 9), (2, 10), (2, 11), (2, 21), (2, 22), (2, 23),
        (3, 11), (3, 21), (4, 7), (4, 9), (4, 10), (4, 22), (4, 23), (4, 25), (5, 7), (5, 12), (5, 13),
        (5, 14), (5, 18), (5, 19), (5, 20), (5, 25), (6, 6), (6, 8), (6, 9), (6, 10),
        (6, 12), (6, 13), (6, 14), (6, 18), (6, 19), (6, 20), (6, 22), (6, 23), (6, 24), (6, 26),

        (8, 5), (8, 6), (8, 7), (8, 9), (8, 10), (8, 11), (8, 12), (8, 14), (8, 18), (8, 20), (8, 21),
        (8, 22), (8, 23), (8, 25), (8, 26), (8, 27), (9, 5), (9, 6), (9, 14), (9, 18), (9, 26), (9, 27),
        (10, 5), (10, 6), (10, 7), (10, 10), (10, 12), (10, 13), (10, 19), (10, 20), (10, 22), (10, 25),
        (10, 26), (10, 27),

        (12, 10), (12, 13), (12, 19), (12, 22),

        (13, 10), (13, 22), (14, 8), (14, 9), (14, 12), (14, 14),
        (14, 18), (14, 20), (14, 23), (14, 24), (15, 8), (15, 12), (15, 13), (15, 14), (15, 18),
        (15, 19), (15, 20), (15, 24), (16, 6), (16, 7), (16, 12), (16, 15), (16, 17), (16, 20),
        (16, 25), (16, 26), (17, 4), (17, 6), (17, 7), (17, 9), (17, 11), (17, 12), (17, 15), (17, 17),
        (17, 20), (17, 21), (17, 23), (17, 25), (17, 26), (17, 28), (18, 3), (18, 4), (18, 6), (18, 10), (18, 14),
        (18, 18), (18, 22), (18, 26), (18, 28), (18, 29), (19, 2), (19, 4), (19, 8), (19, 9), (19, 23),
        (19, 24), (19, 28), (19, 30), (20, 2), (20, 3), (20, 12), (20, 20), (20, 29), (20, 30),
        (21, 3), (21, 11), (21, 12), (21, 13), (21, 19), (21, 20), (21, 21), (21, 31), (22, 11), (22, 12),
        (22, 14), (22, 18), (22, 20), (22, 21), (23, 1), (23, 2), (23, 5), (23, 6), (23, 12), (23, 13), (23, 14),
        (23, 18), (23, 19), (23, 20), (23, 26), (23, 27), (23, 30), (23, 31), (24, 1), (24, 3), (24, 7), (24, 13), (24, 14),
        (24, 18), (24, 19), (24, 25), (24, 29), (24, 31), (25, 5), (25, 7), (25, 8), (25, 24), (25, 25), (25, 27),
        (26, 9), (26, 23), (27, 2), (27, 8), (27, 9), (27, 10), (27, 22), (27, 23), (27, 24), (27, 30),
        (28, 4), (28, 28), (29, 6), (29, 7), (29, 25), (29, 26), (30, 6), (30, 7), (30, 8), (30, 9), (30, 10),
        (30, 11), (30, 21), (30, 22), (30, 23), (30, 24), (30, 25), (30, 26), (31, 7), (31, 9), (31, 23), (31, 25),
        (32, 3), (32, 4), (32, 5), (32, 10), (32, 11), (32, 16), (32, 21), (32, 22), (32, 27), (32, 28), (32, 29),
        (33, 3), (33, 4), (33, 9), (33, 10), (33, 11), (33, 15), (33, 16), (33, 17), (33, 21), (33, 22), (33, 23),
        (33, 27), (33, 28), (34, 4), (34, 5), (34, 7), (34, 14), (34, 18), (34, 25), (34, 27), (34, 28),
        (35, 13), (35, 15), (35, 17), (35, 19), (36, 12), (36, 14), (36, 15), (36, 17), (36, 18), (36, 20),
        (37, 12), (37, 14), (37, 15), (37, 16), (37, 17), (37, 18), (37, 20), (38, 10), (38, 11), (38, 21), (38, 22),
        (39, 9), (39, 10), (39, 22), (39, 23), (40, 9), (40, 23), (42, 7), (42, 9), (42, 23), (42, 25), (43, 10),
        (43, 22), (44, 6), (44, 10), (44, 22), (44, 26), (45, 6), (45, 11), (45, 21), (45, 26), (46, 6), (46, 11),
        (46, 21), (46, 26), (47, 7), (47, 25), (48, 9), (48, 10), (48, 11), (48, 21), (48, 22), (48, 23),
        (49, 9), (49, 23), (51, 9), (51, 23), (52, 7), (52, 25), (53, 9), (53, 23)
    ]

    for y, x in pos:
        board[y][x] = 1

    return board


def blinkership(board):

    # rows -> 27
    # columns -> 15

    pos = [
        (1, 11), (1, 12), (1, 13), (1, 14), (2, 11), (2, 15), (3, 11), (4, 3), (4, 12),
        (4, 15), (5, 1), (5, 2), (5, 4), (5, 5), (6, 2), (6, 3), (6, 4), (6, 5), (6, 9), (7, 3), (7, 4),
        (7, 8), (7, 10), (7, 11), (7, 20), (7, 25), (7, 26), (7, 27), (8, 7), (8, 11), (8, 20), (8, 25), (8, 27),
        (9, 3), (9, 4), (9, 8), (9, 10), (9, 11), (9, 20), (9, 25), (9, 26), (9, 27), (10, 5), (10, 9),
        (11, 1), (11, 2), (11, 4), (11, 5), (12, 2), (12, 3), (12, 12), (12, 15), (13, 11), (14, 11),
        (14, 15), (15, 11), (15, 12), (15, 13), (15, 14)
    ]

    for y, x in pos:
        board[y][x] = 1

    return board


def achimsotherp(board):

    # rows -> 35
    # columns -> 35

    pos = [(
        1, 10), (1, 26), (2, 10), (2, 11), (2, 25), (2, 26), (3, 11), (3, 25), (4, 11),
        (4, 25), (9, 13), (9, 14), (9, 22), (9, 23), (10, 1), (10, 2), (10, 3), (10, 14), (10, 15),
        (10, 21), (10, 22), (10, 33), (10, 34), (10, 35), (11, 2), (11, 3), (11, 4), (11, 15), (11, 16),
        (11, 20), (11, 21), (11, 32), (11, 33), (11, 34), (13, 9), (13, 27), (14, 9), (14, 10),
        (14, 26), (14, 27), (15, 10), (15, 11), (15, 25), (15, 26), (16, 11), (16, 25), (20, 11),
        (20, 25), (21, 10), (21, 11), (21, 25), (21, 26), (22, 9), (22, 10), (22, 26), (22, 27),
        (23, 9), (23, 27), (25, 2), (25, 3), (25, 4), (25, 15), (25, 16), (25, 20), (25, 21), (25, 32),
        (25, 33), (25, 34), (26, 1), (26, 2), (26, 3), (26, 14), (26, 15), (26, 21), (26, 22), (26, 33), (26, 34),
        (26, 35), (27, 13), (27, 14), (27, 22), (27, 23), (32, 11), (32, 25), (33, 10), (33, 11), (33, 25),
        (33, 26), (34, 10), (34, 11), (34, 25), (34, 26), (35, 10), (35, 26)
    ]

    for y,  x in pos:
        board[y][x] = 1

    return board


def maxi(board):

    # rows -> 27
    # columns -> 27

    pos = [(
        1, 19), (2, 18), (2, 19), (2, 20), (3, 13), (3, 14), (3, 15), (3, 20), (3, 21),
        (4, 12), (4, 15), (4, 16), (4, 17), (4, 20), (4, 22), (4, 23), (5, 11), (5, 15), (5, 17),
        (5, 20), (5, 22), (6, 11), (6, 16), (6, 18), (6, 20), (6, 22), (6, 24), (6, 25), (7, 13),
        (7, 18), (7, 20), (7, 24), (7, 25), (8, 1), (8, 2), (8, 3), (8, 4), (8, 10), (8, 12), (8, 17),
        (8, 21), (8, 23), (8, 24), (8, 25), (9, 1), (9, 5), (9, 6), (9, 8), (9, 10), (9, 11), (9, 12), (9, 14),
        (9, 15), (9, 25), (9, 26), (10, 1), (10, 7), (10, 8), (10, 14), (11, 2), (11, 5), (11, 6), (11, 8),
        (11, 11), (11, 14), (11, 16), (11, 17), (12, 8), (12, 10), (12, 12), (12, 14), (12, 16),
        (12, 18), (12, 24), (12, 25), (12, 26), (12, 27), (13, 2), (13, 5), (13, 6), (13, 8), (13, 11),
        (13, 14), (13, 17), (13, 18), (13, 20), (13, 22), (13, 23), (13, 27), (14, 1), (14, 7), (14, 8),
        (14, 12), (14, 14), (14, 16), (14, 20), (14, 21), (14, 27), (15, 1), (15, 5), (15, 6),
        (15, 8), (15, 10), (15, 11), (15, 14), (15, 17), (15, 20), (15, 22), (15, 23), (15, 26),
        (16, 1), (16, 2), (16, 3), (16, 4), (16, 10), (16, 12), (16, 14), (16, 16), (16, 18), (16, 20),
        (17, 11), (17, 12), (17, 14), (17, 17), (17, 20), (17, 22), (17, 23), (17, 26), (18, 14), (18, 20),
        (18, 21), (18, 27), (19, 2), (19, 3), (19, 13), (19, 14), (19, 16), (19, 17), (19, 18), (19, 20), (19, 22),
        (19, 23), (19, 27), (20, 3), (20, 4), (20, 5), (20, 7), (20, 11), (20, 16), (20, 18), (20, 24), (20, 25),
        (20, 26), (20, 27), (21, 3), (21, 4), (21, 8), (21, 10), (21, 15), (22, 3), (22, 4), (22, 6), (22, 8),
        (22, 10), (22, 12), (22, 17), (23, 6), (23, 8), (23, 11), (23, 13), (23, 17), (24, 5), (24, 6), (24, 8), (24, 11),
        (24, 12), (24, 13), (24, 16), (25, 7), (25, 8), (25, 13), (25, 14), (25, 15), (26, 8), (26, 9), (26, 10),
        (27, 9)
    ]

    for y, x in pos:
        board[y][x] = 1

    return board