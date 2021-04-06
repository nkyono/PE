# takes in numerator, denominator, and places. Places represents how many decimal places to compute
# going to assume numerator and denominator are both positive integers
def longDiv(numerator, denominator, places):
    res = ""
    decimal = False
    if numerator < denominator:
        decimal = True
        res = "0."
    numStr = str(numerator)
    numIndex = 0
    decimalPlaces = 0
    remainder = int(numStr[numIndex])
    while(remainder != 0 and decimalPlaces < places):
        if remainder >= denominator:
            i = 0
            while (i < 10):
                i = i + 1
                if i * denominator > remainder:
                    i = i - 1
                    break
            res = res + str(i)
            if decimal:
                decimalPlaces = decimalPlaces + 1
            remainder = int(str(remainder - i * denominator))
        else:
            if res != "" and res != "0.":
                res = res + "0"
                if decimal:
                    decimalPlaces = decimalPlaces + 1
        
        if remainder == 0:
            break
        numIndex = numIndex + 1
        if numIndex == len(numStr):
            if "." not in res:
                res = res + "."
                decimal = True
            numStr = numStr + "0"
            
        remainder = int(str(remainder) + numStr[numIndex])
    print(res)
    return res

def main():
    import math
    assert longDiv(10, 4, 20) == "2.5"
    assert longDiv(1260257, 37, 20) == "34061"
    assert longDiv(1, 3, 20) == "0.33333333333333333333"
    assert longDiv(10, 3, 20) == "3.33333333333333333333"
    assert longDiv(3923, 6173, 257) == "0.63550947675360440628543657864895512716669366596468491819212700469787785517576543009881743074680058318483719423294994330147416167179653329013445650413089259679248339543171877531184189211080511906690426048922728009071764134132512554673578486959339057184513202"

if __name__ == '__main__':
    main()