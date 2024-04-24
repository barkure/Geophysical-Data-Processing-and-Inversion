function q=IntGaussLobato(f,a,b,n,AK,XK)
if(n<7&&nargin==4)
else
XK1=((b-a)/2)*XK+((a+b)/2);
q=((b-a)/2)*((2/n/(n-1))*(subs(str2sym(f), symvar(str2sym(f)), a)+subs(str2sym(f), symvar(str2sym(f)),b))+sum(AK.*subs(str2sym(f), symvar(str2sym(f)),XK1)));
end
ta = (b-a)/2;
tb = (a+b)/2;

switch n

    case 3 %n=3时,采用表8-3中对应的系数进行计算
    q=ta* ((1/3) * (subs(str2sym(f), symvar(str2sym(f)), a)+subs(str2sym(f), symvar(str2sym(f)), b))+1.333333*subs(str2sym(f), symvar(str2sym(f)), tb)); 
    
    case 4 %n=4时,采用表8-3中对应的系数进行计算
    q=ta*((1/6)*(subs (str2sym(f), symvar(str2sym(f)), a)+subs(str2sym(f), symvar(str2sym(f)),b))+0.833333*(subs(str2sym(f), symvar(str2sym(f)), ta*0.447214+tb)+subs(str2sym(f), symvar(str2sym(f)),-ta*0.447214+tb))); 

    case 5 %n=5,采用表8-3中对应的系数进行计算 
    q=ta*((1/10)* (subs(str2sym(f), symvar(str2sym(f)), a)+subs (str2sym(f), symvar(str2sym(f)),b))+0.544444*(subs(str2sym(f), symvar(str2sym(f)), ta*0.654654+tb)+subs(str2sym(f), symvar(str2sym(f)),-ta*0.654654+tb))+ 0.711111*subs(str2sym(f), symvar(str2sym(f)), tb));

    case 6 %n=6,采用表8-3中对应的系数进行计算
    q=ta*((1/15)* (subs(str2sym(f), symvar(str2sym(f)), a)+subs(str2sym(f), symvar(str2sym(f)), b))+0.554858*(subs(str2sym(f), symvar(str2sym(f)), ta*0.285232+tb)+subs(str2sym(f), symvar(str2sym(f)),-ta*0.285232+tb))+0.378475*(subs(str2sym(f), symvar(str2sym(f)), ta*0.765055+tb)+subs (str2sym(f), symvar(str2sym(f)),-ta*0.765055+tb)));
end
