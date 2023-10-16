function dp=couple_exp(z, p, delta1, delta2, delta3, kappa1, kappa2, kappa3)
dp=zeros(3,1);
dp(1)=-j*kappa1*p(2)*exp(-j*2*delta1*z)-j*kappa2*p(3)*exp(-j*2*delta2*z);
dp(2)=-j*kappa1*p(1)*exp(+j*2*delta1*z)-j*kappa3*p(3)*exp(-j*2*delta3*z);
dp(3)=-j*kappa2*p(1)*exp(+j*2*delta2*z)-j*kappa3*p(2)*exp(+j*2*delta3*z);
