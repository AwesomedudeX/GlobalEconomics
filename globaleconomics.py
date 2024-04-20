import streamlit as st

st.set_page_config(page_title="Global Economics Explained", page_icon="icon.jpg", layout="wide")

def titleft(text):
    st.write("---")
    st.title(f":green[{text}]")
    st.write("---")

def sep():
    st.write("---")


opts = ["Homepage", "The Bretton Woods Agreement", "The World Bank", "The International Monetary Fund (IMF)", "People of Economic Influence", "Modern Allied Trade Agreements"]

nav = st.sidebar.radio(":blue[**Navigate:**]", opts)

home = """
Our world, as of now, has globalized into a universal, :green[interconnected] economy. **Millions** of stocks are traded *daily*, all around the world. Companies have set up
headquarters internationally, building factories in foreign countries to maximize their income while putting the least amount of money in, through methods like child
labour where it is legal (eg. China or India), or outsourcing resources to acquire the same quality of material for a much, much lower price. This, however, relies on
the assumption that this connection is entirely secure, which - considering the scale of this reality - is very much ***not*** the case. There have been many cases of
company networks being hacked or compromised in some other way; one famous example being ***Rockstar Games*** - the company that owns (and develops) the *GTA* game
series.
\n
A hacker had managed to gain access to the files of *GTA VI* in its early development stages, and had leaked them to the public via an anonymous social media
account. However, eventually the hacker was caught and sued, and the files resecured, but the public had already started to lose hope for GTA VI, as it had appeared to
look terrible in the files that the hacker had leaked, which may end up reducing the game's future playerbase. These types of setbacks are just some of the smaller
results of company information being compromised, in some cases even leading to companies completely :red[**shutting down**]. For this reason, companies - however much money
they may be making - have to be careful about what they do and what they reveal to the public, because any small slip-ups could be the cause of the company's :red[**downfall**].
\n
:green[Economic globalization] is often helpful, being a catalyst for international relations and variety in products, as well as the combination of different ideas and designs
for various products. Though it is risky, as of now, it's clearly doing more **good** than **harm**, and it's up to the governments and citizens of the world to keep it that way.
"""

agr = """
The Bretton Woods agreement was an international agreement made in ***Bretton Woods, New Hampshire, USA, 1944***. It involved **44 allied countries** who were concerned about rebuilding
their economies after WWII, because of the amount of money and resources they'd spent on warfare and supplies. They wanted to establish a system of rules, institutions and methods that
would help them aid each other in growing their economies after the war. Essentially, it had established a new worldwide monetary system - an international network of institutions made
with the purpose of promoting trade between countries and the regulation of currencies among Western countries - which included a fixed exchange rate based on the *gold standard*. This
means that the value of a country's currency is set by the government, and all printed money must be backed up by gold reserves so that people could cash out in paper currency. However,
certain countries like China and Russia did not want to take part in this, instead building their own economies and growing powerful on their own.
\n
However, later on, the gold standard didn't work out so well, since it stopped the countries from printing money equal to the amount of gold that they actually had. This meant that; when
there was some sort of national crisis, a country would have to go into debt, borrowing money, and paying it back later, just as a regular citizen would get loans at the bank using credit,
and pay them back after a certain amount of time. However, governments (unlike citizens) are able to just print more money, and if they have too much debt, then the value of their country's
currency will drop. This leads to **inflation**, which is when a country gains more and more of its currency, but each unit of currency is worth less.
\n
By the 1960s, the US had high inflation rates, so on August 15, 1971, President Richard Nixon had \"closed the gold window\", which means that the US government would no longer redeem their
printed currency for gold. By 1976, all of the world's major currencies had **floating exchange rates**, which meant that their currency's value was decided on the foreign exchange market; the
market of those who want to buy and sell different currencies. This system continues to be used today, and is one of the major reasons why no currency's value ever stays the same, unless it
is no longer relevant in today's world. As of now, the exchange rates for currencies are based around the US dollar, and while they all affect each other, this currency is at the center of it
all, thanks to the USA's extremely strong economy.
"""

