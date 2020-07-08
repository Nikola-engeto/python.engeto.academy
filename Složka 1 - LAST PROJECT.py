import requests
import bs4
import csv

name = input('Zadejte jméno souboru:')
f = open(name + '.csv' , 'w')

f_writer = csv.writer(f)

web = requests.get(input('Zadejte odkaz na seznam obcí daného okresu:'))
soup = bs4.BeautifulSoup(web.text, "html.parser")

all_village = soup.find_all('td',{'class': 'cislo'})

statemen_header = False

for child in all_village:
    print(child.parent.find_all()[2].string) #
    list1 = []
    list1.append(child.find('a').string) #ID obce
    list1.append(child.parent.find_all()[2].string) #název obce

    exact_village = requests.get('https://volby.cz/pls/ps2017nss/'+child.find('a').attrs['href'])
    exact_village_soup = bs4.BeautifulSoup(exact_village.text, "html.parser")

    brutto_results = exact_village_soup.find(id="ps311_t1")
    list1.append(brutto_results.find('td',{'class':'cislo','headers':'sa2'}).string) #voliči v seznamu
    list1.append(brutto_results.find('td', {'class': 'cislo', 'headers': 'sa3'}).string) # vydane obalky
    list1.append(brutto_results.find('td', {'class': 'cislo', 'headers': 'sa6'}).string) #platné hlasy

    sides = exact_village_soup.find(id= "inner").find_all('tr')

    for line in sides:
        if not line.find('th'):
            list1.append(line.find_all('td',{'class':'cislo'})[1].string) #hlasy daných obcí daným stranám

    if not statemen_header:
        line_names = ['Code', 'Location', 'Registered', 'Envelopes', 'ValidVotes']
        for line in sides:
            if not line.find('th'):
                line_names.append(line.find_all('td')[1].string) #hledáme všechny názvy stran
        f_writer.writerow(line_names)
        statemen_header=True

    f_writer.writerow(list1)

f.close()