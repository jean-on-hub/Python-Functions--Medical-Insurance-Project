# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age,sex,bmi,num_of_children,smoker,name):
  estimated_cost= 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for "+name+" is "+str(estimated_cost)+" dollars.")
  g="The estimated insurance cost for "+name+" is "+str(estimated_cost)+" dollars."
  return estimated_cost,g


# Initial variables for Maria 
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  

# Estimate Maria's insurance cost
cost2,maria_insurance_cost = calculate_insurance_cost(28,0,26.2,3,0,"maria")

#print("The estimated insurance cost for Maria is " + str(insurance_cost) + " dollars.")
print(maria_insurance_cost)
# Initial variables for Omar
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  

# Estimate Omar's insurance cost 
cost1,omar_insurance_cost = calculate_insurance_cost(35,1,22.2,0,1,"omar")

#print("The estimated insurance cost for Omar is " + str(insurance_cost) + " dollars.")
print(omar_insurance_cost)


#assign values to different returns
calculate_insurance_cost(24,1,20.5,0,1,"kojo")
esti_cost,full_statement= calculate_insurance_cost(24,1,20.5,0,1,"kojo")
print(esti_cost)
print(full_statement)
#function to print the difference in insurance cost
def difference_in_insurance_cost(a,b):
  ans=b-a
  print("The difference in insurance cost is " + str(ans) +" dollars.")
difference_in_insurance_cost(cost1,cost2)