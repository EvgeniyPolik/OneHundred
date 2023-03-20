# Подсчет значения в линии, по указанным операциям
def check_sum(line, operations):
    digit_in_string = ''
    sum_line = 0
    current_operation = lambda x, y: x + y
    for symbol in line:
        if symbol in operations:
            sum_line = current_operation(sum_line, int(digit_in_string))
            current_operation = operations[symbol]
            digit_in_string = ''
        else:
            digit_in_string += symbol
    sum_line = current_operation(sum_line, int(digit_in_string))

    return sum_line

# Построение списка всевозможных комбинаций удовлетворяющих условию рекурсивным способом
def get_lines(lines, origin_line, operations, current_line, seek_sum, current_symbol='0', current_position=0):
    if current_position >= len(origin_line) - 1:
        if check_sum(current_line, operations) == seek_sum:
            lines.append(current_line)
            return
        return
    else:
        if current_symbol in (operations.keys()) and current_position < len(origin_line) - 1:
            tmp_line = current_line +  origin_line[current_position + 1]
            get_lines(lines, origin_line, operations, tmp_line, seek_sum, origin_line[current_position + 1],
                      current_position + 1)
        else:
            for item in operations.keys():
                tmp_line = current_line + item
                get_lines(lines, origin_line, operations, tmp_line, seek_sum, item,
                          current_position)
            tmp_line = current_line +  origin_line[current_position + 1]
            get_lines(lines, origin_line, operations, tmp_line, seek_sum, origin_line[current_position + 1],
                      current_position + 1)

# подготовка и запуск перебора
def get_catalog_line(origin_line, operations, seek_sum=100):
    result = []
    get_lines(result, origin_line, operations, origin_line[0], seek_sum)
    return result

collectionNumbers = '123456789'
operations = { '+': lambda x, y: x + y, '-': lambda x, y: x - y }
seek_sum = 100
for line in get_catalog_line(collectionNumbers, operations, seek_sum):
    print(line, end=f' = {check_sum(line, operations)}\n')