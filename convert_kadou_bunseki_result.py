import time

def main():
    file_name = input('稼働分析ログのファイル名(拡張子まで含む)入力 -->')
    threshold = input('保存時に改行させたい閾値(DM)を入力 -->')
    threshold_f = float(threshold)
    converted_lst = []

    with open(file_name, mode='r') as f:
        texts_all = f.readlines()
        i = -1
        for texts in texts_all:
            temp_lst = texts.split(',')
            if float(temp_lst[1]) > threshold_f:
                i += 1
                converted_lst.append('')
            converted_lst[i] += temp_lst[1] + ','

    print(f'サイクル数は {i+1} 回でした')

    with open('Conv' + file_name, mode='w') as fw:
        for texts in converted_lst:
            fw.write(texts + '\n')

if __name__ == '__main__':
    main()
