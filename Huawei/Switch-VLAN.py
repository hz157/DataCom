# 华为交换机 VLAN 配置命令 Excel批量生成脚本
# Huawei Switch Vlan config command for Excel batch generation script
# Last Edit : 2022-07-18

import xlrd2

# 端口模式命令
mode_command = {"trunk":"port link-type trunk","access":"port link-type access"}
# VLAN 通行命令
allow_vlan = {"access":"port default vlan ","trunk":"port trunk allow-pass vlan "}

tables = []

# EXCEL表格读取
def import_excel(excel):
    for rown in range(excel.nrows):
        array = {'interface':'','mode':'','vlan':''}
        array['interface'] = table.cell_value(rown,0)
        array['mode'] = table.cell_value(rown,1)
        array['vlan'] = table.cell_value(rown,2)
        tables.append(array)

# 命令生成
def wirte_text(input_path):
    for i in tables:
        with open(input_path,"a") as f:
            # 接口名称
            f.write("interface " + i['interface'] + "\n")
            # 接口模式
            if i['mode'] == "" :
                f.write(mode_command['access'] + "\n")
            else:
                f.write(mode_command[i['mode']] + "\n")
            # VLAN ID
            if i['vlan'] != "" and i['mode'] != "":
                f.write(allow_vlan[i['mode']] + i['vlan'] + "\n")


# 程序入口
if __name__=='__main__':
    path = input("EXCEL文件路径：\n")
    data = xlrd2.open_workbook('C:/Users/horizon/Desktop/1.xlsx')
    table = data.sheets()[0]
    import_excel(table)
    path = input("命令输出路径：\n")
    wirte_text(path)
    for i in tables:
        print(i)






