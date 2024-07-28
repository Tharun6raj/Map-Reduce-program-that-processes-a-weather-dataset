python
     from mrjob.job import MRJob

     class MRWeather(MRJob):
         def mapper(self, _, line):
             # Skip the header line
             if line.startswith("Date"):
                 return
             
             # Split the line into date and temperature
             date, temp = line.split(',')
             
             # Extract year from the date
             year = date.split('-')[0]
             
             # Emit year and temperature
             yield year, int(temp)

         def reducer(self, year, temps):
             # Find the maximum temperature for the year
             yield year, max(temps)

     if __name__ == '__main__':
         MRWeather.run()
