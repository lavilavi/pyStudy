import codecs
import chardet
import requests

inputFile = 'C:\\Users\\ymizu\\Downloads\\Att.2020-04_30_楠木椋.csv'
output = './out2'


def guess():
    res = requests.get(
        "https://lab-gklp-thai-api.kinto-mobility.jp/vehicle/v1/user/vehicles/6f9b2834-73f5-415f-a0a2-e67755489781")
    # f = open(inputFile, 'rb')
    encoding = chardet.detect(res.text)
    print(res.encoding)
    # f.close()
    return encoding


def read(encoding, should_write):
    f2 = codecs.open(inputFile, 'r', encoding['encoding'])
    f3 = codecs.open(output, 'w', 'utf-8')s
    for i, l in enumerate(f2):
        print(l.rstrip())
        if should_write:
            f3.write(l.rstrip() + '\n')
    f2.close()
    f3.close()


if __name__ == '__main__':
    encd = guess()
    # read(encd, True)
