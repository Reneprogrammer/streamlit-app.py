import streamlit as st
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np

# Set up the Streamlit app
st.title('World Population Map')

# Corrected population data with potential comma issues fixed
data = """
Country,Population
China,1409670000
India,1400744000
United States,335893238
Indonesia,279118866
Pakistan,241499431
Nigeria,223800000
Brazil,203080756
Bangladesh,169828911
Russia,146150789
Mexico,129625968
Japan,124000000
Philippines,112892781
Ethiopia,107334000
Egypt,104462545
Vietnam,100300000
"Democratic Republic of the Congo",95370000
Turkey,85372377
Germany,84607016
Iran,84055000
France,68394000
United Kingdom,67596281
Thailand,66090475
South Africa,62027503
Tanzania,61741120
Italy,58972268
Myanmar,55770232
Colombia,52695952
Kenya,51526000
South Korea,51293934
Spain,48592909
Argentina,46654581
Uganda,45562000
Algeria,45400000
Iraq,43324000
Sudan,41984500
Canada,40769890
Poland,37620000
Morocco,37022000
Uzbekistan,36963262
Ukraine,36700000
Afghanistan,34262840
Angola,34094077
Peru,33725844
Malaysia,33379500
Mozambique,32419747
Saudi Arabia,32175224
Yemen,31888698
Ghana,30832019
Ivory Coast,29389150
Nepal,29164578
Venezuela,28302000
Cameroon,28088845
Madagascar,26923353
Australia,26821557
North Korea,25660000
Niger,25369415
Taiwan,23420442
Syria,22923000
Burkina Faso,22752315
Mali,22395489
Sri Lanka,22037000
Malawi,21507723
Kazakhstan,20075271
Chile,19960889
Zambia,19610769
Romania,19051562
Senegal,18275743
Somalia,18143379
Netherlands,17967505
Guatemala,17602431
Chad,17414717
Cambodia,17091464
Ecuador,16938986
Zimbabwe,15178979
South Sudan,14746494
Guinea,13261638
Rwanda,13246394
Burundi,12837740
Benin,12606998
Bolivia,12006031
Tunisia,11850232
Belgium,11820117
Papua New Guinea,11781559
Haiti,11743017
Jordan,11516000
Cuba,11089511
Czech Republic,10900555
Dominican Republic,10760028
Sweden,10549287
Portugal,10467366
Greece,10413982
Azerbaijan,10151517
Tajikistan,10077600
Israel,9880000
Honduras,9745149
Hungary,9584000
United Arab Emirates,9282410
Belarus,9200617
Austria,9159993
Switzerland,8960817
Sierra Leone,8494260
Togo,8095498
"Hong Kong (China)",7498100
Laos,7443000
Kyrgyzstan,7100000
Turkmenistan,7057841
Libya,6931061
El Salvador,6884888
Nicaragua,6733763
Serbia,6641197
Bulgaria,6445481
"Republic of the Congo",6142180
Paraguay,6109644
Denmark,5961249
Singapore,5917600
"Central African Republic",5633412
Finland,5574011
Norway,5550203
Lebanon,5490000
Palestine,5483450
Slovakia,5424687
Ireland,5281600
New Zealand,5305600
Costa Rica,5262225
Liberia,5248621
Oman,5113071
Kuwait,4670713
Mauritania,4475683
Panama,4064780
Croatia,3855641
Eritrea,3748902
Georgia,3694600
Mongolia,3457548
Uruguay,3444263
"Bosnia and Herzegovina",3277082
"Puerto Rico (US)",3205691
Namibia,3022401
Armenia,2993800
Lithuania,2886515
Jamaica,2825544
Albania,2761785
Qatar,2656032
Moldova,2512758
Gambia,2417471
Botswana,2410338
Lesotho,2306000
Gabon,2233272
Slovenia,2123103
Latvia,1872500
"North Macedonia",1832696
"Guinea-Bissau",1781308
Kosovo,1762220
Bahrain,1577059
"Equatorial Guinea",1558160
"Trinidad and Tobago",1367510
Estonia,1366491
"East Timor",1354662
Mauritius,1261041
Eswatini,1223362
Djibouti,1001454
Cyprus,918100
Fiji,893468
Bhutan,770276
Comoros,758316
Guyana,743699
"Solomon Islands",734887
"Macau (China)",683700
Luxembourg,672020
Montenegro,616695
Suriname,616500
"Western Sahara",587259
Malta,519562
Maldives,515132
"Cape Verde",491233
Brunei,445400
Belize,397483
Bahamas,397360
Iceland,383726
"Northern Cyprus",382836
Transnistria,360938
Vanuatu,301295
"French Polynesia (France)",279890
"New Caledonia (France)",268510
Barbados,267800
Abkhazia,244236
"São Tomé and Príncipe",214610
Samoa,205557
"Saint Lucia",178696
"Guam (US)",153836
"Curacao (Netherlands)",148925
Kiribati,120740
Grenada,112579
"Saint Vincent and the Grenadines",110872
"Aruba (Netherlands)",106739
Micronesia,105754
"Jersey (UK)",103267
"Antigua and Barbuda",100772
Seychelles,100447
Tonga,100179
"U.S. Virgin Islands (US)",87146
Andorra,85101
"Isle of Man (UK)",84530
"Cayman Islands (UK)",71105
Dominica,67408
"Guernsey (UK)",64091
"Bermuda (UK)",64055
"Greenland (Denmark)",56865
"South Ossetia",56520
"Faroe Islands (Denmark)",54547
"American Samoa (US)",49710
"Northern Mariana Islands (US)",47329
"Saint Kitts and Nevis",47195
"Turks and Caicos Islands (UK)",46131
"Sint Maarten (Netherlands)",42938
"Marshall Islands",42418
Liechtenstein,40023
Monaco,38367
"Gibraltar (UK)",34003
"San Marino",33916
"Saint Martin (France)",32358
"British Virgin Islands (UK)",31538
"Åland (Finland)",30547
Palau,16733
"Anguilla (UK)",15701
"Cook Islands",15040
Nauru,11680
"Wallis and Futuna (France)",11369
Tuvalu,10679
"Saint Barthélemy (France)",10585
"Saint Pierre and Miquelon (France)",6092
"Saint Helena, Ascension and Tristan da Cunha (UK)",5651
"Montserrat (UK)",4433
"Falkland Islands (UK)",3662
"Norfolk Island (Australia)",2188
"Christmas Island (Australia)",1692
Niue,1689
"Tokelau (NZ)",1647
"Vatican City",764
"Cocos (Keeling) Islands (Australia)",593
"Pitcairn Islands (UK)",47
"""

# Map settings (you can add your map visualization code here)
# Create some data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sine Wave')

# Display the figure using st.pyplot()
st.pyplot(fig)


