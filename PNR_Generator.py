import random
import array


def generator():
    # Maximum length of password needed
    MAX_LEN = 10

    # Declare arrays of the character that we need in out PNR represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)

    # combine the character randomly selected above at this stage
    temp_pnr = rand_digit + rand_upper + rand_lower

    # now that we are sure we have at least one character from each set of characters, we fill the rest of the password
    # length by selecting randomly from the combined list of character above.
    for x in range(MAX_LEN - 4):
        temp_pnr = temp_pnr + random.choice(COMBINED_LIST)

        # convert temporary PNR into array and shuffle to prevent it from having a consistent pattern where the
        # beginning of the PNR is predictable
        temp_pnr_list = array.array('u', temp_pnr)
        random.shuffle(temp_pnr_list)

    # traverse the temporary PNR array and append the chars to form the final PNR
    pnr = ""
    for x in temp_pnr_list:
        pnr = pnr + x

    # print out password
    return pnr
