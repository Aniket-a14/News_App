import requests
import pycountry


print("\t\t\t\t\t\t\t\t---------------WELCOME TO NEWS APP---------------")
input_country = input("\n\nName of the country you want to search news for: ")
input_countries = [f'{input_country.strip()}']
countries = {}


for country in pycountry.countries:
  countries[country.name] = country.alpha_2

while True:
  codes = [countries.get(country.title(), 'Unknown code')
      for country in input_countries]
  
  
  option = input("\n\nWhich category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
  
  
  response = requests.get(f'https://newsapi.org/v2/top-headlines?country={codes[0]}&category={option}&apiKey=5b6a46e4be3749de84be7111c82ed3c4')
  top_headlines = response.json()
  
  
  
  Headlines = top_headlines['articles']
  
  if Headlines:
      for articles in Headlines:
        b = articles['title'][::-1].index("-")
        if "news" in (articles['title'][-b+1:]).lower():
          print(
            f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
        else:
          print(
            f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
  else:
    print(f"Sorry no articles found for {input_country}, Something Wrong!!!")
  option = input("\nDo you want to search again[Yes/No]?")
  if option.lower() == 'no':
    print("\nThank you!!\nDo visit again")
    break

