# example 3 quality check in textile
# my brother ask me for this programme

weight=input("Enter the weight ") #weight of the clothe
weight=int(weight)
width=input("Enter the width ")  #width of the clothe
width=int(width)
gsm=input("Enter the gsm ")  # gsm of the clothe
gsm=int(gsm)
allow_points=(weight*width)/gsm*2  
print("Allow points are ",allow_points)
if allow_points<=541:
    print("Allow points are", "A grade")
    if allow_points>=540:
        print("Allow points are", "B grade")
else:
            print("invalid entry")