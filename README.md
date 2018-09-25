# pill-bottle
Model the daily contents of a pill bottle that the user takes one half of a pill from each day.

Each day the user takes one pill from the bottle.  If it is a whole pill, the user cuts it in half, eats one half, and returns the other half to the bottle.  If it is a half pill, the user eats it.  The whole or half pill is pulled randomly from the bottle.

In this way, the number of half pill should initially increase, since the ratio of half pills to whole pills will be low.  In this case, it is more likely that the user will pull a whole pill, cut it in half, and return half to the bottle.

But as the number of whole pill decreases and the number of half pills increase, it becomes more likely that the user will pull a half pill, which will cause the half pills to decrease instead of increase, and cause the rate of whole pill to decrease more gradually.

This project aims to plot the daily:
  1. Count of whole pills left in the bottle
  2. Count of half pills left in the bottle
  3. Difference between the count of whole pills and count of half pills in the bottle

