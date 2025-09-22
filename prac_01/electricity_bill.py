# print("Electricity bill estimator")
# price_per_kwh = float(input("Enter cents per kWh: "))
# daily_use_kWh = float(input("Enter daily use in kWh: "))
# number_of_days = int(input("Enter number of billing days: "))
#
# estimated_bill = price_per_kwh / 100 * daily_use_kWh * number_of_day_in_billing_period
# print(f"Estimated bill: ${estimated_bill:.2f} ")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
print("Estimator automatically uses tariff 11 unless specificed")
tariff_type = input("Which tariff? 11 or 31: ")
if tariff_type == 31:
    price_per_kwh = TARIFF_31
else:
    price_per_kwh = TARIFF_11

daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))

estimated_bill = price_per_kwh * daily_use_kWh * number_of_days
print(f"Estimated bill: ${estimated_bill:.2f} ")
