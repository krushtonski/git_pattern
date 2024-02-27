number_rows_of_stars = 4 #total number of rows because we start on 0
start = 0 #starting row number
end = (2 * number_rows_of_stars) #last row number
star_icon = "@"

#Create a for loop with if and else statements:


for row_number in range(start, end):  #Each row has a consequentive number from start to end for all the total rows
    if row_number <= number_rows_of_stars-1: #the number of stars is the same as the row number, if the row number is 5 or less
        print(star_icon)
        star_icon = star_icon + "@"
    else:
        print(star_icon)
        star_icon = star_icon[:-1] #Otherwise, print the reverse order
print("@")