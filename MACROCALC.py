def main():

  while True:
    print "*******Welcome to the MACRONUTRIENT CALCULATOR********"
    calorie_deficit = float(input("Enter your calorie deficit: "))
    Percent_protein = float(input("Percentage of Protein: "))
    Percent_carb = float(input("Percent of Carbohydrates: "))
    Percent_fat = float(input("Percentage of Fats: "))
    Macro_dict = {'Protein': Percent_protein, 'Carbohydrate': Percent_carb, 'Fats': Percent_fat}
    Macro_sum = Percent_protein + Percent_carb + Percent_fat

    if not Total_Macro_Check(Macro_sum):
      continue
    Macro_percentage_to_calorie(calorie_deficit, Percent_protein, Percent_carb, Percent_fat)

#------add food-------------------

    while True:
      diet_plan = raw_input("Would you like to add foods into your diet?(y/n): ")
      if diet_plan == 'y':
        item_name = raw_input("What is the name of the food you would like to add? ")
        size_serv = input("What is the size(grams) in each serving of %s? " % item_name)
        calorie_serv = input("How many calories is in each serving of %s? " % item_name)
        protein_serv = input("How many grams of protein is in each serving of %s? " % item_name)
        carb_serv = input("How many grams of carbohydrates is in each serving of %s? " % item_name)
        fat_serv = input("How many grams of fat is in each serving of %s? " % item_name)
        num_serv = input("How many servings of %s would you like to add? " % item_name)
      
#       diet_foodlist = add_food_item()
#       diet_foodlist.food_database(item_name, size_serv, calorie_serv, protein_serv, carb_serv, fat_serv)
#       diet_foodlist.food_in_diet(item_name, size_serv, calorie_serv, protein_serv, carb_serv, fat_serv, num_serv)
        v = food_database(item_name, size_serv, calorie_serv, protein_serv, carb_serv, fat_serv)
 #       x = food_in_diet(item_name, size_serv, calorie_serv, protein_serv, carb_serv, fat_serv, num_serv)
     
        print add_food(v)
        break

      if diet_plan == 'n':
        break
    answer = raw_input("Are you done using the calculator?(y/n): ")
    if not ask_to_leave(answer):
      break
    else:
      continue







def Total_Macro_Check(total_val):
  if total_val > 100:
    print "Total percentages surpassed 100! Please reenter percentages."
    return False
  if total_val < 100:
    print "Total precentages is less than 100! Please reenter precentages."
    return False
  return True

def Macro_percentage_to_calorie(calorie, protein, carb, fat):
  """ calories in 1 gram of P/C/F """
  cal_in_protein = 4  
  cal_in_fat = 9
  cal_in_carb = 4

  """ multiple percentages with calories """
  mult_protein = protein/100.0
  mult_fat = fat/100.0
  mult_carb = carb/100.0

  calories_of_protein = calorie*mult_protein
  grams_of_protein = calories_of_protein/cal_in_protein
  print "You must eat " + str(calories_of_protein) + " calories of protein which is equivalent to " + str(grams_of_protein) + " grams of protein."
 
  calories_of_fat = calorie*mult_fat
  grams_of_fat = calories_of_fat/cal_in_fat
  print "You must eat " + str(calories_of_fat) + " calories of fat which is equivalent to " + str(grams_of_fat) + " grams of fat."
 
  calories_of_carb = calorie*mult_carb
  grams_of_carb = calories_of_carb/cal_in_fat
  print "You must eat " + str(calories_of_carb) + " calories of carbohydrates which is equivalent to " + str(grams_of_carb) + " grams of carbohydrates."

def ask_to_leave(value):
  if value == 'y':
    return False
  elif value == 'n':
    return True



def food_database(item_name, size_serv, calorie_serv, protein_serv, carb_serv, fat_serv):
  # used to list the different foods when users ask for it
  # food database
  food_dict = [ {
    'food_name': item_name,
    'serving_size': size_serv,
    'serving_calorie': calorie_serv,
    'serving_protien': protein_serv,
    'serving_fat': fat_serv,
    'serving_carb': carb_serv
    } ]
  print food_dict
  return food_dict

def food_in_diet(item_name, size_serv, calorie_serv, protein_serv, carb_serv, fat_serv, num_serv):
    # used to show how much is in the diet plan for the user
  User_diet_dict = [ {
    'food_name': item_name,
    'amount': num_serv*size_serv,
    'serving_calorie': num_serv*calorie_serv,
    'serving_protien': protein_serv,
    'serving_fat': fat_serv,
    'serving_carb': carb_serv
    } ]
  print User_diet_dict
  return User_diet_dict


#---------------------------------------------------------------------------------------------------------------

def add_food(x):
  ask_to_add_another = raw_input("Would you like to add another food?(y/n)")
  if ask_to_add_another == 'y':
    # update
    item_name = raw_input("What is the name of the food you would like to add? ")
    size_serv = input("What is the size(grams) in each serving of %s? " % item_name)
    calorie_serv = input("How many calories is in each serving of %s? " % item_name)
    protein_serv = input("How many grams of protein is in each serving of %s? " % item_name)
    carb_serv = input("How many grams of carbohydrates is in each serving of %s? " % item_name)
    fat_serv = input("How many grams of fat is in each serving of %s? " % item_name)
    num_serv = input("How many servings of %s would you like to add? " % item_name)
    
    x.append( {
      'food_name': item_name,
      'serving_size': size_serv,
      'serving_calorie': calorie_serv,
      'serving_protien': protein_serv,
      'serving_fat': fat_serv,
      'serving_carb': carb_serv
    } )
 
#    User_diet_dict.append = ( {
#      'food_name': item_name,
#      'amount': num_serv*size_serv,
#      'serving_calorie': num_serv*calorie_serv,
#      'serving_protien': protein_serv,
#      'serving_fat': fat_serv,
#      'serving_carb': carb_serv
#    } )
    # add to the dictonary/list
#    print food_dict
    add_food(x)
    return x
  if ask_to_add_another == 'n':
    return False



if __name__ == "__main__":
  main()





