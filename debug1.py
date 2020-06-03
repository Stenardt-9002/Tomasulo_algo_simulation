# import re
# import Hardware1 as Hfiel
# txtparse = ""
# with open("textinout.txt","r") as f:
#     txtparse = f.read()
#
# # print(txtparse)
# pattern = re.compile(r'(\d{4}) (.*)\n?')
# matchiter = pattern.finditer(txtparse)
# # print(matchiter)
# opc_odes1 = []
# res_tothe1rinputs = []
# res_totherinputs = []
#
# for iter in matchiter:
#     # print(iter.group(1),iter.group(2))
#     opc_odes1.append(iter.group(1))
#     res_tothe1rinputs.append(iter.group(2))
#
# # print(opc_odes1)
# # print(res_tothe1rinputs)
# for i in res_tothe1rinputs:
#     # print(i.split(" "))
#     temp_listtemp = []
#     for i12 in i.split(","):
#         temp_listtemp.append(i12.strip()) #removes spaces
#         pass
#
#
#     res_totherinputs.append(temp_listtemp)
#     pass
# # print(res_totherinputs)
#
# # print(Hfiel.STORE_HARDWARE)
# #ADD accordingly Hardware1.py file (number of buffers)
# register_Status = {'F1' :0,'F2' :0,'F3' :0,'F4' :0,'F5' :0,'F6' :0,'F7' :0,'F8' :0,'F9' :0,'F10' :0,'F11' :0,'F12' :0,'F13' :0,'F14' :0,'F15' :0,'F16' :0}
#
# reservation_Station = {'ADD_N' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},
# 'ADD_W_C' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'SUB_N' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'SUB_B' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'MUL_T' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'FP_ADDER' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'FP_SUB' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'FP_MUL' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'HALT' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'REGISTER_COMPLEMENT' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'LOG_XOR' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'LOG_NAND' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'SHIFT_RIGHT' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'SHIT_LEFTF' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'STORE' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'LOAD1' :{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}}
#
#
#
# ##CHCK ALL res_totherinputs registers are valid or not
# for ivar in range(len(res_totherinputs)):
#     for regvar in res_totherinputs[ivar]:
#         if regvar not in register_Status.keys() and opc_odes1[ivar]!="1000":#not halt
#             # if((int)(regvar)):
#             if regvar.isdigit():
#                 pass
#             else:
#                 print("Reached invalid syntax")
#                 print(res_totherinputs[ivar])
#                 # raise("Invalid Syntax Error")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # register_Status : {'ADD_N' ={'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},
# # 'ADD_W_C' =0,'SUB_N' =0,'SUB_B' =0,'MUL_T' =0,'FP_ADDER' =0,'FP_SUB' =0,'FP_MUL' =0,'HALT' =0,'REGISTER_COMPLEMENT' =0,'LOG_XOR' =0,'LOG_NAND' =0,'SHIFT_RIGHT' =0,'SHIT_LEFTF' =0,'STORE' =0,'LOAD1' =0}
# # pieplined_Cases = {}
# CLOCK_VAR = 0
#
# # for in1 in reservation_Station:
# #     print(in1,reservation_Station[in1]['busy'])
#
# instruction_status = Hfiel.add_instruction_status(opc_odes1)
#
#
# # print(instruction_status)
#
#
#
# def completed_fuc(reser_sta):
#     pass
#
#
#
#
#
#
# queue_oper = []
# for operations in range(len(opc_odes1)):
#     queue_oper.append(operations)
#
#
# LENTH_OFINSTRUCTION_STATUS = len(opc_odes1)
#
#
#
# LATEST_OPERATION_ENTERED = 0
# completed_VAR = True
# operation_queue = False
# #this while loop will run until queued operations are emptied
# while completed_VAR:
#
#     #check if issue available for the queued operation and less than length of no of operations
#     if True:
#         LATEST_OPERATION_ENTERED+=1
#         print(LATEST_OPERATION_ENTERED)
#
#     #check which opcode
#
#         if opc_odes1[LATEST_OPERATION_ENTERED-1]=="0000":
#             # addition  ADD_N
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success ADD_N")
#
#
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#
#
#
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="0001":
#             #additon with carry 'ADD_W_C'
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#
#
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="0010":
#             # subtraction normal SUB_N
#
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 print("Success")
#                 # no of operands are correct
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#
#
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="0011":
#             #subtraction with borrow SUB_N
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="0100":
#             #multiplication MUL_T
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="0101":
#             # floating point adder 'FP_ADDER'
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="0110":
#             # floating point subtraction FP_SUB
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#
#                 pass
#
#
#
#
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="0111":
#             # floating point multiplication FP_MUL
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#
#
#
#
#
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1000":
#             # HALT STATUS  HALT
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==2:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#
#
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1001":
#             # register complemet REGISTER_COMPLEMENT
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==2:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1010":
#             # logical xor LOG_XOR
#
#
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1011":
#             # logical bit wise nand LOG_NAND
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1100":
#             # shift right SHIFT_RIGHT
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#
#
#
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1101":
#             # shift right SHIT_LEFTF
#
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==3:
#                 print("Success")
#                 # no of operands are correct
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1110":
#             # store STORE
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==2:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#         elif opc_odes1[LATEST_OPERATION_ENTERED-1]=="1111":
#             # load LOAD1
#             if len(res_totherinputs[LATEST_OPERATION_ENTERED-1])==2:
#                 # no of operands are correct
#                 print("Success")
#
#                 pass
#
#
#             else:
#                 # error in parsing
#                 pass
#
#
#     CLOCK_VAR+=1
#
#     print(instruction_status[0]['issue'])
#     # print(reservation_Station[instruction_status[0]['issue']]['busy'])
#
#
#
#
#
#     completed_VAR = False






























































































































#
#
# reservation_Station = {'ADD_N' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},
# 'ADD_W_C' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'SUB_N' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'SUB_B' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'MUL_T' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'FP_ADDER' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'FP_SUB' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'FP_MUL' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'HALT' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'REGISTER_COMPLEMENT' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'LOG_XOR' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'LOG_NAND' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'SHIFT_RIGHT' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'SHIT_LEFTF' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'STORE' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}},'LOAD1' :{'ex':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'is':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0},'wb':{'busy':0,'op':0,'vj':0,'vk':0,'qj':0,'qk':0}}}
#
# for keys in reservation_Station:
#     print(reservation_Station[keys]['ex'])




































































































































