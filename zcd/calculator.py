''' calcutor '''
#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calsubexp(exp):
    ''' calculate expression '''
    if exp.startswith('-'):
        exp = '0' + exp
    start = 0
    exp_new = ''
    this_opchar = ''
    next_opchar = ''
    op_num1 = ''
    op_num2 = ''
    fresult = 0
    op_list = ['-', '+', '*', '/']
    for index, char in enumerate(exp):
        if char in op_list:
            if char == '-' and exp[index - 1] in op_list:
                continue
            this_opchar = char
            if op_num1 == '':
                op_num1 = exp[start:index]
            else:
                op_num2 = exp[start:index]
                next_opchar = exp[index:index + 1]
            start = index + 1
            if op_num1 != '' and op_num2 != '':
                is_next_opchar_low = next_opchar == '+' or next_opchar == '-'
                is_this_opchar_hig = this_opchar == '*' or this_opchar == '/'
                if is_next_opchar_low or is_this_opchar_hig:
                    fresult = calculate(this_opchar, op_num1, op_num2)
                    op_num1 = ''
                    op_num2 = ''
                    exp_new = exp_new + str(fresult)
                else:
                    pass
        else:
            pass
    return exp_new
def clear_bracket(exp=''):
    '''clear bracket'''
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

def calculate(opchar, op1, op2):
    ''' calculate '''
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

clear_bracket('-10-1*(2-1)*(11+4)')
