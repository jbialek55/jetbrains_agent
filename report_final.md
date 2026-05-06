# Content Usage Analysis: dyatlow.txt

## Methodology

1. **Source article**: `dyatlow.txt` — analyzed in full
2. **Query generation**: LLM (2 models with random rotation) generated 40 targeted search queries covering Reddit, Quora, X/Twitter, and academic sources
3. **Search & scrape**: Tavily AI (`search_depth=advanced`) retrieved up to 4 results per query, deduplicated by URL
4. **Filtering**: Pages with fewer than 500 characters or paywall/error indicators were discarded
5. **Classification**: Each page compared to source article by LLM using 6-category taxonomy with confidence scoring
6. **Models used**: openai/gpt-oss-20b:free, openai/gpt-oss-120b:free

## Statistics

- Pages analyzed: 135
- Related found: 49 (36%)
- Unrelated / discarded: 86

**By usage type:**
- `direct_citation`: 16
- `topic_mention`: 15
- `discussion`: 14
- `indirect_reuse`: 3
- `original_content`: 1

**By confidence:**
- high: 20
- medium: 29
- low: 0

## Research Summary

The article presents a physical mechanism whereby wind‑blown snow accumulation on a cut slope above the Dyatlov Pass tent could trigger a delayed slab avalanche, reconciling previously contradictory evidence. It combines analytical modeling of shear stress in a weak snow layer with numerical Material Point Method simulations to show that a small slab, loaded over 7‑13 hours, could produce the non‑fatal thoracic injuries reported. The work is notable because it offers a quantifiable avalanche hypothesis for a long‑standing mystery, while acknowledging that other puzzling aspects of the incident remain unresolved.

## Related Pages (49)

### 1. The Dyatlov Pass Incident: 11 Undeniable Facts That No Theory ...
- **URL:** https://www.reddit.com/r/TrueCrimeMystery/comments/1swatpy/the_dyatlov_pass_incident_11_undeniable_facts/
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The most scientifically credible response to the 2019 conclusion came in 2021, when a team from ETH Zürich and EPFL published a study... Lead author Johan Gaume... acknowledged they could not claim to have solved the mystery.
- **Summary:** The Reddit post discusses the 2021 Communications Earth & Environment paper by Gaume and Puzrin, referencing its authors and summarizing its conclusions about a slab avalanche. It does not quote the article directly nor provide a URL, but it uses the study's findings to support its argument.

### 2. New to the Dyatlov Pass incident—What theories make the most ...
- **URL:** https://www.reddit.com/r/UnsolvedMysteries/comments/1njjmuz/new_to_the_dyatlov_pass_incidentwhat_theories/
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The Reddit post asks "New to the Dyatlov Pass incident—What theories make the most sense to you?" and describes the incident, linking to a history.com article but not to the source paper.
- **Summary:** The webpage discusses the Dyatlov Pass incident and solicits theories, which is the same topic as the source article, but it does not cite or reuse the source's content. It represents an independent discussion of the topic.

### 3. This has already been posted on this sub but holy cow is ... - Reddit
- **URL:** https://www.reddit.com/r/oddlyterrifying/comments/zzjzr2/this_has_already_been_posted_on_this_sub_but_holy/
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** This has already been posted on this sub but holy cow is this last image that was taken by one of the hikers of the dyatlov pass incident absolutely horrifying. The dyatlov pass is probably one of the most interesting mysteries ever
- **Summary:** The Reddit post discusses the Dyatlov Pass incident and shares an image, but it does not cite or reuse any content from the scientific article. It merely mentions the same historical event, making it a topic mention without attribution.

