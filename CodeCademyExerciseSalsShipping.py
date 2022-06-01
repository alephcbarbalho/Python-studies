
package_weight = input("Enter your package weight: ")

ground_shipping1 = (float(package_weight) * 1.50 + 20.00)
ground_shipping2 = (float(package_weight) * 3.00 + 20.00)
ground_shipping3 = (float(package_weight) * 4.00 + 20.00)
ground_shipping4 = (float(package_weight) * 4.75 + 20.00)

ground_premium = 125.00

drone_shipping1 = (float(package_weight) * 4.50)
drone_shipping2 = (float(package_weight) * 9.00)
drone_shipping3 = (float(package_weight) * 12.00)
drone_shipping4 = (float(package_weight) * 14.25)

best_shipping = ("The best shipping cost for your package is: ")

if float(package_weight) <= 2.00:
    if ground_shipping1 < drone_shipping1 and ground_shipping1 < ground_premium:
        print(best_shipping + str(ground_shipping1))
    elif ground_premium < ground_shipping1 and ground_premium < drone_shipping1:
        print(best_shipping + str(ground_premium))
    else:
        print(best_shipping + str(drone_shipping1))

if float(package_weight) > 2.00 and float(package_weight) <= 6.00:
    if ground_shipping2 < drone_shipping2 and ground_shipping2 < ground_premium:
        print(best_shipping + str(ground_shipping2))
    elif ground_premium < ground_shipping2 and ground_premium < drone_shipping2:
        print(best_shipping + str(ground_premium))
    else:
        print(best_shipping + str(drone_shipping2))

if float(package_weight) > 6.00 and float(package_weight) <= 10.00:
    if ground_shipping3 < drone_shipping3 and ground_shipping3 < ground_premium:
        print(best_shipping + str(ground_shipping3))
    elif ground_premium < ground_shipping2 and ground_premium < drone_shipping3:
        print(best_shipping + str(ground_premium))
    else:
        print(best_shipping + str(drone_shipping3))

if float(package_weight) > 10.00:
    if ground_shipping4 < drone_shipping4 and ground_shipping4 < ground_premium:
        print(best_shipping + str(ground_shipping4))
    elif ground_premium < ground_shipping4 and ground_premium < drone_shipping4:
        print(best_shipping + str(ground_premium))
    else:
        print(best_shipping + drone_shipping4)
