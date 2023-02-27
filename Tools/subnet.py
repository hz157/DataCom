#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ Project: Network Small Tools
# @ File: subnet
# @ Time: 27/2/2023 下午7:35
# @ Author: hz157
# @ Github: https://github.com/hz157

import ipaddress

def subnetCalculation(address: str, subnet_mask: str):
    if len(subnet_mask) == 2 or len(subnet_mask) == 1:
        try:
            # 输入子网掩码长度
            length = int(subnet_mask)
            # 计算子网掩码
            subnet_mask = (0xffffffff >> (32 - length)) << (32 - length)
            # 将子网掩码转换为点分表示
            subnet_mask = ipaddress.IPv4Address(subnet_mask).exploded
        except Exception as e:
            print(e)
    try:
        # 将IP地址和子网掩码转换为IP地址对象和网络对象
        ip = ipaddress.IPv4Address(address)
        net = ipaddress.IPv4Network(address + '/' + subnet_mask, False)
        # 计算网络范围
        network_range = str(net[0]) + '-' + str(net[-1])
        # 计算广播地址
        broadcast_address = str(net.broadcast_address)
        # 计算网络地址
        network_address = str(net.network_address)
        # 计算默认网关
        gateway = str(net[1])
    except Exception as e:
        print(e)
    
    return {'IP地址': str(ip),
            '网络范围': network_range,
            '广播地址': broadcast_address,
            '网络地址': network_address,
            '默认网关(可自定义)': gateway}


# Sample
# if __name__ == '__main__':
#     print(subnetCalculation('192.168.0.100','255.255.255.0'))