### 4. Very Interesting Dyatlov Pass theory : r/UnresolvedMysteries
- **URL:** https://www.reddit.com/r/UnresolvedMysteries/comments/l7h6mf/very_interesting_dyatlov_pass_theory/
- **Usage type:** `indirect_reuse`
- **Confidence:** medium
- **Evidence:** New computer simulation (based partially on animation techniques used in Disney's Frozen ) showed that a small avalanche of icy matter a mere 16 feet long—about the size of an SUV was certainly possible in that terrain.
- **Summary:** The Reddit post discusses a small avalanche theory that aligns with the conclusions of the source article, but it does not explicitly cite or quote the article. The content therefore represents an indirect reuse of the article’s findings without attribution.

### 5. 'Frozen' Animation Code Helped Engineers Solve a 62-Year-Old ...
- **URL:** https://www.reddit.com/r/nottheonion/comments/lbl6kd/frozen_animation_code_helped_engineers_solve_a/
- **Usage type:** `indirect_reuse`
- **Confidence:** medium
- **Evidence:** The post discusses how engineers used a ‘Frozen’ animation code to solve a 62‑year‑old Russian cold case, referring to the Dyatlov Pass incident.
- **Summary:** The Reddit post mentions the Dyatlov Pass mystery and the use of engineering analysis to solve it, which aligns with the source article’s topic of snow avalanche mechanisms at Dyatlov Pass. However, the post does not directly cite or quote the source article, instead it references the case in a general sense, indicating indirect reuse of the source’s conclusions without explicit attribution.

### 6. What really caused the Dyatlov Pass Incident, concerning the nine young Russian hikers, also experienced skiers, who wandered up a mounta...
- **URL:** https://www.quora.com/What-really-caused-the-Dyatlov-Pass-Incident-concerning-the-nine-young-Russian-hikers-also-experienced-skiers-who-wandered-up-a-mountain-in-the-Mansi-region-of-the-Urals-and-never-came-back-alive
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** The Quora answer includes a link to "Mechanisms of slab avalanche release and impact in the Dyatlov Pass incident in 1959 - Communications Earth & Environment" and cites it as the source of the avalanche explanation.
- **Summary:** The Quora page explicitly references the scientific article by linking to it and using its findings to support the avalanche hypothesis for the Dyatlov Pass incident. This constitutes a direct citation of the source article.

### 7. What is the mystery behind the Dyatlov Pass incident in the Ural Mountains, where a group of hikers died under strange circumstances?
- **URL:** https://www.quora.com/What-is-the-mystery-behind-the-Dyatlov-Pass-incident-in-the-Ural-Mountains-where-a-group-of-hikers-died-under-strange-circumstances
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** The answer states "A slab avalanche" and includes a citation link to https://www.nature.com/articles/s43247-020-00081-8.
- **Summary:** The Quora answer explicitly cites the Nature Communications article as the source supporting the avalanche explanation for the Dyatlov Pass incident, making the content directly related and properly referenced.

### 8. Why is the Dyatlov Pass accident one of the most disturbing cases in Russian history?
- **URL:** https://www.quora.com/Why-is-the-Dyatlov-Pass-accident-one-of-the-most-disturbing-cases-in-Russian-history
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** A slab avalanche [[1]]... A team of Swiss and French scientists cracked the case in 2021 [[2]](https://www.nature.com/articles/s43247-020-00081-8).
- **Summary:** The Quora page explicitly cites the Nature Communications article, linking to it as a source for the slab avalanche explanation. This direct citation shows the webpage is using the source article to support its discussion.

### 9. Regarding the Dyatlov incident, to you, what theory best explains why the hikers fled their tents?
- **URL:** https://www.quora.com/Regarding-the-Dyatlov-incident-to-you-what-theory-best-explains-why-the-hikers-fled-their-tents
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** "A team of Swiss and French scientists cracked the case in 2021" and the link to https://www.nature.com/articles/s43247-020-00081-8
- **Summary:** The Quora answer explicitly cites the Nature Communications article, indicating it is used as a source for the discussion of the Dyatlov Pass incident. This is a direct citation, confirming a high-confidence relationship between the two texts.

### 10. What are the main causes of avalanches?
- **URL:** https://www.quora.com/What-are-the-main-causes-of-avalanches
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** The Quora page lists general causes of avalanches (terrain, snowpack, trigger) and includes multiple user answers about avalanche mechanisms, without any reference to the Dyatlov Pass study.
- **Summary:** The webpage discusses avalanche causes, which is the same broad subject as the source article, but it does not cite, quote, or directly reuse any of the article's specific findings. It merely mentions the topic in passing.

### 11. VisionaryVoid on X: "The Dyatlov Pass Incident — the 1959 mystery where nine experienced hikers fled their tent into a deadly blizzard.

In late January 1959, Igor Dyatlov and eight companions set out on a winter ski expedition across the northern Ural Mountains.

They were young, strong, and highly https://t.co/3xdLJbvuNd" / X
- **URL:** https://x.com/VisionaryVoid/status/2026473219788779751
- **Usage type:** `indirect_reuse`
- **Confidence:** medium
- **Evidence:** A 2021 study by Swiss scientists provided strong modelling support: a small but powerful slab of snow slid down the slope, partially burying the tent and injuring some of the hikers.
- **Summary:** The X post describes the same slab‑avalanche mechanism and findings presented in the 2021 Nature Communications article, but it does not cite the paper directly. It restates the study’s conclusions, indicating indirect reuse of the source’s content.

### 12. Global Statistics on X: "@Morbidful The Dyatlov Pass incident refers to the mysterious event in which nine Soviet hikers died in the northern Ural Mountains between February 1 and 2, 1959, under uncertain circumstances.

A seasoned trekking group from the Ural Polytechnical Institute, led by Igor Dyatlov, had set https://t.co/UwJJND4zcB" / X
- **URL:** https://x.com/Globalstats11/status/1957478054147834015
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** The Dyatlov Pass incident refers to the mysterious event ... In 2019 Russia re-investigated the incident and concluded that an avalanche led to the deaths. However, this theory is doubted by some.
- **Summary:** The webpage discusses the Dyatlov Pass incident and mentions the avalanche hypothesis, which is the central topic of the source article. However, it does not cite or directly reference the source article, nor does it attribute specific findings to it, making it a general topic mention.

### 13. TheForgotThings on X: "The Dyatlov Pass Incident. In 1959, nine experienced hikers died under strange and unexplained circumstances in the Ural Mountains of Russia. 

Their bodies were discovered in various stages of undress, scattered across the snowy landscape, with some showing signs of blunt force https://t.co/3CWBYr60UC" / X
- **URL:** https://x.com/TheForgotthings/status/1844310113982505146
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** The Dyatlov Pass Incident. In 1959, nine experienced hikers died ... with some showing signs of blunt force trauma ...
- **Summary:** The webpage mentions the Dyatlov Pass incident and describes injuries similar to those discussed in the source article, but it does not cite or directly reference the article. It merely mentions the same topic without attribution.

### 14. ArchaeoHistories on X: "The Dyatlov Pass Incident remains one of the most chilling and mysterious events in modern history. In 1959, nine experienced hikers—led by Igor Dyatlov—set out on a skiing expedition in the Ural Mountains of Soviet Russia. However, their journey ended in tragedy when their https://t.co/iDBQrlJ8sR" / X
- **URL:** https://x.com/histories_arch/status/1917796250868437222
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The post describes the Dyatlov Pass Incident, noting the hikers’ mysterious deaths, injuries, and theories such as avalanches and supernatural causes.
- **Summary:** The X post discusses the Dyatlov Pass Incident, the same historical event examined in the source article, but it does not cite or reference the article itself. It provides its own narrative and speculation, making it a discussion of the topic rather than a direct citation or reuse of the source content.

### 15. NWS Seattle on X: "(1/2) The Northwest Avalanche Center @nwacus wants us to use extra caution in the Cascades over the next week.

Recent storms, followed by strong winds, have likely pushed snow conditions toward a tipping point in some areas. Persistent slab avalanches have been reported. https://t.co/By0V3cqpUX" / X
- **URL:** https://x.com/NWSSeattle/status/2027556025377636575
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** "Recent storms, followed by strong winds, have likely pushed snow conditions toward a tipping point... Persistent slab avalanches have been reported."
- **Summary:** The webpage discusses current slab avalanche risks caused by recent storms and strong winds, which aligns with the source article's focus on wind‑driven slab avalanche mechanisms. However, the tweet does not cite or directly reference the article, merely mentioning the same general topic.

### 16. Tragic Dyatlov Pass Incident: Using Science to Explore One of the Greatest Mysteries in Soviet History
- **URL:** https://scitechdaily.com/tragic-dyatlov-pass-incident-using-science-to-explore-one-of-the-greatest-mysteries-in-soviet-history/
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** Reference: “Mechanisms of slab avalanche release and impact in the Dyatlov Pass incident in 1959” by Johan Gaume and Alexander M. Puzrin, 28 January 2021, *Communications Earth & Environment*.  DOI: 10.1038/s43247-020-00081-8
- **Summary:** The webpage explicitly cites the source article by name, date, journal, and DOI, indicating a direct reference to the original research. It discusses the same topic—slab avalanche mechanisms in the Dyatlov Pass incident—using the findings from the source article. Thus the content is directly related and properly attributed.

### 17. Dyatlov Pass Explained: Why the 1959 Investigation Failed, Not the Evidence - clutch.
- **URL:** https://clutchjustice.com/2026/04/17/dyatlov-pass-explained-avalanche-investigation-failure/
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** The article cites "Puzrin, A.M. & Gaume, J. (2021). Mechanisms of slab avalanche release and impact in the Dyatlov Pass incident in 1959" and references the 2021 Communications Earth & Environment paper by Puzrin and Gaume.
- **Summary:** The webpagarstechnicae explicitly cites and discusses the 2021 paper by Puzrin and Gaume, directly referencing the source article’s findings on slab avalanche mechanisms in the Dyatlov Pass incident.

### 18. Has an Old Soviet Mystery at Last Been Solved? | The New Yorker
- **URL:** https://www.newyorker.com/magazine/2021/05/17/has-an-old-soviet-mystery-at-last-been-solved
- **Usage type:** `discussion`
- **Confidence:** high
- **Evidence:** A paper corroborating much of Kuryakov’s explanation was published in January by two Swiss engineers in the journal *Communications Earth & Environment*.
- **Summary:** The New Yorker article discusses the same slab‑avalanche mechanism presented in the source paper and references the publication in Communications Earth & Environment, indicating it draws on the source's findings without quoting it directly.

### 19. Puzrin & Gaume
- **URL:** https://dyatlovpass.com/puzrin-gaume
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** “In our new article in Communications Earth & Environment, we report five main findings…" and the page links to the source article URL https://www.nature.com/articles/s43247-020-00081-8.
- **Summary:** The webpage explicitly cites the source article, quoting its authors and linking to the DOI, and discusses its findings in the context of the Dyatlov Pass incident.

### 20. [PDF] Mechanisms of slab avalanche release and impact in the Dyatlov ...
- **URL:** https://scispace.com/pdf/mechanisms-of-slab-avalanche-release-and-impact-in-the-119xlp3z6b.pdf
- **Usage type:** `original_content`
- **Confidence:** high
- **Evidence:** "Mechanisms of slab avalanche release and impact in the Dyatlov Pass incident in 1959" and the full text of the article including the DOI link https://doi.org/10.1038/s43247-020-00081-8 is reproduced verbatim on the webpage.
- **Summary:** The webpage reproduces the full text of the source article, including title, authors, abstract, figures, methods, and references, indicating it is the original content of the article rather than a summary or citation. Thus the two texts are identical and directly related.

### 21. Effects of snow properties on humans breathing into an artificial air pocket – an experimental field study - PMC
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC5732296/
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** "Asphyxia, i.e. hypoxia and hypercapnia, is the primary cause of death from snow avalanche"
- **Summary:** Both texts address snow avalanche phenomena and the physical properties of snow, but the webpage does not cite or directly reference the Dyatlov Pass study. It merely discusses avalanche-related breathing and snow density, making the relationship a general topic mention rather than a direct citation or reuse of the source content.

### 22. [PDF] The influence of snow microstructure on the compressive ... - HAL
- **URL:** https://hal.science/hal-05451252v1/file/Schoettner_etal_Microstructure_mechanical_properties_Acta_Mater_2025.pdf
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** "weak layers" and "snow slab avalanches" are mentioned in the HAL article, indicating a discussion of the same general topic as the source article.
- **Summary:** The HAL webpage discusses weak snow layers and snow slab avalanches, which are related to the source article’s focus on slab avalanche mechanisms, but it does not directly cite or reuse the source’s content. Thus the relationship is a general topic mention rather than a direct citation or reuse.

### 23. Backcountry Skiing, Avalanche Awareness Snow Science Snowpack — SINTR
- **URL:** https://botnw.com/blog/2020/11/10/snow-sintering-and-faceting-the-last-best-ski
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** "A faceted layer is a weak layer. The combination of a weak faceted layer underneath a strong sintered layer is a perfect recipe for a slab avalanche."
- **Summary:** The webpage discusses snow sintering, faceting, and their role in slab avalanche formation, which aligns with the scientific topic of the source article. However, it does not directly cite or quote the source, instead providing its own explanation and analysis of the same concepts.

### 24. [PDF] NEW PERSPECTIVE ON DRIFTING SNOW SLAB AVALANCHE
- **URL:** https://arc.lib.montana.edu/snow-science/objects/ISSW2023_O16.03.pdf
- **Usage type:** `discussion`
- **Confidence:** high
- **Evidence:** "snow density has increased due to densification. In general, sintering of snow particles are promoted by smaller grain size and closer to 0°C under sub‑zero temperatures."
- **Summary:** Both texts examine wind‑driven snow accumulation and sintering as key factors in slab avalanche release. The webpage discusses drifting snow, sintering, and wind‑induced densification, which align with the source article’s analysis of delayed slab release caused by wind‑transported snow and sintering. The content is thematically related but the webpage does not directly cite the source, instead providing its own discussion of similar mechanisms.

### 25. [PDF] Proceedings, International Snow Science Workshop, Breckenridge ...
- **URL:** https://www.slf.ch/fileadmin/user_upload/WSL/Mitarbeitende/schweizj/Schweizer_etal_Avalanche_release_101_ISSW_2016.pdf
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** Our understanding of dry‑snow slab avalanche release improved over the last decade… (PDF title and abstract). The document discusses avalanche release mechanisms but does not cite the Dyatlov Pass article.
- **Summary:** The webpage is a 2016 conference paper on avalanche release theory, which shares the general subject of snow slab avalanches with the 2021 Dyatlov Pass article. However, it does not reference or quote the source article, so the relationship is limited to a common topic rather than direct citation or reuse.

### 26. [PDF] A material point method for snow simulation - UC Davis Mathematics
- **URL:** https://math.ucdavis.edu/~jteran/papers/SSCTS13.pdf
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** Webpage: "A material point method for snow simulation..."; Source article: "Three-dimensional numerical simulations based on the Material Point Method (MPM)..."
- **Summary:** Both documents discuss the use of the Material Point Method for simulating snow behavior. The webpage presents a 2013 method for snow simulation, while the source article applies MPM to model a snow slab avalanche, but the webpage does not cite or directly reference the source article.

### 27. [PDF] RECENT ADVANCES IN MODELING SNOW AND AVALANCHES ...
- **URL:** https://www.dora.lib4ri.ch/wsl/dload/wsl:38006/PDF/Gaume-2023-Recent_advances_in_modeling_snow-(published_version).pdf
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The webpage reviews recent advances in MPM modeling of snow and avalanches, describing avalanche release mechanisms and referencing earlier works by Gaume et al. that investigate slab avalanche dynamics, which are the same subject of the source article.
- **Summary:** Both documents address avalanche mechanics and use the Material Point Method, but the webpage does not explicitly cite the 2021 Nature Communications article. It discusses the same research area and builds on related prior work, indicating a thematic relationship without direct attribution.

### 28. Avalanche.org » Slope Angle
- **URL:** https://avalanche.org/avalanche-encyclopedia/terrain/slope-characteristics/slope-angle/
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** "Slope angle is a key factor for dictating whether or not the terrain can produce an avalanche. Most slab avalanches initiate on slopes where the steepest slope angle is between 30° and 50°"
- **Summary:** The webpage discusses slope angles as a key factor for avalanche initiation, a topic also addressed in the source article when describing the Dyatlov Pass slope. However, the webpage does not cite or directly reference the source article, merely mentioning the general concept of slope angles in avalanche science.

### 29. Glossary
- **URL:** https://migrate.avalanche.ca/glossary/terms/slope-angle
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** The incline of a slope is a significant factor in whether or not it can avalanche. Most avalanches occur on slopes that have an incline of 30-45 degrees ... Below 25 degrees, slopes aren’t steep enough to avalanche and above 60 degrees, new snow sluffs frequently and slab avalanches are rare.
- **Summary:** Both texts discuss avalanche behavior in relation to slope angle, but the webpage does not cite or directly reference the source article. It merely mentions the same general topic, making it a topic mention without attribution.

### 30. Mystery solved: What killed 9 hikers in Dyatlov Pass Incident? - Futurity
- **URL:** https://www.futurity.org/dyatlov-pass-incident-avalanche-2510132-2/
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** In their investigation, published in *Communications Earth & Environment* Gaume and Puzrin attempt to address these points.
- **Summary:** The Futurity article explicitly references the source paper by name and DOI, indicating it is citing the original research. It discusses the same topic—Dyatlov Pass incident and avalanche hypothesis—using the source’s findings, making it a direct citation with high confidence.

### 31. Have Scientists Finally Unraveled the 60-Year Mystery Surrounding ...
- **URL:** https://www.smithsonianmag.com/smart-news/scientists-may-have-finally-unraveled-mystery-dyatlov-pass-incident-180976886/
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** new research published in the journal *Communications Earth and Environment* (https://www.nature.com/articles/s43247-020-00081-8) points toward a more “sensible” explanation... lead author Johan Gaume ... lead author [Johan Gaume] ... Gaume and co-author Alexander M. Puzrin ...
- **Summary:** The Smithsonian article directly cites the source paper, linking to its DOI and naming its authors while summarizing its findings on the Dyatlov Pass avalanche hypothesis. This constitutes a direct citation of the original research.

### 32. Dyatlov Pass incident - Wikipedia
- **URL:** https://en.wikipedia.org/wiki/Dyatlov_Pass_incident
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** In 2021, a team of physicists and engineers led by Alexander Puzrin and Johan Gaume published a new model in *Communications Earth & Environment*[[44]] that demonstrates how even a relatively small slide of snow slab on the Kholat Syakhl slope could cause tent damage and injuries consistent with those suffered by the Dyatlov team.
- **Summary:** The Wikipedia article explicitly cites the 2021 Nature Communications paper (doi:10.1038/s43247-020-00081-8) when discussing the avalanche mechanism model, directly referencing the source article as evidence for the proposed explanation.

### 33. The Dyatlov Pass Incident: New Forensic Perspectives on the Ural Mountains’ Greatest Mystery | Ancient Origins
- **URL:** https://www.ancient-origins.net/news-history-archaeology/dyatlov-pass-incident-00102668
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** Gaume, J., and A. M. Puzrin. 2021. “Mechanisms of slab avalanche release and impact in the Dyatlov Pass incident in 1959.” Communications Earth & Environment 2, Article 10. Available at:<https://www.nature.com/articles/s43247-020-00081-8>
- **Summary:** The webpage explicitly cites the source article in its reference list, indicating a direct use of the article’s content or findings.

### 34. [PDF] Snow-Avalanche Hazard Analysis for Land-Use Planning and ...
- **URL:** https://coloradogeologicalsurvey.org/wp-content/uploads/woocommerce_uploads/B-49.pdf
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** The webpage discusses "slab avalanches" and avalanche dynamics, e.g., "Slab avalanches are fractures of cohesive, well-bonded snow..." and provides extensive analysis of avalanche mechanisms and mitigation.
- **Summary:** Both documents address snow avalanche phenomena, but the webpage does not cite or directly reference the specific Nature article. It merely mentions the same general topic of slab avalanches without attribution.

### 35. [PDF] Proceedings, International Snow Science Workshop, Banff, 2014 738
- **URL:** https://dot.alaska.gov/stwdmno/documents/Seward_Highway_Avalanche_Models.pdf
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** "Snow entrainment has a large impact on avalanche flow regime. It adds mass to the moving avalanche body which can amplify a fluidized or lubricated flow regime."
- **Summary:** Both texts address avalanche dynamics, but the source article focuses on a delayed slab avalanche mechanism at Dyatlov Pass, while the webpage discusses how snow entrainment and temperature affect run‑out distances at Bird Hill. The webpage does not cite or directly reference the Dyatlov study, but it engages in a broader discussion of avalanche physics that overlaps conceptually with the source.

### 36. Dyatlov Pass
- **URL:** https://dyatlovpass.com/
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** The webpage includes a section titled "Puzrin-Gaume avalanche theory" and states: "The Swiss "avalanche" team Alexander Puzrin and Johan Gaume have a second paper in Nature.com [Post-publication careers: follow-up expeditions reveal avalanches at Dyatlov Pass]" linking to the source article.
- **Summary:** The Dyatlov Pass website explicitly references the scientific article by Gaume and Puzrin, citing their work on the slab avalanche mechanism and providing a link to the Nature publication. This constitutes a direct citation of the source.

### 37. Dyatlov autopsies with photos — Mysterious Stories Blog — StrangeOutdoors.com
- **URL:** https://www.strangeoutdoors.com/mysterious-stories-blog/tag/Dyatlov+autopsies+with+photos
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The webpage describes various theories for the Dyatlov Pass incident, including "Avalanche" and discusses why the avalanche hypothesis was questioned, mirroring the subject of the source article which proposes a slab avalanche mechanism.
- **Summary:** Both texts address the Dyatlov Pass incident and consider avalanche explanations, but the webpage does not cite the scientific paper or its specific findings. It provides its own narrative and analysis, making it a discussion of the same topic without direct attribution.

### 38. The Dyatlov Pass Incident: Can Science Explain What Happened to the Hikers? | Discover Magazine
- **URL:** https://www.discovermagazine.com/the-dyatlov-pass-incident-can-science-explain-what-happened-to-the-hikers-42311
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** "new research published in *Nature* aims to explain their deaths by looking at the mountains’ topography and simulating weather dynamics to come to a more natural, snowy conclusion."
- **Summary:** The Discover Magazine article discusses the Dyatlov Pass Incident and explicitly cites the Nature research article (link provided) as the source of the avalanche explanation, making it a direct citation of the original content.

### 39. Katabatic Flow - an overview | ScienceDirect Topics
- **URL:** https://www.sciencedirect.com/topics/earth-and-planetary-sciences/katabatic-flow
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** "Katabatic flows refer to drainage flows of cold air that occur over uneven terrain, primarily driven by radiative cooling at night, leading to the movement of dense air from higher altitudes to lower elevations."
- **Summary:** The webpage discusses katabatic flows in a general sense, while the source article examines katabatic winds as a contributing factor to the delayed slab avalanche in the Dyatlov Pass incident. The two texts share the same topic but the webpage does not cite or directly reuse the source article’s content.

### 40. EarthWord: Katabatic Winds | U.S. Geological Survey
- **URL:** https://www.usgs.gov/news/earthword-katabatic-winds
- **Usage type:** `topic_mention`
- **Confidence:** high
- **Evidence:** "katabatic winds do bear a resemblance to tumbling, since they are essentially winds that flow downhill."
- **Summary:** The USGS page provides a definition of katabatic winds, a key atmospheric phenomenon also discussed in the source article as a trigger for the Dyatlov Pass avalanche. The page does not cite the article but mentions the same concept, making the content related by topic.

### 41. Blog: Understanding and managing depth hoar - Utah Avalanche Center
- **URL:** https://utahavalanchecenter.org/blog/28021
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** Webpage: "When shallow snow sits on the ground under cold clear skies it begins to transform ... into a pile of loose, dry, sugary crystals called depth hoar. Lacking cohesion, and in turn strength, depth hoar is the bane of a snowpack. As a weak base layer, these large grained, faceted crystals can become the failure point for large, dangerous, ... avalanches."
- **Summary:** Both the source article and the webpage discuss depth hoar as a weak snow layer that can trigger avalanches. The webpage provides its own explanation without citing the source article, indicating a discussion of the same topic rather than direct reuse or citation.

### 42. [PDF] Depth Hoar - A Rotten Way to Start the Season
- **URL:** https://www.mtavalanche.com/sites/default/files/MSA%20January%20Final_0.pdf
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The webpage describes depth hoar as a "persistent weak layer" that forms near the base of the snowpack and can trigger avalanches when loaded, which mirrors the source article's discussion of buried depth hoar as a weak layer contributing to slab avalanche release in the Dyatlov Pass incident.
- **Summary:** Both texts discuss depth hoar as a critical weak layer in snowpack stability and avalanche triggering. The webpage does not cite the source article but provides its own analysis of depth hoar, aligning with the concepts presented in the source.

### 43. Zones of Depth Hoar Development, International Snow Service Workshops (ISSW) Proceedings professional paper or poster talk citation record. - Montana State University Library
- **URL:** https://arc.lib.montana.edu/snow-science/item/1288
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** "Weakness associated with depth hoar contributes significantly to full depth avalanches. As a result of the development of thin layers of depth hoar in conjunction with high density snow layers, depth hoar may also assist in causing avalanches associated with crusts."
- **Summary:** The webpage discusses depth hoar development and its role in avalanche formation, a topic also examined in the source article where depth hoar is identified as a weak layer contributing to slab avalanche release. Both texts cover the same physical phenomenon but the webpage does not cite or directly reference the source article, instead providing its own discussion of the concept.

### 44. Modeling snow slab avalanches caused by weak-layer ...
- **URL:** https://tc.copernicus.org/articles/14/131/2020/tc-14-131-2020.pdf
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The webpage discusses "snow slab avalanches caused by weak‑layer failure" and presents a model for weak‑layer collapse, which is a concept also addressed in the source article’s analysis of slab avalanche release.
- **Summary:** Both texts cover the general topic of snow slab avalanches and weak‑layer failure, but the webpage does not cite or directly reference the source article. It provides its own analysis and modeling of weak‑layer collapse, so the relationship is a discussion of the same topic without attribution.

### 45. [PDF] 489 ON THE ROLE OF DEFICIT ZONES OR IMPERFECTIONS IN ...
- **URL:** https://www.slf.ch/fileadmin/user_upload/WSL/Mitarbeitende/schweizj/Schweizer_Review_slab_release_ISSW1998.pdf
- **Usage type:** `discussion`
- **Confidence:** medium
- **Evidence:** The webpage states: "Dry snow slab avalanche formation starts with failure in the weak layer underlying the slab." The source article also analyses a slab avalanche mechanism for the Dyatlov Pass incident, focusing on weak layer failure and slab release.
- **Summary:** Both documents address the physics of dry snow slab avalanches, describing weak‑layer failure and slab release. However, the webpage does not cite or directly reference the 2021 source article; it provides its own analysis of the phenomenon.

### 46. Confirmed: Avalanche is likeliest explanation for tragic Dyatlov Pass incident - Ars Technica
- **URL:** https://arstechnica.com/science/2022/03/confirmed-avalanche-is-likeliest-explanation-for-tragic-dyatlov-pass-incident/
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** Gaume and Puzrin [published their findings](https://www.nature.com/articles/s43247-020-00081-8) in January 2021 in Communications Earth & Environment.
- **Summary:** The Ars Technica article explicitly cites the source paper by linking to its DOI and discusses the same research findings, making it a direct citation of the source article.

### 47. Russia's 'Dyatlov Pass' conspiracy theory may finally be solved 60 ...
- **URL:** https://www.livescience.com/dyatlov-pass-incident-slab-avalanche-hypothesis.html
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** "a study published Thursday (Jan. 28) in the Nature journal Communications Earth & Environment provides the first scientific evidence behind a much more banal hypothesis: A small avalanche, triggered under unusual conditions, pummeled the hikers as they slept, then forced them to flee their tent into the cold, dark night."
- **Summary:** The LiveScience article explicitly references and discusses the same scientific study, providing a direct citation and summarizing its findings, thereby directly reusing the source content with attribution.

### 48. Mechanisms of slab avalanche release and impact in the Dyatlov Pass incident in 1959 – Chair of Geomechanics and Geosystems Engineering | ETH Zurich
- **URL:** https://geomechanics.ethz.ch/project-list/Dyatlov_pass.html
- **Usage type:** `direct_citation`
- **Confidence:** high
- **Evidence:** Mechanisms of slab avalanche release and impact in the Dyatlov Pass incident in 1959... The Dyatlov Pass incident is an intriguing unsolved mystery... Here we show how a combination of irregular topography, a cut made in the slope to install the tent and the subsequent deposition of snow induced by strong katabatic winds contributed after a suitable time to the slab release, which caused severe non-fatal injuries, in agreement with the autopsy results.
- **Summary:** The ETH Zurich project page reproduces the title, abstract, authors, and key figures of the Nature Communications Earth & Environment article, effectively citing the original source. The content is a direct presentation of the article's findings rather than a separate analysis.

### 49. [PDF] terrain parameters of avalanche starting zones
- **URL:** https://arc.lib.montana.edu/snow-science/objects/issw-1994-393-404.pdf
- **Usage type:** `topic_mention`
- **Confidence:** medium
- **Evidence:** "Avalanche frequency data for 44 avalanche paths on Lone Mountain in southwest Montana were correlated with data on the terrain features of avalanche starting zones to determine which terrain parameters affect avalanche frequency."
- **Summary:** Both texts discuss avalanches, but the webpage focuses on avalanche frequency and terrain parameters on Lone Mountain, while the source article examines a specific avalanche event (Dyatlov Pass) and proposes a physical mechanism. The webpage does not cite or directly reference the source article, so the relationship is only that they share the general topic of avalanches, not the same content or findings.

## Discarded as Unrelated (86)

- [Thoughts on the Dyatlov pass incident…..what really happened?](https://www.reddit.com/r/UnsolvedMysteries/comments/18vnqi1/thoughts_on_the_dyatlov_pass_incidentwhat_really/) — `unrelated`
- [Dyatlov pass incident as a horror film : r/horror](https://www.reddit.com/r/horror/comments/qskgk0/dyatlov_pass_incident_as_a_horror_film/) — `unrelated`
- [Why Katabatic Winds are the Most Likely Cause of the Dyatlov Pass ...](https://www.reddit.com/r/DyatlovPass/comments/jchdcg/why_katabatic_winds_are_the_most_likely_cause_of/) — `unrelated`
- [One of the last known pictures taken by the hikers of the dyatlov ...](https://www.reddit.com/r/oddlyterrifying/comments/slvxqc/one_of_the_last_known_pictures_taken_by_the/) — `unrelated`
- [Status of technology and avalanche prevention/forecasting : r/Backcountry](https://www.reddit.com/r/Backcountry/comments/jhd4vj/status_of_technology_and_avalanche/) — `unrelated`
- [Looking for a way to simulate realistic snowdrift formation : r/Simulated](https://www.reddit.com/r/Simulated/comments/t9qhdi/looking_for_a_way_to_simulate_realistic_snowdrift/) — `unrelated`
- [Disney Snow Simulation : r/videos](https://www.reddit.com/r/videos/comments/1r7f0v/disney_snow_simulation/) — `unrelated`
- [[WP] This is the prologue (or the first chapter) of the novel you've ...](https://www.reddit.com/r/WritingPrompts/comments/3konk3/wp_this_is_the_prologue_or_the_first_chapter_of/) — `unrelated`
- [How can an extremely loud noise trigger an avalanche in unstable snow conditions?](https://www.quora.com/How-can-an-extremely-loud-noise-trigger-an-avalanche-in-unstable-snow-conditions) — `unrelated`
- [Why does the snow become almost like concrete after an avalanche stops, and how does this affect your ability to escape?](https://www.quora.com/Why-does-the-snow-become-almost-like-concrete-after-an-avalanche-stops-and-how-does-this-affect-your-ability-to-escape) — `unrelated`
- [Alex Danco (@Alex_Danco) / X](https://x.com/Alex_Danco) — `unrelated`
- [SPLITGATE: Arena Reloaded (@Splitgate) / X](https://x.com/Splitgate) — `unrelated`
- [John Hollenbeck (@john_hollenbeck) / X](https://x.com/john_hollenbeck) — `unrelated`
- [X. It’s what’s happening](https://x.com/search?f=live&vertical=default&q=%EF%BD%84%EF%BD%85%EF%BC%AC%EF%BC%A9%EF%BC%A7%EF%BC%A8%EF%BC%B4%E3%80%80%EF%BC%AD%EF%BC%A5%EF%BC%A4%EF%BC%A9%EF%BC%A1%E3%80%80%EF%BC%B7%EF%BC%AF%EF%BC%B2%EF%BC%AB%EF%BC%B3) — `unrelated`
- [DAN KOE (@thedankoe) / Posts / X - Twitter](https://x.com/thedankoe) — `unrelated`
- [Jan Liphardt (@JanLiphardt) / X](https://x.com/JanLiphardt) — `unrelated`
- [Critical Care Reviews on X: "Emergency care for avalanche buried patients - a narrative review

CCR Journal Watch
https://t.co/Sp06oA6IDG https://t.co/bEtdFbEbfS" / X](https://x.com/CritCareReviews/status/2043065506786144627) — `unrelated`
- [Outside Magazine on X: "In the days leading up to an avalanche in Rocky Mountain National Park, Colorado experienced just a small amount of snow. What went wrong? One expert told us it was a combination of factors that led to the slide. https://t.co/x0XUbwb4Sp" / X](https://x.com/outsidemagazine/status/2019252187159785573) — `unrelated`
- [People on X: "How the 6 Survivors of Deadly Tahoe Avalanche Managed to Stay Alive for Hours amid 'Horrific' Conditions https://t.co/IAcm8cfBff" / X](https://x.com/people/status/2024563662434734325) — `unrelated`
- [Ryan Yates (@rlyatesofficial) / X](https://x.com/rlyatesofficial) — `unrelated`
- [Jamie’s Notes (@jianming_w87187) / X](https://x.com/jianming_w87187) — `unrelated`
- [Flathead Avalanche (@FACAvalanche) / X](https://x.com/FACAvalanche) — `unrelated`
- [Sawtooth Avalanche Center (@SawtoothAvy) / X](https://x.com/SawtoothAvy) — `unrelated`
- [X. It’s what’s happening](https://x.com/search?q=Robert%20L%20Ma&f=live) — `unrelated`
- [[PDF] improving avalanche forecasts by extracting boundary conditions ...](https://www.interpraevent.at/reference/media/450/download/2008_2_583.pdf?v=1) — `unrelated`
- [Avalanche.org » Technical Papers Library](https://avalanche.org/technical-papers/) — `unrelated`
- [[PDF] Typical avalanche problems](https://www.avalanches.org/wp-content/uploads/2022/09/EN_EAWS_avalanche_problems.pdf) — `unrelated`
- [Avalanche Problems | Sierra Avalanche Center](https://www.sierraavalanchecenter.org/avalanche-problems/) — `unrelated`
- [[PDF] Shear strength of discontinuities - Rocscience](https://static.rocscience.cloud/assets/resources/learning/hoek/Practical-Rock-Engineering-Chapter-4-Shear-Strength-of-Discontinuities-Remediated.pdf) — `unrelated`
- [[PDF] shear strength correlations and remedial measure guidelines for long](https://library.ctr.utexas.edu/digitized/texasarchive/1435-2f.pdf) — `unrelated`
- [[PDF] ROCK STRENGTH PROPERTIES AND THEIR MEASUREMENT](https://onlinepubs.trb.org/Onlinepubs/sr/sr247/sr247-014.pdf) — `unrelated`
- [Shear strength (soil) - Wikipedia](https://en.wikipedia.org/wiki/Shear_strength_(soil)) — `unrelated`
- [Response of the Human Torso to Lateral and Oblique Constant-Velocity Impacts - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3242539/) — `unrelated`
- [[PDF] Using video detection of snow surface movements to estimate weak ...](https://infoscience.epfl.ch/bitstreams/78d8cc7f-f0db-4030-85fb-cad0db135654/download) — `unrelated`
- [[PDF] The influence of snow microstructure on the compressive ...](https://www.slf.ch/fileadmin/user_upload/WSL/Mitarbeitende/schweizj/Schoettner_etal_Microstructure_mechanical_properties_Acta_Mater_2025.pdf) — `unrelated`
- [The Friction and Creep of Polycrystalline Ice on JSTOR](https://www.jstor.org/stable/77933) — `unrelated`
- [[PDF] Physics of the Granular State](https://pdodds.w3.uvm.edu/teaching/courses/2009-08UVM-300/docs/others/everything/jaeger1992a.pdf) — `unrelated`
- [[PDF] A Review of Sintering in Seasonal Snow. - DTIC](https://apps.dtic.mil/sti/tr/pdf/ADA335556.pdf) — `unrelated`
- [Reducing Avalanche Risk | REI Expert Advice](https://www.rei.com/learn/expert-advice/avalanche-reducing-risk.html) — `unrelated`
- [Avalanche Bulletin Interpretation Guide](https://www.slf.ch/files/user_upload/SLF/Lawinenbulletin_Schneesituation/Wissen_zum_Lawinenbulletin/Interpretationshilfe/Interpretationshilfe_EN.pdf) — `unrelated`
- [Avalanche Danger Scale – EAWS](https://www.avalanches.org/standards/avalanche-danger-scale/) — `unrelated`
- [Get The Picture - Northwest Avalanche Center](https://nwac.us/get-the-picture/) — `unrelated`
- [[PDF] The influence of forest and topography on snow accumulation and ...](https://www.uvm.edu/~bwemple/SnowHydro/readings/JostWeilerGlunsAlila2007_ForestTopoEffects.pdf) — `unrelated`
- [[PDF] Topographic and vegetation effects on snow accumulation in ... - TC](https://tc.copernicus.org/articles/10/257/2016/tc-10-257-2016.pdf) — `unrelated`
- [Influence of topography and forest characteristics on snow distributions in a forested catchment - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022169417300227) — `unrelated`
- [TC - Topographic and vegetation effects on snow accumulation in the southern Sierra Nevada: a statistical summary from lidar data](https://tc.copernicus.org/articles/10/257/2016/) — `unrelated`
- [[PDF] Efficient particle generation for depth-averaged and fully 3D MPM ...](https://www.mate.polimi.it/biblioteca/add/qmox/15-2025.pdf) — `unrelated`
- [[PDF] Discrete element modeling of crack propagation in weak snowpack ...](https://avalanche.org/wp-content/uploads/2018/08/14_ISSW_Gaume_etal_FINAL-1.pdf) — `unrelated`
- [How to Calculate Slope Angle to Avoid Avalanche Terrain | onX Backcountry](https://www.onxmaps.com/backcountry/blog/slope-angle-calculator) — `unrelated`
- [Ron Perla and the 30-Degree Threshold - The Backcountry Ski Site](https://wildsnow.com/33060/ron-perla-and-the-30-degree-threshold/) — `unrelated`
- [Snow Load Roof Interactive Calculator | FIRGELLI](https://www.firgelliauto.com/blogs/calculators/snow-load-roof-calculator?srsltid=AfmBOoqnfV3CPBHz_YLbgW5HYiZd3j-YVGnZKvpEM_PVagqdXzlJXgqA) — `unrelated`
- [[PDF] Snow loads for building - NBCC 2015 - Maplesoft](https://www.maplesoft.com/products/MapleFlow/civil-engineering-software/PDFs/Structural-Steel/SnowloadsforBuilding-NBCC2015.flow.pdf) — `unrelated`
- [[PDF] ASCE 7-10 Snow Load Provision](https://seaoo.org/downloads/Presentations_CONF/2011_presentation_on_snow_loads.pdf) — `unrelated`
- [[PDF] Three-Dimensional Roof Snowdrifts | FEMA](https://www.fema.gov/sites/default/files/2020-07/fema_roof_snowdrift_design_guide.pdf) — `unrelated`
- [[PDF] SCENARIO-BASED AVALANCHE SIMULATIONS INCLUDING ...](https://arc.lib.montana.edu/snow-science/objects/ISSW2024_P2.11.pdf) — `unrelated`
- [NHESS - The impact of terrain model source and  resolution on snow avalanche modeling](https://nhess.copernicus.org/articles/22/2673/2022/) — `unrelated`
- [[PDF] Distribution of Shear Force in Concrete Slabs](https://publications.lib.chalmers.se/records/fulltext/164525.pdf) — `unrelated`
- [Slab thickness-shear reinforcement interaction on shear strength of interior slab-column connections | Journal of Engineering and Applied Science | Springer Nature Link](https://link.springer.com/article/10.1186/s44147-025-00872-w) — `unrelated`
- [[PDF] A distribution procedure for the analysis of slabs continuous over ...](https://www.ideals.illinois.edu/items/5045/bitstreams/19758/data.pdf) — `unrelated`
- [[PDF] SHEAR BEHAVIOUR OF REINFORCED CONCRETE SLAB UNDER ...](https://amslaurea.unibo.it/id/eprint/5902/1/Pieraccini_Luca_Tesi.pdf) — `unrelated`
- [The Dylatov Pass Incident: Has One of the Biggest Soviet Mysteries ...](https://www.openculture.com/2025/06/the-dylatov-pass-incident-has-one-of-the-biggest-soviet-mysteries-been-solved.html) — `unrelated`
- [[PDF] International Snow Science Workshop](https://arc.lib.montana.edu/snow-science/objects/P__8120.pdf) — `unrelated`
- [[PDF] Research on Weather Conditions and Their Relationship to Crashes](https://dot.nebraska.gov/media/120jdvat/m097-weather-conditions-and-their-relationship-to-crashes.pdf) — `unrelated`
- [Using Self-Driving Car Tech to Predict Avalanches](https://www.govtech.com/fs/Using-Self-Driving-Car-Tech-to-Predict-Avalanches.html) — `unrelated`
- [[PDF] THE EFFECT OF SLOPE ANGLE ON CRITICAL CUT LENGTH ...](https://arc.lib.montana.edu/snow-science/objects/ISSW2024_P3.12.pdf) — `unrelated`
- [[PDF] The effect of propagation saw test geometries on critical cut length](https://egusphere.copernicus.org/preprints/2024/egusphere-2024-690/egusphere-2024-690.pdf) — `unrelated`
- [[PDF] The effect of propagation saw test geometries on critical cut length](https://nhess.copernicus.org/articles/25/321/2025/nhess-25-321-2025.pdf) — `unrelated`
- [[PDF] A GUIDANCE FOR THE INTERPRETATION OF PROPAGATION ...](https://arc.lib.montana.edu/snow-science/objects/ISSW2024_O3.4.pdf) — `unrelated`
- [[PDF] Dynamic Avalanche Modeling in Natural Terrain](https://arc.lib.montana.edu/snow-science/objects/issw-2009-0448-0453.pdf) — `unrelated`
- [[PDF] WHAT ARE THE LIMITATIONS OF DYNAMICAL MODEL USE IN ...](https://arc.lib.montana.edu/snow-science/objects/ISSW2024_P2.10.pdf) — `unrelated`
- [[PDF] Machine learning for automated avalanche terrain exposure scale ...](https://nhess.copernicus.org/articles/25/4375/2025/nhess-25-4375-2025.pdf) — `unrelated`
- [[PDF] LOOKING BACK AT THE LAST 15 YEARS OF OPERATIONAL ...](https://arc.lib.montana.edu/snow-science/objects/ISSW2024_P1.2.pdf) — `unrelated`
- [Remote Sensing Tools Advance Avalanche Research | U.S. Geological Survey](https://www.usgs.gov/centers/norock/science/remote-sensing-tools-advance-avalanche-research) — `unrelated`
- [Home - AIARE](https://avtraining.org/) — `unrelated`
- [Dyatlov Pass Radiation: What Investigators Actually Found
 – Headcount Coffee](https://www.headcountcoffee.com/blogs/coffee-news/the-dyatlov-pass-radiological-evidence-what-investigators-found?srsltid=AfmBOopEY2m_5mR1hWbHK2JB_6WvPiVmysQY1Xob1Q5E1n2Eslx3PABV) — `unrelated`
- [The Katabatic and Anabatic Winds of Alaska - Matanuska Glacier Helicopters](https://matanuskaglacierhelicopters.com/the-katabatic-and-anabatic-winds-of-alaska/) — `unrelated`
- [The interaction of katabatic winds and the formation of blue-ice areas in East Antarctica | Journal of Glaciology | Cambridge Core](https://www.cambridge.org/core/journals/journal-of-glaciology/article/interaction-of-katabatic-winds-and-the-formation-of-blueice-areas-in-east-antarctica/21C1967EF85C011113E00E9C2EF12477) — `unrelated`
- [What is Depth Hoar? | Avalanche Safety 101 | The Next Summit: A Mountain Blog](https://thenextsummit.org/what-is-depth-hoar/) — `unrelated`
- [[PDF] Numerical modelling of seismic slope failure using MPM](https://www.igs.uni-stuttgart.de/institut/publikationen/Publikationen/2016/311_Bhandari_FH_CM_Sharma_Westrich.pdf) — `unrelated`
- [Improvements of MPM and Its Applications in Modelling Rapid Soil/Water Movements](https://www.repository.cam.ac.uk/items/312f89c3-c9b6-4236-bc43-22c134c80604) — `unrelated`
- [[PDF] Anticrack model for skier triggering of slab avalanches](https://avalanche.org/wp-content/uploads/2018/08/11_CRST_Heierli_etal.pdf) — `unrelated`
- [[PDF] Measurements of snow slab displacement in Extended Column ...](https://avalanche.org/wp-content/uploads/2018/08/14_CRST_vanHerwijnenBirkeland_ECT_SlabDisplacement.pdf) — `unrelated`
- [Avalanche Danger Prediction Python Library](https://zenodo.org/records/17277192) — `unrelated`
- [Modeling of snow avalanche dynamics using open source software OpenFOAM](https://ui.adsabs.harvard.edu/abs/2021EGUGA..23.6110R/abstract) — `unrelated`
- [[PDF] the influence of terrain parameters on the spatial variability](https://avalanche.org/wp-content/uploads/2018/08/11_Thesis_Guy.pdf) — `unrelated`
- [Avalanche Problems | Colorado Avalanche Information Center](https://avalanche.state.co.us/forecasts/tutorial/avalanche-problems) — `unrelated`
