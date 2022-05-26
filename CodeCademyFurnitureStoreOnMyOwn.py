
product1_name = "Lovely Loveseat"
product1_description = "Material: Tufted polyester blend on wood;\nDimensions: 32 inches high x 40 inches wide x 30 inches deep;\nColor options: Red or white."
product1_price = 254.00

product2_name = "Stylish Settee"
product2_description = "Material: Faux on birch;\nDimensions: 29.50 inches high x 54.75 inches wide x 28 inches deep;\nColor: Black."
product2_price = 180.50

product3_name = "Luxurious Lamp"
product3_description = "Material: Glass and iron;\nDimensions: 36 inches tall;\nColor: Brown with cream shade."
product3_price = 52.15

sales_tax = .088

greeting_part1 = "Hello and welcome to our Furniture Store! What is your name?"
print(greeting_part1)
customer_name = input("Please, share your name with us: ")
greeting_part2 = "Alright, " + customer_name + ", would you like to see our products list?"
print(greeting_part2)
customer_answer = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
product_list = 0
while product_list != 1:
    if customer_answer == "1":
        print("1: " + product1_name + "\n2: " + product2_name + "\n3: " + product3_name)
        product_list += 1
        know_details = 0
        customer_answer2 = input("And now, do you want to know more about one of them?\nAnswer:\n1: for details about " + product1_name + ";\n2: for details about " + product2_name + ";\n3: for details about " + product3_name + ";\n4: if you have lost your interest: ")
        while know_details != 1:
            if customer_answer2 == "1":
                print("Details about 1:" + product1_name + ":\n" + product1_description)
                know_details += 1
                know_price1 = 0
                customer_answer3 = input("Would you like to know " + product1_name + " price to decide if you'd want to check it out?\nAnswer 1 for \"Yes\" and 2 for \"No\": ")
                while know_price1 != 1:
                    if customer_answer3 == "1":
                        print("The price of " + product1_name + " is $" + str(product1_price))
                        know_price1 += 1
                        buying1_will = 0
                        customer_answer6 = input("Would you like to buy "+product1_name+" for $"+str(product1_price)+" plus taxes?\nAnswer 1 for \"Yes\" and 2 for \"No\": ")
                        while buying1_will != 1:
                            if customer_answer6 == "1":
                                print("Great choice! You won't regret it! It will be $"+str(product1_price+(product1_price*sales_tax))+". How would you like to pay?")
                                buying1_will += 1
                                payment1_method = 0
                                customer_answer9 = input("Answer 1 for \"Credit Card Payment\" or 2 for \"Payment in Cash\": ")
                                while payment1_method != 1:
                                    if customer_answer9 == "1":
                                        print("Alright! That's it! Thank you so much for buying a "+product1_name+" at our Furniture Store!")
                                        payment1_method += 1
                                    elif customer_answer9 == "2":
                                        print("Alright! That's it! Thank you so much for buying a "+product1_name+" at our Furniture Store!")
                                        payment1_method += 1
                                    else:
                                        print("I'm sorry, that's not a valid response for which form of payment you'd rather choose.")
                                        customer_answer9 = input("Answer 1 for \"Credit Card Payment\" or 2 for \"Payment in Cash\": ")
                            elif customer_answer6 == "2":
                                print("Thank you for showing up, anyway. Until next time!")
                            else:
                                print("I'm sorry, that's not a valid response for if you'd like to buy "+product1_name+" for $"+str(product1_price)+" plus taxes. ")
                                customer_answer6 = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
                    elif customer_answer3 == "2":
                        print("Thank you for showing up, anyway. Until next time!")
                        know_price1 += 1
                    else:
                        print("I'm sorry, that's not a valid response for if you'd like to know " + product1_name + " price to decide if you'd want to check it out. ")
                        customer_answer3 = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
            elif customer_answer2 == "2":
                print("Details about 2:" + product2_name + ":\n" + product2_description)
                know_details += 1
                know_price2 = 0
                customer_answer4 = input("Would you like to know " + product2_name + " price to decide if you'd want to check it out?\nAnswer 1 for \"Yes\" and 2 for \"No\": ")
                while know_price2 != 1:
                    if customer_answer4 == "1":
                        print("The price of " + product2_name + " is $" + str(product2_price))
                        know_price2 += 1
                        buying2_will = 0
                        customer_answer7 = input("Would you like to buy " + product2_name + " for $" + str(product2_price) + " plus taxes?\nAnswer 1 for \"Yes\" and 2 for \"No\": ")
                        while buying2_will != 1:
                            if customer_answer7 == "1":
                                print("Great choice! You won't regret it! It will be $" + str(product2_price + (product2_price * sales_tax)))
                                buying2_will += 1
                                payment2_method = 0
                                customer_answer10 = input("Answer 1 for \"Credit Card Payment\" or 2 for \"Payment in Cash\": ")
                                while payment2_method != 1:
                                    if customer_answer10 == "1":
                                        print("Alright! That's it! Thank you so much for buying a "+product2_name+" at our Furniture Store!")
                                        payment2_method += 1
                                    elif customer_answer10 == "2":
                                        print("Alright! That's it! Thank you so much for buying a "+product2_name+" at our Furniture Store!")
                                        payment2_method += 1
                                    else:
                                        print("I'm sorry, that's not a valid response for which form of payment you'd rather choose.")
                                        customer_answer10 = input("Answer 1 for \"Credit Card Payment\" or 2 for \"Payment in Cash\": ")
                            elif customer_answer7 == "2":
                                print("Thank you for showing up, anyway. Until next time!")
                            else:
                                print("I'm sorry, that's not a valid response for if you'd like to buy " + product2_name + " for $" + str(product2_price) + " plus taxes. ")
                                customer_answer7 = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
                    elif customer_answer4 == "2":
                        print("Thank you for showing up, anyway. Until next time!")
                        know_price2 += 1
                    else:
                        print("I'm sorry, that's not a valid response for if you'd like to know " + product2_name + " price to decide if you'd want to check it out. ")
                        customer_answer4 = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
            elif customer_answer2 == "3":
                print("Details about 3:" + product3_name + ":\n" + product3_description)
                know_details += 1
                know_price3 = 0
                customer_answer5 = input("Would you like to know " + product3_name + " price to decide if you'd want to check it out?\nAnswer 1 for \"Yes\" and 2 for \"No\": ")
                while know_price3 != 1:
                    if customer_answer5 == "1":
                        print("The price of " + product3_name + " is $" + str(product3_price))
                        know_price3 += 1
                        buying3_will = 0
                        customer_answer8 = input("Would you like to buy " + product3_name + " for $" + str(product3_price) + " plus taxes?\nAnswer 1 for \"Yes\" and 2 for \"No\": ")
                        while buying3_will != 1:
                            if customer_answer8 == "1":
                                print("Great choice! You won't regret it! It will be $" + str(product3_price + (product3_price * sales_tax)))
                                buying3_will += 1
                                payment3_method = 0
                                customer_answer11 = input("Answer 1 for \"Credit Card Payment\" or 2 for \"Payment in Cash\": ")
                                while payment3_method != 1:
                                    if customer_answer11 == "1":
                                        print("Alright! That's it! Thank you so much for buying a " + product3_name + " at our Furniture Store!")
                                        payment3_method += 1
                                    elif customer_answer11 == "2":
                                        print("Alright! That's it! Thank you so much for buying a " + product3_name + " at our Furniture Store!")
                                        payment3_method += 1
                                    else:
                                        print("I'm sorry, that's not a valid response for which form of payment you'd rather choose.")
                                        customer_answer11 = input("Answer 1 for \"Credit Card Payment\" or 2 for \"Payment in Cash\": ")
                            elif customer_answer8 == "2":
                                print("Thank you for showing up, anyway. Until next time!")
                            else:
                                print("I'm sorry, that's not a valid response for if you'd like to buy " + product3_name + " for $" + str(product3_price) + " plus taxes. ")
                                customer_answer8 = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
                    elif customer_answer5 == "2":
                        print("Thank you for showing up, anyway. Until next time!")
                        know_price3 += 1
                    else:
                        print("I'm sorry, that's not a valid response for if you'd like to know " + product3_name + " price to decide if you'd want to check it out. ")
                        customer_answer4 = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
            elif customer_answer2 == "4":
                print("Thank you for showing up, anyway. Until next time!")
                know_details += 1
    elif customer_answer == "2":
        print("Thank you for showing up, anyway. Until next time!")
        product_list += 1
    else:
        print("I'm sorry, that's not a valid response: ")
        customer_answer = input("Answer 1 for \"Yes\" and 2 for \"No\": ")
