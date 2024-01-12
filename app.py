#!/usr/bin/env python3

"""Python app for testing pythagoras approximations"""

from src import pythagoras

diffs:list = []
diff_percents:list = []

def main() -> None:
    """Main function""" 
    for i in range(1,5000):
        for j in range(1,5000):
            calc = pythagoras.calc((i,j))
            diff = abs(calc - pythagoras.approx((i,j)))

            diffs.append(diff)
            diff_percents.append((diff/calc)*100)

    avg_err:float = round(sum(diffs)/len(diffs),2)
    avg_err_percent:float = round(sum(diff_percents)/len(diff_percents),2)
    print(
        f'Avg error: {avg_err} \nAvg error percent: {avg_err_percent}%'
    )

if __name__=="__main__":
    main()
