# Import client library
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import numpy as np

qdrant_client = QdrantClient(host='localhost', port=6333)

# Create collection
qdrant_client.recreate_collection(
    collection_name='startups', 
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)

qdrant_client.upload_collection(
    collection_name='startups',
    vectors=[
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
        np.random.rand(768).tolist(),
    ],
    payload=[
  {
    "name": "SaferCodes",
    "images": "https://safer.codes/img/brand/logo-icon.png",
    "alt": "SaferCodes Logo QR codes generator system forms for COVID-19",
    "description": "QR codes systems for COVID-19.\nSimple tools for bars, restaurants, offices, and other small proximity businesses.",
    "link": "https://safer.codes",
    "city": "Chicago"
  },
  {
    "name": "Human Practice",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/373036-94d1e190f12f2c919c3566ecaecbda68-thumb_jpg.jpg?buster=1396498835",
    "alt": "Human Practice -  health care information technology",
    "description": "Point-of-care word of mouth\nPreferral is a mobile platform that channels physicians\u2019 interest in networking with their peers to build referrals within a hospital system.\nHospitals are in a race to employ physicians, even though they lose billions each year ($40B in 2014) on employment. Why ...",
    "link": "http://humanpractice.com",
    "city": "Chicago"
  },
  {
    "name": "StyleSeek",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/3747-bb0338d641617b54f5234a1d3bfc6fd0-thumb_jpg.jpg?buster=1329158692",
    "alt": "StyleSeek -  e-commerce fashion mass customization online shopping",
    "description": "Personalized e-commerce for lifestyle products\nStyleSeek is a personalized e-commerce site for lifestyle products.\nIt works across the style spectrum by enabling users (both men and women) to create and refine their unique StyleDNA.\nStyleSeek also promotes new products via its email newsletter, 100% personalized ...",
    "link": "http://styleseek.com",
    "city": "Chicago"
  },
  {
    "name": "Scout",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/190790-dbe27fe8cda0614d644431f853b64e8f-thumb_jpg.jpg?buster=1389652078",
    "alt": "Scout -  security consumer electronics internet of things",
    "description": "Hassle-free Home Security\nScout is a self-installed, wireless home security system. We've created a more open, affordable and modern system than what is available on the market today. With month-to-month contracts and portable devices, Scout is a renter-friendly solution for the other ...",
    "link": "http://www.scoutalarm.com",
    "city": "Chicago"
  },
  {
    "name": "Invitation codes",
    "images": "https://invitation.codes/img/inv-brand-fb3.png",
    "alt": "Invitation App - Share referral codes community ",
    "description": "The referral community\nInvitation App is a social network where people post their referral codes and collect rewards on autopilot.",
    "link": "https://invitation.codes",
    "city": "Chicago"
  },
  {
    "name": "Hyde Park Angels",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/61114-35cd9d9689b70b4dc1d0b3c5f11c26e7-thumb_jpg.jpg?buster=1427395222",
    "alt": "Hyde Park Angels - ",
    "description": "Hyde Park Angels is the largest and most active angel group in the Midwest. With a membership of over 100 successful entrepreneurs, executives, and venture capitalists, the organization prides itself on providing critical strategic expertise to entrepreneurs and ...",
    "link": "http://hydeparkangels.com",
    "city": "Chicago"
  },
  {
    "name": "GiveForward",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/1374-e472ccec267bef9432a459784455c133-thumb_jpg.jpg?buster=1397666635",
    "alt": "GiveForward -  health care startups crowdfunding",
    "description": "Crowdfunding for medical and life events\nGiveForward lets anyone to create a free fundraising page for a friend or loved one's uncovered medical bills, memorial fund, adoptions or any other life events in five minutes or less. Millions of families have used GiveForward to raise more than $165M to let ...",
    "link": "http://giveforward.com",
    "city": "Chicago"
  },
  {
    "name": "MentorMob",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/19374-3b63fcf38efde624dd79c5cbd96161db-thumb_jpg.jpg?buster=1315734490",
    "alt": "MentorMob -  digital media education ventures for good crowdsourcing",
    "description": "Google of Learning, indexed by experts\nProblem: Google doesn't index for learning. Nearly 1 billion Google searches are done for \"how to\" learn various topics every month, from photography to entrepreneurship, forcing learners to waste their time sifting through the millions of results.\nMentorMob is ...",
    "link": "http://www.mentormob.com",
    "city": "Chicago"
  },
  {
    "name": "The Boeing Company",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/49394-df6be7a1eca80e8e73cc6699fee4f772-thumb_jpg.jpg?buster=1406172049",
    "alt": "The Boeing Company -  manufacturing transportation",
    "description": "",
    "link": "http://www.boeing.com",
    "city": "Chicago"
  },
  {
    "name": "NowBoarding \u2708\ufe0f",
    "images": "https://static.above.flights/img/lowcost/envelope_blue.png",
    "alt": "Lowcost Email cheap flights alerts",
    "description": "Invite-only mailing list.\n\nWe search the best weekend and long-haul flight deals\nso you can book before everyone else.",
    "link": "https://nowboarding.club/",
    "city": "Chicago"
  },
  {
    "name": "Rocketmiles",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/158571-e53ddffe9fb3ed5e57080db7134117d0-thumb_jpg.jpg?buster=1361371304",
    "alt": "Rocketmiles -  e-commerce online travel loyalty programs hotels",
    "description": "Fueling more vacations\nWe enable our customers to travel more, travel better and travel further. 20M+ consumers stock away miles & points to satisfy their wanderlust.\nFlying around or using credit cards are the only good ways to fill the stockpile today. We've built the third way. Customers ...",
    "link": "http://www.Rocketmiles.com",
    "city": "Chicago"
  },
  {
    "name": "EVENTup",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/23238-2b626f5dac2bd64425f502de100b652b-thumb_jpg.jpg?buster=1415649722",
    "alt": "EVENTup -  marketplaces bridging online and offline events online scheduling",
    "description": "Largest online marketplace for Event Spaces. \nEventup is a marketplace that allows consumers to find both commercial venues and unique residential properties and book them for their event. We make the venue selection and booking process easier and provide access to experiences that were previously unattainable ...",
    "link": "http://EVENTup.com",
    "city": "Chicago"
  },
  {
    "name": "Trunk Club",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/34734-030f38d5fbe71b30f8dff2516009aeef-thumb_jpg.jpg?buster=1331831837",
    "alt": "Trunk Club -  retail fashion personalization",
    "description": "Hand-selected outfits shipped to your door\nTraditional retail or e-commerce doesn't work well for most guys, and we\u2019ve built our business around the idea that there\u2019s a better way. We send guys a trunk of awesome clothes personalized for them by a real person on our team - each guy keeps what he likes and ...",
    "link": "http://www.trunkclub.com/",
    "city": "Chicago"
  },
  {
    "name": "Stylisted",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/198597-dc1e80e9fb5c325414a50872df92105a-thumb_jpg.jpg?buster=1430243061",
    "alt": "Stylisted -  location based services marketplaces beauty",
    "description": "Premier marketplace for in-home beauty service delivery\nStylisted is a website and mobile application that allows women to book in-home hair styling and makeup appointments from a network of vetted freelance beauty professionals.\nWomen want the help of skilled makeup artists and hairstylists for special event preparation, ...",
    "link": "http://www.Stylisted.com",
    "city": "Chicago"
  },
  {
    "name": "CancerIQ",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/183714-444e9d7ff2951c9713781f56d79f31e7-thumb_jpg.jpg?buster=1378406599",
    "alt": "CancerIQ -  health care information technology big data ventures for good personal health",
    "description": "Predictive analytics to eliminate cancer (Rock Health)\nOur team has modeled proven cancer genetics workflows at top academic centers, and translated them into a suite of digital health tools. Our cloud-based cancer risk clinic \u201cin a box\u201d, helps providers:\n- Predict cancer by automatically processing lifestyle, clinical, ...",
    "link": "http://www.canceriq.com",
    "city": "Chicago"
  },
  {
    "name": "Kiwi Solar",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/1029-4546f6ff9b57bccaa98ece907bdf6eb0-thumb_jpg.jpg?buster=1351632225",
    "alt": "Kiwi Solar -  clean technology clean energy solar residential solar",
    "description": "Simple, high-value solar ownership\nKiwi is bringing homeowners the simplest, most valuable way to own solar.\nThe JuiceBox, Kiwi\u2019s first product, brings together the best equipment, local installers, financing and software to make solar easy for homeowners to understand and buy.\nPVPower, now Kiwi, ...",
    "link": "http://www.ownkiwi.com",
    "city": "Chicago"
  },
  {
    "name": "YCharts",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/32997-13456632ed1acc1a9bbbd3a170035378-thumb_jpg.jpg?buster=1352834334",
    "alt": "YCharts -  financial services big data visualization investment management",
    "description": "The Financial Terminal of The Web.\nYCharts is a financial software company that was founded in 2009 and is backed by Morningstar. YCharts provides the analytic power of a financial terminal (such as Bloomberg, FactSet, CapIQ), but with the ease of use and accessibility of a modern website. Investment ...",
    "link": "https://ycharts.com",
    "city": "Chicago"
  },
  {
    "name": "Obama for America",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/75054-5d5e8c07899639dbc1b49faf8de7a5ec-thumb_jpg.jpg?buster=1352131410",
    "alt": "Obama for America -  politics",
    "description": "",
    "link": "http://barackobama.com",
    "city": "Chicago"
  },
  {
    "name": "Groupon",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/32211-2ebb323a7147718469ae5730c7dfb615-thumb_jpg.jpg?buster=1326842463",
    "alt": "Groupon -  retail deals discounts travel",
    "description": "Daily Deals. Delivered.\nGroupon features a daily deal on the best stuff to do, see, eat, and buy in 45 countries, and soon beyond (read: Space). We have about 10,000 employees working across our Chicago headquarters, a growing office in Seattle and Palo Alto, CA, local markets throughout ...",
    "link": "https://www.groupon.com",
    "city": "Chicago"
  },
  {
    "name": "Sidewalk",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/12882-50004250482c969e2c1c63b7228c708f-thumb_jpg.jpg?buster=1406856296",
    "alt": "Sidewalk -  lead generation big data sales automation small and medium businesses",
    "description": "Local intelligence layer\nSidewalk provides business intelligence for sales and marketing teams that enables them to close more deals faster with their dream SMB clients.\nSidewalk scores SMBs from 0-100 to determine their social rank and interest in your product so you don't have to. ...",
    "link": "http://www.getsidewalk.com",
    "city": "Chicago"
  },
  {
    "name": "Food Genius",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/23841-a051e2f9e346250aea64df756341d02a-thumb_jpg.jpg?buster=1315729457",
    "alt": "Food Genius -  food and beverages big data restaurants data mining",
    "description": "Feeding the foodservice Industry smarter data and analytics.\nWe're feeding the Foodservice Industry smarter data and analytics.\nFood Genius is a leading foodservice data provider specializing in gathering, preparing, and serving granular foodservice menu data and analytics. Food Genius supports foodservice manufacturers, ...",
    "link": "http://getfoodgenius.com",
    "city": "Chicago"
  },
  {
    "name": "Caterva",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/43240-b048dae5aced86e90596bd55f8d95335-thumb_jpg.jpg?buster=1339095691",
    "alt": "Caterva -  digital media social media machine learning big data",
    "description": "Engagement Automation\nCaterva is pioneering Engagement Automation solutions that utilize advances in big data, machine Learning, and social analytics. Our automated solutions enable websites to drive more engagement without requiring deep technical and analytical expertise or knowledge ...",
    "link": "http://caterva.com",
    "city": "Chicago"
  },
  {
    "name": "TempoIQ",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/79393-d67a8527c6dc6565999423ac06a92d48-thumb_jpg.jpg?buster=1334628110",
    "alt": "TempoIQ -  analytics big data databases internet of things",
    "description": "Sensor Data Analytics\nTempoDB is the time series database service. Available as a hosted or deployed solution, TempoDB makes it possible to store and analyze the massive streams of time series data generated by connected devices and sensors that break traditional databases.",
    "link": "http://tempoiq.com",
    "city": "Chicago"
  },
  {
    "name": "Konekt",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/317209-83b3feddd854007fb54abeb421fcf58b-thumb_jpg.jpg?buster=1410898855",
    "alt": "Konekt -  telecommunications developer tools internet of things cloud infrastructure",
    "description": "Build connected devices that work everywhere\nKonekt makes it incredibly easy for anyone to add cellular connectivity to their hardware devices. \u00a0Think of it as Heroku for Cellular Connected Hardware.\nKonekt allows makers, OEMs, and systems integrators of all sizes and levels of sophistication to build devices ...",
    "link": "http://www.konektdata.com",
    "city": "Chicago"
  },
  {
    "name": "MobileX Labs",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/103128-93fea14f97a464d21c7b60d9bf702a32-thumb_jpg.jpg?buster=1393466323",
    "alt": "MobileX Labs -  mobile SaaS mobile games gamification",
    "description": "Apps, Games, and Tools for the Mobile Generation\nMobileX Labs (MXL) is an uber fast growing app solutions company based in Chicago, IL. We currently operate under 3 company divisions.\nNativ App Builder\nWebsites are great, but Apps are better. Apps are the best way to get tailored content at your fingertips. ...",
    "link": "http://www.MobileXLabs.com",
    "city": "Chicago"
  },
  {
    "name": "Razorfish",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/33524-bdfcb9fb20de0dcc3ae67ef5672e6389-thumb_jpg.jpg?buster=1326843723",
    "alt": "Razorfish -  consulting",
    "description": "",
    "link": "http://www.razorfish.com",
    "city": "Chicago"
  },
  {
    "name": "Classkick",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/511338-4b5dc4a90922f53e0e816ef5c67c50c5-thumb_jpg.jpg?buster=1413389520",
    "alt": "Classkick -  k 12 education Higher Education",
    "description": "Students Learn Together\nNumbers\n- Launched fall 2014\n- 150K downloads\n- Average 30% wk/wk growth\n- 50 states / 70 countries\n- 45K questions answered/week\n- Engine of growth: 65% of signups are word-of-mouth, 100% are organic, $0 spent marketing\nCreated by teachers and engineers, Classkick ...",
    "link": "http://getclasskick.com",
    "city": "Chicago"
  },
  {
    "name": "Retrofit",
    "images": "https://d1qb2nb5cznatu.cloudfront.net/startups/i/31493-3f56c1c186e7c79d7bf75823efa49147-thumb_jpg.jpg?buster=1325984024",
    "alt": "Retrofit -  health care health care information technology personal health health and wellness",
    "description": "Expert-led, data-driven weight loss.\nRetrofit is the data-driven weight loss company. Created by the nation\u2019s leading obesity experts and using groundbreaking internet technology, we intend to deliver the industry\u2019s best outcomes. Obesity is America's #1 healthcare crisis. Because diets do not work, ...",
    "link": "http://www.retrofitme.com",
    "city": "Chicago"
  }
]
,
    batch_size=256
)
