import csv
from glob import glob
import os

import my_logger 
import null_patch


def main():
#************************************************************************
# 
# チャンネルを確認して、指定した値である場合は指定した範囲をNullにする
#
#  →　下の設定値を入力して「python app.py」で実行
# 
#************************************************************************
    # settings[0]：確認するチャンネル
    # settings[1]：チャンネルの値（この値と等しいとき、指定範囲にnullを挿入）
    # settings[2]：settings[0]から何個Nullにするのかを指定
    lg = my_logger.get_logger(__name__, 'errlog.txt')
    act_flg = True
    settings = []
    try:
        setting_csv_url = glob(f'setting.csv')
        csv_file = open(setting_csv_url[0], "r", encoding="utf-8", errors="", newline="" )
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        next(f)
    except:
        act_flg = False
        lg.debug('You should create setting.csv')
    
    try:
        for row in f :
            cnf_ch      = int(row[0])
            check_value = int(row[1])
            null_num    = int(row[2])
            settings += [[cnf_ch,check_value,null_num]]
    except:
        act_flg = False
        lg.debug('Please confirm setting.csv')
    
    #案件情報
    try:
        info_csv_url = glob(f'info.csv')
        csv_file = open(info_csv_url[0], "r", encoding="utf-8", errors="", newline="" )
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        next(f)
        info = f
    except:
        act_flg = False
        lg.debug('You should create info.csv')



    #案件情報
    try:
        for row in info:
            FL_ID = row[0]
            password = row[1]
            offset = int(row[2])
    except:
        act_flg = False
        lg.debug('Please confirm setting.csv')

    #ここにcsvがあるディレクトリを指定
    folder = glob(os.getcwd()+'\data')
    if len(folder) == 0:
        act_flg = False
        lg.debug('You should create "data" folder here')
    
    if act_flg: 
        lg.debug('"setting.csv","info.csv" check OK.')
        try:
            null_patch.main(folder[0],settings,offset,FL_ID,password)
            lg.debug('null patch done')
        except:
            lg.debug('"null_patch" act error')
            lg.debug('Please confirm target csv in data_folder')

if __name__=="__main__":
    main()