#! /usr/bin/env python
# -*- coding: utf-8 -*-
''' calculator '''

def calsubexp(exp):
    ''' calculate expression inside () '''
    start = 0
    op_list = ['-', '+', '*', '/']
    for index, this_opchar in enumerate(exp): #2-10*1*2--1
        if this_opchar in op_list:
            if (this_opchar == '-' and exp[index - 1] in op_list) or (index == 0):
                continue
            op_num1 = exp[start:index]
            extra_exp = exp[index + 1:]
            op_num2 = get_opnum2(extra_exp, op_list)
            if op_num2 == '':
                raise ValueError
            next_opchar = exp[index + 1 + len(op_num2):index + 1 + len(op_num2) + 1]
            is_next_opchar_low = next_opchar == '+' or next_opchar == '-' or next_opchar == ''
            is_this_opchar_hig = this_opchar == '*' or this_opchar == '/'
            if is_next_opchar_low or is_this_opchar_hig:
                fresult = calculate(this_opchar, op_num1, op_num2)
                exp = exp[:start] + str(fresult) + exp[index + 1 + len(op_num2):]
                break;
            start = index + 1
    if get_opnum2(exp, op_list) == exp:
        return exp
    else:
        return calsubexp(exp)
def clear_bracket(exp=''):
    '''clear bracket'''
    print exp
    try:
        localz = exp.find(')')
        if localz == -1:
            return calsubexp(exp)
        locala = exp[:localz].rfind('(')
        subexp = exp[locala + 1:localz]
        # calculate brackte value
        bvalue = calsubexp(subexp)
        # relpace bvalue
        suba = exp[:locala]
        subz = exp[localz + 1:]
        newexp = suba + str(bvalue) + subz
        return clear_bracket(newexp)
    except ValueError:
        print 'Invailed expression!Please check it again!'
def get_opnum2(extra_exp, op_list):
    ''' get opnum2 '''
    num2 = ''
    for index, char in enumerate(extra_exp):
        if index == 0 or char not in op_list:
            num2 = num2 + char
        else:
            return num2
    return num2
def calculate(opchar, op1, op2):
    ''' calculate '''
    if op1[0] == '+' or op2[0] == '+':
        raise ValueError
    fop1 = float(op1)
    fop2 = float(op2)
    if   opchar == '*':
        return fop1 * fop2
    elif opchar == '/':
        return fop1 / fop2
    elif opchar == '+':
        return fop1 + fop2
    else:
        return fop1 - fop2

print clear_bracket('-10-1*(2-10*1*2.12-*-1)/(11+4)/+2')
