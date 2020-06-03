



# Quantities of each hardware and total time taken(time for issue and write back is included)
STORE_HARDWARE = {
'ADD_N' :[1,8,'ADD_N'],
'ADD_W_C' :[1,8,'ADD_W_C'],
'SUB_N' :[1,8,'SUB_N'],
'SUB_B' :[1,8,'SUB_B'],
'MUL_T' :[1,13,'MUL_T'],
'FP_ADDER' :[1,23,'FP_ADDER'],
'FP_SUB' :[1,26,'FP_SUB'],
'FP_MUL' :[1,26,'FP_MUL'],
'HALT' :[1,6,'HALT'],
'REGISTER_COMPLEMENT' :[1,3,'REGISTER_COMPLEMENT'],
'LOG_XOR' :[1,3,'LOG_XOR'],
'LOG_NAND' :[1,3,'LOG_NAND'],
'SHIFT_RIGHT' :[1,6,'SHIFT_RIGHT'],
'SHIT_LEFTF' :[1,6,'SHIT_LEFTF'],
'STORE' :[1,4,'STORE'],
'LOAD1' :[1,4,'LOAD1']
}




# ADD_N =[1,8]
# ADD_W_C =[1,8]
# SUB_N =[1,8]
# SUB_B =[1,8]
# MUL_T =[1,13]
# FP_ADDER =[1,23]
# FP_SUB =[1,26]
# FP_MUL =[1,26]
# HALT =[1,6]
# REGISTER_COMPLEMENT =[1,3]
# LOG_XOR =[1,3]
# LOG_NAND =[1,3]
# SHIFT_RIGHT =[1,6]
# SHIT_LEFTF =[1,6]
# STORE =[1,4]
# LOAD1 =[1,4]









def Hardwarecase(arg):
    pass


def add_instruction_status(opcodelist):
    hardwareList = []
    instruction_status = []

    #save execution status of each operation
    for opvar in range(len(opcodelist)):
        temp_dict = {'issue':0,'exec':0,'writeback':0,'completed_yet':0,'started':0,'key':0}

        if opcodelist[opvar]=="0000":
            temp_dict['completed_yet'] = STORE_HARDWARE['ADD_N'][1]
            temp_dict['key'] = 'ADD_N'
            hardwareList.append('ADD_N')

            pass



        elif opcodelist[opvar]=="0001":
            #additon with carry 'ADD_W_C'
            temp_dict['completed_yet'] = STORE_HARDWARE['ADD_W_C'][1]
            temp_dict['key'] = 'ADD_W_C'
            hardwareList.append('ADD_W_C')


            # no of operands are correct
            # print("Success")




        elif opcodelist[opvar]=="0010":
            temp_dict['completed_yet'] = STORE_HARDWARE['SUB_N'][1]
            temp_dict['key'] = 'SUB_N'
            hardwareList.append('SUB_N')

            # subtraction normal SUB_N


            # print("Success")






        elif opcodelist[opvar]=="0011":
            temp_dict['completed_yet'] = STORE_HARDWARE['SUB_B'][1]
            temp_dict['key'] = 'SUB_B'
            hardwareList.append('SUB_B')

            #subtraction with borrow SUB_B

            # no of operands are correct
            # print("Success")

            pass



        elif opcodelist[opvar]=="0100":
            temp_dict['completed_yet'] = STORE_HARDWARE['MUL_T'][1]
            temp_dict['key'] = 'MUL_T'
            hardwareList.append('MUL_T')

            #multiplication MUL_T

            # no of operands are correct
            # print("Success")

            pass



        elif opcodelist[opvar]=="0101":
            temp_dict['completed_yet'] = STORE_HARDWARE['FP_ADDER'][1]
            temp_dict['key'] = 'FP_ADDER'
            hardwareList.append('FP_ADDER')

            # floating point adder 'FP_ADDER'

            # no of operands are correct
            # print("Success")

            pass



        elif opcodelist[opvar]=="0110":
            temp_dict['completed_yet'] = STORE_HARDWARE['FP_SUB'][1]
            temp_dict['key'] = 'FP_SUB'
            hardwareList.append('FP_SUB')

            # floating point subtraction FP_SUB

            # no of operands are correct
            # print("Success")

            pass







        elif opcodelist[opvar]=="0111":
            temp_dict['completed_yet'] = STORE_HARDWARE['FP_MUL'][1]
            temp_dict['key'] = 'FP_MUL'
            hardwareList.append('FP_MUL')

            # floating point multiplication FP_MUL

            # no of operands are correct
            # print("Success")

            pass









        elif opcodelist[opvar]=="1000":
            temp_dict['completed_yet'] = STORE_HARDWARE['HALT'][1]
            temp_dict['key'] = 'HALT'
            hardwareList.append('HALT')

            # HALT STATUS  HALT

            # no of operands are correct
            # print("Success")

            pass






        elif opcodelist[opvar]=="1001":
            temp_dict['completed_yet'] = STORE_HARDWARE['REGISTER_COMPLEMENT'][1]
            temp_dict['key'] = 'REGISTER_COMPLEMENT'
            hardwareList.append('REGISTER_COMPLEMENT')

            # register complemet REGISTER_COMPLEMENT

            # no of operands are correct
            # print("Success")

            pass



        elif opcodelist[opvar]=="1010":
            temp_dict['completed_yet'] = STORE_HARDWARE['LOG_XOR'][1]
            temp_dict['key'] = 'LOG_XOR'
            hardwareList.append('LOG_XOR')

            # logical xor LOG_XOR



            # no of operands are correct
            # print("Success")



        elif opcodelist[opvar]=="1011":
            temp_dict['completed_yet'] = STORE_HARDWARE['LOG_NAND'][1]
            temp_dict['key'] = 'LOG_NAND'
            hardwareList.append('LOG_NAND')

            # logical bit wise nand LOG_NAND

            # no of operands are correct
            # print("Success")

            pass



        elif opcodelist[opvar]=="1100":
            temp_dict['completed_yet'] = STORE_HARDWARE['SHIFT_RIGHT'][1]
            temp_dict['key'] = 'SHIFT_RIGHT'
            hardwareList.append('SHIFT_RIGHT')

            # shift right SHIFT_RIGHT

            # no of operands are correct
            # print("Success")

            pass







        elif opcodelist[opvar]=="1101":
            temp_dict['completed_yet'] = STORE_HARDWARE['SHIT_LEFTF'][1]
            temp_dict['key'] = 'SHIT_LEFTF'
            hardwareList.append('SHIT_LEFTF')

            # shift right SHIT_LEFTF


            # print("Success")
            # no of operands are correct

            pass



        elif opcodelist[opvar]=="1110":
            temp_dict['completed_yet'] = STORE_HARDWARE['STORE'][1]
            temp_dict['key'] = 'STORE'
            hardwareList.append('STORE')

            # store STORE

            # no of operands are correct
            # print("Success")

            pass



        elif opcodelist[opvar]=="1111":
            # load LOAD1

            # no of operands are correct
            temp_dict['completed_yet'] = STORE_HARDWARE['LOAD1'][1]
            temp_dict['key'] = 'LOAD1'
            hardwareList.append('LOAD1')

            # print("Success")

            pass

        instruction_status.append(temp_dict)

    # print(instruction_status)
    hardwareList = list(set(hardwareList))
    return instruction_status,hardwareList