imf = """
The International Monetary Fund (IMF) is a United Nations agency that works in collaboration with the World Bank. It was created by the Bretton Woods Agreement (1944) to bring more stability to international
financial affairs and to assist with the expansion of world trade. It involved the same 44 allied countries that had contributed to the Bretton Wooods Agreement and was funded primarily by **quotas** (proportional
shares), which is an amount of money that each of the companies pay based on their economy; countries with a larger economy (like the USA) have to pay more than those with a smaller economy (like Tuvalu). The more
a country pays in their **quotas**, the more influence they'll have on the decisions they'll make involving the IMF.
\n
The IMF monitors exchange rates and provides short-term financial assistance to its member countries. It works to promote international cooperation, improve financial stability, encourage international trade,
boost employment rates, sustain economic growth and minimize poverty by doing 3 things:

 1. *Assess each company's current situation every year*
 2. *Offer funds and loans to member countries*
 3. *Keep services mostly free in areas of banking and financial system supervision and regulation*

These are the main things that the IMF does to achieve its goals. It also is responsible for monitoring exchange rates, promoting good governance and getting rid of corruption, and providing short-term help to
financially struggling countries, as well as to demand reforms in these countries so that they don't need further loans, and are able to pay off those that they have.
"""

wb = """
The World Bank Group - founded in 1944 and made up of the IBRD (International Bank for Reconstruction and Development) and the IDA (International Development Association) - is one of the largest sources of funding
and information for developing countries in the world. Its headquarters is located in Washington, DC, USA, and it has five institutions that share a common goal of minimizing poverty, improving general prosperity
and encouraging sustainable development internationally. It offers financing, policy advice and technical assistance to governments of developing countries, with the IDA focusing on the poorest countries, while the
IBRD focuses on the average-income and creditworthy poor countries. The World Bank works to improve the financial states of all countries, regardless of their class, but is limited by the companies that have stakes
in the IMF (International Monetary Fund); it tends to be more oriented towards economically large countries, since they pay more to have a higher stake in the IMF, which limits the other countries' ability to make
decisions, creating somewhat of a bias. However, things are improving, and the World Bank is working to help poorer countries get back on their feet, but sometimes, the control of powerful countries like the US
becomes an issue, preventing some countries from getting the help they need, while offering loans to certain corrupt military dictatorships.
"""

pei = """
After WWII, there were **3** important figures in early economic globalization, one disagreeing with the other two; John Maynard Keynes, Friedrich Hayek & Milton Friedman.
First, let's discuss Keynes;
\n
John Maynard Keynes believed that government intervention in the daily economy was neccessary to keep the economy stable. He said that their job was to prevent the economy from
destabilizing - if inflation started to show, and prices started to go up, it was the government's job to reduce their own (as well as their citizens') spending and to increase
taxes so that demand would come down and the currency's value would come back up; inversely, if a recession were to occur, the government was supposed to reduce taxes and promote
spending so that their economy would return to having enough money in circulation. This was accepted for a brief amount of time (~1945-1960) in most allied first world countries
like the US, Canada and Britain, before the theory of Hayek & Friedman started to become more popular.
\n
Their idea - which became popularized from the 1960s and after - was that society was too complicated to be planned, and so having a free society with minimal government intervention
was best. They argued that the market could not be tracked and predicted, so it was best to leave it to the people. However, this left 2 possibilities - either; the people would adjust
themselves based on current prices and product rates or; they would continue with whatever they were doing, leading to either inflation (too much spending - reduced monetary value) or
a recession (not enough money circulating - spiked monetary value and failing economy). If this happened, it would be hard to save, and the government would likely go a good bit further
into debt (most large countries nowadays are in debt) trying to rebalance the value of their currency.
\n
However, over time, these processes do take a toll on the value of a currency; 100 CAD in 1960 would be worth about 1000 CAD today (www.inflationcalculator.ca?y1=1960&y2=2023&i=100) - 10%
of what it was worth before! Though this does seem like an extremely large change, it happened over **63 years**, which means that it's not too late to stop the inflation. It all depends
on the citizens of the world, and the people that govern them.
"""

gatt = """
After the UN (United Nations) international alliance was formed (1945), 23 member countries came together to establish a UN agency in 1947 called the **General Agreement on Tariffs and Trade (GATT)**. The member
countries agreed to gradually get rid of *tariffs* - import tax, made to reduce competition between local and foreign products by causing an increase in sales price for imported products - and other trade barriers
between themselves, so that international trade could thrive, regardless of what countries were involved. The GATT is based on four basic principles:

1. To conduct trade without discrimination (between the buying or selling countries)
2. To treat imported goods from member countries in the same way as similar local goods
3. To protect local industries in member countries through tariffs; not with import quotas or fees
4. To require any country that applied to become a member to present a list of tariffs and other trade restrictions that would be imposed on member countries

By 1955, the GATT had 131 members and accounted for more than 90% of international trade; this then went on to become the World Trade Organization (WTO).
"""

