import sys
import urllib.request
from flask import Flask
from flask import request


# insert flask annotation here
app = Flask(__name__)

@app.route('/')
def main():
    
    Ns = request.args.get('N',default = 10, type = int)
    if not Ns:
        Ns=10
    N = int(Ns)
    my_array=[]
    for i in computepi(N):
        my_array.append(str(i))
    my_array = my_array[:1] + ['.'] + my_array[1:]
    big_string = "".join(my_array)
    
    
  
    return big_string


def computepi(N):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    counter = 0
    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
            if counter>N-1:
                break
            else:
                counter=counter+1
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2



if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
