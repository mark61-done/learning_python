#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
name = "  JOHn  ."
clean_name = name.strip().lower().replace('.','')
print(clean_name)  # Output: john

#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_one = "The Dog Breed is German Shepherd"
sliced_one = sentence_one[8:22]
print(sliced_one)  # Output: Breed is German
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
sliced_two = sentence_two[13:29]
print(sliced_two)  # Output: Clinton forces

#Split the below sentence using a semicolon
# i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
sentence = "The lazy dog; ran so fast; it hit the wall."
split_sentence = sentence.split(';')
print(split_sentence)  # Output: ['The lazy dog', ' ran so fast', ' it hit the wall.']
print(len(split_sentence))  # Output: 3

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name = "  Joh.n"
last_name = "   Do,e"
clean_first_name = first_name.strip().replace('.', '')
clean_last_name = last_name.strip().replace(',', '')
full_name = clean_first_name + " " + clean_last_name
print(full_name)  # Output: John Doe

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
clean_r = r.strip('[]').replace('"', '').replace(',', '')
print(clean_r)  # Output: EWC

num1 = 2000
num
