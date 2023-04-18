   	 	  		#include <iostream>
	
     			 	 	#include <math.h>
	
     		 		 	using namespace std;
	
     		 		 	int main() {
	
     		 	  	int a=40;
	
     			 	  int b=72;
	
     	    		int n[] = {0,0,0,0,0,0,0,0,0};
	
    	 	 	   string s = "";
	
     	   		 int iter = 0;
	
     				 		for (int i = a; i < b; i++){iter++;}
	
     			  	 n[3] = iter;
	
      		  		n[2] = 116;
	
      		 	  while(n[7] == 0){n[7] = n[2];}
	
     		  	  n[8] = n[7] - n[2]*2 + 1 + n[7] + n[2];
	
     	 					int temp = n[8];
	
      			   n[5] = n[8];
	
     		  	 	n[8] = 101;
	
     	 	 	  for (int i = 0; i < 4; i++){n[1] += pow(10, i);}
	
    			 			 n[1] = n[1] / 10;
	
      		  		if (n[1] != 0)
	
      		  		{
	
     		 			 if (n[1] == 0){n[0] = 127;}
	
     	 					else{n[0]=toupper(char(int(tolower(char(77)))+1));}
	
      		 			}
	
     		 	   n[4] = n[int(sizeof(n)/sizeof(n[0])/2)] + 81;
	
      		  		n[6] = n[4] + 2147483647*2 + 26;
	
     	 					for (int c : n)
	
     	  		  {
	
      		   	int x = 0;
	
     		 			 s.push_back(char(c));
	
      		  		}
	
     			  		cout << s;
	
     					 	}


