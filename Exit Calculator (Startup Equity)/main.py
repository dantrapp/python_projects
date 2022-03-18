eq = 0.01 #Your Total Equity In Percentage Of Company Authorized Shares (i.e. 0.05 = 5%)

mc = 3.65 #Marketcap of company in billions. Base this on any potential exit amount, or valuation in the instance of secondary share sale.

sell = 1 #Percentage of shares to sell (1 == 100%). Use less than 1 if selling in secondary markets (eg. .2 == 20%).

company_total_shares = 10_000_000 #total issued shares of company

your_initial_equity_shares = (company_total_shares * eq)

'''
ISO Configurator
if non-RSA share allotment and if priced round; 409a valuation impacts options exercise.
'''
  
value_409a = (3.8 * 1_000_000) #e.g. 5 = $5,000,000 valuation, configure this to adjust 409a valuation

option_cost = (value_409a / company_total_shares)
cost_to_exercise = (your_initial_equity_shares * option_cost)

'''
POST SERIES A DILUTION CALCULATOR: using a rough average dilution of 20% series A, 20% series B, 15% series C, 10% series D; calculate total dilution of shares
'''

rounds = [.8, .6, .45, .35] #aggregated round value dilution percentage; inverted for math.

total_rounds = 4 #adjust total funding rounds here


def dilution(x):
  total_dilution = 0
  global your_initial_equity_shares
  if total_rounds <= 4:
    total_dilution += (eq * rounds[x - 1])
  else: 
    total_dilution += (eq * rounds[3])
  return total_dilution
    
    


'''
MAIN CALCULATOR: Primary calculator that calculates and prints the output of the above functions + extra calculations within this function. 
'''

def main_calc(x, y, z):
  td = dilution(total_rounds)
  marketcap = (y * 1_000_000_000)
  per_share_value = (marketcap / company_total_shares)
  total = td * marketcap
  sold = total * z
  capgains = sold * .49 #adjust short-term cap gains %
  longterm = sold * .65 #adjust long-term cap gains %
  arr = .106 #average rate of return, based on SPY.
  roi = longterm * arr
  roi_lt = roi * .80 #long-term gains on investment
  remaining_equity_value = total - sold
  remaining_equity = (eq * 100) * (1 - sell)
  remaining_shares = (your_initial_equity_shares * (1 - sell))
  sold_shares = your_initial_equity_shares * sell
  total_ISO_profit = sold - cost_to_exercise
  per_share_profit = per_share_value - option_cost
 
 
  
  print(f"The Total Market Cap Of The Company Is: ${marketcap:,.2f}\n\nYour total holdings are ${total:,.2f} from {td:,.3%} remaining equity percentage after dilution from an original {x:.2%} equity stake after {total_rounds} total funding rounds from initial grant, with a total of {your_initial_equity_shares:,.2f} shares at an estimated per share value of ${per_share_value:,.2f} assuming a total of 10m authorized shares, not factoring for issuance of new shares in future funding rounds.\n\n-- ISO Option Cost Basis --\nIf you were given options in the form of ISO's, instead of granted shares as restricted stock awards (RSA's), we'll use the FMV per share from the current 409a valuation to determine your option cost basis and profit.\n\nYour price per option ${option_cost:,.2f} is based on a 409a valuation of ${value_409a:,.2f}, so the total cost of exercising {your_initial_equity_shares:,.2f} options would be ${cost_to_exercise:,.2f} if exercised before a rise in FMV.\n\nIf you sold {z:.2%} of your holdings it would equal {sold_shares:,.2f} shares worth ${sold:,.2f}, and netting a per share profit of ${per_share_profit:,.2f} and a total profit of ${total_ISO_profit:,.2f} if selling options instead of restricted stock.\n\nYou would be left with a remaining stake of {remaining_equity:,.2f}% in the company, and a remaining share count of {remaining_shares:,.2f} worth ${remaining_equity_value:,.2f}\n\nYou'd have an estimated takehome of ${capgains:,.2f} after selling ${sold:,.2f} with a 51% capital gains tax. \n\nYou'd have ${longterm:,.2f} estimated takehome after selling ${sold:,.2f} with a long-term tax of 35%\n ")

  print(f"Using a low-to-moderate risk investing strategy, your ROI from an inital net of ${longterm:,.2f} (long-term) would gross ${roi:,.2f} on an annual rate of return at {arr:.2%} (average S&P return), and after 20% on long-term gains, a net of ${roi_lt:,.2f} per year after taxes.")
       
       

#RUN IT!
#dilution(total_rounds) #execute dilution
print(main_calc(eq, mc, sell))
