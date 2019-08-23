with open('inputa.txt', 'r') as input_map:
    src_map = []
    line_count = 0
    for line in input_map.readlines(): 
        src_map.append(line.rstrip())
        line_count += 1

line_length = len(src_map[0])
generation_map = [[0 for x in range(line_length)] for y in range(line_count)]
solution_map = [['X' for x in range(line_length)] for y in range(line_count)]

for line in range(line_count):
    if src_map[line][0] == 'O':
        start_postition = (line, 0)

for line in range(line_count):
    if src_map[line][line_length-1] == 'O':
        end_postition = (line, line_length-1)

generation_map[start_postition[0]][start_postition[1]] = 1
pos_to_check = []
store_to_check = [start_postition]

generation = 2

while True:
    pos_to_check, store_to_check = store_to_check, pos_to_check
    store_to_check.clear()
    for position in pos_to_check:
        if position[0] != line_count-1:
            if src_map[position[0]+1][position[1]] == 'O':
                if generation_map[position[0]+1][position[1]] == 0:
                    generation_map[position[0]+1][position[1]] = generation
                    store_to_check.append((position[0]+1, position[1]))
        
        if position[0] != 0:
            if src_map[position[0]-1][position[1]] == 'O':
                if generation_map[position[0]-1][position[1]] == 0:
                    generation_map[position[0]-1][position[1]] = generation
                    store_to_check.append((position[0]-1, position[1]))

        if position[1] != line_length-1:
            if src_map[position[0]][position[1]+1] == 'O':
                if generation_map[position[0]][position[1]+1] == 0:
                    generation_map[position[0]][position[1]+1] = generation
                    store_to_check.append((position[0], position[1]+1))

        if position[1] != 0:
            if src_map[position[0]][position[1]-1] == 'O':
                if generation_map[position[0]][position[1]-1] == 0:
                    generation_map[position[0]][position[1]-1] = generation
                    store_to_check.append((position[0], position[1]-1))
    generation += 1
    if generation_map[end_postition[0]][end_postition[1]] != 0:
        break

# for line in generation_map:
#     print(' '.join(str(x) for x in line))

top_generation = generation
pos_to_check = [end_postition]
solution_map[end_postition[0]][end_postition[1]] = 'O'

while True:
    did_turn = False
    top_generation -= 1

    pos_to_check, store_to_check = store_to_check, pos_to_check
    if top_generation == 0:
        break

    for position in pos_to_check:
        if position[0] != line_count-1:
            if did_turn:
                break
            if generation_map[position[0]+1][position[1]] == top_generation:
                solution_map[position[0]+1][position[1]] = 'O'
                store_to_check.append((position[0]+1, position[1]))
                did_turn = True
        
        if position[0] != 0:
            if did_turn:
                break
            if generation_map[position[0]-1][position[1]] == top_generation:
                solution_map[position[0]-1][position[1]] = 'O'
                store_to_check.append((position[0]-1, position[1]))
                did_turn = True

        if position[1] != line_length-1:
            if did_turn:
                break
            if generation_map[position[0]][position[1]+1] == top_generation:
                solution_map[position[0]][position[1]+1] = 'O'
                store_to_check.append((position[0], position[1]+1))
                did_turn = True

        if position[1] != 0:
            if did_turn:
                break
            if generation_map[position[0]][position[1]-1] == top_generation:
                solution_map[position[0]][position[1]-1] = 'O'
                store_to_check.append((position[0], position[1]-1))
                did_turn = True

with open('solution.txt', 'r+') as sol_file:
    for line in solution_map:
        sol_file.write(''.join(str(x) for x in line)+'\n')