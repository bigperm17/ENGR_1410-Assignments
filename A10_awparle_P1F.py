#Adam Parler   ENGR 1410-013    January 31, 2014
#Problem Statement: Calculate the weight of a metal rod

def A10_awparle_P1F(V,SG):

	g=1.25; #m/s^2
	rho_w=1000; #[-]
	lb_f=0.225; #[pound-force]

	Wi=V*SG*rho_w*g;
	Weight=Wi*lb_f;
	return Weight

