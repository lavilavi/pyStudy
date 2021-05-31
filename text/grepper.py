import os


# if
#     os.path.splitext(f)[1] == '.txt'
def recursively_grep(path, word):
    outf = open('out3.txt', 'w')
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames]
    print(result)
    for f in result:
        if 'zip' not in f:
            matched = []
            already_set = False
            reader = open(f, 'r', encoding='utf-8')
            lines = reader.readlines()
            for i, l in enumerate(lines):
                if word in l or 'subject: 【KINTO】お客様情報の変更受付完了のお知らせ' in l:
                    matched.append(i)

            if len(matched) != 0:
                for j in matched:
                    if not already_set:
                        already_set = True
                        outf.write('\n' + f + '\n')
                    outf.write(lines[j] + '\n')
                    outf.flush()
    outf.close()


if __name__ == '__main__':
    recursively_grep('C:\\Users\\yuki\\Documents\\wappcore', 'subject: 属性変更受付連絡')
