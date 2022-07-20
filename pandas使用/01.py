import pandas as pd

mydataset = {
  'sites': ["Google", "Ru noob", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)