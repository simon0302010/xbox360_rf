# xbox_rf init module script
# 
# Example that shows how to use the
# xbox_rf librabry
#
# Created by Tino Goehlert
# 
# www.astrorats.org | @_tin0_

import xbox_rf

# Initialize wiringPi and start
# Boot secuence.
print("initializing..")
xbox_rf.Init()
print("done")
