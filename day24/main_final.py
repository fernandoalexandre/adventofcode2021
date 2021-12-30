def get_recursive_models(model_num: list, curr_z: int) -> None:
    step = len(model_num)
    match step:
        case 0:
            [get_recursive_models(model_num + [w], curr_z + w + 16) for w in range(1, 10)]
        case 1:
            [get_recursive_models(model_num + [w], (curr_z * 26) + w + 3) for w in range(1, 10)]
        case 2:
            [get_recursive_models(model_num + [w], (curr_z * 26) + w + 2) for w in range(1, 10)]
        case 3:
            [get_recursive_models(model_num + [w], (curr_z * 26) + w + 7) for w in range(1, 10)]
        case 4:
            [get_recursive_models(model_num + [w], int(curr_z / 26)) for w in range(1, 10) if (curr_z % 26) - 10 == w]
        case 5:
            [get_recursive_models(model_num + [w], (curr_z * 26) + w + 6) for w in range(1, 10)]
        case 6:
            [get_recursive_models(model_num + [w], int(curr_z / 26)) for w in range(1, 10) if (curr_z % 26) - 14 == w]
        case 7:
            [get_recursive_models(model_num + [w], (curr_z * 26) + w + 11) for w in range(1, 10)]
        case 8:
            [get_recursive_models(model_num + [w], int(curr_z / 26)) for w in range(1, 10) if (curr_z % 26) - 4 == w]
        case 9:
            [get_recursive_models(model_num + [w], int(curr_z / 26)) for w in range(1, 10) if (curr_z % 26) - 3 == w]
        case 10:
            [get_recursive_models(model_num + [w], (curr_z * 26) + w + 11) for w in range(1, 10)]
        case 11:
            [get_recursive_models(model_num + [w], int(curr_z / 26)) for w in range(1, 10) if (curr_z % 26) - 3 == w]
        case 12:
            [get_recursive_models(model_num + [w], int(curr_z / 26)) for w in range(1, 10) if (curr_z % 26) - 9 == w]
        case 13:
            [get_recursive_models(model_num + [w], int(curr_z / 26)) for w in range(1, 10) if (curr_z % 26) - 12 == w]
        case 14:
            # end
            if curr_z == 0:
                print(''.join(map(str, model_num)))
            else:
                return None


def main():
    get_recursive_models([], 0)


if __name__ == "__main__":
    main()
