# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def clean_damages(lst):
  new_lst=[]
  conversion = {"M": 1000000,
              "B": 1000000000}
  for item in lst:
    if item.find('M') != -1:
      new_item = item.strip('M')
      new_item_float = float(new_item) * conversion.get("M")
      new_lst.append(new_item_float)
    elif item.find('B') != -1:
      new_item = item.strip('B')
      new_item_float = float(new_item) * conversion.get("B")
      new_lst.append(new_item_float)
    else:
      new_lst.append(item)

  return new_lst


updated_damages = clean_damages(damages)

print(updated_damages)

# write your construct hurricane dictionary function here:

def hurricane_by_name(lst):
  hurricanes = {}
  for i in range(0, 34):
    hurricane = {}
    hurricane[i] = {
      "Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": updated_damages[i],
      "Deaths": deaths[i]}
    hurricanes[lst[i]] = hurricane[i]
  return dict(hurricanes)

hurricane_by_name = hurricane_by_name(names)

print(hurricane_by_name)


# write your construct hurricane by year dictionary function here:

def hurricane_by_year(dict_):

  hurricanes_by_year = {}

  for hurricane in dict_.values():
    current_year = hurricane["Year"]
    current_cane = hurricane
    if current_year not in hurricanes_by_year.keys():
      hurricanes_by_year[current_year] = [current_cane]
    else:
      hurricanes_by_year[current_year].append([current_cane])


  return dict(hurricanes_by_year)

hurricane_by_year = hurricane_by_year(hurricane_by_name)

print(hurricane_by_year)

# write your count affected areas function here:

def areas_counter(dict_):

  counter_dict = {}

  for hurricane in dict_.values():
    areas_affected = hurricane.get("Areas Affected")
    #print(areas_affected)
    for area in areas_affected:
      if area not in counter_dict.keys():
        count_value = 1
        counter_dict[area] = count_value
      else:
        counter_dict[area] +=1

  return dict(counter_dict)


print(areas_counter(hurricane_by_name))

# write your find most affected area function here:

def most_affected(areas_affected):
  counter_dict = {}
  max_area = str()
  max_area_count = 0
  for lst in areas_affected:
    for item in lst:
      if item not in counter_dict.keys():
        count_value = 1
        counter_dict[item] = count_value
      else:
        counter_dict[item] +=1

  for key,value in counter_dict.items():
    if value >= max_area_count:
      max_area_count = value
      max_area = key
    else:
      None

  return dict(counter_dict), max_area, max_area_count

most_affected = most_affected(areas_affected)

print(most_affected)


# write your greatest number of deaths function here:

def number_deaths(_dict):

  max_death_hurricane = str()
  max_death = 0

  for hurricane in _dict.values():
    if hurricane.get("Deaths") > max_death:
      max_death_hurricane = hurricane["Name"]
      max_death = hurricane.get("Deaths")
    else:
      None
  return max_death_hurricane, max_death

#print(number_deaths(hurricane_by_name))

# write your catgeorize by mortality function here:
def mortality_rating(_dict):

  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

  mortality_scale = {0: 0,
                    1: 100,
                    2: 500,
                    3: 1000,
                    4: 10000}

  for hurricane in _dict.values():
    if hurricane.get("Deaths") > 0 and hurricane.get("Deaths") <= 100:
      hurricanes_by_mortality[0].append(hurricane.get("Name"))
    elif hurricane.get("Deaths") > 100 and hurricane.get("Deaths") <= 200:
      hurricanes_by_mortality[1].append(hurricane.get("Name"))
    elif hurricane.get("Deaths") > 200 and hurricane.get("Deaths") <= 500:
      hurricanes_by_mortality[2].append(hurricane.get("Name"))
    elif hurricane.get("Deaths") > 500 and hurricane.get("Deaths") <= 1000:
      hurricanes_by_mortality[3].append(hurricane.get("Name"))
    elif hurricane.get("Deaths") > 1000 and hurricane.get("Deaths") <= 10000:
      hurricanes_by_mortality[4].append(hurricane.get("Name"))
    elif hurricane.get("Deaths") > 10000:
      hurricanes_by_mortality[5].append(hurricane.get("Name"))


  return dict(hurricanes_by_mortality)


mort_rating = mortality_rating(hurricane_by_name)

print(mort_rating)

# write your greatest damage function here:

def max_damage(_dict):

  max_damage_hurricane = str()
  max_damage = 0

  for hurricane in _dict.values():
    if hurricane.get("Damage") == "Damages not recorded":
      None
    elif hurricane.get("Damage") > max_damage:
      max_damage_hurricane = hurricane["Name"]
      max_damage = hurricane.get("Damage")
      continue
  return max_damage_hurricane, max_damage

max_damage = max_damage(hurricane_by_name)

print(max_damage)

# write your catgeorize by damage function here:

def damage_rating(_dict):

  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}

  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}

  for hurricane in _dict.values():
    if hurricane.get("Damage") == "Damages not recorded":
      None
    elif hurricane.get("Damage") == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricane.get("Name"))
    elif hurricane.get("Damage") > damage_scale[0] and hurricane.get("Damage") <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricane.get("Name"))
    elif hurricane.get("Damage") > damage_scale[1] and hurricane.get("Damage") <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricane.get("Name"))
    elif hurricane.get("Damage") > damage_scale[2] and hurricane.get("Damage") <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricane.get("Name"))
    elif hurricane.get("Damage") > damage_scale[3] and hurricane.get("Damage") <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricane.get("Name"))
    elif hurricane.get("Damage") > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricane.get("Name"))


  return dict(hurricanes_by_damage)


damage_rating = damage_rating(hurricane_by_name)

print(damage_rating)
