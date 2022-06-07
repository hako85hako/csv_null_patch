import os
import csv
from glob import glob

#************************************************************************
# チャンネルを確認して、指定した値である場合は指定した範囲をNullにする
#************************************************************************
def main(folder,settings,offset,FL_ID,password):
    data = []
    #編集用パス指定
    csv_paths = glob(f'{folder}/*.csv')
    for csv_path in csv_paths:
        dirname = os.path.basename(csv_path)
        dirname_year = dirname[17:21]
        dirname_month = dirname[22:24]
        dirname = FL_ID + '_' + dirname_year + '-' + dirname_month + '-01'
        try:
            #csv読み込み
            f = open(csv_path, 'r')
        except:
            #return frame.show_error(not_read_file)
            return print("not_read_file")
        #headerの取得
        header = next(f)
        #リスト形式
        f = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        #listの個数分forを回す
        data = []
        for row in f:
            #結果の入子
            items = []
            try:
                for i in range(int(offset)):
                    if i == int(offset) :
                        item = row[i]
                        items += [item]
                        break
                    else:
                        item = row[i]
                        items += [item]
            except:
                return print("offset_write_error")
            for setting in settings:
                buff = []
                try:
                    check_chanel = int(row[(offset)+setting[0]])
                except:
                    check_chanel = "null"
                if check_chanel == setting[1]:
                    for j in range(setting[2]):
                        if j == 0 :
                            item = 0
                        else:
                            item = "null"
                        buff += [item]
                else :
                    for j in range(setting[2]):
                        item = row[setting[0] + offset + j]
                        buff += [item]
                items += buff
            data += [items]
        try:
            data.insert(0, [FL_ID,password])
            #nullpatch_dir = folder+'/nullpatch/'
            nullpatch_dir = os.getcwd()+'/nullpatch/'
            makedirs(nullpatch_dir)
            path = nullpatch_dir + dirname+'.csv'
            f = open(path, 'w',newline="")
            writer = csv.writer(f)
            writer.writerows(data)
        except:
            return print("faile_write_file")
        finally:
            f.close()


def makedirs(nullpatch_dir):
    if not os.path.isdir(nullpatch_dir):
        os.makedirs(nullpatch_dir)

