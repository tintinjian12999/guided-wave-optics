clear all
kappa1=2;
kappa2=2;
kappa3=2;
delta1=0;
delta2=0;
delta3=0;
q1=sqrt(kappa1^2+delta1^2);
q2=sqrt(kappa2^2+delta2^2);
q3=sqrt(kappa3^2+delta3^2);
[Z,A] = ode45(@couple_exp,[0 2*pi/kappa1], [1 0 0], [], delta1, delta2, delta3, kappa1, kappa2, kappa3);
plot(q1*Z,abs(A(:,1)).^2,q2*Z,abs(A(:,2)).^2,'--',q3*Z,abs(A(:,3)).^2,'.')
axis([0 2*pi 0 1.4])
xticks(0:pi/2:2*pi);
xticklabels({'0', '\pi/2', '\pi', '3\pi/2', '2\pi'}); 
xlabel("Normalized distance qz");
ylabel("Transmitted and coupled intensity");