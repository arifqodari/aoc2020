import re


def get_passports(input_filepath):
    """
    parse input filepath into list of passports
    each passport data is separated by blank line
    and each data (key:value) in a passport is separated by space
    """
    passports = []
    with open(input_filepath, "r") as f:
        passport = {}
        for line in f:
            line = line.strip()

            # if found blank line, put previous passport data to the list
            if line == "":
                passports.append(passport)
                passport = {}

            for item in line.split():
                (key, value) = item.split(":")
                passport[key] = value

        # append the last passport
        passports.append(passport)
    return passports


def is_valid(passport):
    """
    check whether a passport is valid
    all required fields should be present
    except the cid is optional
    """
    requireds = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    check = [required in passport.keys() for required in requireds]
    return all(check)


def is_valid2(passport):
    """
    check whether a passport is valid
    cid still optional
    but the other fields have additional requirements
    """

    # byr
    byr = passport["byr"]
    byr_valid = len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002

    # iyr
    iyr = passport["iyr"]
    iyr_valid = len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020

    # eyr
    eyr = passport["eyr"]
    eyr_valid = len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030

    # hgt 
    hgt = passport["hgt"]
    if hgt.endswith("cm"):
        hgt_num = int(hgt.replace("cm", ""))
        hgt_valid = hgt_num >= 150 and hgt_num <= 193
    elif hgt.endswith("in"):
        hgt_num = int(hgt.replace("in", ""))
        hgt_valid = hgt_num >= 59 and hgt_num <= 76
    else:
        hgt_valid = False

    # hcl
    hcl_valid = re.match("^#[0-9a-f]{6}$", passport["hcl"]) is not None

    # ecl
    pattern = "^(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$"
    ecl_valid = re.match(pattern, passport["ecl"]) is not None

    # pid
    pattern = "^[0-9]{9}$"
    pid_valid = re.match(pattern, passport["pid"]) is not None

    return all([
        byr_valid,
        iyr_valid,
        eyr_valid,
        hgt_valid,
        hcl_valid,
        ecl_valid,
        pid_valid
        ])


def part1(passports):
    print("=" * 10 + " Part 1 " + "=" * 25)
    n_valids = 0
    for passport in passports:
        if is_valid(passport):
            n_valids += 1
    print(f"number of valid passports = {n_valids}")


def part2(passports):
    print("\n" + "=" * 10 + " Part 2 " + "=" * 25)
    n_valids = 0
    for passport in passports:
        if is_valid(passport):
            if is_valid2(passport):
                n_valids += 1
    print(f"number of valid passports = {n_valids}")
    

def main(input_filepath):
    passports = get_passports(input_filepath)
    part1(passports)
    part2(passports)


if __name__ == "__main__":
    from sys import argv

    main(argv[1])
