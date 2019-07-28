

def ryerson_letter_grade(pct):
    pct = int(pct)
    grade_dict = {range(0, 50): 'F', range(50, 53): 'D-', range(53, 57): 'D', range(57, 60): 'D+', range(60, 63): 'C-',
                  range(63, 67): 'C', range(67, 70): 'C+', range(70, 73): 'B-', range(73, 77): 'B', range(77, 80): 'B+',
                  range(80, 85): 'A-', range(85, 90): 'A', range(90, 151): 'A+'
                  }
    for key in grade_dict:
        if pct < 0 or pct > 150:
            return None
        if pct in key:
            return grade_dict[key]


def is_ascending(items):
    if len(items) == 0 or len(items) == 1:
        return True
    else:
        truth_checker = []
        for element in range(len(items)):
            if element == 0:
                truth_checker.append('1')
            else:
                if items[element] > items[element - 1]:
                    truth_checker.append('1')
        if len(truth_checker) == len(items):
            return True
        else:
            return False


def riffle(items, out=True):
    result = []
    if len(items) > 0:
        half = int(len(items) / 2)
    else:
        return result
    first_half = []
    second_half = []
    for element in range(0, half):
        first_half.append(items[element])
    for element_ in range(half, len(items)):
        second_half.append(items[element_])
    if out:
        for i in range(len(first_half)):
            result.append(first_half[i])
            result.append(second_half[i])
    elif not out:
        for j in range(len(first_half)):
            result.append(second_half[j])
            result.append(first_half[j])
    return result


def only_odd_digits(n):
    n = str(n)
    for i in n:
        if int(i) % 2 == 0:
            return False
        else:
            continue
    return True


def pyramid_blocks(n, m, h):
    all_sum = 0
    for i in range(0, h):
        all_sum += (n + i) * (m + i)
    return all_sum


def is_cyclops(n):
    n_list = []
    zero_counter = 0
    if n == 0:
        return True
    else:
        for i in str(n):
            n_list.append(i)
        if len(n_list) % 2 != 0:
            for j in range(len(n_list)):
                if n_list[j] == '0':
                    zero_counter += 1
            if zero_counter == 1 and n_list[int((len(n_list) / 2))] == '0':
                return True
            return False
        return False


def domino_cycle(tiles):
    if len(tiles) == 0:
        return True
    elif len(tiles) == 1:
        if tiles[0][0] == tiles[0][1]:
            return True
        return False
    for i in range(len(tiles)):
        try:
            if tiles[-1][-1] != tiles[0][0]:
                return False
            if tiles[i][1] != tiles[i + 1][0]:
                return False
        except IndexError:
            continue
    return True


def count_dominators(items):
    highest_value = 0
    dominator_count = 0
    for i in range(len(items) - 1, -1, -1):
        if items[i] > highest_value:
            highest_value = items[i]
            dominator_count += 1
    return dominator_count


def extract_increasing(digits):
    str_digits = digits
    new_list = []
    new_list.append(int(digits[0]))
    new_list_index_counter = 0
    plus_counter = 1
    minus_counter = 0
    for i in range(1, len(digits)):
        test_digit = int(str_digits[i - minus_counter:i + plus_counter])
        previous_digit = int(new_list[new_list_index_counter])
        if test_digit > previous_digit:
            new_list.append(test_digit)
            new_list_index_counter += 1
            minus_counter = 0
            plus_counter = 0
        else:
            minus_counter += 1
            plus_counter -= 1
        plus_counter += 1
    return new_list


def words_with_letters(words, letters):
    result_list = []
    letter_check = 0

    for i in range(len(words)):
        letter_list = [char for char in words[i]]
        print(letter_list)
        for j in range(len(letter_list)):
            for h in letters:
                print(h)
                print(letter_list[j])
                if h == letter_list[j]:
                    letter_check += 1

        if letter_check == len(letters):
            result_list.append(words[i])

    with open('words.txt', 'r') as words:
        lines = [l.rstrip() for l in words.readlines()]


def taxi_zum_zum(moves):
    pos_x = 0
    pos_y = 0
    state = 'north'
    for i in moves:
        if i == 'F' and state == 'north':
            pos_y += 1
        elif i == 'F' and state == 'south':
            pos_y -= 1
        elif i == 'F' and state == 'west':
            pos_x -= 1
        elif i == 'F' and state == 'east':
            pos_x += 1
        elif i == 'R' and state == 'north':
            state = 'east'
        elif i == 'R' and state == 'south':
            state = 'west'
        elif i == 'R' and state == 'west':
            state = 'north'
        elif i == 'R' and state == 'east':
            state = 'south'
        elif i == 'L' and state == 'north':
            state = 'west'
        elif i == 'L' and state == 'south':
            state = 'east'
        elif i == 'L' and state == 'west':
            state = 'south'
        elif i == 'L' and state == 'east':
            state = 'north'
    return pos_x, pos_y


if __name__ == '__main__':
    a = 'a'
    # print(ryerson_letter_grade(150))
    # print(is_ascending([1, 1, 1, 1]))
    # print(riffle(['bob', 'jack'], out=True))
    # print(only_odd_digits(0))
    # print(pyramid_blocks(10**6, 10**6, 10**6))
    # print(is_cyclops(77781088999))
    # print(domino_cycle([(2, 2)]))
    # print(count_dominators([99]))
    # print(extract_increasing('123456789' * 100))
    # words_with_letters(lines, 'egr')
    # print(words_with_letters(['antimnemonic', 'omh'], 'antmnadeic')) TERMINARRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    # print(taxi_zum_zum('FFLLLFRLFLRFRLRRL'))




