eq = 0.05 #Your Equity In Percentage (i.e. 0.05 = 5%)
mc = 2.85 #Marketcap of company in billions. 
sell = 0.15 #Percentage of shares you'd sell after lockup.
company_total_shares = 10_000_000 #total issued shares of company
your_initial_equity_shares = (company_total_shares * eq)



def cap_calc(x, y, z):
  
  marketcap = (y * 1_000_000_000)
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
 
  
  print(f"The Total Market Cap Of The Company Is: ${marketcap:,.2f}\n\nYour total holdings are ${total:,.2f} at {x:.2%} equity stake, for a total of {your_initial_equity_shares:,.2f} shares. \n\nIf you sold {z:.2%} of your holdings it would be worth ${sold:,.2f}.\n\nYou would be left with a remaining stake of {remaining_equity}% in the company, for a remaining share count of {remaining_shares:,.2f}, worth ${remaining_equity_value:,.2f}\n\nYou'd have an estimated takehome of ${capgains:,.2f} after selling ${sold:,.2f} with a 51% capital gains tax. \n\nYou'd have ${longterm:,.2f} estimated takehome after selling ${sold:,.2f} with a long-term tax of 35%\n ")

  print(f"Using a low-to-moderate risk investing strategy, your ROI from an inital net of ${longterm:,.2f} (long-term) would gross ${roi:,.2f} on an annual rate of return at {arr:.2%}, and after 20% on long-term gains, a net of ${roi_lt:,.2f} per year after taxes.")


#RUN IT!
print(cap_calc(eq, mc, sell))
