relative_vertical = []
self_pos = (0, 4)
allies = [(0, 6), (0, 5), (0, 1), (0, 0)]

for i in range(1, 8):
    if self_pos[1] - i >= 0:
        relative_vertical.append([0 + self_pos[0], self_pos[1] - i])
    if self_pos[1] + i < 8:
        relative_vertical.insert(0, [0 + self_pos[0], self_pos[1] + i])
print(relative_vertical)
top_nearest = [0, -9]
bot_nearest = [0, 9]

for move in relative_vertical:
    if move in allies:
        if move[1] < self_pos[1] and move[1] > top_nearest[1]:
            top_nearest[1] = move[1]
        if move[1] > self_pos[1] and move[1] < bot_nearest[1]:
            bot_nearest[1] = move[1]

print("self", self_pos)
print("top n", top_nearest, "bot n",  bot_nearest)

if top_nearest != [0, -9]:
    t_i = relative_vertical.index(tuple(top_nearest))
    relative_vertical = relative_vertical[:t_i]
    relative_vertical.append(top_nearest)
if bot_nearest != [0, 9]:
    b_i = relative_vertical.index(tuple(bot_nearest))
    relative_vertical = relative_vertical[b_i:]

print(relative_vertical)

# if left_n != [-9, self.y]:
#     l_i = horizontal_moves.index(left_n)
#     horizontal_moves = horizontal_moves[l_i:]
# if right_n != [9, self.y]:
#     r_i = horizontal_moves.index(right_n)
#     horizontal_moves = horizontal_moves[:r_i]
#     horizontal_moves.append(right_n)
# for move in horizontal_moves:
#     move[0] -= self.x
#     move[1] -= self.y


# relative_horizontal = []
# self_pos = (3, 7)
# allies = [(2, 7), (1, 7), (0, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
# for i in range(1, 7):
#     if i + self_pos[0] < 8:
#         relative_horizontal.append((i + self_pos[0], 0 + self_pos[1]))
#     if -i + self_pos[0] >= 0:
#         relative_horizontal.insert(0, (-i + self_pos[0], 0 + self_pos[1]))
# left_nearest = [-9, 7]
# right_nearest = [9, 7]
# print(relative_horizontal)
# for move in relative_horizontal:
#     if move in allies:
#         if move[0] < self_pos[0] and move[0] > left_nearest[0]:
#             left_nearest[0] = move[0]
#         elif move[0] > self_pos[0] and move[0] < right_nearest[0]:
#             right_nearest[0] = move[0]

# print(left_nearest, right_nearest)
# l_i = relative_horizontal.index(tuple(left_nearest))
# r_i = relative_horizontal.index(tuple(right_nearest))
# relative_horizontal = relative_horizontal[:r_i]
# relative_horizontal = relative_horizontal[]
# relative_horizontal.append(right_nearest)
# print(relative_horizontal)



# relative_horizontal = []
# self_pos = (3, 7)
# allies = [(2, 7), (1, 7), (0, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
# for i in range(1, 7):
#     if i + self_pos[0] < 8:
#         relative_horizontal.append((i, 0))
#     if -i + self_pos[0] >= 0:
#         relative_horizontal.insert(0, (-i, 0))
# print(relative_horizontal)
# print("current pos:", self_pos)
# coords = [0, 0]
# left_nearest = [-9, 7]
# right_nearest = [9, 7]
# for move_index in range(len(relative_horizontal)):
#     coords[0] = relative_horizontal[move_index][0] + self_pos[0]
#     coords[1] = relative_horizontal[move_index][1] + self_pos[1]
#     print(f"relative to {self_pos} coords:", coords)
#     if tuple(coords) in allies:
#         print("ally on the way, ", coords)
#         print(f"ally x = {coords[0]}, self x = {self_pos[0]}")
#         if coords[0] < self_pos[0]:
#             if coords[0] > left_nearest[0]:
#                 left_nearest = coords
#                 print("changed to:", left_nearest)
#         if coords[0] > self_pos[0]:
#             if coords[0] < right_nearest[0]:
#                 right_nearest = coords
#         print("left", left_nearest)
#         print("right", right_nearest)

#     print("=====")

# print(left_nearest, right_nearest)
        

# # print(relative_horizontal)