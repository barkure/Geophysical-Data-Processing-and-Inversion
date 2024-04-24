x=linspace(0,2,49);
y=linspace(0,2,49);
[X,Y]=meshgrid(x,y);
u=peEllip5(51,0,2,51,0,2);
surf(X,Y,u)