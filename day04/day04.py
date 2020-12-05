def validate_part1(passport):
    return all(k in passport for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def validate_part2(passport):
    try:
        if passport['hgt'].endswith('cm'):
            valid_height = 150 <= int(passport['hgt'][:-2]) <= 193
        elif passport['hgt'].endswith('in'):
            valid_height = 59 <= int(passport['hgt'][:-2]) <= 76
        else:
            valid_height = False

        return (1920 <= int(passport['byr']) <= 2002
                and 2010 <= int(passport['iyr']) <= 2020
                and 2020 <= int(passport['eyr']) <= 2030
                and valid_height
                and passport['hcl'][0] == '#' and set(passport['hcl'][1:]).issubset('0123456789abcdef')
                and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                and len(passport['pid']) == 9 and passport['pid'].isdigit())
    except KeyError:
        return False


def parse(passport_data):
    passports = ['']
    for it in passport_data:
        if it != '':
            passports[-1] = passports[-1] + ' ' + it
        else:
            passports.append(it)
    return [{p.split(':')[0]: p.split(':')[1] for p in passport.split()} for passport in passports]


with open("input.txt") as file:
    data = parse(file.read().splitlines())

print("PART ONE")
part1 = sum(map(validate_part1, data))
print(part1)

print("PART TWO")
part2 = sum(map(validate_part2, data))
print(part2)
