n = 3;
ren = 1;
while ( ren <= n ):
    col = 1;
    while ( col <= ren -  1 ):
        print("  ");
        col+=1
    col = 1;
  
    while ( col <= n - ren + 1):
        print("* ")
        col+=1
    print("\n")
    ren+=1
