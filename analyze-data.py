from datetime import timedelta, date
import pandas as pd
import sys, datetime

def daterange(start, end):
  for n in range(int((end - start).days)):
    yield start + timedelta(n)

def main(argv):
  
  if len(argv) == 0:
    print('You must pass some parameters.')
    return

  df = pd.read_csv(argv[0])

  arg_split = argv[1].split('-')
  start_date = date(int(arg_split[0]), int(arg_split[1]), int(arg_split[2]))
  
  arg_split = argv[2].split('-')
  end_date = date(int(arg_split[0]), int(arg_split[1]), int(arg_split[2]))

  for single_date in daterange(start_date, end_date + timedelta(days=1)):
    print len(df.loc[df['date'].str.contains(str(single_date))].index)

  print 'Total Data: ', len(df.index)

if __name__ == '__main__':
  main(sys.argv[1:])