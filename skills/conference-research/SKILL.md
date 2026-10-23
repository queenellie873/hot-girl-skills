---
name: conference-research
description: Before a conference or meetup, works out who the user should message. Finds which companies at the event are hiring for the roles they want, then finds the people they're loosely connected to at those companies (1st connections they rarely talk to, 2nd connections with a few mutuals, fellow alumni, old coworkers), checks who has posted about the event or said they'll be there, and ranks them. Hands back a shortlist with what they share and where each fact came from. Use when the user says "i'm going to X, who should i reach out to", "which companies at X are hiring for Y", "do i know anyone at these companies", or shares their LinkedIn connections export. Research only - it reads public pages and files the user provides, and never logs in, scrapes LinkedIn or sends anything. To write the messages, use cold-outreach-for-jobs. Based on the MIT and LinkedIn study "A Causal Test of the Strength of Weak Ties".
license: MIT
---

# conference research

figure out who to message before the event: the companies hiring for ur role, the people u half-know there, and which of them will actually be in the room. // a Hot Girls Code skill :)

**the event and what ur looking for:** $ARGUMENTS

if that's empty, use whatever the user pasted. if there's still nothing, ask one short question: "which event is it, and what roles are u going for?"

credit: the ranking comes from ["The power of weak ties in gaining new employment"](https://news.mit.edu/2022/weak-ties-linkedin-employment-0915) (MIT News, 2022), about the study "A Causal Test of the Strength of Weak Ties" by Rajkumar, Saint-Jacques, Bojinov, Brynjolfsson and Aral, published in *Science*. this skill turns the findings into steps an agent can follow.

## why weak ties

the study ran for five years across about 20 million LinkedIn users, and found that the people u know a little are more likely to lead to a new job than the people u know well. ur close friends mostly know the same people and openings u do. an acquaintance sits in a different circle and hears about things u never would. three findings shape this skill:

- **moderately weak beats both ends.** going by mutual connections, usefulness rises and then falls. the peak is around 10 mutuals: past that, the tie is too close to ur own circle to add much. as co-author Sinan Aral put it, "Moderately weak ties are the best"
- **the less u talk, the more they add.** going by how often two people message, the ties with the least contact led to the most job moves
- **it's strongest in tech.** the effect was biggest in digital, software-heavy industries

be honest with the user about what this is: a pattern across millions of people and the job moves that followed new connections. it isn't a promise that any one person will reply. use it to decide who goes first, not who gets left off.

## the five steps

1. what are u looking for
2. find who's hiring
3. find ur people
4. check who'll be there
5. rank them

do them in order. each step only uses what the steps before it confirmed.

## step 1: what are u looking for

ask for, and write down:

- the event: name, dates, city
- the roles: titles, level or years of experience, location or remote
- the user's own background, for matching later: schools, bootcamps or programs, past employers, communities and orgs they're part of

only use what the user tells u. don't fill in their background from their name or guess at it.

## step 2: find who's hiring

skip this if the user already has a company list. otherwise use a web search tool (TinyFish search and fetch if it's connected; any search tool works):

1. find the event's public exhibitor or sponsor list and pull the company names
2. check each company's own careers page for open roles that match. a job board is only a pointer to the real posting
3. keep a company only if u opened a page showing a matching role. note the role title, the experience line quoted from the posting, and the link
4. if a careers page wouldn't load or search, mark the company "couldn't check". don't guess

two things that catch people out:

- **titles don't tell u the level.** a title without "senior" often still asks for 5+ years, and "associate" means different things at different companies. open the posting and read the experience line every time
- **some postings are legal notices.** a posting written as "Employer / Title / Duties / Requirements", or "requires two (2) years of experience in the position offered", may be a labour-certification notice for someone already chosen. keep it, but tell the user to confirm with a recruiter that it's open to outside applicants

read public pages only: no logging in, no filling in forms, and no paid browser automation unless the user asks for it.

## step 3: find ur people

u can't see the user's network, and u shouldn't try to scrape it. work from what they give u. ask for whichever of these they can get:

- **their connections export.** LinkedIn lets u download ur own connections as a file (in settings, under data privacy, "get a copy of your data", then pick connections; the menus move around, so search LinkedIn help if it's not there). it lists each connection's name, company, position and the date u connected. read the file where it is and match the company column against the list from step 2. company names are typed by hand, so match loosely and flag anything ur unsure of. the export can be out of date, so mark every match "per ur export, check their profile"
- **people they looked up.** on a company's LinkedIn page, the people tab can be filtered by school and by connection level. the user runs the search and pastes or tells u the names, titles and how many mutual connections each one shows
- **people they already have in mind.** a recruiter who posted about the event, a speaker, someone from a community slack

for each person, ask the user two quick things if u don't have them: how many mutual connections, and when they last talked.

## step 4: check who'll be there

an in-person ask only works on someone who's going. for each person from step 3, find out if they've posted about the event or said they'll be there, and give them one of three labels:

| label | what counts | examples |
|---|---|---|
| **going** | they said so themselves, or the event says so | they're on the event's speaker list. they posted "see u in Houston" or "come find me at our booth". they told the user |
| **maybe** | a sign they care about the event, but nothing that says they'll be there | they shared or liked a post about it. they used the event hashtag. they're a recruiter at a company with a booth |
| **don't know** | nothing either way | no posts, no listing |

where to look:

- **public pages u can open:** the event's speaker and schedule pages, the company's blog or careers events page (these sometimes name who's staffing the booth), and public posts outside LinkedIn
- **what the user finds on LinkedIn:** they search posts for the event's name or hashtag, filter by the company or by their own connections, and paste or tell u who posted and what it said. u don't search LinkedIn urself

searches that tend to work: the event's name plus "booth", and the event's name filtered to the user's 1st connections. broad ones like "event + hiring + engineer" mostly return unrelated job posts. and posts almost never say what level a company is hiring for, so the level comes from step 2, not from posts

rules:

- **a label needs a source.** write down the post, page or sentence it came from. no source means "don't know"
- **"maybe" is never written as "going".** working at a company with a booth doesn't mean that person is travelling. the message for a "maybe" asks ("will u be at the event?"), it doesn't assume
- **quote posts, don't improve them.** if u mention what someone posted, use what it actually said
- **posts go stale.** note the date. a post from last year's event isn't a sign for this year
- **hashtags get reused.** a short event hashtag is often shared with other conferences, so search the event's name as well, and drop any post that's about a different event
- **not going isn't a dead end.** someone at a target company who isn't attending can still be asked who from their team will be at the booth

## step 5: rank them

first sort by tie, weakest useful ties on top:

| order | who | why | message to draft |
|---|---|---|---|
| 1 | **loose 1st connections** at a target company: connected, but haven't talked in ages or never really did | already connected, so a DM is free, and it's the kind of tie the study found most useful | hiring lead or fellow attendee |
| 2 | **2nd connections with a few mutuals** (1 to about 10), more so if they share a school, employer or community | the moderately weak middle. a mutual can also make the intro | mutual connection first, then the person |
| 3 | **shared background, no mutuals:** fellow alumni, same bootcamp or program, same past employer, same community | not connected yet, but there's a true first line | hiring lead or community |
| 4 | **no overlap:** recruiters, hiring leads and speakers at companies from step 2 | cold, but they're at the event to meet people | hiring lead or speaker |

then, inside each group, sort by step 4: **going** first, then **maybe**, then **don't know**.

one exception: someone with no overlap who is **going** and has **posted that they're hiring at the event** moves up to sit with group 2. they've told the world they want to be found.

**check what each person handles.** a recruiter's headline often says it ("campus recruiting", "internships only"). if they don't own the user's kind of role, keep them on the list but mark the message "ask who to meet": they can point the user to the right team, they just can't hire for it.

**close contacts go in their own lane.** a friend or old teammate at a target company should hear from the user today: they'll reply, and they can refer. just don't stop there. per the study, they're less likely to know about something the user doesn't already.

keep the list short. ten people the user really wants to meet beats fifty they'll never follow up with.

## never make anything up

- every person, title, company, school, mutual count and post comes from the user's file, the user's own words, or a public page u opened. if u can't say which, it doesn't go on the list
- never guess that two people share a school or employer because it looks likely. a shared thing counts only when both sides are confirmed
- never say someone is attending, hiring or posted something unless step 4 has a source for it
- never invent a contact, an email or a profile link. if the user needs one, they look it up
- if the export and what the user says disagree, ask

## keep other people's info private

the connections file is full of other people's details. read it where it is. don't copy it, don't paste it into a search or any outside tool, and ignore the email column completely. the shortlist is for the user only: nothing from it goes in a repo, a public doc or a PR.

## what u hand back

a short table, best first, then a note on anything u couldn't check.

| person | company and role | tie | what u share | going? | where it's from | draft |
|---|---|---|---|---|---|---|
| Renee A. | Northwind, engineering manager | 1st, last talked 2023 | worked together at a past internship | going: posted "come find me at our booth" last week | ur export + the post u pasted | hiring lead |
| Marcus T. | Northwind, recruiter | 2nd, 6 mutuals | same university | maybe: shared the event's schedule post | u looked him up | mutual connection, then hiring lead (ask if he'll be there) |
| Dani O. | Fabrikam, software engineer | none | same bootcamp | don't know | u told me | community |

(names and companies above are made up.)

under the table, list the open roles from step 2 that each company matched, with links, and remind the user to apply before they message anyone there. then offer to draft the messages with `cold-outreach-for-jobs`, naming the event and asking for a few minutes there.

## check before u deliver

- does every company have a role u opened a page for, with the link?
- does every person have a source for each detail?
- is every shared thing confirmed on both sides?
- does every "going" and "maybe" have a post or page behind it, with a date?
- is anyone marked as a hiring contact for a role they don't handle?
- is anyone marked "going" who is really a "maybe"?
- are loose ties ranked above close ones, with close contacts in their own lane?
- did u mark export matches as "check their profile"?
- is the list short enough to act on?
- did anything from the connections file leave the conversation? it shouldn't have
