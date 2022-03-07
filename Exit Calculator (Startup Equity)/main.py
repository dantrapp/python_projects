eq = 0.05 #Your Equity In Percentage (i.e. 0.05 = 5%)
mc = 4 #Marketcap of company in billions. 
sell = 0.10 #Percentage of shares you'd sell after lockup.
company_total_shares = 10_000_000 #total issued shares of company
your_initial_equity_shares = (company_total_shares * eq)


#if non-RSA share allotment and if priced round; 409a valuation impacts options exercise.

value_409a = 10 * 1_000_000 #e.g. 5 = $5,000,000 valuation
option_cost = (value_409a / company_total_shares)
cost_to_exercise = (your_initial_equity_shares * option_cost)



def cap_calc(x, y, z):
  
  marketcap = (y * 1_000_000_000)
  per_share_value = (marketcap / company_total_shares)
  total = x * marketcap
  sold = total * z
  capgains = sold * .49
  longterm = sold * .65
  arr = .106
  roi = longterm * arr
  roi_lt = roi * .80
  remaining_equity_value = total - sold
  remaining_equity = (eq * 100) * (1 - sell)
  remaining_shares = (your_initial_equity_shares * (1 - sell))
  sold_shares = your_initial_equity_shares * sell
  total_ISO_profit = sold - cost_to_exercise
  per_share_profit = per_share_value - option_cost
 
 
  
  print(f"The Total Market Cap Of The Company Is: ${marketcap:,.2f}\n\nYour total holdings are ${total:,.2f} at {x:.2%} equity stake, with a total of {your_initial_equity_shares:,.2f} shares at a per share value of ${per_share_value:,.2f}.\n\n-- ISO/NSO - Option Cost Basis --\nIf your shares were purchased as ISO/NSO, instead of granted as restricted stock, we'll use the FMV per share from the 409a valuation to determine your option cost basis and profit.\n\nYour price per option ${option_cost:,.2f} is based on a 490a valuation of ${value_409a:,.2f}, so the total cost of exercising your options would be ${cost_to_exercise:,.2f} \n\nIf you sold {z:.2%} of your holdings it would equal {sold_shares:,.2f} shares worth ${sold:,.2f}, and netting a per share profit of ${per_share_profit:,.2f} and a total profit of ${total_ISO_profit:,.2f} if selling options instead of restricted stock.\n\nYou would be left with a remaining stake of {remaining_equity}% in the company, and a remaining share count of {remaining_shares:,.2f} worth ${remaining_equity_value:,.2f}\n\nYou'd have an estimated takehome of ${capgains:,.2f} after selling ${sold:,.2f} with a 51% capital gains tax. \n\nYou'd have ${longterm:,.2f} estimated takehome after selling ${sold:,.2f} with a long-term tax of 35%\n ")

  print(f"Using a low-to-moderate risk investing strategy, your ROI from an inital net of ${longterm:,.2f} (long-term) would gross ${roi:,.2f} on an annual rate of return at {arr:.2%} (average S&P return), and after 20% on long-term gains, a net of ${roi_lt:,.2f} per year after taxes.")


#RUN IT!
print(cap_calc(eq, mc, sell))