nafta = """
In 1989, Canada and the US signed the Free Trade Agreement, which opened up trade between them and removed many tariffs. This was done because Canada wanted access to the US's vast market, and the US wanted access
to Canada's many natural resources. This was mutually beneficial, as Canada could provide resources to the US while making a profit, while the US could sell goods back to Canada, creating a cycle that helps both
countries. However, Canada was able to keep the right to protect its cultural industries and other areas like education and healthcare; it had also excluded a few resources, like water.
\n
Unfortunately, this immediately created controversy in Canada, as some people believed that the deal would inevitably undermine Canada's independence, and that it would slowly lose it to the US. Fortunately, this
hadn't stopped the agreement from continuing on, and in 1994, when Mexico was added to the agreement, it became the North American Free Trade Agreement (NAFTA). At this time, it became the largest free trade area
in the world, with a population of 360 000 000 people!
\n
NAFTA had immediately eliminated half of the trade barriers between all three countries, and would gradually remove the rest in the next 15 years. The benefits and losses of this agreement are controversial, but
it has appeared to work well as of now, despite having caused many losses in all three countries.
"""

usmca = """
The **USMCA (United States-Mexico-Canada Agreement)** is an updated version of the **North American Free Trade Agreement (NAFTA)** that had replaced it in 2018. Essentially, it was a modernized version of **NAFTA**
that was modified to include other provisions like information-based property, digital trade and more environmental and worker regulations. Each country had made various compromises to finalize the agreement; one
example was that the US got increased access to Canada's cheese market, which led to online shoppers in Canada seeing an increase in duty-free limits, which went from \$20 to \$150. These was also an agreement that
the deal would be reviewed (and modified if needed) by all three countries every six years.
"""

if nav == "Homepage":
    titleft("Global Economics Explained")
    st.write(home)

elif nav == "The Bretton Woods Agreement":
    titleft("The Bretton Woods Agreement")
    st.image("brettonwoods.jpg", "https://www.rachanaranade.com/blog/bretton-woods-agreement", width=1000)
    sep()
    st.write(agr)

elif nav == "The International Monetary Fund (IMF)":
    titleft("The International Monetary Fund (IMF)")
    st.image("imf.png", "https://en.wikipedia.org/wiki/International_Monetary_Fund", width=500)
    st.write(imf)

else:

    titleft(nav)

    if nav == "The World Bank":
        st.image("wb.jpg", "https://www.im-portal.org/membership/members/world-bank", width=600)
        st.write(wb)

    elif nav == "People of Economic Influence":

        c1, c2, c3 = st.columns(3)

        c1.subheader("John Maynard Keynes")
        c2.subheader("Friedrich Hayek")
        c3.subheader("Milton Friedman")

        sep()

        c1.image("johnmaynardkeynes.jpg", "https://www.stfaiths.co.uk/profile/john-maynard-keynes/")
        c2.image("friedrichhayek.jpg", "https://www.britannica.com/biography/F-A-Hayek")
        c3.image("miltonfriedman.jpg", "https://www.cato.org/milton-friedman-bio", width=310)


        st.write(pei)

    elif nav == "Modern Allied Trade Agreements":

        c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

        c1.image("gatt.jpg", "https://www.linkedin.com/pulse/principles-objectives-article-7-gatt-arnaud-partie")
        c3.image("nafta.jpg", "https://www.agweb.com/news/policy/nafta-20-timeline-murky")
        c5.image("usmca.jpg", "https://usmca.com/", width=400)

        sep()

        ex1 = st.expander("General Agreement on Tariffs and Trade (GATT)")
        ex1.subheader(":green[General Agreement on Tariffs and Trade (GATT)]", divider=True)
        ex1.write(gatt)

        c1, c2 = st.columns(2)
        
        ex2 = c1.expander("North American Free Trade Agreement (NAFTA)")
        ex2.subheader(":green[North American Free Trade Agreement (NAFTA)]", divider=True)
        ex2.write(nafta)
        
        ex3 = c2.expander("United States-Mexico-Canada Agreement (USMCA)")
        ex3.subheader(":green[United States-Mexico-Canada Agreement (USMCA)]", divider=True)
        ex3.write(usmca)
