function q=IntGuass(f,a,b,n,AK,XK)
if(n<5&&nargin==4)
    AK=0;
    XK=0;
else
    XK1=((b-a)/2)*XK+((a+b)/2);
    q=((b-a)/2)*sum(AK.*subs(sym(f),symvar(f),XK1));
end
ta=(b-a)/2;
tb=(b+a)/2;
switch n
    case 1,%n=1
        q=2*ta*subs(sym(f),symvar(sym(f)),tb);
    case 2,%n=2
        q=ta*(subs(sym(f),symvar(sym(f)),ta*0.5773503+tb)+...
            subs(sym(f),symvar(sym(f)),-ta*0.5773503+tb));
    case 3,%n=3
        q=ta*(0.55555556*subs(sym(f),symvar(sym(f)),ta*0.7745967+tb)+...
            0.55555556*subs(sym(f),symvar(sym(f)),-ta*0.7745967+tb)+...
            0.88888889*subs(sym(f),symvar(sym(f)),tb));
    case 4,%n=4
        q=ta*(0.3478548*subs(sym(f),symvar(sym(f)),ta*0.8611363+tb)+...
            0.3478548*subs(sym(f),symvar(sym(f)),-ta*0.8611363+tb)+...
            0.6521452*subs(sym(f),symvar(sym(f)),ta*0.3398810+tb)+...
            0.6521452*subs(sym(f),symvar(sym(f)),-ta*0.3398810+tb));
    case 5,%n=5
        q=ta*(0.2369269*subs(sym(f),symvar(sym(f)),ta*0.9061793+tb)+...
            0.2369269*subs(sym(f),symvar(sym(f)),-ta*0.9061793+tb)+...
            0.4786287*subs(sym(f),symvar(sym(f)),ta*0.5384693+tb)+...
            0.4786287*subs(sym(f),symvar(sym(f)),-ta*0.5384693+tb)+...
            0.5688889*subs(sym(f),symvar(sym(f)),tb));
end
q=double(q);