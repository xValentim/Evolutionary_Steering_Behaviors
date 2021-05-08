def sierpinski_carpet()

'''void sc(){          // sierpinski carpet
  for (float i = 1; i <= L; i++){
    for (float j = 1; j <= L; j++){
      for (float kk = 0; kk <= k-1; kk++){
        /*float aux1 = round((i) / pow(3, kk));
        float aux2 = round((j) / pow(3, kk));*/
        if(floor((i-1) / pow(3, kk)) % 3.0 == 1.0 && floor((j-1) / pow(3, kk)) % 3.0 == 1.0){ 
          mol[(int)i][(int)j] = 0;
        }
      }
    }
  }
  aux = 1;
}'''