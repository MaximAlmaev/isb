from file_works import *
from NISP_1 import freq_binary_test
from NISP_2 import con_ide_bits_test
from NISP_3 import longest_seq_test


def main():
    settings = read_json('settings.json')
    P_I_STAT = return_arr(settings["p_i"])
    LEN_SEQ = settings["len_of_seq"]
    LEN_BLOCK = settings["len_of_block"]
    test_sequences = read_json('gen_seq.json')

    print(test_sequences["java"])
    test_arr = return_arr(test_sequences["java"])
    freq_binary_test(test_arr)
    con_ide_bits_test(test_arr)
    longest_seq_test(test_arr, P_I_STAT, LEN_SEQ, LEN_BLOCK)

    print(test_sequences["cpp"])
    test_arr = return_arr(test_sequences["cpp"])
    freq_binary_test(test_arr)
    con_ide_bits_test(test_arr)
    longest_seq_test(test_arr, P_I_STAT, LEN_SEQ, LEN_BLOCK)



if __name__ == "__main__":
    main()