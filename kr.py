OPEN = '[{('
CLOSE = ']})'
UNARY = '!"\','


def main(file):
    line, delimiters = getLines(file)
    parr_list = []
    quotes = 0
    for char in line.replace(" ",''):
        if char in delimiters:
            if char in OPEN:
                parr_list.append((char, OPEN.index(char)))
            elif char in CLOSE:
                try:
                    c, ind = parr_list.pop()
                    if CLOSE.index(char) != ind:
                        print('Разделители не сбалансированы', file=open('res.txt', 'w', encoding='utf-8'))
                        return
                except IndexError:
                    print('Разделители не сбалансированы', file=open('res.txt', 'w', encoding='utf-8'))
                    return
            elif char in UNARY:
                quotes += 1
    if len(parr_list) != 0:
        print('Разделители не сбалансированы', file=open('res.txt', 'w', encoding='utf-8'))
        return
    if quotes % 2 != 0:
        print('Разделители не сбалансированы', file=open('res.txt', 'w', encoding='utf-8'))
        return
    print('Разделители сбалансированы', file=open('res.txt', 'w', encoding='utf-8'))


def getLines(file):
    with open(file) as f:
        return f.readlines()

if __name__ == '__main__':
    main('file.txt')