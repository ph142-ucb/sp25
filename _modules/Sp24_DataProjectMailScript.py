import re

# Function to extract emails from a string
def extract_emails(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# Extract emails from the first sheet and second sheet
sheet1_emails = """
333adamjee@berkeley.edu
anoushkashukla@berkeley.edu
apingol@berkeley.edu


cristinazambrano@berkeley.edu
halvizurescruz@berkeley.edu
jrempel@berkeley.edu
katenotkatie@berkeley.edu
msramir@berkeley.edu
neel_patel@berkeley.edu
nmahida2004@berkeley.edu
phoebeh@berkeley.edu
roynuma@berkeley.edu
ryanhsu@berkeley.edu
sid.ramkrishnan@berkeley.edu
vflores724@berkeley.edu
_joycetruong@berkeley.edu
alina.akheli@berkeley.edu
andrescarrsol02@berkeley.edu
ashley.huerta@berkeley.edu
avijuan@berkeley.edu
chloelfoo@berkeley.edu
cleolin@berkeley.edu
emma.collo@berkeley.edu
fridacalvo@berkeley.edu
hanbin@berkeley.edu
kassiemendoza21@berkeley.edu
leeseunghwa@berkeley.edu
leungt@berkeley.edu
lwang26@berkeley.edu
lxly@berkeley.edu
matteolee24@berkeley.edu
meghana_ammula@berkeley.edu
mliu69@berkeley.edu
ryanou190@berkeley.edu
sophiasafa@berkeley.edu
varun.kandula@berkeley.edu
wlew0924@berkeley.edu
xinannawang@berkeley.edu
ellaliu@berkeley.edu
jasminelatimer@berkeley.edu
jeremiah.shim@berkeley.edu
jianpugao@berkeley.edu
jiayuan.li@berkeley.edu
jieyuz@berkeley.edu
jonannet@berkeley.edu
jxckchung123@berkeley.edu
lindathamizharasan@berkeley.edu
mayrap8@berkeley.edu
melaniecjulia@berkeley.edu
mgvelazquez@berkeley.edu
priyankakrishna@berkeley.edu
visitxay_hanmonty@berkeley.edu
vivianon@berkeley.edu
bawa@berkeley.edu
daria.wohlfarth@berkeley.edu
jasminelobo@berkeley.edu
lauren-tran@berkeley.edu
helena.liu@berkeley.edu
isabelleahuang@berkeley.edu
janeth05@berkeley.edu
peiyi.tampeng@berkeley.edu
richelmn@berkeley.edu
rubencorez8126@berkeley.edu
santiago.dordi@berkeley.edu
christindoan@berkeley.edu
cmacaraig@berkeley.edu
kvy@berkeley.edu
rachelarakawa@berkeley.edu
sabreenyaqubi@berkeley.edu
srujana.poluri@berkeley.edu
violetpark@berkeley.edu
wprosale@berkeley.edu
yunyicho@berkeley.edu
abedhammouda@berkeley.edu
beatricexle@berkeley.edu
czhang213@berkeley.edu
emanakilah@berkeley.edu
g.2021@berkeley.edu
garteaga03@berkeley.edu
jadavel03@berkeley.edu
jonathan.wang25@berkeley.edu
ktabot1@berkeley.edu
padmamuppirala@berkeley.edu
tathyas@berkeley.edu
wfdraco809@berkeley.edu
abigail.cruzreyes@berkeley.edu
anzhang9@berkeley.edu
camryn@berkeley.edu
cawong20@berkeley.edu
citlali.ac@berkeley.edu
cong0317@berkeley.edu
destinyogu@berkeley.edu
ecampbell02@berkeley.edu
isabellavibiana@berkeley.edu
jillliang0202@berkeley.edu
joellej@berkeley.edu
katesotelo8@berkeley.edu
lobo@berkeley.edu
mborozan@berkeley.edu
nairs24@berkeley.edu
seraphini.wang@berkeley.edu
svkang@berkeley.edu
vivianlucrecia@berkeley.edu
ade.keila@berkeley.edu
alexyu05152019@berkeley.edu
alma.g.castillo@berkeley.edu
annevictoriady@berkeley.edu
charissechih@berkeley.edu
ejkang@berkeley.edu
emm14@berkeley.edu
erikatam@berkeley.edu
esmegrenstam12@berkeley.edu
gracie.osborne27@berkeley.edu
ilham215@berkeley.edu
jane-lee@berkeley.edu
microraptorellchen@berkeley.edu
nkandlikar@berkeley.edu
pooja.manapat@berkeley.edu
srimank@berkeley.edu
sruthi.karanam@berkeley.edu
vikvij06@berkeley.edu
21millek@berkeley.edu
aditya04@berkeley.edu
adolfoescalante25@berkeley.edu
akasargod@berkeley.edu
alif.satyawan@berkeley.edu
anealsingh@berkeley.edu
beastybog@berkeley.edu
heidi.miao@berkeley.edu
huythomas16@berkeley.edu
hvhaisha@berkeley.edu
ishasharma12@berkeley.edu
jliu26@berkeley.edu
khushikethana@berkeley.edu
lucyekim@berkeley.edu
michaelramirez@berkeley.edu
namyar@berkeley.edu
nkeough@berkeley.edu
noemi_v@berkeley.edu
prekshaa@berkeley.edu
rithvik.chuppala@berkeley.edu
shailipatel@berkeley.edu
trishle@berkeley.edu
aaescoto@berkeley.edu
adeliner24@berkeley.edu
casey.nguyen@berkeley.edu
christopher.alog@berkeley.edu
clark_cutler@berkeley.edu
csowder@berkeley.edu
daleensidhu@berkeley.edu
elizabeth_lampley@berkeley.edu
ggppangg03@berkeley.edu
gissel82703@berkeley.edu
hcal.16@berkeley.edu
igknott@berkeley.edu
johnson.z.zhang@berkeley.edu
lindenlovett@berkeley.edu
matthew2024@berkeley.edu
meganminamide@berkeley.edu
michelle.zhao@berkeley.edu
mtea@berkeley.edu
nora_oyama@berkeley.edu
ranedragovich@berkeley.edu
roma_ranade@berkeley.edu
sannie@berkeley.edu
slindquist@berkeley.edu
stephenjrlee@berkeley.edu
vanessateo@berkeley.edu
adriana_ellard@berkeley.edu
amakhija1@berkeley.edu
arimhong@berkeley.edu
catherine.flowers@berkeley.edu
elhsieh@berkeley.edu
emmpitcher@berkeley.edu
jillianwilson@berkeley.edu
kevinlu15@berkeley.edu
lan.anthony@berkeley.edu
mariamaslai@berkeley.edu
mianikolev@berkeley.edu
parnitc@berkeley.edu
shrutigattapa@berkeley.edu
stephaniegiron@berkeley.edu
tcysun25@berkeley.edu
trevinoy@berkeley.edu
valahleli28@berkeley.edu
allernphun@berkeley.edu
andunn02@berkeley.edu
andylam2001@berkeley.edu
c-yu@berkeley.edu
donzeiserl@berkeley.edu
emsmith1@berkeley.edu
evacordero@berkeley.edu
francescamcohn@berkeley.edu
franklin90531@berkeley.edu
hannahkim1226@berkeley.edu
helen.jin@berkeley.edu
isadoraz@berkeley.edu
jabbler@berkeley.edu
jdm125@berkeley.edu
juliannagoldfarb@berkeley.edu
l.espinoza10@berkeley.edu
presleyp@berkeley.edu
rabiam1893@berkeley.edu
rishi_raghavan@berkeley.edu
stephwong@berkeley.edu
"""

sheet2_emails = """
nathanbrenner@berkeley.edu, preethi.subbiah@berkeley.edu, juliasarabia@berkeley.edu, sonomacarlos@berkeley.edu
annaloekito@berkeley.edu, deidra.lemoine@berkeley.edu, maximiliano.mendez@berkeley.edu, ldominguez21@berkeley.edu, vpuc@berkeley.edu 
abdurraheem@berkeley.edu, emrbrk112@berkeley.edu, abdurrahman@berkeley.edu, rovinya@berkeley.edu, ameliachloe@berkeley.edu
brendaduong@berkeley.edu, katherinejeiyun@berkeley.edu, winni52@berkeley.edu, jenellesoo@berkeley.edu
cindyn@berkeley.edu, johanzhang@berkeley.edu, jonathanpham2002@berkeley.edu, crystalong@berkeley.edu, jordanwu4@berkeley.edu
taloa_cardinal@berkeley.edu, mayaezekiel@berkeley.edu, romitakara@berkeley.edu, an_do@berkeley.edu, jrangel@berkeley.edu
francesca_kaitlynd@berkeley.edu, seanrezaie@berkeley.edu, azanahmed@berkeley.edu, daniela.villegas@berkeley.edu, adinathlane@berkeley.edu
spgyee@berkeley.edu, rmoe@berkeley.edu, johnnyluu@berkeley.edu, elwinter8768@berkeley.edu
charlize1001@berkeley.edu, franchesca_rb@berkeley.edu, eliang68@berkeley.edu, jacquelinewoo@berkeley.edu, emikmeng@berkeley.edu
alyssa.n.chang@berkeley.edu, steven.huang@berkeley.edu,  adithya_sivakumar@berkeley.edu, aileennathania@berkeley.edu
lucas_leon@berkeley.edu, lladrov@berkeley.edu, kaitlynmcdermott@berkeley.edu, davalynle@berkeley.edu, ellieyrkim@berkeley.edu 
ines.huret@berkeley.edu, ematcham@berkeley.edu, srosenblatt@berkeley.edu, jaimeleon374@berkeley.edu, alanguirre66@berkeley.edu
afolgar@berkeley.edu, bella.alcocer@berkeley.edu, colin.lowery@berkeley.edu, jasminet@berkeley.edu, leahbiruk@berkeley.edu
beatriceongawan@berkeley.edu, bryanchen13217@berkeley.edu, eshapuri@berkeley.edu, rachnasaha@berkeley.edu
kaylenelin@berkeley.edu, madisonbdavid@berkeley.edu, tycsun@berkeley.edu, prinsiiipe@berkeley.edu, ashleybui@berkeley.edu
shannonfinan@berkeley.edu, catherine.murphy@berkeley.edu, maddiebobbitt@berkeley.edu, lilycolbert@berkeley.edu
"ertan4@berkeley.edu, devinjleung@berkeley.edu, caitng07@berkeley.edu, hanalee25@berkeley.edu, chrisyoo@berkeley.edu	"
stephanymei@berkeley.edu, carmenramos@berkeley.edu, tranphuongnghi19@berkeley.edu, johanna.liu@berkeley.edu, anitachamraj@berkeley.edu
fengsuoyi@berkeley.edu, shuyingliu@berkeley.edu, derekxiang0605@berkeley.edu, mcongli@berkeley.edu
sxmao@berkeley.edu, shiyu_li@berkeley.edu, madeline_sit@berkeley.edu, al_rutherford@berkeley.edu, cioni_lia@berkeley.edu
ryannmayo@berkeley.edu, pateelkamak@berkeley.edu, zacchini@berkeley.edu, julietdelcore@berkeley.edu
drauchwerger@berkeley.edu,  collin.cunane@berkeley.edu, skybriggs@berkeley.edu, etain.williams@berkeley.edu, vherrero@berkeley.edu
anushkasavla@berkeley.edu, andalal@berkeley.edu, npkulkarni@berkeley.edu, nayna@berkeley.edu
sarpdkurtoglu@berkeley.edu, vlertchareonyong@berkeley.edu, patricia.hsieh@berkeley.edu, kyazgan@berkeley.edu, nicholas.labao@berkeley.edu
equijada@berkeley.edu, carolina.ibanez@berkeley.edu. joycetruong@berkeley.edu, sbecaria@berkeley.edu, bmtz@berkeley.edu
devinjleung@berkeley.edu, caitng07@berkeley.edu, ertan4@berkeley.edu, hanalee25@berkeley.edu, chrisyoo@berkeley.edu
hjkim04@berkeley.edu, seongju1126@berkeley.edu, wooji05@berkeley.edu, josh510@berkeley.edu
deeya.kalan@berkeley.edu, anishasavarala@berkeley.edu, payoonsalehi@berkeley.edu, anvidamani@berkeley.edu
selenashen@berkeley.edu, chloesun@berkeley.edu, tressiecostantino@berkeley.edu, ariakumar@berkeley.edu, veravictoria@berkeley.edu
mkatuna@berkeley.edu, madams3@berkeley.edu, mihir_pandya@berkeley.edu, deidra_lemoine@berkeley.edu
dianaoro03@berkeley.edu, fouza905@berkeley.edu, jiawuxie@berkeley.edu, laureho@berkeley.edu, davkiwins@berkeley.edu
fcdmelendres@berkeley.edu, itzelkm25@berkeley.edu, manisha10241999@gmail.com, nwalzer09@berkeley.edu
loriebmartinez@berkeley.edu, misookpham@berkeley.edu, cmsm@berkeley.edu, mia.kasilag@berkeley.edu
jasminegriffiths@berkeley.edu, ldelapena@berkeley.edu, dangtrantankhoa2205@berkeley.edu, ngoccatthinguyen@berkeley.edu
nathan.levy@berkeley.edu, jiyeon.suh@berkeley.edu, yaqubi@berkeley.edu, annajacobowitz@berkeley.edu, christindoan@berkeley.edu
yuchen_gao206@berkeley.edu, kennywong@berkeley.edu, langxil@berkeley.edu, braedenj@berkeley.edu, cesiagomezmarcelino@berkeley.edu
armandona@berkeley.edu, alex_yu@berkeley.edu, melodyfan928@berkeley.edu, 26matthewho@berkeley.edu, anneangeles@berkeley.edu
munenoch@berkeley.edu, erintak@berkeley.edu, elaina-55@berkeley.edu, andrewchan@berkeley.edu, lisaeun@berkeley.edu
kiannacastro@berkeley.edu, ndharni@berkeley.edu, kor.bear@berkeley.edu, dreamlopez@berkeley.edu, estrella.sanchez@berkeley.edu
bolos@berkeley.edu, julissa3922@berkeley.edu, shivaameryeyabut@berkeley.edu, isa.vivona@berkeley.edu, niraj@berkeley.edu
"""

sheet1_emails_list = extract_emails(sheet1_emails)
sheet2_emails_list = extract_emails(sheet2_emails)

# Remove duplicates
sheet1_emails_set = set(sheet1_emails_list)
sheet2_emails_set = set(sheet2_emails_list)

# Find missing emails
missing_emails = sheet1_emails_set - sheet2_emails_set

# Print missing emails
print("Missing Emails:")
for email in missing_emails:
    print(email)



#FORMULA #2
# # Define the list of email addresses and course codes
# listA_B = [
#     "apingol@berkeley.edu	pbhlth-142-lab-101b-in-person",
#     "anoushkashukla@berkeley.edu	pbhlth-142-lab-101b-in-person",
#     "anushkasavla@berkeley.edu	pbhlth-142-lab-101b-in-person",
#     # Add more email addresses and course codes as needed
# ]

# # Initialize dictionaries to store the course codes for each email domain
# course_dict = {}

# # Process each email and course code pair
# for entry in listA_B:
#     email, course_code = entry.split('\t')
#     domain = email.split('@')[1]

#     # Check if the domain already exists in the dictionary
#     if domain in course_dict:
#         # If the domain exists, append the course code to its list
#         course_dict[domain].append(course_code)
#     else:
#         # If the domain doesn't exist, create a new list with the course code
#         course_dict[domain] = [course_code]

# # Print the results
# for domain, courses in course_dict.items():
#     print(f"Domain: {domain}")
#     print("Courses:")
#     for course in courses:
#         print(course)
#     print()
