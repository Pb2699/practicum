import logging
import os
# from sacremoses import MosesTokenizer, MosesDetokenizer
import argparse

logger = logging.getLogger()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, required=True, help="directory of the corpus")
    parser.add_argument("--output_dir", type=str, required=True, help="directory of the output")
    parser.add_argument("--corpus_name", type=str, required=True, help="corpus name without")
    parser.add_argument("--lang", type=str, required=True, help="language name in short as filename extention")
    parser.add_argument("--longest", type=int, default=100, help="the limits of  longest sentence")
    parser.add_argument("--word_limit", type=int, default=40, help="the limits of longest word")

    args = parser.parse_args()
    data_dir = args.data_dir
    output_dir = args.output_dir
    file_lang_name = os.path.join(data_dir, args.corpus_name + "." + args.lang)
    
    flitered_file_lang_name = os.path.join(output_dir, args.corpus_name + ".filtered." + args.lang)
    
    count_discarded = 0
    filtered_info = {"empty_line":0, "too_long_sen":0, "too_long_word":0}
    # print(file_lang_name)
    with open(file_lang_name, "r") as fl, open(flitered_file_lang_name, "w+") as f_fl:
        for lang in fl:
            lang = lang.strip()
            #if i%10000 == 0:
            #    logger.error(f"{i}")
            lang_word_list = lang.split()
            lang_len = len(lang_word_list)
            # empty line
            if lang_len == 0:
                filtered_info["empty_line"] += 1
                continue
            # too long sentence
            if lang_len > args.longest:
                filtered_info["too_long_sen"] += 1
                continue
            
            # filter sentences contain very big words
            for word in lang_word_list:
                if len(word) > args.word_limit:
                    # filtered_info["too_long_word"] += 1
                    print(" ".join(lang_word_list))
                    filtered_info["too_long_word"] += 1
                    continue
            #output line pairs
            f_fl.write(lang)
            f_fl.write("\n")
            
    print(filtered_info)
    # logger.error("f{count_discarded}")

    # mt = MosesTokenizer(lang='en')
    # # text = u'This, is a sentence with weird\xbb symbols\u2026 appearing everywhere\xbf'
    # expected_tokenized = u'This , is a sentence with weird \xbb symbols \u2026 appearing everywhere \xbf'
    # tokenized_text = mt.tokenize(text, return_str=True)
    # tokenized_text == expected_tokenized

    # print(file_lang_name)
    # print(file_tgt_name)
    # print(file_lang_name)
    # text = "Hello!"
    # print(text)


if __name__ == "__main__":
    main()
