from unittest import result
import model
import view
import operation
import logger

def button_click():
    some_str = view.inp()
    some_tuple = operation.op(some_str)
    model.init(some_tuple[0], some_tuple[1])
    if some_tuple[2] == '+':
        result = model.sum()
    elif some_tuple[2] == '-':
        result = model.sub()
    elif some_tuple[2] == '*':
        result = model.mult()
    else:
        result = model.div() 
    logger.write(some_str, result)
    view.view_data(result)