#
# import sys
# import re
# import time
# import Hardware1 as Hfiel
# from os import system, name
#
# HALTOPCODE = -1
# def clear():
#
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
#
#     else:
#         _ = system('clear')
#
# clear()
# print("Enter commands in textinout.txt file as specified in format in README")
# simulate = input("Enter\"yes\" if you want simulation else get final answer \n")
#
# txtparse = ""
# with open("textinout.txt","r") as f:
#     txtparse = f.read()
#
# # print(txtparse)
# strings1 = txtparse.split("\n")
# strings1.remove('')
# try:
#     HALTOPCODE = strings1.index('1000')
# except:
#     HALTOPCODE = -1
# # print(strings1,HALTOPCODE)
# pattern = re.compile(r'(\d{4}) (.*)\n?')
# matchiter = pattern.finditer(txtparse)
# # print(matchiter)
# opc_odes1 = []
# res_tothe1rinputs = []
# res_totherinputs = []
#
# for iter in matchiter:
#     # print(iter.group(1),iter.group(2))
#     opc_odes1.append(iter.group(1))
#     res_tothe1rinputs.append(iter.group(2))
#
# # print(opc_odes1)
# # print(res_tothe1rinputs)
# for i in res_tothe1rinputs:
#     # print(i.split(" "))
#     temp_listtemp = []
#     for i12 in i.split(","):
#         temp_listtemp.append(i12.strip()) #removes spaces
#         pass
#
#
#     res_totherinputs.append(temp_listtemp)
#     pass
# # print(res_totherinputs)
# # print(opc_odes1)
# if HALTOPCODE!=-1:
#     opc_odes1 = opc_odes1[:HALTOPCODE]+["1000"]+opc_odes1[HALTOPCODE:]
#     temp1 = res_totherinputs[:HALTOPCODE]
#     temp1.append([])
#     temp2 = res_totherinputs[HALTOPCODE:]
#     res_totherinputs = temp1+temp2
#
# # print(res_totherinputs)
# # print(opc_odes1)
#
#
# temp_ereg = ["R1","R2","R3","R4","R5"]
# # print(Hfiel.STORE_HARDWARE)
# #ADD accordingly Hardware1.py file (number of buffers)
# register_Status = {'F1' :0,'F2' :0,'F3' :0,'F4' :0,'F5' :0,'F6' :0,'F7' :0,'F8' :0,'F9' :0,'F10' :0,'F11' :0,'F12' :0,'F13' :0,'F14' :0,'F15' :0,'F16' :0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0}
#
# reservation_Station = {'ADD_N' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},
# 'ADD_W_C' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'SUB_N' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'SUB_B' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'MUL_T' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'FP_ADDER' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'FP_SUB' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'FP_MUL' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'HALT' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'REGISTER_COMPLEMENT' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'LOG_XOR' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'LOG_NAND' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'SHIFT_RIGHT' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'SHIT_LEFTF' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'STORE' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}},'LOAD1' :{'ex':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytowrite':0},'is':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0,'readytoexec':0},'wb':{'busy':0,'op':-1,'vj':0,'vk':0,'qj':0,'qk':0}}}
#
#
# ##CHCK ALL res_totherinputs registers are valid or not
# for ivar in range(len(res_totherinputs)):
#     for regvar in res_totherinputs[ivar]:
#         if regvar in temp_ereg:
#
#             print("Reached invalid syntax")
#             print("Cannot use this name of variable")
#             print(res_totherinputs[ivar])
#             sys.exit(0)
#             # raise("Invalid Syntax Error")
#
#         if regvar not in register_Status.keys() and opc_odes1[ivar]!="1000" :#not halt
#             # if((int)(regvar)):
#             # print(regvar)
#
#
#             if regvar.isdigit():
#                 pass
#             else:
#
#                 print("Reached invalid syntax")
#                 print(res_totherinputs[ivar])
#                 sys.exit(0)
#                 # raise("Invalid Syntax Error")
#
#
# CLOCK_VAR = 0
#
# map_table = {} #for placement #orignal name register to renamed register ,operations reading it
#
# # map_table_WAW = {}
# RAISEEXCEPTION = []
#
#
# get_hardwareused_list = []
# instruction_status ,get_hardwareused_list= Hfiel.add_instruction_status(opc_odes1)
#
#
# # print(instruction_status)
# # check_War Hazard
# def check_War(reservation_Station,registername,opcodereceived):
#
#
#     #check for WAW ;correct this when creating WAW function
#     if registername in map_table.keys():
#         stringappend =  str(registername)+ " is already renamed for instruction "+ str(opcodereceived)
#         RAISEEXCEPTION.append(stringappend)
#         return [False]
#
#
#     getlist_ofoperationthatarereading = []
#     for keys1 in reservation_Station.keys():
#         for stagespipeline in reservation_Station[keys1].keys():
#             if reservation_Station[keys1][stagespipeline]['vk'] == registername or reservation_Station[keys1][stagespipeline]['vj'] == registername:
#                 # if reservation_Station[keys1][stagespipeline]['vk'] == registername:
#                 #
#                 #     pass
#                 # if reservation_Station[keys1][stagespipeline]['vj'] == registername:
#                 #     pass
#                 if opcodereceived>reservation_Station[keys1][stagespipeline]['op']:
#                     getlist_ofoperationthatarereading.append(reservation_Station[keys1][stagespipeline]['op'])
#                 # for placement in temp_ereg:
#                 #     if register_Status[placement]==0:
#                 #         return True,placement,opcodereceived
#
#                 # return the name of placeholder register
#
#     # if no one is reading it
#     if getlist_ofoperationthatarereading == []:
#         return [True]
#
#     #get empty register as placement
#     getlist_ofoperationthatarereading = list(set(getlist_ofoperationthatarereading))
#     for placement in temp_ereg:
#         if register_Status[placement]==0:
#
#             return [True,placement,getlist_ofoperationthatarereading,opcodereceived]
#
#
#     # if no placement is available then stall
#     RAISEEXCEPTION.append("No Free registers are available to rename it")
#     return [False]
#
#
#
#
# def completed_fuc(reser_sta):
#     for i in reser_sta:
#         if i['completed_yet'] != -1:
#             return False
#     print("Done With Excecution of program")
#     return True
#
# # check_Waw(register_Status,map_table_WAW,res_totherinputs[trarvar][0])
# def check_Waw(register_Status,map_table1,regster_name):
#     reg_name_key = ""
#     if register_Status[regster_name] == 0:
#         # mean register is available that mean no problem
#         return [True]
#     if regster_name in map_table.keys():
#         stringappend =  str(regster_name)+ " is already renamed "
#         RAISEEXCEPTION.append(stringappend)
#
#         return [False]
#         pass
#
#     if register_Status[regster_name]!=0:
#         # print("register DEBUG2")
#         if regster_name not in map_table1.keys():
#             #mean not already renamed
#             # print("debug3",regster_name)
#
#             # find name of register not occupied
#             for keys1 in temp_ereg:
#                 if register_Status[keys1]==0:#register available
#                     reg_name_key = keys1
#                     break
#
#
#         # busy
#
#     if reg_name_key == "":
#         #no free register available thus stall
#         return [False]
#
#     return [True,reg_name_key]
#
#
# LENTH_OFINSTRUCTION_STATUS = len(opc_odes1)
#
# SELECTED_OPERANDS_LIST  = ["1000","1001","1110","1111"]
#
# LATEST_OPERATION_ENTERED = 0
# completed_VAR = True
# operation_queue = False
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #this while loop will run unti
#
# # print(opc_odes1)
# while completed_VAR:
#
#
#     CLOCK_VAR+=1
#
#     for trarvar in range(LENTH_OFINSTRUCTION_STATUS):
#         # print((type)(opc_odes1[trarvar]))
#
#         if trarvar>=CLOCK_VAR:
#             #break for loop
#             break
#         elif opc_odes1[trarvar] in SELECTED_OPERANDS_LIST:
#             if opc_odes1[trarvar]=="1000":
#                 # HALT
#                 clear()
#                 print("reached")
#                 completed_VAR = False #program halted
#                 RAISEEXCEPTION.append("HALT encountered, program HALTED")
#                 # sys.exit("Program Halted ")
#                 # for load store complement
#
#             else:
#                 #issue
#
#
#
#                 if instruction_status[trarvar]['started'] == 0:
#
#                     continue_WAW_var_allowed = True
#                     continue_WAR_var_allowed = True
#                     continue_WAR = check_War(reservation_Station,res_totherinputs[trarvar][0],trarvar) #which register name and operation
#                     continue_WAR_var_allowed = continue_WAR[0]
#                     # if #renamed by WAR function
#
#
#
#
#                     if len(continue_WAR)==4:
#                         #renamed by WAR method
#                         # if register_Status[res_totherinputs[trarvar][0]]!=0:#the register is not free
#                         #     map_table_WAW[res_totherinputs[trarvar][0]] = continue_WAR[1] #map new reg name in WAW table
#                         #     continue_WAW_var_allowed = True #allowed
#                         if continue_WAR[0]:#renamed
#                             continue_WAW_var_allowed = True
#                             continue_WAW = []
#                             pass
#
#                     else:
#                         continue_WAW = check_Waw(register_Status,map_table,res_totherinputs[trarvar][0])
#                         continue_WAW.append(trarvar)#added
#                         continue_WAW_var_allowed = continue_WAW[0]
#
#                         # continue_WAR = [True]#define var
#
#
#                         ## DEBUG:
#                         # if trarvar ==1 :
#                         #     print("DEBUGAY")
#                         #     print(continue_WAW)
#
#                     if continue_WAR_var_allowed and continue_WAW_var_allowed:#allowed register renaming
#                         # print("DEBUGE2")
#                         if len(continue_WAR)==4:
#                             map_table[res_totherinputs[trarvar][0]] = [continue_WAR[1],continue_WAR[2],continue_WAR[3]]#new name and the list of read operation that new to be completed bfore write
#                             #new reg
#                         elif len(continue_WAW)==3:
#                             map_table[res_totherinputs[trarvar][0]] = [continue_WAW[1],trarvar]
#                             # print("DEBIG5",continue_WAW)
#                             # print("DEBIG6",continue_WAR)
#
#                             pass
#                         # # if len(continue_WAW)==3:
#                         #     pass
#                         # f a matching functional unit is available, issue the instruction.
#
#                         if reservation_Station[instruction_status[trarvar]['key']]['is']['busy'] ==0 :# issue is not busy   then can only be issue done and writing register is free
#                             if register_Status[res_totherinputs[trarvar][0]]==0 or (res_totherinputs[trarvar][0] in map_table.keys() and  len(map_table[res_totherinputs[trarvar][0]])==2  and trarvar>=map_table[res_totherinputs[trarvar][0]][1] ) :
#                                 # and trarvar>map_table[res_totherinputs[trarvar][0]][1]
#                                     # print("DEBUG!Q")
#
#                                 instruction_status[trarvar]['started'] = 1
#                                 instruction_status[trarvar]['issue'] = CLOCK_VAR
#                                 instruction_status[trarvar]['completed_yet'] -= 1
#
#                                 #declare hardware busy
#                                 # reservation_Station[res_totherinputs[trarvar]] = [instruction_status[trarvar]['key'],trarvar]
#                                 #save register in which is has to write
#                                 # if new register available
#                                 if len(continue_WAR)==4:
#                                     register_Status[continue_WAR[1]] = [instruction_status[trarvar]['key'],trarvar]
#                                 elif len(continue_WAW)==3:
#                                     # print("DEBIG6")
#                                     register_Status[continue_WAW[1]] = [instruction_status[trarvar]['key'],trarvar]
#                                     pass
#
#                                 else:
#                                     register_Status[res_totherinputs[trarvar][0]] = [instruction_status[trarvar]['key'],trarvar]
#
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['busy'] = 1 #now busy
#
#
#
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['op'] = trarvar
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['readytoexec'] = 1
#                                 # reservation_Station[instruction_status[trarvar]['key']]['busy']
#
#
#
#
#
#
#                                 if res_totherinputs[trarvar][1].isdigit()==False:
#
#                                     if register_Status[res_totherinputs[trarvar][1]] == 0: #register available
#
#                                         reservation_Station[instruction_status[trarvar]['key']]['is']['vj'] = res_totherinputs[trarvar][1] #the name of register which is available
#                                         reservation_Station[instruction_status[trarvar]['key']]['is']['qj'] = 0 #no one has occupied it
#                                         # reservation_Station[instruction_status[trarvar]['key']]['vj'].append(res_totherinputs[trarvar][1]) #the name of register which is available
#                                         # reservation_Station[instruction_status[trarvar]['key']]['qj'].append(0)  #no one has occupied it
#                                         # register renamed
#                                         if res_totherinputs[trarvar][1] in map_table.keys():
#                                             if len(map_table[res_totherinputs[trarvar][1]])==3:
#                                                 if trarvar in map_table[res_totherinputs[trarvar][1]][1]:
#                                                     reservation_Station[instruction_status[trarvar]['key']]['is']['vj'] = map_table[res_totherinputs[trarvar][1]][0] #the name of register which is available
#                                                     reservation_Station[instruction_status[trarvar]['key']]['is']['qj'] = 0 #no one has occupied it
#
#                                                 pass
#                                             pass
#
#                                     else:
#                                         # reservation_Station[instruction_status[trarvar]['key']]['vj'].append(0) #nothing means hardare is not free
#                                         # reservation_Station[instruction_status[trarvar]['key']]['qj'].append(register_Status[res_totherinputs[trarvar][1]][1])  #which operation except that operation no one else can access this
#                                         # check
#                                         reservation_Station[instruction_status[trarvar]['key']]['is']['vj'] = 0 #nothing means hardare is not free
#                                         reservation_Station[instruction_status[trarvar]['key']]['is']['qj'] = register_Status[res_totherinputs[trarvar][1]][1]  #which operation except that operation no one else can access this
#
#
#                                 # else if digit then none of our concern
#
#
#
#
#                 else:
#                     #writeback stage
#                     if instruction_status[trarvar]['completed_yet'] ==1:
#                         print("DEBUGREACHED HERE1")
#
#
#                         # execution to writeback
#                         reg1 = res_totherinputs[trarvar][1]
#
#                         if reg1.isdigit()==False:
#                             if (isinstance((register_Status[res_totherinputs[trarvar][1]]),list)):
#                                 # add WAR HAZARD renaming
#
#                                 temp_passvar = (register_Status[res_totherinputs[trarvar][1]][1]==trarvar)
#
#
#                             else :
#                                 if (isinstance((register_Status[res_totherinputs[trarvar][1]]),int)):
#                                     temp_passvar = (register_Status[res_totherinputs[trarvar][1]]==0)
#
#
#
#                             # Check WAR Hazard and register renaming access for register who are allowed to read it
#
#
#                             if (reg1 in map_table.keys()):
#                                 if len(map_table[reg1])==3:
#
#                                     temp_passvar2 = trarvar in map_table[reg1][1]#list of operations allowed
#                                     temp_passvar = (temp_passvar2 and temp_passvar)
#
#
#                                     if temp_passvar2==False:#first renamed register
#                                         if isinstance(register_Status[map_table[reg1][0]],list):
#
#                                             temper1 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1) #means renamed reg are done
#                                             # temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]==-1 #means renamed reg are done
#                                             temp_passvar = (temper1 and temp_passvar)
#
#
#                                 elif len(map_table[reg1])==2:
#                                     if isinstance(register_Status[map_table[reg1][0]],list) :
#
#                                         temp_passvar2 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1)#means renamed register are done
#                                         temp_passvar = temp_passvar and temp_passvar2
#
#
#
#                         else:
#                             temp_passvar = True
#                             pass
#
#
#
#
#
#
#
#                         # check whether writing register new register renamed can handle same operation
#                         if isinstance(register_Status[res_totherinputs[trarvar][0]],int):
#
#                             #check if not renamed
#
#
#                             if res_totherinputs[trarvar][0] in map_table.keys():
#                                 # the register is being used and renamed and being written on
#                                 # temp_passvar123 = map_table
#
#                                 # renamed for WAR
#                                 if len(map_table[res_totherinputs[trarvar][0]])==3:
#                                     if register_Status[map_table[res_totherinputs[trarvar][0]][0]][1]==trarvar:
#                                         temp_passvar = temp_passvar and True
#
#                                     else:
#                                         temp_passvar = temp_passvar and False
#
#                                 elif len(map_table[res_totherinputs[trarvar][0]])==2:
#                                     if map_table[res_totherinputs[trarvar][0]][1] == trarvar:
#                                         temp_passvar = temp_passvar and True
#
#                                         pass
#                                     else:
#                                         temp_passvar = temp_passvar and False
#
#                             # else:
#                             #     case is not possible
#
#
#                         elif isinstance(register_Status[res_totherinputs[trarvar][0]],list):
#                             if register_Status[res_totherinputs[trarvar][0]][1]==trarvar:
#                                 temp_passvar = temp_passvar and True
#                                 pass
#                             else:
#                                 temp_passvar = temp_passvar and False
#                                 pass
#
#
#
#                         #check WAW renaming
#
#
#                         if temp_passvar :
#                             print("DEBUGE2")
#                             if ((isinstance(register_Status[res_totherinputs[trarvar][0]],list)) and (register_Status[res_totherinputs[trarvar][0]][1]==trarvar)) or (isinstance(register_Status[res_totherinputs[trarvar][0]],int) and ( register_Status[map_table[res_totherinputs[trarvar][0]][0]][1]==trarvar  )):
#
#
#
#
#                                 if reservation_Station[instruction_status[trarvar]['key']]['wb']['busy'] == 1 and reservation_Station[instruction_status[trarvar]['key']]['wb']['op']==trarvar:#only that hardware
#                                     #hardware is fre
#                                     # print("DEBUGREACHED HERE")
#
#                                     instruction_status[trarvar]['writeback'] = CLOCK_VAR
#                                     instruction_status[trarvar]['completed_yet'] -= 1
#
#
#
#
#                         # #writeback
#                         # if register_Status[res_totherinputs[trarvar][1]]==0 and register_Status[res_totherinputs[trarvar][2]]==0:
#                         #
#                         #     instruction_status[trarvar]['issue'] = CLOCK_VAR
#                         #     instruction_status[trarvar]['completed_yet'] -= 1
#                         #
#                         #
#                         #
#                         #     register_Status[res_totherinputs[trarvar][0]] = 0 # hardware is completed and freed
#
#
#
#
#
#                         #excution +
#                     elif instruction_status[trarvar]['completed_yet']>0:
#                         #check is hardware not busy
#
#                         #dont allow execution if renamed register is not in list
#
#                         # instruction_status
#                         reg1 = res_totherinputs[trarvar][1]
#
#                         if reg1.isdigit()==False:
#                             if (isinstance((register_Status[res_totherinputs[trarvar][1]]),list)):
#                                 # add WAR HAZARD renaming
#
#                                 temp_passvar = (register_Status[res_totherinputs[trarvar][1]][1]==trarvar)
#
#
#                             else :
#                                 if (isinstance((register_Status[res_totherinputs[trarvar][1]]),int)):
#                                     temp_passvar = (register_Status[res_totherinputs[trarvar][1]]==0)
#
#
#
#                             # Check WAR Hazard and register renaming access for register who are allowed to read it
#
#
#
#
#
#
#                             if (reg1 in map_table.keys()):
#                                 if len(map_table[reg1])==3:
#
#                                     temp_passvar2 = trarvar in map_table[reg1][1]#list of operations allowed
#                                     temp_passvar = (temp_passvar2 and temp_passvar)
#
#
#                                     if temp_passvar2==False:#first renamed register
#                                         if isinstance(register_Status[map_table[reg1][0]],list):
#
#                                             temper1 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1) #means renamed reg are done
#                                             # temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]==-1 #means renamed reg are done
#                                             temp_passvar = (temper1 and temp_passvar)
#
#
#                                 elif len(map_table[reg1])==2:
#                                     if isinstance(register_Status[map_table[reg1][0]],list) :
#
#                                         temp_passvar2 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1)#means renamed register are done
#                                         temp_passvar = temp_passvar and temp_passvar2
#
#
#
#
#
#
#
#                         else:
#                             temp_passvar = True
#                             pass
#
#
#                         # print(trarvar,temp_passvar)
#                         if temp_passvar :
#                             # print("DEBUGE2")
#                             if (res_totherinputs[trarvar][0] in map_table.keys() and len(map_table[res_totherinputs[trarvar][0]])==2 and map_table[res_totherinputs[trarvar][0]][1] == trarvar ) or ((isinstance(register_Status[res_totherinputs[trarvar][0]],list)) and (register_Status[res_totherinputs[trarvar][0]][1]==trarvar)) or (isinstance(register_Status[res_totherinputs[trarvar][0]],int)and ( register_Status[map_table[res_totherinputs[trarvar][0]][0]][1]==trarvar  )):
#
#                                 # check if ex to
#                                 # print("fetish",temp_passvar,trarvar)
#
#
#                                 if reservation_Station[instruction_status[trarvar]['key']]['ex']['busy'] == 1 and reservation_Station[instruction_status[trarvar]['key']]['ex']['op'] == trarvar :#excution unit of hardware is free or being used by that instruction
#                                 # only if busy and is used by that instruction only and execution is available
#                                     instruction_status[trarvar]['completed_yet'] -=1
#                                     instruction_status[trarvar]['exec'] =CLOCK_VAR
#                                     # reservation_Station[instruction_status[trarvar]['key']]['exechandling'][0] = trarvar
#
#                                     # mark for write back
#                                     if instruction_status[trarvar]['completed_yet'] ==1 :
#                                         reservation_Station[instruction_status[trarvar]['key']]['ex']['readytowrite'] = 1
#
#
#                                         # free execution statement
#                                         # make case when 2 so that you free up execute state of hardware
#
#
#
#
#
#
#
#
#
#
#                     if instruction_status[trarvar]['completed_yet'] == 0:
#                         #nothing to do instruction in completed
#                         #if hardware busy due to this traverse then declare it free
#                         # free write back
#
#                         reservation_Station[instruction_status[trarvar]['key']]['wb']['busy'] = 0
#
#                         reservation_Station[instruction_status[trarvar]['key']]['wb']['op'] = -1
#                         reservation_Station[instruction_status[trarvar]['key']]['wb']['vj'] = 0
#                         reservation_Station[instruction_status[trarvar]['key']]['wb']['vk'] = 0
#                         reservation_Station[instruction_status[trarvar]['key']]['wb']['qj'] = 0
#                         reservation_Station[instruction_status[trarvar]['key']]['wb']['qk'] = 0
#                         instruction_status[trarvar]['completed_yet'] = -1
#                         #
#                         #
#                         #free hardware
#                         # free renamed hardware
#                         doubleifpor= True
#                         if res_totherinputs[trarvar][0] in map_table.keys():
#                             # print("DEBUG5 Reached",(map_table[res_totherinputs[trarvar][0]][0]))
#                             if register_Status[res_totherinputs[trarvar][0]]!=0:
#                                 if register_Status[res_totherinputs[trarvar][0]][1]==trarvar:
#                                     temmmpempstr  = "Write register done "+str(res_totherinputs[trarvar][0])
#                                     RAISEEXCEPTION.append(temmmpempstr)
#                                     register_Status[res_totherinputs[trarvar][0]]=0
#                                     doubleifpor = False
#
#
#                                 pass
#                             elif isinstance(register_Status[map_table[res_totherinputs[trarvar][0]][0]],list):
#
#                                 if register_Status[map_table[res_totherinputs[trarvar][0]][0]][1] == trarvar:
#                                     temmmpempstr  = "BUFFER TRANSFER FROM to "+str(map_table[res_totherinputs[trarvar][0]][0])+" to its original register"
#                                     RAISEEXCEPTION.append(temmmpempstr)
#                                     register_Status[map_table[res_totherinputs[trarvar][0]][0]] = 0
#                                     doubleifpor = False
#
#                         if doubleifpor:
#                             register_Status[res_totherinputs[trarvar][0]]=0
#                         # register_Status[res_totherinputs[trarvar][2]]=0
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #all instruction except 2 input
#
#
#
#
#         elif instruction_status[trarvar]['completed_yet']!=-1 : #the instruction is not done
#
#
#             # print("noton",trarvar)
#
#             if instruction_status[trarvar]['started'] == 0:
#
#                 continue_WAW_var_allowed = True
#                 continue_WAR_var_allowed = True
#                 continue_WAR = check_War(reservation_Station,res_totherinputs[trarvar][0],trarvar) #which register name and operation
#                 continue_WAR_var_allowed = continue_WAR[0]
#                 # if #renamed by WAR function
#
#
#
#
#                 if len(continue_WAR)==4:
#                     #renamed by WAR method
#                     # if register_Status[res_totherinputs[trarvar][0]]!=0:#the register is not free
#                     #     map_table_WAW[res_totherinputs[trarvar][0]] = continue_WAR[1] #map new reg name in WAW table
#                     #     continue_WAW_var_allowed = True #allowed
#                     if continue_WAR[0]:#renamed
#                         continue_WAW_var_allowed = True
#                         continue_WAW = []
#                         pass
#
#                 else:
#                     continue_WAW = check_Waw(register_Status,map_table,res_totherinputs[trarvar][0])
#                     continue_WAW.append(trarvar)#added
#                     continue_WAW_var_allowed = continue_WAW[0]
#
#                     # continue_WAR = [True]#define var
#
#
#                     ## DEBUG:
#                     # if trarvar ==1 :
#                     #     print("DEBUGAY")
#                     #     print(continue_WAW)
#
#                 if continue_WAR_var_allowed and continue_WAW_var_allowed:#allowed register renaming
#                     # print("DEBUGE2")
#                     if len(continue_WAR)==4:
#                         if res_totherinputs[trarvar][0] not in map_table.keys():
#                             map_table[res_totherinputs[trarvar][0]] = [continue_WAR[1],continue_WAR[2],continue_WAR[3]]#new name and the list of read operation that new to be completed bfore write
#                         #new reg
#                     elif len(continue_WAW)==3:
#                         if res_totherinputs[trarvar][0] not in map_table.keys():
#                             map_table[res_totherinputs[trarvar][0]] = [continue_WAW[1],trarvar]
#
#
#                         pass
#                     # # if len(continue_WAW)==3:
#                     #     pass
#                     # f a matching functional unit is available, issue the instruction.
#
#                     if reservation_Station[instruction_status[trarvar]['key']]['is']['busy'] ==0 :# issue is not busy   then can only be issue done and writing register is free
#                         if register_Status[res_totherinputs[trarvar][0]]==0 or (res_totherinputs[trarvar][0] in map_table.keys() and  len(map_table[res_totherinputs[trarvar][0]])==2  and trarvar>=map_table[res_totherinputs[trarvar][0]][1] ) :
#                             # and trarvar>map_table[res_totherinputs[trarvar][0]][1]
#                                 # print("DEBUG!Q")
#
#                             instruction_status[trarvar]['started'] = 1
#                             instruction_status[trarvar]['issue'] = CLOCK_VAR
#                             instruction_status[trarvar]['completed_yet'] -= 1
#
#                             #declare hardware busy
#                             # reservation_Station[res_totherinputs[trarvar]] = [instruction_status[trarvar]['key'],trarvar]
#                             #save register in which is has to write
#                             # if new register available
#                             if len(continue_WAR)==4:
#                                 register_Status[continue_WAR[1]] = [instruction_status[trarvar]['key'],trarvar]
#                             elif len(continue_WAW)==3:
#                                 # print("DEBIG6")
#                                 register_Status[continue_WAW[1]] = [instruction_status[trarvar]['key'],trarvar]
#                                 pass
#
#                             else:
#                                 register_Status[res_totherinputs[trarvar][0]] = [instruction_status[trarvar]['key'],trarvar]
#
#                             reservation_Station[instruction_status[trarvar]['key']]['is']['busy'] = 1 #now busy
#
#
#
#                             reservation_Station[instruction_status[trarvar]['key']]['is']['op'] = trarvar
#                             reservation_Station[instruction_status[trarvar]['key']]['is']['readytoexec'] = 1
#                             # reservation_Station[instruction_status[trarvar]['key']]['busy']
#
#
#
#
#
#
#
#
#                             if register_Status[res_totherinputs[trarvar][1]] == 0: #register available
#
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['vj'] = res_totherinputs[trarvar][1] #the name of register which is available
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['qj'] = 0 #no one has occupied it
#                                 # reservation_Station[instruction_status[trarvar]['key']]['vj'].append(res_totherinputs[trarvar][1]) #the name of register which is available
#                                 # reservation_Station[instruction_status[trarvar]['key']]['qj'].append(0)  #no one has occupied it
#                                 # register renamed
#                                 if res_totherinputs[trarvar][1] in map_table.keys():
#                                     if len(map_table[res_totherinputs[trarvar][1]])==3:
#                                         if trarvar in map_table[res_totherinputs[trarvar][1]][1]:
#                                             reservation_Station[instruction_status[trarvar]['key']]['is']['vj'] = map_table[res_totherinputs[trarvar][1]][0] #the name of register which is available
#                                             reservation_Station[instruction_status[trarvar]['key']]['is']['qj'] = 0 #no one has occupied it
#
#                                         pass
#                                     pass
#
#                             else:
#                                 # reservation_Station[instruction_status[trarvar]['key']]['vj'].append(0) #nothing means hardare is not free
#                                 # reservation_Station[instruction_status[trarvar]['key']]['qj'].append(register_Status[res_totherinputs[trarvar][1]][1])  #which operation except that operation no one else can access this
#                                 # check
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['vj'] = 0 #nothing means hardare is not free
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['qj'] = register_Status[res_totherinputs[trarvar][1]][1]  #which operation except that operation no one else can access this
#
#
#
#
#
#                             #check second register now
#                             if register_Status[res_totherinputs[trarvar][2]] == 0: #register available
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['vk'] = res_totherinputs[trarvar][2] #the name pf register which is available
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['qk'] = 0 #no one has occupied it
#                                 # reservation_Station[instruction_status[trarvar]['key']]['vk'].append(res_totherinputs[trarvar][2]) #the name pf register which is available
#                                 # reservation_Station[instruction_status[trarvar]['key']]['qk'].append(0) #no one has occupied it
#                                 if res_totherinputs[trarvar][2] in map_table.keys():
#                                     if len(map_table[res_totherinputs[trarvar][2]])==3:
#
#                                         if trarvar in map_table[res_totherinputs[trarvar][2]][1]:
#                                             reservation_Station[instruction_status[trarvar]['key']]['is']['vj'] = map_table[res_totherinputs[trarvar][2]][0] #the name of register which is available
#                                             reservation_Station[instruction_status[trarvar]['key']]['is']['qj'] = 0 #no one has occupied it
#
#                                             pass
#                                         pass
#
#                             else:
#
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['vk'] = 0 #nothing means hardare is not free
#                                 reservation_Station[instruction_status[trarvar]['key']]['is']['qk'] = register_Status[res_totherinputs[trarvar][2]][1]  #which operation except that operation no one else can access this
#                                 # reservation_Station[instruction_status[trarvar]['key']]['vk'].append(0) #nothing means hardare is not free
#                                 # reservation_Station[instruction_status[trarvar]['key']]['qk'].append(register_Status[res_totherinputs[trarvar][2]][1])  #which operation except that operation no one else can access this
#
#
#
#
#
#
#
#             else:
#                 #writeback stage
#                 if instruction_status[trarvar]['completed_yet'] ==1:
#                     print("DEBUGREACHED HERE1")
#
#
#                     # execution to writeback
#
#                     # check WAW HAZARD if renaming took place
#
#
#                     if (isinstance((register_Status[res_totherinputs[trarvar][1]]),list) and isinstance((register_Status[res_totherinputs[trarvar][2]]),list)):
#                         temp_passvar = (register_Status[res_totherinputs[trarvar][1]][1]==trarvar and register_Status[res_totherinputs[trarvar][2]][1]==trarvar)
#
#                     else :
#                         if (isinstance((register_Status[res_totherinputs[trarvar][1]]),int) and isinstance((register_Status[res_totherinputs[trarvar][2]]),int)):
#                             temp_passvar = (register_Status[res_totherinputs[trarvar][1]]==0 and register_Status[res_totherinputs[trarvar][2]]==0)
#
#                         else:
#                             temp_passvar = False
#
#                     # if temp_passvar and register_Status[res_totherinputs[trarvar][0]][1]==trarvar:
#                         # print("DEBUGE2")
#
#
#                     # Check WAR Hazard and register renaming access for register who are allowed to read it
#
#                     reg1 = res_totherinputs[trarvar][1]
#                     reg2 = res_totherinputs[trarvar][2]
#                     #check map table if register renaming has taken place
#                     # if map table has key
#                     if (reg1 in map_table.keys()) or (reg2 in map_table.keys()):
#                         if (reg1 in map_table.keys()) and (reg2 in map_table.keys()):
#                             if len(map_table[reg1])==3 and len(map_table[reg2])==3:
#                                 temp_passvar1 = trarvar in map_table[reg1][1]
#                                 temp_passvar2 = trarvar in map_table[reg2][1]
#                                 temp_passvar = temp_passvar1 and temp_passvar2
#                                 # if both are in map table and both renamed register are done processing
#                                 if temp_passvar1==False and temp_passvar2==False:
#                                     temper1 = instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1 #means renamed reg are done
#                                     temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]['completed_yet']==-1 #means renamed reg are done
#                                     temp_passvar = temper1 and temper2
#
#
#
#                         elif (reg1 in map_table.keys()):
#                             if len(map_table[reg1])==3:
#                                 temp_passvar2 = trarvar in map_table[reg1][1]#list of operations allowed
#                                 if isinstance(register_Status[reg2],int):
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg2]==0))
#
#                                 else:
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg2][1]==trarvar))
#
#                                 if temp_passvar2==False:#first renamed register
#                                     if isinstance(register_Status[map_table[reg1][0]],list):
#
#                                         temper1 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1) #means renamed reg are done
#                                         # temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]==-1 #means renamed reg are done
#                                         if isinstance(register_Status[reg2],int):
#                                             temp_passvar = (temper1 and (register_Status[reg2]==0))
#
#                                         else:
#                                             temp_passvar = (temper1 and (register_Status[reg2][1]==trarvar))
#
#                                     else:
#                                         if isinstance(register_Status[reg2],int):
#                                             temp_passvar = (register_Status[reg2]==0)
#
#                                         else:
#                                             temp_passvar = (register_Status[reg2][1]==trarvar)
#                             elif len(map_table[reg1])==2:
#
#
#
#                                 if isinstance(register_Status[map_table[reg1][0]],list) :
#
#                                     temp_passvar2 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1)#means renamed register are done
#                                     if isinstance(register_Status[reg2],int):
#                                         temp_passvar = (register_Status[reg2]==0)and temp_passvar2
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg2][1]==trarvar)and temp_passvar2
#
#                                 else:
#                                     if isinstance(register_Status[reg2],int):
#                                         temp_passvar = (register_Status[reg2]==0)
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg2][1]==trarvar)
#
#
#
#
#
#                         elif (reg2 in map_table.keys()):
#                             if len(map_table[reg2])==3:
#
#                                 temp_passvar2 = trarvar in map_table[reg2][1]#list of operations allowed
#                                 if isinstance(register_Status[reg1],int):
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg1]==0))
#
#                                 else:
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg1][1]==trarvar))
#
#                                 if temp_passvar2==False:#first renamed register
#                                     # print("DEBUGAY,",register_Status[map_table[reg2][0]])
#                                     if isinstance(register_Status[map_table[reg2][0]],list):
#                                         temper1 = (instruction_status[register_Status[map_table[reg2][0]][1]]['completed_yet']==-1) #means renamed reg are done
#                                         # temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]==-1 #means renamed reg are done
#                                         if isinstance(register_Status[reg1],int):
#                                             temp_passvar = (temper1 and (register_Status[reg1]==0))
#
#                                         else:
#                                             temp_passvar = (temper1 and (register_Status[reg1][1]==trarvar))
#                                     else:
#                                         if isinstance(register_Status[reg1],int):
#                                             temp_passvar = (register_Status[reg1]==0)
#
#                                         else:
#                                             temp_passvar = (register_Status[reg1][1]==trarvar)
#                                         pass
#
#
#                             elif len(map_table[reg2])==2:
#
#
#                                 if isinstance(register_Status[map_table[reg2][0]],list) :
#
#                                     temp_passvar2 = (instruction_status[register_Status[map_table[reg2][0]][1]]['completed_yet']==-1)#means renamed register are done
#                                     if isinstance(register_Status[reg1],int):
#                                         temp_passvar = (register_Status[reg1]==0)and temp_passvar2
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg1][1]==trarvar)and temp_passvar2
#
#                                 else:
#                                     if isinstance(register_Status[reg1],int):
#                                         temp_passvar = (register_Status[reg1]==0)
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg1][1]==trarvar)
#                                     pass
#
#
#
#
#
#
#                     # check whether writing register new register renamed can handle same operation
#                     if isinstance(register_Status[res_totherinputs[trarvar][0]],int):
#
#                         #check if not renamed
#
#
#                         if res_totherinputs[trarvar][0] in map_table.keys():
#                             # the register is being used and renamed and being written on
#                             # temp_passvar123 = map_table
#
#                             # renamed for WAR
#                             if len(map_table[res_totherinputs[trarvar][0]])==3:
#                                 if register_Status[map_table[res_totherinputs[trarvar][0]][0]][1]==trarvar:
#                                     temp_passvar = temp_passvar and True
#
#                                 else:
#                                     temp_passvar = temp_passvar and False
#
#                             elif len(map_table[res_totherinputs[trarvar][0]])==2:
#                                 if map_table[res_totherinputs[trarvar][0]][1] == trarvar:
#                                     temp_passvar = temp_passvar and True
#
#                                 else:
#                                     temp_passvar = temp_passvar and False
#                                     pass
#
#                                 pass
#
#                         # else:
#                         #     case is not possible
#
#
#                     if isinstance(register_Status[res_totherinputs[trarvar][0]],list):
#                         if register_Status[res_totherinputs[trarvar][0]][1]==trarvar:
#                             temp_passvar = temp_passvar and True
#                             pass
#                         else:
#                             temp_passvar = temp_passvar and False
#                             pass
#
#
#
#                     #check WAW renaming
#
#
#
#
#
#
#
#                     if temp_passvar :
#
#                         if ((isinstance(register_Status[res_totherinputs[trarvar][0]],list)) and (register_Status[res_totherinputs[trarvar][0]][1]==trarvar)) or (isinstance(register_Status[res_totherinputs[trarvar][0]],int) and ( register_Status[map_table[res_totherinputs[trarvar][0]][0]][1]==trarvar  )):
#
#
#
#
#                             if reservation_Station[instruction_status[trarvar]['key']]['wb']['busy'] == 1 and reservation_Station[instruction_status[trarvar]['key']]['wb']['op']==trarvar:#only that hardware
#                                 #hardware is free
#                                 # print("DEBUGREACHED HERE")
#
#                                 instruction_status[trarvar]['writeback'] = CLOCK_VAR
#                                 instruction_status[trarvar]['completed_yet'] -= 1
#
#
#
#
#
#
#
#
#
#                     #excution +
#                 elif instruction_status[trarvar]['completed_yet']>0:
#                     #check is hardware not busy
#
#                     #dont allow execution if renamed register is not in list
#
#                     # instruction_status
#
#                     if (isinstance((register_Status[res_totherinputs[trarvar][1]]),list) and isinstance((register_Status[res_totherinputs[trarvar][2]]),list)):
#                         # add WAR HAZARD renaming
#
#                         temp_passvar = (register_Status[res_totherinputs[trarvar][1]][1]==trarvar and register_Status[res_totherinputs[trarvar][2]][1]==trarvar)
#
#
#                     else :
#                         if (isinstance((register_Status[res_totherinputs[trarvar][1]]),int) and isinstance((register_Status[res_totherinputs[trarvar][2]]),int)):
#                             temp_passvar = (register_Status[res_totherinputs[trarvar][1]]==0 and register_Status[res_totherinputs[trarvar][2]]==0)
#
#
#                         else:
#                             temp_passvar = False
#
#
#
#
#                     # Check WAR Hazard and register renaming access for register who are allowed to read it
#
#                     reg1 = res_totherinputs[trarvar][1]
#                     reg2 = res_totherinputs[trarvar][2]
#                     #check map table if register renaming has taken place
#                     # if map table has key
#                     if (reg1 in map_table.keys()) or (reg2 in map_table.keys()):
#                         if (reg1 in map_table.keys()) and (reg2 in map_table.keys()):
#                             if len(map_table[reg1])==3 and len(map_table[reg2])==3:
#
#                                 temp_passvar1 = trarvar in map_table[reg1][1]
#                                 temp_passvar2 = trarvar in map_table[reg2][1]
#                                 temp_passvar = temp_passvar1 and temp_passvar2
#                                 # if both are in map table and both renamed register are done processing
#                                 if temp_passvar1==False and temp_passvar2==False:
#                                     temper1 = instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1 #means renamed reg are done
#                                     temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]['completed_yet']==-1 #means renamed reg are done
#                                     temp_passvar = temper1 and temper2
#
#                                     pass
#
#                         elif (reg1 in map_table.keys()):
#                             if len(map_table[reg1])==3:
#
#                                 temp_passvar2 = trarvar in map_table[reg1][1]#list of operations allowed
#                                 if isinstance(register_Status[reg2],int):
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg2]==0))
#
#                                 else:
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg2][1]==trarvar))
#
#                                 if temp_passvar2==False:#first renamed register
#                                     if isinstance(register_Status[map_table[reg1][0]],list):
#
#                                         temper1 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1) #means renamed reg are done
#                                         # temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]==-1 #means renamed reg are done
#                                         if isinstance(register_Status[reg2],int):
#                                             temp_passvar = (temper1 and (register_Status[reg2]==0))
#
#                                         else:
#                                             temp_passvar = (temper1 and (register_Status[reg2][1]==trarvar))
#
#                                     else:
#                                         if isinstance(register_Status[reg2],int):
#                                             temp_passvar = (register_Status[reg2]==0)
#
#                                         else:
#                                             temp_passvar = (register_Status[reg2][1]==trarvar)
#
#                             elif len(map_table[reg1])==2:
#
#
#
#                                 if isinstance(register_Status[map_table[reg1][0]],list) :
#
#                                     temp_passvar2 = (instruction_status[register_Status[map_table[reg1][0]][1]]['completed_yet']==-1)#means renamed register are done
#                                     if isinstance(register_Status[reg2],int):
#                                         temp_passvar = (register_Status[reg2]==0)and temp_passvar2
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg2][1]==trarvar)and temp_passvar2
#
#                                 else:
#                                     if isinstance(register_Status[reg2],int):
#                                         temp_passvar = (register_Status[reg2]==0)
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg2][1]==trarvar)
#
#
#
#
#
#
#
#
#
#
#
#                         elif (reg2 in map_table.keys()):
#                             print("\nCELL GAMES BY HETAP",trarvar)
#                             if len(map_table[reg2])==3:
#
#                                 temp_passvar2 = trarvar in map_table[reg2][1]#list of operations allowed
#                                 if isinstance(register_Status[reg1],int):
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg1]==0))
#
#                                 else:
#                                     temp_passvar = (temp_passvar2 and (register_Status[reg1][1]==trarvar))
#                                 # print
#                                 if temp_passvar2==False:#first renamed register
#                                     # print("DEBUGAY,",register_Status[map_table[reg2][0]])
#                                     if isinstance(register_Status[map_table[reg2][0]],list):
#                                         temper1 = (instruction_status[register_Status[map_table[reg2][0]][1]]['completed_yet']==-1) #means renamed reg are done
#                                         # temper2 = instruction_status[register_Status[map_table[reg2][0]][1]]==-1 #means renamed reg are done
#                                         if isinstance(register_Status[reg1],int):
#                                             temp_passvar = (temper1 and (register_Status[reg1]==0))
#                                             print("IT shoud be here value",temp_passvar)
#
#                                         else:
#                                             temp_passvar = (temper1 and (register_Status[reg1][1]==trarvar))
#                                     else:
#                                         if isinstance(register_Status[reg1],int):
#                                             temp_passvar = (register_Status[reg1]==0)
#
#                                         else:
#                                             temp_passvar = (register_Status[reg1][1]==trarvar)
#                                         pass
#
#                             elif len(map_table[reg2])==2:
#                                 # print("hold still")
#                                 # print(map_table[reg2])
#                                 #
#                                 # print(register_Status[map_table[reg2][0]])
#
#
#                                 # print(register_Status[map_table[reg2][0]][1])
#
#                                 if isinstance(register_Status[map_table[reg2][0]],list) :
#
#                                     temp_passvar2 = (instruction_status[register_Status[map_table[reg2][0]][1]]['completed_yet']==-1)#means renamed register are done
#                                     if isinstance(register_Status[reg1],int):
#                                         temp_passvar = (register_Status[reg1]==0)and temp_passvar2
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg1][1]==trarvar)and temp_passvar2
#
#                                 else:
#                                     if isinstance(register_Status[reg1],int):
#                                         temp_passvar = (register_Status[reg1]==0)
#                                         pass
#                                     else:
#                                         temp_passvar = (register_Status[reg1][1]==trarvar)
#                                     pass
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#                     # print(trarvar,temp_passvar)
#                     if temp_passvar :
#                         # print("DEBUGE2")
#                         if (res_totherinputs[trarvar][0] in map_table.keys() and len(map_table[res_totherinputs[trarvar][0]])==2 and map_table[res_totherinputs[trarvar][0]][1] == trarvar ) or ((isinstance(register_Status[res_totherinputs[trarvar][0]],list)) and (register_Status[res_totherinputs[trarvar][0]][1]==trarvar)) or (isinstance(register_Status[res_totherinputs[trarvar][0]],int)and ( register_Status[map_table[res_totherinputs[trarvar][0]][0]][1]==trarvar  )):
#
#                             # check if ex to
#                             # print("fetish",temp_passvar,trarvar)
#
#
#                             if reservation_Station[instruction_status[trarvar]['key']]['ex']['busy'] == 1 and reservation_Station[instruction_status[trarvar]['key']]['ex']['op'] == trarvar :#excution unit of hardware is free or being used by that instruction
#                             # only if busy and is used by that instruction only and execution is available
#                                 instruction_status[trarvar]['completed_yet'] -=1
#                                 instruction_status[trarvar]['exec'] =CLOCK_VAR
#                                 # reservation_Station[instruction_status[trarvar]['key']]['exechandling'][0] = trarvar
#
#                                 # mark for write back
#                                 if instruction_status[trarvar]['completed_yet'] ==1 :
#                                     reservation_Station[instruction_status[trarvar]['key']]['ex']['readytowrite'] = 1
#
#
#                                     # free execution statement
#                                     # make case when 2 so that you free up execute state of hardware
#
#
#
#
#
#
#
#
#
#
#                 if instruction_status[trarvar]['completed_yet'] == 0:
#                     #nothing to do instruction in completed
#                     #if hardware busy due to this traverse then declare it free
#                     # free write back
#
#                     reservation_Station[instruction_status[trarvar]['key']]['wb']['busy'] = 0
#
#                     reservation_Station[instruction_status[trarvar]['key']]['wb']['op'] = -1
#                     reservation_Station[instruction_status[trarvar]['key']]['wb']['vj'] = 0
#                     reservation_Station[instruction_status[trarvar]['key']]['wb']['vk'] = 0
#                     reservation_Station[instruction_status[trarvar]['key']]['wb']['qj'] = 0
#                     reservation_Station[instruction_status[trarvar]['key']]['wb']['qk'] = 0
#                     instruction_status[trarvar]['completed_yet'] = -1
#                     #
#                     #
#                     #free hardware
#                     # free renamed hardware
#                     doubleifpor= True
#                     if res_totherinputs[trarvar][0] in map_table.keys():
#                         # print("DEBUG5 Reached",(map_table[res_totherinputs[trarvar][0]][0]))
#                         if register_Status[res_totherinputs[trarvar][0]]!=0:
#                             if register_Status[res_totherinputs[trarvar][0]][1]==trarvar:
#                                 temmmpempstr  = "Write register done "+str(res_totherinputs[trarvar][0])
#                                 RAISEEXCEPTION.append(temmmpempstr)
#                                 register_Status[res_totherinputs[trarvar][0]]=0
#                                 doubleifpor = False
#
#
#                             pass
#                         elif isinstance(register_Status[map_table[res_totherinputs[trarvar][0]][0]],list):
#
#                             if register_Status[map_table[res_totherinputs[trarvar][0]][0]][1] == trarvar:
#                                 temmmpempstr  = "BUFFER TRANSFER FROM to "+str(map_table[res_totherinputs[trarvar][0]][0])+" to its original register"
#                                 RAISEEXCEPTION.append(temmmpempstr)
#                                 register_Status[map_table[res_totherinputs[trarvar][0]][0]] = 0
#                                 doubleifpor = False
#
#                     if doubleifpor:
#                         register_Status[res_totherinputs[trarvar][0]]=0
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     clear()
#     print('\nCLOCK = ',CLOCK_VAR)
#     # for keys in reservation_Station.keys():
#     print("\nHardware Reservation Table")
#     for keys in get_hardwareused_list:
#         if keys not in ["LOAD1","STORE","REGISTER_COMPLEMENT"]:
#
#             print(keys,'issue ',reservation_Station[keys]['is'])
#             print('execute ',reservation_Station[keys]['ex'])
#             print('write back ',reservation_Station[keys]['wb'])
#             print()
#
#     print()
#     print("\nHardware Reservation Table for Load Store Complement")
#     for keys in get_hardwareused_list:
#         if keys in ["LOAD1","STORE","REGISTER_COMPLEMENT"]:
#
#             print(keys,'issue :',reservation_Station[keys]['is']["busy"],end= " ")
#             print('operation: ',reservation_Station[keys]['is']["op"],end= " ")
#             print('vj :',reservation_Station[keys]['is']["vj"],end= " ")
#
#             print('qj: ',reservation_Station[keys]['is']["qj"],end = "   ")
#
#             print(keys,'issue :',reservation_Station[keys]['ex']["busy"],end= " ")
#             print('operation :',reservation_Station[keys]['ex']["op"],end= " ")
#             print('vj :',reservation_Station[keys]['ex']["vj"],end= " ")
#
#             print('qj :',reservation_Station[keys]['ex']["qj"],end = "   ")
#
#             print(keys,'issue: ',reservation_Station[keys]['wb']["busy"],end= " ")
#             print('operation: ',reservation_Station[keys]['wb']["op"],end= " ")
#             print('vj: ',reservation_Station[keys]['wb']["vj"],end= " ")
#
#             print('qj: ',reservation_Station[keys]['wb']["qj"],end = "   ")
#
#
#             # print('execute ',reservation_Station[keys]['ex'])
#             # print('write back ',reservation_Station[keys]['wb'])
#             print()
#
#     print()
#
#     print("Instruction STATUS")
#     instruction_status_keyforprint = ['issue', 'exec', 'writeback', 'completed_yet', 'key']
#     for i1 in instruction_status:
#         for j12 in instruction_status_keyforprint:
#             print(j12," : ",i1[j12],end = " ")
#         print()
#     # print(instruction_status)
#
#
#
#     print()
#     print("Instructions Input\n")
#     for leinstr in range(LENTH_OFINSTRUCTION_STATUS):
#         if instruction_status[leinstr]['completed_yet']!=-1:
#             print(opc_odes1[leinstr],end = " ")
#             for regprit in res_totherinputs[leinstr]:
#                 if (regprit in map_table.keys()):
#                     if len(map_table[regprit])==3:
#                         # renamed for WAR
#                         if (leinstr in map_table[regprit][1]):
#                             print(regprit,end = " ,")
#
#                             # print(regprit,end = " ,")
#                         else:
#                             print(map_table[regprit][0],end = " ,")
#
#
#                         # renamed for WAW
#                     elif len(map_table[regprit])==2:
#                         if leinstr>=map_table[regprit][1]:
#                             print(map_table[regprit][0],end = " ,")
#
#                             # print()
#                         else:
#                             print(regprit,end = " ,")
#
#                             pass
#                         pass
#                 # elif regprit in map_table.keys():
#                 #     print(map_table[regprit][0],end = " ")
#                 else:
#                     print(regprit,end = " ,")
#                     pass
#             print()
#         else:
#             print(opc_odes1[leinstr]," is now completed")
#
#     print("\nRegister Status")
#     print(register_Status)
#     # for i12 in register_Status.keys():
#     #     if i12 not in temp_ereg:
#     #         print(i12," : ",register_Status[i12],end = " ")
#
#
#
#     print("\n")
#
#     print("Renamed Register list")
#     for keyuar in map_table.keys():
#         if isinstance(register_Status[map_table[keyuar][0]],list):
#             print("Instruction ",register_Status[map_table[keyuar][0]][1]+1,"   ",keyuar," is renamed to ",map_table[keyuar][0],end = " " )
#             # print(map_table[keyuar][0])
#             # print(len(map_table[keyuar][0]))
#             if len(map_table[keyuar])==3:
#                 print("Renamed For WAR")
#             elif len(map_table[keyuar])==2:
#                 print("Renamed For WAW")
#
#
#     print()
#     if map_table!={}:
#         print("\nmap_table\n")
#         print(map_table)
#         print()
#     if RAISEEXCEPTION!=[]:
#         print("EXCEPTION Handled Messages")
#         for messages in RAISEEXCEPTION:
#             print(messages)
#     RAISEEXCEPTION = []
#     print('\nCLOCK = ',CLOCK_VAR)
#
#
#
#
#
#         # copy stuff from issue unit to exec unit in
#
#
#     #shift from issue to ex only if ex is free
#     for eachharwareexunit in reservation_Station.keys():
#         if reservation_Station[eachharwareexunit]['ex']['busy'] == 0:
#             #excution is free
#             if reservation_Station[eachharwareexunit]['is']['busy'] == 1 and reservation_Station[eachharwareexunit]['is']['readytoexec']== 1:
#                 #issue is being used
#                 # now convert issue to execute
#                 # free issue and declare ex as busy
#                 reservation_Station[eachharwareexunit]['ex']['busy'] = 1
#                 reservation_Station[eachharwareexunit]['is']['busy'] = 0
#                 reservation_Station[eachharwareexunit]['ex']['op'] = reservation_Station[eachharwareexunit]['is']['op']
#                 reservation_Station[eachharwareexunit]['ex']['vj'] = reservation_Station[eachharwareexunit]['is']['vj']
#                 reservation_Station[eachharwareexunit]['ex']['vk'] = reservation_Station[eachharwareexunit]['is']['vk']
#                 reservation_Station[eachharwareexunit]['ex']['qk'] = reservation_Station[eachharwareexunit]['is']['qk']
#                 reservation_Station[eachharwareexunit]['ex']['qj'] = reservation_Station[eachharwareexunit]['is']['qj']
#
#
#                 reservation_Station[eachharwareexunit]['is']['op'] = -1
#                 reservation_Station[eachharwareexunit]['is']['vj'] = 0
#                 reservation_Station[eachharwareexunit]['is']['vk'] = 0
#                 reservation_Station[eachharwareexunit]['is']['qj'] = 0
#                 reservation_Station[eachharwareexunit]['is']['qk'] = 0
#                 # reservation_Station[eachharwareexunit]['is']['vj'] = 0
#
#
#                 reservation_Station[eachharwareexunit]['is']['readytoexec'] = 0
#
#
#     # ex to wb unit of ex
#     for eachhardwareunit in reservation_Station.keys():
#         if reservation_Station[eachhardwareunit]['wb']['busy'] ==0:
#             # available
#             # if reservation_Station[instruction_status[trarvar]['key']]['wb']['busy'] == 0:
#                 #hardware is free
#                 # transfer all stuff from ex to wb\
#             if reservation_Station[eachhardwareunit]['ex']['busy'] == 1 and reservation_Station[eachhardwareunit]['ex']['readytowrite']==1:
#                 reservation_Station[eachhardwareunit]['wb']['busy'] = 1 #now busy
#                 reservation_Station[eachhardwareunit]['ex']['busy'] = 0 #freed
#                 reservation_Station[eachhardwareunit]['wb']['op'] = reservation_Station[eachhardwareunit]['ex']['op']
#                 reservation_Station[eachhardwareunit]['wb']['vj'] = reservation_Station[eachhardwareunit]['ex']['vj']
#                 reservation_Station[eachhardwareunit]['wb']['vk'] = reservation_Station[eachhardwareunit]['ex']['vk']
#                 reservation_Station[eachhardwareunit]['wb']['qj'] = reservation_Station[eachhardwareunit]['ex']['qj']
#                 reservation_Station[eachhardwareunit]['wb']['qk'] = reservation_Station[eachhardwareunit]['ex']['qk']
#
#
#                 reservation_Station[eachhardwareunit]['ex']['op'] = -1
#                 reservation_Station[eachhardwareunit]['ex']['vj'] = 0
#                 reservation_Station[eachhardwareunit]['ex']['vk'] = 0
#                 reservation_Station[eachhardwareunit]['ex']['qj'] = 0
#                 reservation_Station[eachhardwareunit]['ex']['qk'] = 0
#
#
#
#                 # now in write state
#                 reservation_Station[eachhardwareunit]['ex']['readytowrite'] = 0
#
#
#
#
#
#
#
#     # rename register when everyone is done reading from it
#
#     listtoremovefromdict = []
#     for keyvar in map_table.keys():
#         if len(map_table[keyvar])==3:
#             busy = False
#             for eachoperation in map_table[keyvar][1]:#list of operation reading it
#
#                 if instruction_status[eachoperation]['completed_yet']>0:#inwriteback stages or completed (we dont have to read reg)
#                     busy = True#even if one is busy
#                     break
#             # print("bvusy",busy)
#             if busy == False:
#                 register_Status[keyvar] = register_Status[map_table[keyvar][0]]
#                 register_Status[map_table[keyvar][0]] = 0
#                 # map_table.pop(keyvar,None)
#                 listtoremovefromdict.append(keyvar)
#
#         elif len(map_table[keyvar])==2:
#             # busy = False
#             if instruction_status[map_table[keyvar][1]]['completed_yet']==-1:
#                 register_Status[keyvar] = register_Status[map_table[keyvar][0]]
#                 register_Status[map_table[keyvar][0]] =0
#                 #original register done writing therefore done writing
#                 listtoremovefromdict.append(keyvar)
#
#                 pass
#             pass
#
#
#
#     # print("removedick",listtoremovefromdict)
#     for keyvar in listtoremovefromdict:
#         str11 = "REGISTER RENAMED "+str(keyvar)+" to its original name"
#         RAISEEXCEPTION.append(str11)
#         map_table.pop(keyvar,None)
#
#
#
#
#
#
#
#
#
#
#
#
#
#     if completed_fuc(instruction_status):
#         completed_VAR = False
#     # debug purposes
#     # time.sleep(timdiff)
#     if simulate=="yes":
#         x123 = input("\nPress enter to go to next clock")
