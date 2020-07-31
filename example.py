# -*- coding: utf-8 -*-
import gspeech
import time
from session import order


def counter(numStr):
    numDic = {
        '한': 1,
        '두': 2,
        '세': 3,
        '네': 4,
        '다섯': 5,
        '여섯': 6,
        '일곱': 7,
        '여덟': 8,
        '아홉': 9,
        '열': 10
    }
    return numDic[numStr]


def parse(stt):
    i = 0
    stt = stt.split()
    print(stt)
    for s in stt:
        if '에서' in s:
            i = stt.index(s)
    store = stt[i].replace('에서', '')
    detail_address = stt[i+1].replace('으로', '')
    menu_ordered = stt[i+2]
    n = stt.index('개')
    quantity = counter(stt[n-1])
    for l in range(i+3, n-1):
        menu_ordered += stt[l]

    return {'store': store, 'detail_adr': detail_address, 'menu_ordered': menu_ordered, 'quantity': quantity}


def main():
    gsp = gspeech.Gspeech()
    stt_list = []
    while True:
        # 말하면 음성인식되는 순간 stt에다가 문자열 형태로 담는다
        stt = gsp.getText()

        if stt is None:
            break
        elif stt == '메로나':
            print('주문을 말씀하세요.')
        else:
            adrs1 = "고려대학교안암캠퍼스"
            ordered = parse(stt)

            store = ordered['store']
            detailAdr = ordered['detail_adr']
            menu = ordered['menu_ordered']
            quantity = ordered['quantity']

            order(adrs1, store, detailAdr, menu, quantity)
        print(stt)
        time.sleep(0.01)
        if ('메로나 그만' in stt):
            break


main()
