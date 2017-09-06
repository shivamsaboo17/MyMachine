
% function: Short description
%
% Extended description
o1 = input('enter the first parameter');
o2 = input('enter the second parameter');
x = [1; 2; 2; 3; 3; 4; 5; 6; 6; 6; 8; 10];
y = [-890;-1411;-1560;-2220;-2091;-2878;-3537;-3268;-3920;-4163;-5471;-5157];
figure;
plot(x,y);
h = o1 + o2*.x;
plot(x,h);
