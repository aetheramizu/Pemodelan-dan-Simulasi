# Agent-Based Models with Python: An Introduction to Mesa

> Complete study pack for the Santa Fe Institute *Complexity Explorer* course taught by
> **Project Mesa** (Jackie Kazil & Tom Pike), built around Epstein & Axtell's **Sugarscape
> with Traders** model. It contains, for all 21 sessions: the YouTube link, the direct
> MP4, the official transcript, and the notebook code for that session.

**Why this file exists:** it is the raw material for writing a video series that explains
the Mesa code line by line. Every code block below is verbatim from the course repo, and
every transcript is the spoken narration that goes with it, so an agent can map
*"what is said in minute 4"* to *"which line of code is on screen"*.

---

## Contents

| # | Session | Length | YouTube | Code |
|---|---------|--------|---------|------|
| 1 | Introduction | 1:36 | [watch](https://youtu.be/fUrUWnWGHEQ) | — |
| 2 | Sugarscape with Traders Overview | 6:37 | [watch](https://youtu.be/d_LsDaYi9U8) | — |
| 3 | Start Google Colab & Initiate Classes | 12:36 | [watch](https://youtu.be/9UcruDxNyiw) | `Session_3_Start_Colab_and_Initiate_Model.ipynb` |
| 4 | Upload the Landscape | 9:48 | [watch](https://youtu.be/P97_8aYUL6Y) | `Session_4_Upload_The_Landscape.ipynb` |
| 5 | Agentize the Landscape Part I | 10:41 | [watch](https://youtu.be/iRw8YpewpQE) | `Session_5_Agentize_The_Landscape_part_1.ipynb` |
| 6 | Agentize the Landscape Part II | 13:13 | [watch](https://youtu.be/jylBFLhI-uA) | `Session_6_Agentize_The_Landscape_part_2.ipynb` |
| 7 | Initialize Traders | 25:33 | [watch](https://youtu.be/kOrocERLtTM) | `Session_7_Initialize_Traders.ipynb` |
| 8 | Sugar & Spice Step Functions | 17:40 | [watch](https://youtu.be/AUtAueSYQFc) | `Session_8_Sugar_and_Spice_Step_Functions.ipynb` |
| 9 | Traders Move Part I (Initiate Move) | 7:40 | [watch](https://youtu.be/hrUPIW4BNNo) | `Session_9_Traders_Move_part_1.ipynb` |
| 10 | Traders Move Part II (Identify Neighbors) | 13:13 | [watch](https://youtu.be/vVm6U8iO-Ck) | `Session_10_Traders_Move_part_2.ipynb` |
| 11 | Traders Move Part III (Maximize Welfare) | 19:13 | [watch](https://youtu.be/cO_4pdgTerU) | `Session_11_Traders_Move_part_3.ipynb` |
| 12 | Traders Move Part IV (Move to Best Closest Option) | 18:34 | [watch](https://youtu.be/mThJ2hThOs0) | `Session_12_Traders_Move_part_4.ipynb` |
| 13 | Traders Eat | 13:16 | [watch](https://youtu.be/0JHbP2vJxAw) | `Session_13_Traders_Eat.ipynb` |
| 14 | Traders Trade Part I (Get Neighbors) | 14:11 | [watch](https://youtu.be/ggZgf2aciNg) | `Session_14_Traders_Trade_part_1.ipynb` |
| 15 | Traders Trade Part II (MRS & Price) | 12:54 | [watch](https://youtu.be/T1sQYt0mquk) | `Session_15_Traders_Trade_part_2.ipynb` |
| 16 | Traders Trade Part III (Trade Sugar & Spice) | 17:54 | [watch](https://youtu.be/3rG52ZWy6FE) | `Session_16_Traders_Trade_part_3.ipynb` |
| 17 | Traders Trade Part IV (Complete Trade) | 14:33 | [watch](https://youtu.be/nTEai0dTCRw) | `Session_17_Traders_Trade_part_4.ipynb` |
| 18 | Data Collector (Model Level) | 21:56 | [watch](https://youtu.be/ymVD4ofs8OQ) | `Session_18_Data_Collector_Model.ipynb` |
| 19 | Data Collector (Agent Level) | 17:14 | [watch](https://youtu.be/w6wV7H3lCL0) | `Session_19_Data_Collector_Agent.ipynb` |
| 20 | Batch Run | 15:18 | [watch](https://youtu.be/IRCGJndsgpw) | `Session_20_Batch_Runner.ipynb` |
| 21 | Conclusion | 1:02 | [watch](https://youtu.be/JeqhJuUmqy4) | — |

**Total runtime:** 4:44:42 across 21 sessions. **Code:** 18 notebooks, sessions 3–20.

## Sources

- Course home: https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa
- Lecture list: https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17326
- Code repository: https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial
- Video files (S3): https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/

---

## How to use this file

1. **`## Session N` heading** — one per lesson, in teaching order.
2. **Links block** — YouTube (with duration), MP4, lesson page, notebook.
3. **Transcript** — the narration, cleaned of caption timestamps and rolling
   duplicates. It is speech-to-text, so proper nouns wobble (`Mesa` → `Misa`,
   `Jupyter` → `Jupiter`, `Colab` → `collab`, `Sugarscape` → `sugar skate`,
   `AgentSet` → `agent set`). Fix these when quoting.
4. **Code** — cells in notebook order. Each is preceded by an HTML comment
   `<!-- cell N: code -->` (invisible when rendered) marking the notebook cell
   boundary, so a script can say *"the fifth cell adds the traders"*.

The transcripts are the *spoken* layer; the notebooks are the *written* layer. They do
not line up cell-by-cell, because the instructor types live and backtracks. When they
disagree, the notebook is what actually runs.

---

## Session 1 — Introduction

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=fUrUWnWGHEQ |
| Length | 1:36 |
| Video title | Session 1: Introduction |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+1+Introduction.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17326 |

### Transcript

<!-- 249 words -->

hi I'm Jackie Hazel one of the original creators of Mesa and I'm Tom Pike I'm one of the developers on team Mesa and I'll be walking you through the tutorial Mesa is an open source Python 3 library that allows eight users to quickly create agent-based models using a decoupled architecture Mesa includes the ability to run browser-based visualizations but also the ability to run headless being built in Python it gives users the ability to take advantage of other tools in the python ecosystem for data handling such as pandas Network X Jupiter notebooks and more over the next several lessons in order to learn some Mesa some Python and some things about age-based modeling we'll be building the seminal model sugarscape with Traders created by Rob Axtell and Josh Epstein uh in order to do this I'll be demonstrating the code through uh Google's Jupiter environment which is known as collab this is free the to anyone with a Google account although you can use whichever integrated development environment I you would like right each session of code will be available through Santa Fe institute's complexity Explorer GitHub and all the code is available in dot Pi files through mesa's examples repositories found in this on its GitHub page in the first lesson we'll be talking to Rob Axtell one of the co-creators of the sugar skate model As you move through the lessons please don't hesitate to ask questions we hope you enjoy this tutorial

### Code

*No notebook for this session — it is lecture, demo or discussion only.*

---

## Session 2 — Sugarscape with Traders Overview

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=d_LsDaYi9U8 |
| Length | 6:37 |
| Video title | Session 2: Sugarscape with Traders Overview |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+2+Sugarscape+Overview.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17598 |

### Transcript

<!-- 1382 words -->

so welcome to session two with Santa Fe institute's complexity Explorer Mesa tutorial agent-based modeling in Python I'm here with Rob Axtell one of the co-creators of the sugarscape model particularly the one we're using sugar escape with Traders right in the book growing artificial societies so Rob could you please introduce for us to sugarscape with Traders model okay well thank you for the introduction Tom and happy to be here talking to you guys so in the surescape model as you guys remember there's are there are resources distributed around the landscape and on that landscape in the simplest case is just sugar but in order to address models of trade Traders we only have a second commodity so the second commodity is what we call not normally spice and then we give the agents uh preferences for both the sugar and the spice and then they're going to given the fact that those resources are heterogeneous on the landscape the agents encounter them differentially will accumulate them at different rates and then we'll find that there's some advantage to trading them back and forth now how did we specify the ways that the trade would happen it turns out that in economics there's a well understood theory of uh bilateral bargaining as it were that's called the Edgeworth box that is uh say Tom has so much sugar and a certain amount of spice I have different amounts we have so many different preferences for the whether maybe time like sugar more than spice and I'm the reverse we meet in general the idea is that he's been out accumulating these things I've been committed these things we meet and in general there's some way for us to rearrange our Holdings and the key is to make us both better off so we both benefit from the trade and so the way economists do this is what's through What's called the you know you compute the marginal rate of substitution of these things and then that gives that determines kind of a local price at which you want to trade the sugar for this place and uh if Tom has got one price and I have a different price we just pick a price in the middle somewhere and we'll trade at that price and then we can exchange uh at that price we are both better off after the trade that's a whole kind of theory of how it works and then so we did on the sugarscape models we just implemented that every time agents are immediate neighbors they end up being they engage in this kind of trade when they're on the sugar and spice landscape now it turns out that um conventional theory has a lot to say about how that should work and the usual kind of supply and demand story would apply should apply when you think about the fact that there's going to be some you know in the case of the sure State model looking a few hundred buyers a few hundred sellers they should follow the supply and demand calculus but it turns out that um in this distributed decentralized bottom-up view of the world that we have in the sugarscape um you know whether supply and demand equilibria obtain or not is a scientific question you can ask you know what conditions will it obtain or not and so just you know the basic result is that and markets where people only engage in bilateral trade and that Global exchange is in essence there's some kind of friction uh limiting the achievement of the supply and demand equilibrium and so what you observe in the sugarcane model then is You observe these departures from the pure supply and demand configuration uh in essence you get you know you get somewhat less quantity traded that's the frictional part of it but the prices are being about the power right so you can get to get the price to turn out right more or less but the quantity is suppressed but then over time people trade more and so just one way to think about then the uh the trader model and the sugarscape is just that it's a bottom-up view of how supply and demand emerges uh from the interactions of it in the individual you know purpose of Agents we won't say rationalists so they're somewhat rational in the sense that they're doing what's best for themselves but they're not rational incentive trying to you know I'm training with Tom I'm not seeking out like you know Bill Gates to treat with her George Sora or something I'm just trading with where we're in my neighborhood so uh is it fairly conventional view but rendered at the level of a lot of interacting agents now it turns out that economists had worked out some of the theory for this but in fact when we built that model in 94 or some book came out in 96 um the much of the theory was still in development in the sense and so it turns out that um what we know today which is quite interesting I think is that um these decentralized models have quite good computational complexity meaning that they can easily be produced by agents who are just doing that running around trading stuff locally at their prices whereas if you try to compute the market clearing price from the top down as it were by say aggregating everybody's preferences and saying you know how much what should the price be this include the market that is actually known today only known by the way from 94 forward really as a very hard computational problem to definitely kind of you know an NP type hard problem it turns out the a computer scientist to find a new complexity class that's in between p and p that would include this of this walrusian fixed Point problem of Market set but without going down that uh into those details ideas that some uh a bottom-up view of decent employees view of exchange among individuals leading to a kind of a market clearing price is a is kind of a different perspective than the usual just supply and demand for uh picture but is in some sense the Richer one and probably a more realistic one and imagining that you know somebody you know when you drive home tonight and you see the price of gas on the corner uh it's just not clear that you know some uh Auctioneer has computed that from that top down much more likely that the gas station manager has just decided to raise the price today by a penny or reduce it by a penny and that's the way real economies were created a bunch of adaptive agents are all adapting to one another not waiting for an Auctioneer to announce the market clear price Vector that makes the economy uh work at full speed so but with that is background there are several in the chapter on this in the sugarscape there are several excursions based on that journal idea things like you know what if you suddenly changed the preferences of the agents or what if you suddenly have a shortage of one of the goods those kinds of things you can see how the prices adapt and come back in so uh there are several different variations on that in the sugarscape book but the key idea is that some just having trade among the individuals each one doing this Edgeworth barter uh yeah and uh leading there to something that looks like a market clearing price that was the basic idea of many years ago um and uh and I think it's we still the test of time insofar as there have been a lot of abm's of Market phenomena subsequent to that model and many of them use this kind of uh decentralized uh price formation procedure to uh understand how markets all right awesome thank you very much Rob there's no way I could have given an introduction uh so now that you understand where the you're going to see with Traders models come from let's get started

### Code

*No notebook for this session — it is lecture, demo or discussion only.*

---

## Session 3 — Start Google Colab & Initiate Classes

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=9UcruDxNyiw |
| Length | 12:36 |
| Video title | Session 3: Start Google Colab & Initiate Classes |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+3-+Start+Colab+and+Initiate+Model.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17208 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_3_Start_Colab_and_Initiate_Model.ipynb |

### Transcript

<!-- 1896 words -->

welcome to session three of complexity explorers Mesa tutorial in this session we'll we'll set up our Google collab instance which will allow us all to be working off a common environment right and we'll initiate our classes if you don't want to use Google codelab and use your own integrated development environment that is entirely up to you just please appreciate there might be some challenges that should be fairly easy to resolve now let's get started so the first thing I want to do is if you open up a Google page and you will need a Google account for this such as an email right just search Google collab and then go to their welcome to collaboratory link which should pull right up we can initiate with a new notebook well we should then uh which should get a screen that looks something like this first thing I do is rename it so I can hit file go to rename and I'm going to call this Mesa tutorial all right we'll use this file uh to build our Mesa uh with Traders model throughout the rest of the lessons next up we need to import our dependencies so as this is a Mesa tutorial the first thing will be to install Mesa we use exclamation point pip install Mesa now the trick is Mace is constantly under development and at some point there might be a change to how Mesa operates that could make that could cause issues with this tutorial so if there is an option to use something called pinning where you could do pip install Mesa equal sign and then the version of Mesa that you want to use right so as an example we use 0.8 which is an older version of Mesa okay I and then Google collab will install it right uh as it uh if this ever happens uh then we'll be able to add a text box later into the videos to tell you which version of Mesa was the latest before there was a breaking change all right uh as you can see here once you install one then you could change that number the current version as of this video is 1.1 but we anticipate uh based uh on some changes so we'll go to 2.0 here the next couple months but there should be any breaking changes for this tutorial all right and as you can see here uh it uploads now version 1.1 right and critically it uninstalls the previous version that we uh had just installed to make sure that there's no conflicts right however for the rest of the tutorial we're just going to do uh pip install Mesa um and if there's ever a reason to pin to a specific version of Mesa we will add that uh as a text box inside the video all right as you can see here uh it's already installed right so next up after we install Mesa right you could clear the output if you want by right clicking on the output field now we have to import it okay so now that we've installed it we can now import it okay uh a kind of good tip to have make to help the readability of your code particularly in colab or uh Jupiter lab right is that you can add text Fields uh as headers so you can collapse uh cells of code you don't want to see right so in this case I we use hashtag or pound sign import dependencies and then use the right arrow on the upper right side of the cell to move it up to the top you see this little arrow off the side right allows you to collapse those cells so that they're hidden okay all right so I can now add another text field all right and in this case we're going to initiate our resource classes so this three agent classes that we use um in uh sugarscape with Traders the first two are resource classes uh which are um our sugar agents and our spice agents so to initiate these we're going to do class sugar right and then uh we're gonna pass in mesa.agent with a capital A right this Imports mesa's agent class or inherence mesa's agent class from what we imported uh in a previous cell coding cell all right so that's how you initiate a class in Mesa all right it's always good to comment so your code is more readable for you or other people that look at it and so what is sugar uh sugar is an agent that contains an amount of sugar and that agent and then what it really does for each step is that it grows one unit or one amount of sugar for each iteration of the model for each turn okay now that we've got our comments we can now I use mesa's initiate function or initialize in order to initialize uh this class so you do death underscore init underscore and then per mate python syntax self right and then for this lesson we'll just use a print statement to say I am sugar so we're going to run that and if we have any syntax errors those will then show underneath the cell all right now we do the same thing for spice so class spice all right uh open parentheses Mesa dot agent with a capital a okay and then we'll add uh our comments to make our code more readable and understandable to both Us and other users and spice is the same as sugar where it contains an amount of spice then grows one amount of spice at each turn okay once we got our comments right now we can uh initialize are our spice agent the same way we initialize our sugar agent so use python syntax of classes it'll be def underscore init underscore self uh in parentheses and then for this lesson uh we'll just do print I am spice and just to make sure our classes are initiating the way we think they are all right next we're going to add a new type of class so this is going to be our Trader class all right so I'm going to put in a header here this will be the longest and most complex of all the cells we're going to have in this model due to the amount of activity that our Trader agents will use okay and then but this still initiates the same way as our other resource classes so in this case it's going to be class and then Trader with a capital T and then Mesa dot agent with a capital A because inheriting the agent class uh from Mesa and then we'll put in a similar comment code so Trader has a metabolism right that's how much sugar and spice they process for each uh step or each turn right and they harvest and trade uh sugar and spice all right so this is really what um the dynamic of the sugarscape with training bottle right is that you have sugar and spice and then you have Trader agents that need to use that Sugar and Spice to survive and they so they then Harvest and trade that Sugar and Spice to optimize their support and then just like sugar and spice we use pythons to initialize or initiate function deaf underscore in it underscore self right now I'm going to put print I am a Trader this is just to make sure that our code is initializing the way we think we do their model right so now I have our three uh Asian classes uh that have been built okay so the next thing we want to do is create a model class so similar to the previous ones we'll create a header I'm going to call this our model class and then for our model class right we initiated the same way as the sugar spice in the trade it would put class this word called sugarscape Capital G1 Mt this is to follow the nomenclature that Rob Axtell and Josh Epstein use in that book growing artificial societies foreign when we inherit from Mesa we're going to do model with a capital M as you can see with all our classes we're capitalizing the name of the class so in order to identify it as a class right then we'll put our commentary so that way it's easier to read and remember what each thing does right and this class is a model class to manage the sugar escape with Traders model again this is identified in the book as g1mt and just to be clear the book we're using is growing artificial societies by Rob Axtell and Josh Epstein from 1996.

I add two short points will actually reference specific page numbers uh if necessary based off the python code we write to replicate uh their model now that we've put our notes in we're going to initialize uh the model class the same way we initialized our Trader and resources class by first using the initialize function def underscore in it and then per python convention open parenthesis self and that uh and then now we're going to call each of our model classes so we're self.spice right and then equal spice remember capital letter for our capital S for spice right and then the function to say I want to initiate that class then we're going to call uh self.sugar all right that's going to equal an instance of our sugar class right so capital S right with open close parentheses and then the same uh with trade right self.trader capital T for Trader and then parentheses to initiate our trade of class okay so we now have our model class setup where we initiate each of our subclasses our agent subclasses okay so now we want to create an instance right of our sugar and state model so uh just like we create instance of our spice sugar Trader class we create instance of our sugar Escape g1mt right um and so this is uh our model class calls our this our instance of that calls hormonal class which calls our Trader class which and calls our agent classes now I want to see if they do what he said but nothing happens all right why is that because you got to put the function uh call of open close parentheses right in order to make sure that your model gets initiated calls that function and sure enough uh sugarscape ga1t initializes each of our Asian classes and then they produce uh our um uh they per initiate each one of those producing the print statements fine all right now so uh once that's done you can do a save and pin revision because this will uh represents the end of session three where we've import our dependencies and initiated each uh of our agent classes and our model classes and they all work together so thanks for joining us I will see you for session four in which we start to add more functionality to each of our classes thanks for joining us

### Code

From `Session_3_Start_Colab_and_Initiate_Model.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
!pip install mesa
```

<!-- cell 3: code -->

```python
import mesa
```

<!-- cell 4: markdown -->

> # Resource Classes

<!-- cell 5: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar: 
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn 
  """

  def __init__(self): 
    print("I am Sugar")
```

<!-- cell 6: code -->

```python
class Spice(mesa.Agent):
  """
  Spice: 
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self):
    print("I am Spice")
```

<!-- cell 7: markdown -->

> # Trader Agent

<!-- cell 8: code -->

```python
class Trader(mesa.Agent): 
  """
  Trader: 
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self):
    print("I am Trader")
```

<!-- cell 9: markdown -->

> # Model Class

<!-- cell 10: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """
  
  
  def __init__(self, width=50,height=50):
    self.spice = Spice()
    self.sugar = Sugar()
    self.trader = Trader()
```

<!-- cell 11: markdown -->

> # Run Sugarscape

<!-- cell 12: code -->

```python
model = SugarscapeG1mt()
```

---

## Session 4 — Upload the Landscape

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=P97_8aYUL6Y |
| Length | 9:48 |
| Video title | Session 4: Upload the Landscape |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+4+-+Upload+the+Landscape.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17209 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_4_Upload_The_Landscape.ipynb |

### Transcript

<!-- 1563 words -->

welcome to session 4 of complexity Explorer's Mesa tutorial agent-based modeling in Python in this lesson we're going to upload a landscape so that we can agentize that landscape and create the environment for our Trader agents to harvest and trade sugar and spice let's get started please open your Google collab instance now the first thing we want to do is install Mesa and then import it through our dependencies now if you're using these header functions that are available in collab you can also then collapse these cells to make your code more readable all right we then got to instantiate our sugar and spice resource classes it also collapse this and then our Trader agent class foreign next we could instantiate our model class our sugarscape G1 Mt following the growing artificial societies convention and this one right now just calls or instantiates each one of those other classes in a model instance that if we run it just prints out each of the model or each of the classes right for aging classes for sugar spice and Trader and that initialize the landscape we're going to focus mostly in the model class the first thing we're going to want to do is set the size of our landscape Now using Mesa Convention we follow the Cartesian grid coordinate system so it's width or your effectively your x-axis and then height or you use keyword arguments or quarks to set this keyword arguments have the advantage uh that I we can change these parameters later on but we also can initiate them to a base class so that way we don't have an error if we forget to uh if we forget to put in those parameters when we call the model so first you always want to make sure we have good comments All right so with our width and height parameters we want to assign those attributes to our model class all right this is just setting ourself.width is going to equal width and our self.hype will equal height now that we've done that we want to initiate the Mesa grid class so that way we could create our grid space in which to load our sugar spice and trade in Trader agents this will provide the environment in which they're going to operate in order to grow for sugar and spice or harvest and trade for our Trader agents and now the good thing about Mesa is that you could see all the code it's somewhat python all the way down right so when we call the grid class we're actually calling this space.py file which is available in the Mesa repo right as you look through here's the Base Class of grid right and then here's a lot of the uh the functions that we'll be using for the grid class all right that does things like git neighborhoods iterate through any of the cells and numerous other functions all right as you can see here this is a class we'll be using which is multi-grid which allows multiple agents to be in one cell at any other time there's also other classes you can call such as hex Grid or network or continuous space all right and all of these you can audit and kind of see how those classes function as well as if you need to add other classes and potentially even contribute to Mesa right so to call this we just need to call that instantiate that class just like we instantiated our sugar spice and Trader agents so call this self.grid all right they'll call the Mesa dot space file which is just this file in the Repository our locally installed on your computer or in this collab instance and then we're calling the multi-grid class okay so with that takes a couple arguments so first our width all right again our x-axis and then our height and then it has another keyword argument called Taurus which we're going to set to faults now Taurus means is just the shape I it looks like a donut if you wrap your left and right size to it talk to each other and you're top and bottom to touch each other following growing artificial societies we're going to set this to false all right now that we have uh now that we're calling ourself.grid the next thing we want to do is read in the landscape from our supplementary material so if you look at complexity explore supplementary material right you'll see a sugar Dash map.txt file right so we want to upload that right for a sugar distribution okay to upload this we're going to use a another python Library called numpy where you use a function called gen from text so you do sugar distribution equals np.gen from text Sugar Dash map dot txt okay so to make this function work we first have to import numpy so we go up to our import dependencies right under Mesa we could do import numpy as MP right doing this is pretty standard Mesa Convention to call numpy MP all right so that's part one now we could call that function another thing we have to do is make sure that a sugar map is loaded so python knows where to look for it all right to do that in colab is fairly simple we'll show you a couple different ways but first we'll hit the file off to the left hit load the upload file and then wherever you downloaded it from the supplementary or materials uploaded all right and now python knows to look in your local file system all right in order to find that file and now I want to make sure that it did what we expected it to do so we're going to print out the shape of the sugar distribution and shape is just a numpy function to understand what uh what the data structure is that we called in okay so to look at this we'll call shape all right um and as you'll see oh we made a mistake also you can see we have an attribute error Mesa does not have an attribute called spay spice it's actually called space so that's easy enough read that and then call it in as you can see we have a 50 by 50 right that's our width and height and we called or we printed the sugar distribution at 30.

so that's just the column at your x-axis of 30 right and we could also see the Y position all right so put 15 here so now I got a width and our height all right so if we call that we could see you know we have uh that the value of our sugar at x equals 30 and y equals 15 is 4. all right so that's actually the highest value so we're up on a hill uh a Sugar Hill for that one and that just shows us that help us understand the data structure of our sugar distribution all right so we know what exactly we're looking at so now we want to make our spice distribution we're going to do this just by converting our sugar distribution all right so again using numpy functions another benefit of python you have this Rich ecosystem that you can leverage to get you know lots of functions and capability without having it coded all from scratch yourself all right we're going to use their flip function along for the sugar distribution which just flips it along its X and Y axis all right and then we're going to use a python the standard python visualization library and probably most common all right matplotlib to create a heat map so we can verify that our landscape looks the way we think it should all right now one trick is that they put the origin in the upper left corner not the lower right so we're going to have to use their keyword argument to switch the origin to the lower left so it's consistent with the Cartesian grid coordinate system we also need to import a matplotlib so again standard python convention for matplotlab is you import matplotlib dot Pi plot as PLT right and then for a Jupiter notebook or Jupiter instance like we're now we do percent sign matplotlib inline so it will actually appear beneath our cell and now it can run import that so we run that cell right we run our model class all right and now I can see our sugar distribution and that looks uh like we would expect it to and is consistent with growing artificial societies all right now I could check our spice distribution make sure that it flipped the way we wanted it to right and sure enough now we got Hills of sugar and spice in each quadrant of our sugarscape landscape foreign now that we've successfully now for this lesson we have successfully uploaded uh our sugarscape landscape which in the next lesson we can start to agentize in order to create our sugarscape with trading agent-based model thank you for joining us and we hope to see you in the next session where we start to agentize the sugar uh

### Code

From `Session_4_Upload_The_Landscape.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
!pip install mesa
```

<!-- cell 3: code -->

```python
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 4: markdown -->

> # Resource Classes

<!-- cell 5: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar: 
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn 
  """

  def __init__(self, unique_id, model, pos, max_sugar): 
    print("I am sugar")
```

<!-- cell 6: code -->

```python
class Spice(mesa.Agent):
  """
  Spice: 
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self):
    print("I am spice")
```

<!-- cell 7: markdown -->

> # Trader Agent

<!-- cell 8: code -->

```python
class Trader(mesa.Agent): 
  """
  Trader: 
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self):
    print("I am Trader")
```

<!-- cell 9: markdown -->

> # Model Class

<!-- cell 10: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """
  
  
  def __init__(self, width=50,height=50):
    
    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height 
    
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material 
    sugar_distribution =np.genfromtxt("sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)
    plt.imshow(spice_distribution, origin="lower")
```

<!-- cell 11: markdown -->

> # Run Sugarscape

<!-- cell 12: code -->

```python
model = SugarscapeG1mt()
```

---

## Session 5 — Agentize the Landscape Part I

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=iRw8YpewpQE |
| Length | 10:41 |
| Video title | Session 5: Agentize the Landscape Part I |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+5+Agentize+the+Landscape.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17210 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_5_Agentize_The_Landscape_part_1.ipynb |

### Transcript

<!-- 1799 words -->

SE five of M of complexity explorers Mesa tutorial agent tise the landscape part one in this one we'll start to turn the sugar data we have from our sugar map uh into agents that we can use for our agent based model let's get started okay so the first thing want do is if you remember from session four right so we're gonna uh make sure that a sugarm map. txt file is uploaded so that we can use it right and at this time for the PIP install Mesa we're going to the quiet argument all right so that way it doesn't produce as much uh as much output so it starts to install everything and see there right then we're going to import uh the same libraries we had last time right we're GNA you know run uh our sugar class which is inherits mesa.

aent our spice class uh which inherits uh mesa. agent right our Trader class also an agent right uh and then our sugarscape un which actually herit mod we've set up our height width we establish a multi- grid right um and then we uh read in our sugar distribution we flip that Sugar distribution to make our spice distribution and then when we call our model right we get this image um of our sugar uh of our Sugar Hills right so now what we want to do uh is start to turn our give some attributes to our sugar agent okay so in a typical Mesa model you'll always have at least two uh parameters for your agent so one's unique ID right so every agent has a unique ID right and then the model in this case we're also going to add position right uh and then the attribute of the max sugar which is the max of amount of sugar that e each that each sugar agent can have right based off the readin from the font okay so now we're going to inherit um the unique ID and model all right uh from our Mesa agent class so we can use Python super.

init right we'll do unique ID right um and we'll do the model okay now if you ever want to see what these mean of the source code that are choosing you can always go to mesa's um uh the Mesa GitHub repository you can also click view Source if you're in collab that'll show you the code we're using in this case we'll go to the GitHub Mesa Library right as you can see here we're in uh the Mesa GitHub repo in Mesa folder and then the agent. piy so when we call that class is we're actually calling class agent right as you can see here it has unique ID and model it also has position but we're just going to uh pass that in as its own attribute instead of inh so then we're g to do uh using standard python syntax we're going to do uh self.

position pause for position that's going to equal pause or the agent's position right um and then we're gonna use max sugar for two attributes first the current amount of to instantiate the current amount of sugar right so this is the one we can uh reduce if an agent eats it all right um or takes it all and then the amount of Mac sugar it has so that way we could keep track of how what's the most sugar that this particular cell can have in the multi- grid okay so this right here then in stand iates sugar agents right with those four parameters right the model the position that they're at and then the amount of sugar they have at any given time the most amount of sugar that they can have okay so now we go back down to our model right and what we want to do is um use a for Loop all right to now assign uh each um use a for Loop to create uh each agent or instantiate each agent okay so now to do this we're going to use one of mesa's uh well first we have to set up our agent ID right so this is just uh so we could make that unique ID which should just use account and then we're going to use this for Loop right um uh which requires first a parameter all share second that we don't use then this position in a tupple XY we're use Ma's uh function chord iter which just is a function to iterate over every uh grid cell uh in mesa's space function right so you can see uh what exactly cord iter does right um we can use a print function so that way you could see what attributes are part of uh the self.

coordinator okay right so we do print okay underscore and then the topple XY and we run this and now we're actually going to get an error why do you ask right uh because we didn't uh it's not self. cordinator it's self. grid right so it's very important to when you think about what you're referring to in Mesa that you know what um what sub uh module it is right and so this is part of the self deck grid which was from Mesa space. multi-grid all right so we're calling a class from Mesa space right you can see here every grid will have a list of things that are in that grid right and its position all right and just like the mesa.

agent if you ever want to see what that code is uh that's creating the multi- grid right then you can either uh view source to that or in this case if we go to Mesa then mesa. space all right we could see that's where the chord iter function is okay so it's b. space right and then chord iter which is a subf function of the multi-grid class right um so it's at line 195 and if we scrolled up we'd be able to see class multi-grid all right so that's why I call mesa. space right it's in the Mesa folder in the space uh folder and then multi-group right okay so now we're going to take this for Loop and we're going to uh instantiate our agents uh so first we got to get um the sugar from the sugar distribution all right and because the sugar distribution has the same width and height as our grid we'll just be able that X and Y uh will be able to reuse um to aate through our sugar distribution right and now we know that some areas have no sugar so we want to do is only uh instantiate an agent uh if that crid cell actually has some sugar on it right uh and so then we dogar sugar equals and then we're going to call our sugar agent that's what the big S is for right um and then we're going to put those parameters that we just created so agentcor ID then we're going to pass in self because this is our model class so that self gets translated to model uh when it goes to the uh agent class okay next we got a pass in the position which in this case is a tuple all right for uh XY right um and then the final bit is what their Max sugar is all right which is then used twice both to create its initial sugar amount all right uh as well as to create um uh as well as to I store how much sugar that can the most sugar that cell could have that given time all right so we've now created a sugar um object class or a sugar agent that we've instantiated in an object class all right um that we now need to place on the grid so once again we go to self.

grid so now we're referencing our mesa. space. multi-grid right and we're going to place an agent all right uh at that location right and so we're going to use now this sugar uh object agent that we've created and we're g to position it in the Tuple at XY we then are going to iterate our agent ID by adding one to it and so that way every time we go through this Loop right each sugar agent won't get its own uh unique ID so once again we go uh we iterate through um the every grid cell identify um the uh the position that we're at identify how much sugar should be there instantiate the amount of sugar and the position H into a uh grid cell right uh and then place that agent on the grid and just so you can see what this looks like or um we're going to add a print statement uh so that way once we're done uh we can see uh we can you can identify um everything that we've done right so we got unique ID model uh position Mac sugar right and now I want to see uh how this impacts uh what happens when we iterate over the grrip so we use the same for Loop here 4ore XY and self.

grid. cord it right and then we're going to print it so it's going to iterate through and create all those agents then we're iterate through it again just so you can see the impact that it has on the model right okay so now as you go through you can see if there's a cell with sugar in it right you can see some have don't right now you can see a sugar agent object at a specific hexadecimal memory location all right so that's saying hey at this uh that's where you see the capital S for sugar and right is located at this specific memory location right so now that there's something in that uh in that grid cell right uh you get that uh agent object and so then this wraps up the first session of uh session five or the first part of agent ties the landscape session five right and then next time what we're going to do uh is we're going to um add in the spice uh and a and finish uh creating our sugar and spice landscape all right so thank you for joining us and we hope you enjoyed session five if you have any questions or comments uh please don't hesitate to use the Forum that's associated with complexities Explorer I look forward

### Code

From `Session_5_Agentize_The_Landscape_part_1.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
!pip install mesa --quiet
```

<!-- cell 3: code -->

```python
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 4: markdown -->

> # Resource Classes

<!-- cell 5: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar
```

<!-- cell 6: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self):
    print("I am spice")
```

<!-- cell 7: markdown -->

> # Trader Agent

<!-- cell 8: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self):
    print("I am Trader")
```

<!-- cell 9: markdown -->

> # Model Class

<!-- cell 10: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height

    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1
        print(sugar.unique_id, sugar.pos, sugar.max_sugar)
```

<!-- cell 11: markdown -->

> # Run Sugarscape

<!-- cell 12: code -->

```python
model = SugarscapeG1mt()
```

---

## Session 6 — Agentize the Landscape Part II

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=jylBFLhI-uA |
| Length | 13:13 |
| Video title | Session 6: Agentize the Landscape Part II |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+6+Agentize+the+Landscape+Part+2.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17211 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_6_Agentize_The_Landscape_part_2.ipynb |

### Transcript

<!-- 1823 words -->

session six of complexity explorers Mesa tutorial in this session we're going to finish agentizing the landscape by turning our sugar distributions into agents as well as adding both our sugar and spice agents to our schedule let's get started so if you open up your Google collab before we begin make sure that you have uploaded your sugarmap.txt this file is necessary to ensure that I can actually read the distribution is the upload button okay it's found in the course material right now we're going to import our dependencies right so previously we've done this pip install Mesa quiet but a more common convention for this is to do a python try accept state try and then you try and import Mesa if that doesn't work then you do the PIP install and again we'll be using the quiet parameter so that way we don't get it we reduce the amount of output and then after we install we can import so now that we've saved from that and now all our import functions aren't one cell so we could get rid of this set next is our resource classes right so here's our sugar class that makes uses a black formatting right so in that case you actually don't want the space between the quotes and the class however there's a library for that called Black and that'll fix it for you if you ever decide to make a contribution here's our spice class we'll be updating that later right our Trader class which we'll discuss in later lessons and then finally uh our model class run this is where we initialize our model we'll be working most of the time right uh and just want to make sure it's all still working all right um so the first thing we want to do here is we're not going to need this print statement anymore all right this is the for Loop where we take our sugar map.txt and sugar distribution and turn that into agents and place them on the grid but we also need to put our agents in a scheduler so that way we could track what order they're activating this is important as the activation order of any agent-based model does have an impact as was shown by Dr Ken Comer in his dissertation who goes first but if you want to see all of the options remember this is a good amazing GitHub page go into Mesa and in the time.py file you can see all the activation classes so you have your base scheduler your random activation simultaneous activation and Stage activation right but the one we'll be using I and for our model is random activation by type because we have sugar spice and Traders okay and all these have different variations on how to select your activation regime which depending on your model will uh will have various impacts as you try and replicate your phenomenon of Interest right so to imp or to create instantiate an object called schedule called self.schedule right there'll be Mesa at that time uh dot random activation rise of our imported Mesa the time.py file and now the class random activation by type and so we can initiate that and now we have uh instantiated an instance of our random activation by type class all right we'll store that in self that's good now we want to make sure that we add our agent into the schedule so they're in a location if you will on the grid right and now they need to be stored inside the schedule so they'll be their behaviors will be activated uh throughout the model and as we'll see later the schedule looks for the step function as the way to determine what step each agent should be doing in the model right so now that we've done that now we need to create our spice uh agents right so we've created our sugar agents now we're going to create our spice agents and so now we're uh just to fall in the exact same process iterating through um each element of our grid because that is a 50 by 50 array just like our sugar and spice distribution is our spice distribution is a 50 by 50 array all right and we'll just follow that same process now this kind of violates the dry principle or do not repeat yourself um in that word using pretty much the exact same code for our spice agent as we are for our sugar as we did for our sugar age so now the first thing we're doing is identifying what's the max spice at that location now is the sugar spice and grid all have a 50 by 50 array it's not strictly necessary to have both these for Loops be a very large model this can add a lot of overhead that's not necessary right the impact has had would be all the sugar agents will be sequential in their agent IPS and then all the spice agents would be sequential which may not be desirable for personal preferences or other reasons right but we don't actually need it and since the age of by type will keep track of which agents are sugar which agents of spice or which agents are Traders uh we're I'm actually not going to use this remember we did want to provide you some uh inside of the you know various options or choices uh that are really up to you uh when you're making your model right but now pretty much follow the very similar code right so identify what the max spice is at that x y coordinate right then if it's above zero so again this is to make sure we don't create unnecessary agents right then we're going to instantiate um uh a spice class object so that we can add it to the grid and add it to the scheduler okay so I have our space class okay uh and you know follows the same Convention as a sugar class then we place it on the grid until we call our grid object and use a place agent function for the Mesa space.pi file and then we're going to place it in our random activation by type scheduler right which is instantiate ourselves that schedule attribute uh and then we're going to iterate through and add one to our agent ID so now that we've done that we need to update our spice function or our spice class rather so it actually uh takes in those parameters or as seen in the last lesson we'll get an error all right so we'll run this just to get it stored in memory and I'll scroll up to our spice class and add those same parameters so first is unique ID right this is required by Mesa that all agents have a unique ID that way you can keep track of them in the scheduler I'll point it to your model their position so they know where they are all right and then the parameter which is the max amount of spice that they can have and then we create the attribute substantiate once we uh once we call the spice class right so we can use a super init function to inherit the attributes that are acquired by Mesa from the Asian class which is your unique ID and model pointer then we'll play some make sure they put them on a position so they know where they're at okay and then the max spice we use Twice first to keep track of how much spice is actually at that location is a Trader agent start harvesting it all right and then uh to remember what's the maximum amount of spice that could be at that agent right so that particular cell doesn't just keep growing uh and growing uh without stopping now if you want you can also add comments right just to make sure other people that look at your code are aware of uh the two differences of those attributes right so the first one tells us how much spice at a given time step right and the most spice that could be at a given location all right so that once we've done that we want our you know uh run the cell so it gets stored memory and now we want to test to make sure that our code is doing what we think it should be doing all right so an easy way to do that is to add a print statement it needs to be above the agent ID otherwise you'll get an error uh because uh it will you'll reference an agent ID that hasn't actually instantiated a agent net right and so the way we're going to test this one is we're going to reference our scheduler uh and that has a dictionary called agents by type which will have all the sugar agents uh and one key all the spice agents and another key and all the trader agents and another key right um uh and then you could call their agent ID right which is another key that will refer it to its agent object okay it should actually be sugar in that space okay all right so now we're referencing uh our dictionary that's keeping track of all the agents by type I only use two things it's type right it's our first key value it's a dictionary of dictionaries and then the agent ID is the second key and then the value for that is the agent object and it works the same for spice that'll work for the same for Traeger and again whereas Asia by type come from you can look in the time.py file under the random activation class right and see that dictionary all right so run that to keep it in memory right then we run it and we get a new okay so we look at our Trace boxes name error name Max spice is not defined uh looks like we added an extra underscore uh when we created Max spice that's easy enough delete that extra underscore run then run again all right as you can see we get a sear uh the printout of sugar and spice alternating objects with their hexadecimal memory location right now again if we had uh kept that other for Loop it would have been all sugar and then all spice in my case I decided not to do two for Loops because the Mesa would keep track of it all right so that concludes session six uh where we have finished ancientizing our landscape and the next lesson we're going to instantiate our Trader class and start building out our Traders thank you

### Code

From `Session_6_Agentize_The_Landscape_part_2.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Resource Classes

<!-- cell 4: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar
```

<!-- cell 5: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice
```

<!-- cell 6: markdown -->

> # Trader Agent

<!-- cell 7: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self):

    print("I am Trader")
```

<!-- cell 8: markdown -->

> # Model Class

<!-- cell 9: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, seed =3):
    super().__init__()
    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    self._seed = seed
    print(self._seed)



    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        #print(self.schedule.agents_by_type[Sugar][agent_id])
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        #print(self.schedule.agents_by_type[Spice][agent_id])
        agent_id += 1
```

<!-- cell 10: markdown -->

> # Run Sugarscape

<!-- cell 11: code -->

```python
model = SugarscapeG1mt()
```

<!-- cell 12: code -->

```python
model2 = SugarscapeG1mt()
```

<!-- cell 13: code -->

```python
try1 = model.random.getstate()
try2 = model2.random.getstate()

try1==try2
```

<!-- cell 14: code -->

```python
model.__dict__
```

<!-- cell 15: code -->

```python
try1 == try2
```

<!-- cell 16: code -->

```python
import random

random.seed(3)

try1 = random.getstate()
```

<!-- cell 17: code -->

```python
random.seed(3)

try2 = random.getstate()
```

<!-- cell 18: code -->

```python
try1 == try2
```

<!-- cell 19: code -->

```python
help(model.random)
```

---

## Session 7 — Initialize Traders

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=kOrocERLtTM |
| Length | 25:33 |
| Video title | Session 7: Initialize Traders |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+7+Initialize+Traders.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17325 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_7_Initialize_Traders.ipynb |

### Transcript

<!-- 3503 words -->

the session 7 of complexity explorers agent-based modeling of python Mesa tutorial in this session we'll continue to form our sugar and spice Traders our sugar and spice agents and initialize our Trader agents so let's get started little forewarning this one is somewhat monotonous a little bit longer than the previous ones so the first thing we want to do is make sure that you've uploaded your sugarmap.txt file all right here's the upload button uh and then you import your dependencies you've done headers you can then collapse that uh that's so right we then have our sugar agent class that we built that have a couple attributes positioned Max sugar uh and the amount of sugar that has all right and then the same with spice then we have our Trader agent uh where we'll initialize this towards the end of the lesson and then we have our model class uh where I initiate our model and this will is our main manager of the agent interactions all right so in this we build our sugar and spice agents based off our grid allocations all right and if you run it should work and you can see all your spice and sugar objects right so now we can get rid of those print statements I kind of uh verify what we believe is happening in our uh in our simulation so far and now uh we're going to create our Trader agents right so our Traders have a lot of variables and so it's going to take a little bit to kind of build all these variables in now we're going to be somewhat for Boost in building this uh just to make sure it's very clear uh to all the people going through this so the first thing I as uh keyword argument or Quark that's the initial population and we're going to set this to the default of 200 which is a population size in our reference book growing artificial societies by axtel and Epstein okay uh then they have several parameters so you have your uh first the minimum endowment of sugar and spice right which are both between 25 and 50.

all right so we're going to Quick create quarks for that and down the underscore Min and endowment underscore Max right and then we have a metabolism for each agent for uh sugar all right uh and spice and again uh these are going to have vary so we have metabolism underscore mint at one right metabolism underscore Max at 50. and again we're defaulting these parameters uh to uh or correction metabolism backs at five uh we're defaulting these parameters to what was in growing artificial societies right now we have the same for Min and Max right so we're doing these as keyword arguments so they uh automatically set to something all right um but they could later on uh be parameters that we alter to see what impacts it has on the functioning of our simulation okay now that we've done that right we want to uh carry those variables over into attributes of the bottle uh so potentially they could be referenced depending on how you set up your model you don't necessarily have to do this Set uh but uh for us we're going to do it so that way the model has attributes that could be referenced later for data collectors of other things right and so really again somewhat uh monotonous but we just do initial population equals our initial population uh our initial endowment uh underscore Min equals endowment underscore Bend right we want to make sure that we're always putting in our uh in our comments I'm gonna do a little bit of cleanup here just to make sure everything follows the same structure all right but we initialize the width and height of sugarscape and now we're going to initiate uh our population attributes all right so just to keep them uh you keep everything the same so you have consistent structure throughout um on for easier readability I will call this initiate population attributes okay so now our initial population our endowment min and then we just want to make sure that it follows the same order right so population endowment Bend endowment Max metabolism Max I would just go through and we add each of these again depending on how your model's set up you might just want to pass in the parameter to initiate it um in this case we're going to make each of our parameters an attribute of the model so now yeah each of these parameters will actually be a range that we'll use later on right so that way we can have a heterogeneous population one aspect of agent-based modelings uh is the heterogeneity of the population which produces novel emerging hate behavior that a homogeneous population could not typically do on its own all right this becomes with a key value added of agent-based models because it allows for kind of richer uh emergence and bottom-up simulations uh because each agent because of the diversity of your Asian population right so each one of these that Min and Max all right will uh use later on uh so that way as we initialize our 200 agents they have variance uh in what the metabolism is what their vision is right and then this has an impact on the overall output uh of the model right so now just to make sure we got our keyword argument uh keyword arguments uh match our uh model attributes uh and for ease of uh readership right they're all in the exact same order right so there's initial population uh endowment metabolism fission right then our attributes follow that same pattern initial population endowment metabolism Vision well this makes increases the readability okay all right so now we've done our uh we'll just add one more for Loop okay so we got our for Loop for our sugar our for Loop for our spice and now we're going to add our for Loop for our initial population or just to the standard python Convention of four I right I in range right and then the uh parameter self underscore initial population so that way later on if we made it 50 or we made it 5 billion uh the model would account for that without a lot of forecast foreign so now the next thing we're going to have to do after this uh is then uh get each of those ancient attributes all right uh so that uh we can initialize each Asian object right so we're going to initialize in this case 200 uh Trader agents uh each with uh varying attributes all right so um first we have to give them an x and y coordinate right so I have to put them in our 50 by 50 grid Square so we use uh Python's random function Rand Rage which returns uh in int and remember for Mesa Convention here x-axis is your width right so standard Cartesian coordinate system all right and the other bit though is we didn't actually import Rand a random is part of the mesa.model agent class right so uh typically you get an error saying that random is unknown but because you're inheriting it uh from the mesa.model class that is why we're not importing it uh so we'll do the same so we do for X now we do the same for our height which is our y-axis use rant range that returns a an integer right because if it return to float uh you'll get an error from Mesa because you can't have a float root coordinate okay and now we have to add each of the attributes uh for our agents right and if you want to see where we got this from it's always good to document your kind of sources or provide references for your users and in this case we're basing all of this off-growing artificial societies specifically uh page 108.

so now uh the first two will do it again just like up above we've initialized the population you've got your uh your width and your height all right so now we'll follow that same pattern of attack endowment metabolism and vision all right again this just kind of uh follows the principle of least surprise if it's in one order in one place you want to make uh sure it's in that same order uh in all the other places all right so first we'll need the additional initial endowment of sugar for each Trader agent okay and per growing artificial societies they use a uniform distribution so again we'll use Python's random uh library in this case we use uh uniform and we'll do uh just your lower and upper ranges which is your dominant Min which is 25 or defaulted to 25 and your endowment Max which was 50.

but we'll also then do int right I uh just kind of to be consistent with what's implied uh in growing artificial societies right then we do the same thing uh for spice right in self.random dot uniform and then uh we use the attributes endowment underscore Min and endowment underscore box now again you could just pass these in as parameters and reference the parameters during the initialization during the initial initiation phase of the model but in this case we turn them into model attributes uh that um uh so they could be referenced uh later on okay um so again we start with endowment next up is metabolism and it's just going to follow the same process make sure we put in our comments right so first we're given the endowment then we give them the metabolism each agent has a metabolism for sugar and a metabolism for spice as well their attributes and again this determines uh how much sugar and spice that each agent will burn uh every step of the bottle right or tick of the bottle so every time the model goes to one of the sequences each agent will burn a certain amount of sugar and spice and if they lose all their sugar and spice then they are considered to have died and are removed from the bottom look I want to just make sure to check it and again well kind of from the implication of growing artificial societies we're going to turn these into ins uh we have sugar we just do the same thing for spice and again uh potentially on how you want to code it out could say this violates a dry principle and turn all these into helper functions uh in this case we're just going to again as stated earlier be a little bit more verbose uh so it's uh more obvious specifically what's happening in the simulation and then next up is Vision right so they we have a position for our agent we have a sugar amount of sugar and spice endowment they have uh amount of sugar and spice they burn between one and five um and now we're going to do the same for vision right all the same process so now as it iterates through this for Loop all right for each one ah each of these variables sugar spice Vision metabolism sugar will all uh all get one integer and then we will assign that to our Trader so that we got a process for getting each specific attribute of the agent we can instantiate each traitor object so it's similar to Sugar and Spice we make a variable Trader I call our Trader class that's the capital T and then we'll have to pass in you know the kind of standard attributes so first right is always uh your unique ID right every agent must have a unique ID just for the standard bookkeeping practices what then you've got your model uh and then we'll go through um the same process right position sugar endowment spice of diamond sugar metabolism spice uh and fission and just instantiate each Asian attribute with that you know correct this it should be unique ID comma self right and then that will reference the model class that we're in right now all right model with uh if we put model there that would have given us an error all right so next up is position so we make a tuple of our X and Y that was randomly assigned right uh and then we're gonna again be a little bit more for both we actually have to put in whether or not they're using them more or fun noiman neighborhood or rather we're going to put it in so you understand uh that's an attribute to Mesa right so you have more equals faults that means they're using just up down up then we're going to use keyword arguments this is just to make sure that uh as you're going through this tutorial get the exact right parameters uh where uh when you pass it up to the trader and this will reduce the chance for error again would be a little bit more vote for both here uh but we're doing that intentionally to hopefully prevent you from getting uh unexpected errors right so it goes more sugar spice and Metabolism underscore sugar unless it's going to equal your metabolism underscore sugar right so it's just passing um one variable into a parameter of the same name and again principle of least surprise uh F follows one pattern at one place you want to make sure it follows that same pattern uh as you uh in another place right so uh it will go sugar spice metabolism sugar metabolism spice uh and then fission right and again this is just to make sure we don't accidentally uh or reduce a chance for uh incorporating it right so now that we've created our trainer object we need to do the same things that we did with our sugar and spice objects all right uh sorry it should be agent underscore ID not unique ID I should probably go back through and correct this make sure you don't have any spelling mistakes like I do or other issues right uh but now that we've created our Trader object just like our uh sugar and spice object we want to make sure that we add them to the schedule uh and place them on the grid alright so again always add comments so Place agent okay self.grid Place underscore agent right then you pass in your object and you pass in uh their X and Y position you could also write this as trader.poss all right and then it will pass in that specific attribute of the agent all right then we'll add it to the schedule okay and then finally we want to make sure we iterate our agent underscore ID otherwise we'll just be overwriting uh the same agent so let's say it's 4032 I'll have uh is a Asian 4032 recreated 200 times right then always code a little test a little so we're going to put a print statement in here to make sure that they each have a unique ID they're each on a unique position they have some amount of sugar all right and they have some type of metabolism all right since we use effectively the same code for the metabolism as we did for the vision and we'll just leave it at what all right so do metabolism spice okay so now we got this for Loop we instantiate our agent then we add them into our model make sure that we iterate through now we need to make sure that well if we run this just to show you we'll get an error oops and it looks like our name error Trader is not defined so we never ran this cell so first we got to run this cell foreign and now right some of our parameters in there if we run this right we look at our Trace back right we see that we get an unexpected keyword argument more um uh and that's because when we initiate the trader class uh it doesn't have any of the parameters that we put so again this just follows the same pattern beak underscore ID get an agent ID model right which is the self and the previous one their position uh they're more and again we'll use keyword arguments here just so it uh defaults out all right so again more is a type of neighborhood and uh Von Neumann it's its fault more is up down left right diagonals but anointment is top bottom left right which is what was done at growing artificial societies and then we're going to put uh we'll just put these at a zero so that way if something doesn't get passed through like we should think it should create a pretty obvious issue all right okay we fall the same pattern more sugar spice metabolism sugar metabolism spice and then vision so again it's very verbose for this but uh hopefully this should prevent uh you from having uh any errors or issues uh when you actually run your code so now just like uh the sugar and spice agents first we're going to do a super in it so that way you could just inherit uh the unique ID and model from our agent class and then we just go through the same laundry list of attributes so first you have your position then we have how they're looking at their neighbor right so this is an agent attribute to say uh how they're looking at their neighbors which grids they look at right then the amount of sugar that they have the amount of spice that they have kicked off with an initial endowment then how quickly or how much uh sugar they burn in each step than how much uh spice they burn at each step right so if they're burning a lot of spice so chances for survival are less because they might run out of spice and not be able to continue on let's say unless they randomly add up on a very rich Spice Hill right and then their Vision right so if they have a low vision of one they can't see very far they have a high vision of five uh that they could see further again that might increase their chances of survival because they can uh optimize uh which path they're taking more effectively and again it just follows all the same patterned and we've instantiated our Trader agents right so now let me run it okay well look at that we can see that each one's got a unique ID they got a position so now we can actually see if our keyword arguments are working the way we thought so if I comment out one of these attributes instead of getting an error doing metabolism spice and so we print that out you can see it all just defaults to zero okay uncomment data another interesting thing to be aware of right our unique subtlety if you look at these we're seeing at most four when our Max is five uh and the reason for that is because when we do int it doesn't round it just truncates right so we get uh you know some float number between uh one and five right but it'll be like 4.9 all right and then that'll uh just be truncated before right so in order to be consistent with uh growing artificial societies who want to make sure that we account for the fact that agents can in fact you know have uh a vision of five an a dominant of 25 or even a metabolism of five uh so it's a pretty easy fix well we're just uh add a plus one to each of these and so now we brought that here run our instantiate our model again as you can see now I get some fives and some fours in there to twos and some three so that way um when it truncates if we have 5.1 it'll truncate to um five so uh it's just important point to understand you know particularly python Primitives what they actually do instead of maybe assuming that they're rounding okay uh in this case right so in this case in truncate it doesn't round all right so uh now I want to save this right we have now instantiated our Trader agents that was a long one uh but thanks for joining us and that uh concludes session seven where initialize our Trader agents see you for the next lesson

### Code

From `Session_7_Initialize_Traders.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Resource Classes

<!-- cell 4: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar
```

<!-- cell 5: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice
```

<!-- cell 6: markdown -->

> # Trader Agent

<!-- cell 7: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision
```

<!-- cell 8: markdown -->

> # Model Class

<!-- cell 9: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      print(trader.unique_id, trader.pos, trader.sugar, trader.metabolism_spice)
      agent_id += 1
```

<!-- cell 10: markdown -->

> # Run Sugarscape

<!-- cell 11: code -->

```python
model = SugarscapeG1mt()
```

---

## Session 8 — Sugar & Spice Step Functions

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=AUtAueSYQFc |
| Length | 17:40 |
| Video title | Session 8: Sugar & Spice Step Functions |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+8+Sugar+and+Spice+Step+Functions.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17327 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_8_Sugar_and_Spice_Step_Functions.ipynb |

### Transcript

<!-- 2639 words -->

welcome to Session 8 of complexity explorers basic tutorial agent-based modeling and python in this session we're going to add our sugar and spice step functions and walk through two different ways in which to iterate through your steps in order to run them up let's get started first open up your instance of Google collab or your preferred development environment okay so first we'll show you another trick here on how to reference uh files in this case in Google codelab right so instead of having to upload it like we've done in the previous lessons I'm actually just going to upload it to my local to my Google Drive that's stored in my account uh and then I'm just going to reference it locally in my Google Drive which should make my life a little bit easier right so from google.com you get to import drive right and then you're going to mount your truck so this is these are just Google collab functions all right uh it says drive.mount open quotation marks forward slash content forward slash drive and uh quotation marks all right so now this way my model can actually reference the files in my Google Drive okay we have our resource classes our sugar and spice our Trader class that we've already built to make sure we're running these so our model will run all right so make sure you hit play uh if you haven't already all right then here we're actually uh read in my sugar dot map I'm gonna do content forward slash drive and forward slash capital M for my then capital D and drive forward slash sugar map Dot txt okay and you want to make sure your stuff's uh all your classes are running so you don't get an error and then because mounting uh referencing things from a code environment are always tricky let's make sure that it's all actually running okay now that we've updated that we can get rid of this press print statement from session seven we're not going to need that where we uh we're verif uh verifying our Traders right and now we want to add our step functions into our sugar class so a step function in Mesa is just Mesa Convention uh for you know what every agent should do for that particular step all right some other terms for these might be called sticks are ticks rather uh in this case Mesa made the choice uh to use step functions and so other classes of Mesa like time and data collector uh we'll look for the step function all right now as always this good practice uh to comment your code right so our step function is really just the sugar growth function right this is going to add one unit of sugar for each step right until we reach our Max sugar okay which we uh parameter parameterized or we established in the initiation of the model right so to do this it's going to update ourself.amount attribute that was just use Python's primitive Min function we'll use Open brackets for a list and then whichever is smaller between self.max underscore sugar right and the current amount of sugar should be comma right South dot amount plus one so I really have a list of two things my Mac sugar and myself that amount plus one whichever one's smaller uh that's what I'm going to update my amount to right so this is just a one-line way to make sure that my uh the amount of sugar I have is updating uh once per uh time step in my simulation all right um and then just to make sure right code a little test a little next thing I do is we'll write a print statement unique ID so I can tell they're different agents right self that amount and then self dot Mac sugar and since nothing's consuming um the sugar at the grid space uh those two numbers should be the same all right so expect to see agent ID so an integer and then the same number for the amount in Mac sugar and now that we've added it to our sugar class what we need to do uh is add a step function uh into our model class that we'll call all the agent step functions that's important to make sure that your function is aligned to the outermost function so one tab over right should be aligned to the def dot in it or the initialization function right and then we're just going to iterate through uh our uh sugar agents all right in order to call their step function now in this case this is kind of discussed in session two we're using a very kind of unique activation function right so Mesa has staged and it has random activation uh but it doesn't have a combination of the two so really we're doing a stage activation of sugar spice but then for our Traders right we want to randomly activate them so each Trader doesn't have like a first or second mover Advantage right as for iterating through our Traders and as they're trading right so it's a pretty unique activation function and a good thing right about coding a python and having Mesa being kind of python all the way down so to speak right uh is that I we can do this fair Fairly simply right so make our step function right all that's going to do is call our sugar step function right so um let me iterate right so we just got a for Loop that goes through all our sugar agents then we call our sugar step run that to make sure it's stored memory then we run our model and nothing happens why is that well because the step function isn't called all right um instead of call the step function right uh it's just another iterator uh for a range for some range right so in this case we'll just do five steps right and then uh since we instantiate the model class now just like we call the sugar step function now we call the model step function and run that okay so calls a sugar step function at the bottom so to speak then the model step function then we run it and sure enough uh we're getting what we're going to expect which is a unique ID plus a amount of the max amount of sugar and the amount which is the same thing right and I'll run through uh five iterations all right uh for that okay so now um we do have to account for something so again we're running this kind of unique activation function which is an um uh this organic to Mesa all right um and so we want to make sure uh that we're actually advancing uh our scheduler inside our core Mesa right so if you go to uh time dot Pi in the Mesa file you'll see that there's step and there's time so there's two ways that Mesa can account for time a step is kind of the primary and then time allows you to run a continuous clock these are then both attributes of the base scheduler all right so that is actually not advancing because we're not using that kind of uh traditional uh scheduled dot step function that Mesa expects to see right so a typical Mesa model would say self.schedule.step right and then the time.pi file would advance that uh would Advance Step at time for you all right uh but since we're not calling that function because we're doing this unique stage activation plus a random activation right uh that does anything so to see that we just do a print.self.schedule.steps right then self.schedule that time and you'll see that nothing's happening and this is important because data collector looks at steps as well right and so later on when we're doing data collection uh if we don't Advance the steps all events will occur at Step Zero which will be problematic I should run it all right see that'd be good uh zero steps for the five uh the five iterations we go through all right so it's fairly easy to fix we just we're going to reference uh mesa's uh steps dot attribute and then add fund We'll add a note here because it's Unique just saying uh it's important for data collector to track the number of steps and then we can run it again good comments here right uh you notice we didn't touch time right you see steps Advanced and time did not right because um we're not going to need time for data collection uh we're just going to let that remain at zero that's for more advanced models when you might be running a continuous clock high as well right for the purposes of this model though we could just uh worry about steps right so now that we've Advanced our sugar uh now we're going to do the same thing for spikes right so four Spice itself that schedule that agent uh by type right and then we'll do a spice with a capital S because uh we're referencing the uh agent class right and then values because it's just uh stored in a dictionary or a dictionary with spice is the key and a list of Spice objects uh um as the value and then we call Spice dot step right just like sugar all right and then so now we go up to our spice agent all right and we're going to do the exact same thing we did here right which is we create a step function I'm sure it's a tab over one right that's gonna be called Step again right so that way uh the scheduler knows what the is looking for steps or make sure it's the same thing right and then we'll put our comments Spike growth spice growth function adds one unit of spice each step until maximum and since the spice or sugar agents don't consume each other right it doesn't matter that they're all kind of run in sequence right the order for that doesn't matter right well with Traders they might get first mover advantage or something depending on what they move right and then we'll just use the same kind of one line uh function to update uh or the amount of spice at that particular so I got Max spice then we have our Min of a list of self.max Spice and self that about uh plus one all right so again we want to use our print statement just to validate that what we think is happening is in fact actually happening in our model so just like sugar we'll do self.unique ID self Max spice and then self dot amount and what we expect to see is that those the same because nothing is consuming the spice at this point um so then we run it make sure we update that class and we get an error all right uh so if we follow our Trace back we can see that we did for spice or I wrote for spice and self that activation by types versus type all right which does not exist I can see that in a traceback I run it again right and we get a bunch of unique IDs plus the same amount of uh Max spice and uh amount of spice at that location and again this will theoretically run uh for or will actually run for five steps right so uh now we have our step functions for sugar and spice and our step function for our model right so as always make sure we have good comments so again just to emphasize this point this is a unique uh step function that combines uh stage activation uh plus uh stage activation the agent so sugar spice and the traitors and then for each of the Traders right uh it's gonna randomize them every time we call it and that will be uh in a couple of the next lessons all right okay so we're gonna but we gotta make sure that people understand that or at least have some inkling of it so a unique step function that does staged activation of sugar and spice and then randomly activates Traders comment this here right so uh step our sugar agents then we'll step our spice agents again because the sugar and spice don't interact with each other uh we could just do those sequentially and it will have no impact at all so now we've got the first two uh stages of our schedule which of our stage activation which is sugar and then spice but and then we're making sure that we iterate through all right so now uh there's one other thing is we kind of did this 4i and range here but typically uh we could store that inside uh our model with a function all right so we're going to do def uh run model right and then it'll be uh start that out with self as always okay I kind of did this a little bit backwards here instead of uh model run underscore run uh typical convention would be uh run model right so run underscore model okay and it's an inside a class you got using standard python convention yourself right and then we'll use a keyword argument again called Step underscore count all right and we'll default that to a thousand steps uh which is kind of what we see at growing artificial societies all right and then we'll just take that same four uh loop we did previously all right and we'll put it inside uh this model or correction this function all right if you show 4i and range stepcat this time and then we just call uh self that step because we're inside the function right and that will call uh the function uh our step function for the model right so just got layers of Step functions each of our agents all right gets a step function so Sugar and Spice all right we could get rid of this print statement now sort of valid verified that's working the way we think all right and then we have our show our sugar has a step function our spice has a step function all right and then we can run our model so get rid of this for Loop all right then right we actually have to call right so instantiate a version of our model or an instance of our model rather and then we're just going to call that function run underscore model since running it a thousand times would be kind of silly right now or actually use a keyword argument uh and we're going to set it at five again okay so I know we want to make sure it's doing what we think so we'll do a print statement here and we'll run it right you can see it iterates through zero through four uh so we now have the ability to run our model completely encapsulated inside our model function right so now I have a run model function and then once we instantiated instance of that model we can run it right that concludes session eight all right uh of our sugar and spice step functions and then for session nine uh we'll start with our Traders and start having them take some action uh beginning with thank you for joining and we'll see you next time

### Code

From `Session_8_Sugar_and_Spice_Step_Functions.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Resource Classes

<!-- cell 4: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 5: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 6: markdown -->

> # Trader Agent

<!-- cell 7: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision
```

<!-- cell 8: markdown -->

> # Model Class

<!-- cell 9: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      print(i)
      self.step()
```

<!-- cell 10: markdown -->

> # Run Sugarscape

<!-- cell 11: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=5)
```

---

## Session 9 — Traders Move Part I (Initiate Move)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=hrUPIW4BNNo |
| Length | 7:40 |
| Video title | Session 9: Traders Move Part I |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+9+Trader+Move+Part+1.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17328 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_9_Traders_Move_part_1.ipynb |

### Transcript

<!-- 1285 words -->

welcome to Session 9 of complexity Explorer's Mesa tutorial agent-based modeling in Python and this session will start the first of four sessions that focus on moving our agents across the sugarscape landscape so they can identify the best location to move to in order to survive and throw so let's get started please open up your Google collab instance okay so to start we want to make sure that your sugar map that txt file is available to your Google Drive either by mounting your drive or by manually uploading it through the file system all right then we can import our dependencies since we'll really be using this you also have the option if you added a header to collapse that all right we then have our sugar and spice resource classes uh where they grow yeah one unit per step right and we could collapse that right both of those cells at once here's our Trader agent where we'll spend the majority of the uh of the rest of this tutorial building out our agent behaviors and then our instantiation of the model class where there's a lot of code to instantiate our environment right and then from our last lessons to step our sugar and spice right uh just to make sure that it's still working for the last time what we'll do is we'll run our class right run on instantiation of that bottle and it still seems like it's all working all right so uh for this one we can just move down to one step count and get rid of this print statement right and now we'll focus on how we uh step or agents so again we're using a pretty uh unique step tool that we can use uh mesa's step functions as well as customize it one of the advantages of Mesa right so the first thing we need to uh do I is build out our move step function right uh and the trick here is that how agents move matters right so this reference uh who goes first by Dr Ken Comer out of George Mason really is a great study on why uh the Asian order actually matters and can produce different results based off what activation regime you decide in this case we'll use random activation to make sure there isn't a first move or a second mover advantage or any other type of movement now the trick with this is that our agents can die right and per python you can't um if you're iterating through a dictionary and you start removing uh keys that produces a runtime error right so we need to set the conditions that we can remove agents at each step uh if they in fact uh you know run out of energy and effectively die need to be removed so to do that uh what we have to do is first get our list of Trader age so using pythons or correction basis activation by type just like we did for Sugar and Spice all right we will get all a list of our Trader objects right so if we do values this will give us a list of Trader agent objects right so now the next thing we want to do right is wrap those in a list so that way we can iterate through it more efficiently and remove agents okay right and so then with that list right um and actually if you look at this we got Traders we got capital t trader right it's always good to try and make your uh you're naming your variables as clear as possible so as Traders is probably a little bit too ubiquitous uh throughout this uh throughout the code we have so far uh we're gonna change this to Trader Shuffle just to make it a little bit clearer and more readable for uh anybody else that may take a look at this code all right to that we have Trader Shuffle right comments are always good so I want to explain to any user uh you know what we're thinking here and as well as to remind ourselves uh why we had to um uh you know make these choices so in this case we want to account for ancient death and removal right which uh if we did purely in the python dictionary structure would result in a runtime error so we're going to make some notes to that effect and now that we have our list of Trader agents right we want to randomize it to account uh to kind of mitigate any type of mover Advantage based off their position all right uh and so we could use Python's uh primitive random library and Shuffle right uh and then just put in our list Trader Shuffle Now if we look at the documentation for that we know that it actually doesn't return anything it just takes that object where it's that list object where it's stored and shuffles it all up so just by running this command we know that list of Trader agent objects will be read that will build here in just a section a second uh so right what we're doing is we create a list of our uh Trader agent objects right and then uh we Shuffle that list so that every time we run a step function uh each agent is in a different movement order right so this will be a function this agent dot move is now a function that we have to build uh in our trader.class so I'll run that all right and then we'll go up to our Trader class right and we'll add this function into our Trader class so this is our initialization of our Trader class right and so now we build uh the move function right so it'll just be uh death uh move right and then open parentheses self close parenthesis okay and now for this one we just want to make sure that our model class calling our Trader class uh is working all right so we'll just add a print statement uh maybe a little bit more verbosa necessary but it says I am an agent all right I meant to make sure it's iterating through each of the agents right uh and I'm about to move right and we use Python's dot format syntax right so we put curly braces for where we want to put the variable and then we'll have it call itself.uniqueid so that way we know it's changing agents as it iterates through that all right uh and so this will allow us to kind of test to make sure that our calling uh of the um a calling of the boo function is in fact giving us a randomized list uh of our agents right uh so run that okay store it in memory all right then we go down to where we call our model class right uh and instantiate it and run it once all right and sure enough we get a um uh sure enough we get you know a randomized list of our agents and if you want you can clear that out put if you also want you can uh save a copy of this so we're stored there right and so that wraps up uh session nine right uh on our first part of moving agents right the next three lessons will have them identify and where to go based off their best choice in order to survive and thrive within the sugar and spice landscape see you next time

### Code

From `Session_9_Traders_Move_part_1.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Resource Classes

<!-- cell 4: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 5: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 6: markdown -->

> # Trader Agent

<!-- cell 7: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision

  def move(self):

    print("I am agent {} and am about to move".format(self.unique_id))
```

<!-- cell 8: markdown -->

> # Model Class

<!-- cell 9: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    for agent in trader_shuffle:
      agent.move()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 10: markdown -->

> # Run Sugarscape

<!-- cell 11: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 10 — Traders Move Part II (Identify Neighbors)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=vVm6U8iO-Ck |
| Length | 13:13 |
| Video title | Session 10: Traders Move Part II |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+10+Traders+Move+Part+2.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17329 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_10_Traders_Move_part_2.ipynb |

### Transcript

<!-- 1978 words -->

welcome to session 10 of complexity Explorer's Mesa tutorial agent-based modeling and python in this session we'll continue with part two of four of our agent's move function where we identify all possible neighbors that our Trader agents can move to let's get started please open up your collab or other development environment and we'll begin so first you want to make sure that your dependencies are imported and that you've linked your sugarmap.txt file either as a file or through linking it with your Google Drive Right There we have our resource classes sugar and spice and we won't be engaging with these in this session so you can collapse this if you would like next is our Trader agent uh class right that we started last time where we added the move function we'll be using the rest of our the time into our tutorial and then our model class we initiate the model and our step functions that do a stage random activation that call uh our that calls at this point our agent move function okay so make sure to run this right and then just to make sure it's running from last time we instantiate an instance of our model and then run it for one step right so that's working now we can begin to update our agent move function foreign as always it's important to have good comments so you or other users can understand what's happening in the model now in this case there's more formal ways to pass through arguments and discuss returns uh which will be shown a little bit later but go beyond the scope of this tutorial all right so first what's our move function going to do it's a function for identifying a Trader agent uh to identify the optimal move location for each step right and this is going to occur in four parts so the first part which we're going to discuss here is identify all the neighboring cells that the agent can move to right so what are the possible moves that the agent can make all right the next one is which will be the next session is to determine which of those cells will provide the maximum welfare to the agent and then finally all right you want to identify the nearest cell and this is per growing artificial societies and then uh for that one it'll just be one function called for Mesa to move the trader agent from the cell that they're in uh to that particular cell for part one in order to identify all possible moves we're going to use pythons list comprehension and maces get neighborhood function in order to create a list of all possible cells that the agent can move to all right so we create a local variable for our move function called Neighbors right and then neighbors is going to equal a list that iterates through all uh all the neighbors based off the vision that agent has right so be neighbors equals and Open brackets I for I in self all right so now we've got a uh refer to our model class that has the grid function in it because that's where the function of git neighbors is stored right so the agent variable the agent class has a local variable called Model right in model we established our grid right and in the grid class in Mesa is a function called git neighborhood and just to be clear about that we can show that class we could show the actual code in that class from uh from mesa's GitHub repository or from your locally stored version right so if we go directly to that line you can see here that this is the get neighborhood function in mesa's space right there's a couple parameters there's a position you're more right whether you're using your board of employment neighborhood right whether or not to include the center and the radius for us the radius is the vision of our agents if you remember from the instantiation some agents could see up to five cells uh in any direction and some agents could see only one cell which matters in their competitive Fitness on the landscape all right so we have to pass in each of the these parameters so first of the position right that's a class attribute called self.com have to do ourselves that more which is set the faults because we're using the Von Neumann neighbor up down uh left right not the diagonals all right and then whether or not we include the seven now that by default in maces set the faults so we got to set it to true in the sense that the trader agents can stay on the cell if that gives them the highest Fitness right then finally we pass in ourself that Vision uh parameter which translates to how far the radius that you use for your git neighborhood and is how far any agent could see right based off our initiation of each Trader agent in our model class right the final criteria based off growing artificial societies is a Trader agent cannot move to a cell where there's another Trader agent right so if it is not occupied right then this is a permissible cell for or grid space for this Trader agent to move to right so for this part we will add a helper function called is occupied by other and then we will uh use that to determine whether or not that cell should be added to the added to our list right so we just create a function inside the class called is occupied by other right with underscores then you have the kind of python syntax required self and this will take one parameter which is your position all right then we'll put some comments in here uh and typically you would uh or so this could be a helper function in a more formal uh commenting you would put that pause uh is a tuple all right uh that is passed in is the argument right and it returns and this function will turn a Boolean right true or false uh on whether it is occupied by a Trader instance right so first uh the agents are allowed to stay in their same position right so if the position we're passing it is the same as the agent's position self.poss all right then we could just return false right so the significance so going back to the uh the activation method here is that Sugar and Spice each Crow and then all the agents determine whether all the trader agents determine whether or not they should move so it's possible that an agent with a low metabolism uh for Sugar and Spice right and depending on where they're at in the space may want to stay in one spot and just Harvest that one growth of sugar and spice for each step so if that's the case we return false because it is not occupied by another agent now we have to put a conditional if it is occupied by another agent to do that it's fairly straightforward first make sure you're indents are aligned uh properly all right but we have to get our uh the contents of uh the cell that we're looking at all right Mesa has a function for that all right so again we refer back to the local model instance inside this agent we use our grid uh grid attribute that we set up in our initial model and then we use the Mesa function I get cell list contents right and we pass in the parameter pause all right so again just to emphasize that Trader agent has an attribute called model which refers to the model class right in that model class is an attribute called grid where we instantiate a grid space for mesaspace.pi and then we use a function from that class called git cell list which takes a parameter position once we get that all right then we want to iterate through all the possible contents of that cell right that function returns a list to see if it's occupied by another tradery so to be thorough just like we were with the kit neighborhood we could go inside mace's code and in this case I'm using GitHub but it's also locally on your installed version as well as through the documentation and we can see how the git cell list contest content actually looks and that's just part of mace's space dot Pi file which contains the grid class we instantiated when we set up our model class okay and from there you can see that it returns a list all right and now we iterate through this list in order to determine if it is an instance of Trader all right so 4A or well it should be some type of agent whether sugar spice or Trader agent now we could just put a conditional that uh determines what it is so we could use pythons is instance right and then this takes two parameters our a for our agent object that may be in the cell list right and then Trader all right so if that object is an instance of our Trader class or make sure Traders capitalize T right uh then we want to return true right that would tell us that it is occupied uh and so it would not be added to the list comprehension uh that we're using uh in the uh in our agent move function okay now if it isn't so it's either not the cell that we're in right uh and the cell is not occupied by a Trader agent then we're going to return false right so that means that it can be added to our uh list comprehension okay and so now we have our helper function is occupied by other and again this criteria was established in the growing artificial societies I uh movement rules uh that Rob Axel and Josh Epstein set up right so now we have a pretty good uh kind of uh where we have completed our function uh so we now want to verify that it's doing what we think it's doing okay so easy way to do that is just to add a print function right and we want to check to make sure uh so we can check it in this case by going what's our position and then what is the list of positions we're getting out of our neighbors right uh if our self deposition is also in our neighbors and we know we have our uh our Boolean function set up correctly uh and the function is doing what we expect it to do which is provide a list of possible move locations our Trader agent is allowed to go to all right so after we do that we'll just run it and sure enough we're getting at least partially what we think right which is you get a tuple of our position then you get a list of couples of the grid locations of everything else and you can see here that the uh self dot position is also uh in the list of tuples which means that our function is working the way we expect it to uh and that we are sufficiently identifying the possible or allowable move locations our Trader agent can go to right so thanks for joining session 10.

all right and the next one we'll look through all those uh positions and we'll determine which position gives each agent the maximum welfare thanks again and we'll see you next time

### Code

From `Session_10_Traders_Move_part_2.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Resource Classes

<!-- cell 4: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 5: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 6: markdown -->

> # Trader Agent

<!-- cell 7: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False


  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    print(self.pos, neighbors)
```

<!-- cell 8: markdown -->

> # Model Class

<!-- cell 9: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    for agent in trader_shuffle:
      agent.move()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 10: markdown -->

> # Run Sugarscape

<!-- cell 11: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 11 — Traders Move Part III (Maximize Welfare)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=cO_4pdgTerU |
| Length | 19:13 |
| Video title | Session 11: Traders Move Part III |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+11+Traders+Move+Part+3.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17330 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_11_Traders_Move_part_3.ipynb |

### Transcript

<!-- 2800 words -->

to session 11 of complexity explorers makes the tutorial agent-based modeling and Piper in this session agents are going to determine from the potential neighbor cells they could move to which one will provide them the greatest welfare to do this is going to get a little involved since we're going to create five helper functions as we look through each of our neighbors to determine which is the best spot to move to let's get started first open up your Google collab or other development environment or make sure your dependencies are imported and critically they have that your instance is connected to your sugarmap.txt file all right next we got our resource classes right of sugar and spice and these are fairly simple where they grow one unit of sugar or spice for each step then we have our Trader agent we'll be working uh for this lesson all right we're working on part two of our move function determine which move maximizes our welfare and we have our model class which instantiates our models and then calls each of the agents uh step functions which in this case is just move for Traders and we instantiate an instance of our model uh and then based off last time where we printed out our position in Neighbors it all seems to still be working so then we go on to part two we're again going to use list comprehension in order to assess the value uh or the which neighbor maximizes uh an agent's welfare right so we're going to use uh list comprehension again we're gonna if you remember from last time neighbors is a list of tuples that gives the location for each of the neighbor cells that the agent can move to so we're going to iterate through each of those positions and then we're going to add a helper function that's going to calculate the welfare for each of those grid cells where we have to get the amount of sugar and spice in there and then for each agent's unique attributes determine uh which one is best for them so to do this we have to start with a helper function this is good we're going to call this calculate welfare that'll be part of our Trader class so it'll be self.calculate welfare and then we're going to pass in a couple variables so uh and this is we're going to change this a little bit over this lesson but first for now we'll just start with how much sugar and how much spice the agent has right and then uh we're going to iterate for the position right in our neighbors right so neighbors is a list of tuples with each position all right so we just iterate through those tuples and then for each of those we calculate the welfare so now uh we're going to put our helper function I uh above our function right for me this just helps I mean keep my code organized so I know where to look for things uh later on I'll add a couple more comments to make sure I can easily split up where my main functions for my Trader are where my helper functions are and we're going to create our function calculate welfare self right uh sugar and spice remember self is part of python syntax uh just to identify that is part of this class okay and then we're going to add some comments uh in this case I'm going to make sure I know where this function kind of fits for my Trader agent right uh part two self.boob if you're doing more formal programming you do things like uh State specifically uh the arguments you know what type of data structure it is in float Etc data type it is right and then what it returns now for the purpose of this uh this tutorial we're just going to make sure that our code is more readable now to determine our welfare we're using this thing called the Cobb Douglas function gives you the output for each varying input of sugar and spice to determine which one's the best out if you're interested in the cop Douglas function we'll put this link in the notes so you can take a look at all right now that link shows you the function or the generalizable form uh for because we're using it for a specific instance right in this case our sugar and spice landscape and a Trader with metabolism uh we can use the functional form all right so first to do this we need to calculate the total resources that the agent has all right so create one called M total so metabolism total What's the age's total metabolism all right so this will be there uh what the agent has for their sugar uh and their spice if remember from our initiation each agent is unique create a critical factor of agent-based modelings that you have a heterogeneous or a diverse population all right so once we get their unique metabolism for Sugar and Spice which will help them determine uh which cell uh the amount of sugar and spice they have there which one they value more right then we could just uh plug that into our Cobb Douglas and its functional folder right so this is going to be sugar raised to the exponent of the amount uh so the amount of sugar they have raised to the exponent of their metabolism for their sugar divided by the total metabolism multiplied by our spice again raised to the exponent of their metabolism spice divided by their total metabolism and this will provide that with a float right where the higher the value the more valuable that particular cell block is right but so far we're only passing in there uh the amount of sugar and spice they have uh and we'll add in the specifics of the cell in just a second okay but this gives us our Cobb Douglas functional form as we wrote a helper function uh with quite a bit of code all right we now want to test this to make sure there's no syntax errors and that we're getting back with what we expect yeah so add a print statement welfares run a function it turns red so we got a syntax error in here somewhere right I added in an extra bracket into my list comprehension statement that's fairly easy delete that and now we run it and sure enough we get a list all right uh of our um of the return of our cop Douglas function because it's just using what that agent has for their sugar and spice amount at that time all right it's the list is just the same uh based off the number of neighbors that they potentially moved to all right so now we've got a couple helper functions all right well we're going to add to the sugar the amount of sugar for the position that they're iterating over now in this case this is going to seem a little bit verbose because we're making uh two helper functions one get sugar amount and another one called get sugar or get uh sugar and then the same for a spice and that's because later on we're going to use uh these helper functions multiple times all right just remember because we've written out this whole code beforehand and optimized it a little bit all right well I it's going to seem a little bit cleaner than the actual process of coding there's lots of iteration and you make choices that later on you might have to try and uh change because it's not what you want so but we add two helper functions right so get sugar amount and get spice them out this take in one argument uh position all right and then this is going to be a helper function to a helper function right uh since it supports calculate welfare so uh per mile particularly coder coding Dynamics so I can identify my functions I'm going to put this one uh as the these functions above or is occupied by others and calculate welfare so create uh you know first get sugar amount that takes one argument pause which is a tuple that has your grid coordinates your X and Y for a specific position add some comments uh because it's you know getting become a pretty involved code so I'll make sure I could we could go through it or somebody else can go through and understand what we did I'm going to say where it's moved or where it's used at least at this point and again in a future session I will use will be able to reuse these uh these functions for other aspects uh based off the uh agent's interaction with both uh sugar and spices that it has to consume it after it determines uh which one is the best and again if you don't do this typically right off the bat it takes a couple your coding is very much iterative uh so you particularly got a complex model it may take you a couple times to get it the way you want iterating through and optimizing your agents so for this one we're gonna we gotta identify if it's a sugar patch all right so we're going to create another helper function called get sugar all right that we'll use later on huh in addition to this function right and then we gotta so we gotta confirm is it actually a sugar patch so is it if it's a sugar patch right we need to return the amount of sugar uh that is in that patch so in our sugar object so that way we can assess uh its welfare okay and if you remember from our sugar uh agent class that has an attribute called amount hence why we're doing uh sugar patch dotama right so we got to get the sugar Asian object right and then get its attribute sugar patch uh which would be dot amount right if it isn't a sugar patch so it just returns zero right so now that we have that we need to create our helper function uh get sugar so again def dot get sugar self because it's part of python syntax and it's part of the trader class right I and then the position as the one argument passing and then some comments to make sure we know what this function is doing make our code more readable for both us and for others so now just like in our neighbors we have to get all the contents of that cell so we can figure out which one's the sugar patch and which one's the spice patch and there shouldn't be any other agents unless it's the cell that work that the agent is currently so we use Python's embedded function of self.model.grid right so we point to uh our attribute of our model our grid which instantiated our space and then we use the function git cell list contents right which takes one argument our position this will return a list of agent objects right that are in that multi-grid all right and then we iterate through those objects and if the type of the agent is sugar remember we gotta make sure that s is capitalized that's how we determine that it's a the sugar class then we want to return that agent and then in our get sugar amount function uh we that'll become the sugar patch variable and then we just access its dot amount attribute if it's there is no sugar agent we just return none right so in our sugar amount that would return uh you know effectively a false for is it if it's a sugar patch and return zero okay so now we've linked these various functions together right uh four sugar so that way we could treat the amounts of sugar uh so our agents can calculate the welfare so now we need to do the same things for spice right uh so since we kind of got this structure here I'll just start with Git spice uh itself.poss add some comments and then follow effectively uh the same pattern as I did previously but instead of using uh sugar I'll be using spice all right now there's definitely multiple paths to the same outcome uh and uh if you were coding this you might make choices uh that uh whether you want sugar or spice becomes a variable uh so you have less functions for instance right uh in this case uh we are not doing that but the point is there's just multiple uh options uh when you're coding all right and everybody has their own style there's always trade-offs between readability uh lines of code you know uh and efficiency all right so again we use the get the cell contents that returns a list of agent objects uh or that we iterate through that cell if the type is Agent is spiced we return the agent if not none right now we need that to be called by our get spice amount all right which uh takes the you know self uh argument and pause for position so then we create our comments and all this is going to look pretty reflective uh to our get spice or get sugar amount and get sugar and then we have our spice patch now we'll use our embedded we call our git spice right uh and then if the spice patch is an instance or if it is a spice patch right so uh if uh the get spice returns something other than none right then we'll access that spice agents uh amount attribute and return that to our model which would be an INT right that gets fed into our calculate uh welfare parameter right so that amount is used to calculate our Cobb Douglas function which then produces a value right so our agent will have a list of uh values for each of their neighbors to do it so to be clear here's our amount function right inside our sugar class or amount attribute sorry inside our sugar class okay so now right we can print our welfare and see if those numbers vary based off the amount of sugar and spice uh in each of the neighbor positions that we're iterating through we run a test our print function we're actually going to see that the variance of each cell is pretty minimal and we think this is based off how much sugar and spice they should start with and how much sugar and spice is in each cell so you're not getting a lot of variation from uh spot to spot so we want to kind of double check to make sure it's doing what we think it's doing right so we can add a couple other print functions in here um just to make sure that we're collecting uh the Sugar and Spice from those patches all right and that those are being included as part of our calculate welfare slash cop Douglas function all right um so just to do that I got a print statement that says spice and then the spice patch which just to confirm that is a spice object right and then in the get sugar one I'll add a slightly different print statement right so in the sugar patch we print right and then identify that it's sugar and then for this one instead of returning uh the object I'll have it return uh the actual amount so make sure run the stealth to store it memory and then I'll run this cell uh and sure enough I'm getting spice objects and I'm getting uh variation uh for our uh sugar amount so let's see what we think uh there is variance in the uh welfare list that's outputted right it's just not very much because the agents are still consuming from their base amount of sugar and spice uh in the landscape so that concludes session 11.

that was pretty involved I wrote five helper functions but we did calculate the welfare of each of our neighbors so now the agents could decide which one's the closest one that would give them the most welfare and then 12 will conclude our sugar and spice move function where they actually move to the neighbor that will give them the maximum welfare see you next time

### Code

From `Session_11_Traders_Move_part_3.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Resource Classes

<!-- cell 4: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 5: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 6: markdown -->

> # Trader Agent

<!-- cell 7: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      print("Sugar ", sugar_patch.amount)
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      print("Spice ", spice_patch)
      return spice_patch.amount
    return 0


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function part 2 self.move()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    #print(welfares)
```

<!-- cell 8: markdown -->

> # Model Class

<!-- cell 9: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    for agent in trader_shuffle:
      agent.move()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 10: markdown -->

> # Run Sugarscape

<!-- cell 11: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 12 — Traders Move Part IV (Move to Best Closest Option)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=mThJ2hThOs0 |
| Length | 18:34 |
| Video title | Session 12: Traders Move Part IV |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+12+Traders+move+part+4.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17331 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_12_Traders_Move_part_4.ipynb |

### Transcript

<!-- 2913 words -->

session 12 complexity explores Mesa tutorial agent-based modeling and python in this session we'll complete our agent move function where we identify the closest cell that provides maximal welfare and moves our agent thing let's get started first make sure that you have your IDE open or if you're using your Google collab instance that is open and connected alright then want to make sure that your sugarmap.txt is available to your Google co-lab instance if you're doing that which you can load manually or connect your Google drive right then we make sure our sugar and spice resource classes are loaded and then we make sure that our Trader class is also Limited of several helper functions where we get sugar and spice identify if it's occupied but also we can determine what are our viable moves and how much welfare they provide all right we have our model class which initiates our model and then controls our agent uh movement which we could collapse for ease right uh and then we instantiate that class and run it see our print statements from session 11 so go up here into our sugar get spice amount get sugar amount and delete those because you won't be needing those for this lesson foreign can continue with identifying which cell will produce the maximal welfare and then which one of those cells is closest so to do this we need to leverage the fact that we have two lists and lists are structured so that their indexed so that they're sequential in their index position matters but first We'll add our comment to make sure we link it to our previous comment of a cell this is section three find the closest best option with that being said it's important to understand that neighbors is a list of tuples that gives position and Welfare right is in that same sequence but instead of providing neighbors provides the amount of welfare that cell provides our agent right we can use the fact that lists have to be sequential in order to I in order to identify which position gives us the max welfare right so first we need to identify what our Max welfare is right so you do Max welfare it's a local variable equals Max right from our list of welfares all right so that will give us that number using Python's primitive Max function once we identify what our Max welfare is that our next challenge would be to link these two lists together so that way we can find the positions of the cells that have the max welfare so we'll create a third data structure to link the neighbors and the welfares together is this you know kind of linking these together we want to make sure we have good comments so the first part is you'll find the highest welfare uh in welfares and next we'll want to make a list that gives us all the indices uh of those Max welfares so we can extract the positions from our neighbors list all right so to do that we'll uh use Python's list comprehension again uh make a comment so we understand what's Happening Here which is now we want to extract uh the index of all the max welfare cells so that way we can then get the neighbor the Tuple positions that are located in our neighbors list I know it's probably a little bit confusing to listen to but after this we'll do a print statement so that way you can see exactly what we're talking about so call this one local variable candidate in this indices right and then use I for I right in range of neighbors or where I could use neighbors or welfare in this case we use welfares and now uh we have to determine if we want to add it to our candidacy indices now the typical way to do this is uh or what might be the intuitive way to do this right is to do the pythons equal right to say are these the value of welfares and the value of uh the max welfare the same right this however presents a significant problem uh that could cause challenges later when you compare two floats uh to each other right uh so if we say I for I and range of lengths welfares or neighbors right if welfare's at that index is the same as Maxwell fairs right due to how float numbers are stored this could become hugely problematic the key challenge here is when you're comparing two real numbers which are stored in uh encode is Floats or in Python if you want to be very careful of using this function and there's a better way so if you want to learn more about this we'll put this uh discussion in the chat but this is a pretty good uh description of decimal numbers versus footage right to address this instead of using equals we use pythons math dot is close function right and we also put this link in the chat if you want to see the python documentation right so instead of uh if welfare equals Max welfare I want to do if right math dot is close and then we're going to compare the welfare indices right so what that welfare is at that index with the max welfare and although based off how this particular program works uh we don't necessarily need to do this right there is a keyword argument in that is close function that's important to know which is uh how specific you want it to be so in this case it goes to uh it typically can go to nine decimal places but in this case we'll go to two um just to demonstrate this function right as you can see here we got some challenges so math is underscored red all right make sure this is if not is but math is underscore red because we haven't imported uh Python's math library right so what we want to do is head up to our uh head up to our dependencies right and then I just added import math I'm going to put it here on the numpy it kind of fits with that and it is a primitive uh or a standard python Library and now we could go back down and see if we got rid of all our warnings about potential syntax errors all right so now create our third list candidate indices which extracts the index of all the um neighbor cell of all the welfare cells that are equal to math Max welfare or close to I should say Max welfare and that because welfares and neighbors have the same index setup that'll give us the index the indices we need to extract uh the locations from Neighbors okay so that's what we're going to do with this next line of code right so put a comment convert index to position of those cells we'll call this local variable candidates to be a neighbor's eye for that index for I uh in candidate indices so since candid indices is a list of the index that indexes from welfare that have the maximal welfare and that those index match the neighbors index to make the candidates list a list of couples that have the maximum welfare which is the positions that our agent could potentially might sound pretty confusing so since we have quite a bit of code where we're have two lists we make a third list from those two and then reduce that down to one list of Tuple positions when in doubt do a print statement so do print and then we'll do our kind of key list so Neighbors candidate indices and then candidates right so this will show us uh what give us a list of tuples a list of index for that right uh and then a list of candidates you run that okay and then we run that and this kind of obviously looks like a hot mess right this is a lot of information to process look really close and you know what you're looking for uh it uh you'll be able to see in one line um what we uh where you have your neighbors then the indices that have actual welfare and then the list of those Tuple position but since we're getting so much information here there's a lot of visual noise it's really hard to kind of suss out exactly what's happening so I got a technique that I use it's somewhat hacky I'm not gonna uh dispute that but I'll put an error condition so I only get one line and it's easier to process right so I'll just use the word stop which is not a variable so I'll get um an error right you can see here what we're looking for we got five we got a list of five positions position for the last position right it has maximal welfare and then so what we get for our final list of candidates is a tuple with that position all right so that's really what we've done with these bits of code taken Neighbors release of tuffles welfares which is a list uh synced with that list of neighbors that tells us what their maximum welfare is right we create the indices uh that have the maximum welfare and then we just extract out those Tuple positions so now we have a pretty straightforward problem of going through those positions identifying which ones are closer so it remains consistent with the book growing artificial societies right to move them to the closest position right uh with the best option right and then we move our agents which is just will be one line of code using mesa's move function all right so now uh we're gonna do something a little bit different just to show this is much a Python tutorial as it is a Mesa tutorial right is we use a function uh to get the minimum distance right and this function instead of putting the trader class we'll actually put it uh just as a function that any one of our classes can access so instead of using self it'll be Min get distance right uh and we'll just use a Pythagorean theorem so it needs our position the position we're looking to that will use list comprehension again right old tricks are the best tricks right uh for uh to iterate through our candidate positions and get their distance right and that will give us the minimum distance uh to any position that has maximal welfare so to do this again I like to keep my code clean I am going to uh or at least easy to read hopefully uh so I'm going to add another header called helper functions right so these are helper functions that any one of the classes can use if you're using an IDE with different dot py files right then you just import the function from whatever.py file you're using right so do our function get distance right and that will take two uh arguments position one and position two and then we'll add a comment so we know what this function's for all right this is again we're just going to use the Pythagorean theorem uh which works in a euclidean space all right so calculate the euclidean distance uh between two points so that way we can find the minimum distance of all the tuples that our agent has the potential of items to move to well I then we're also going to put or for me I like to know where the these helper functions are moved to so it's easier for me to understand how the codes are tied together so I'm going to put a used in trader.move all right so now uh we'll do our actual function right so it's a tuple position one said Tuple right just X1 you know y1 equals position one and then X2 Y2 equals position two this is just extracting the Tuple uh into uh their specific location so we can then put them through the Pythagorean theorem uh and then the distance of our x positions right so X2 uh X1 minus X2 and then the distance of our y position or between our y positions y1 minus Y2 um and then we just have to return right now we could use the square root function in our math library that we imported so Mass DOT square root of the distance squared of x plus the distance between the Y positions squared right take the square root of that voila we have our distance between um between the position that we're at and the position of maximal welfare and you can see here we're not getting any uh errors or we don't see any syntax errors and then we're just going to iterate through the candidate's position to get that distance to find the minimum distance and now we have to do the same thing that we did previously which is we know there might be multiple positions uh that could have the same distance uh and so we want to make sure that we have a list of final candidates that all are close to our minimal position right so do position four position uh in candidates all right and then we use the same process we used for our candidate indices where we'll uh use math dot is close and compare those two positions all right so get the distance um from our candidate position and compare that with our minimum distance I know there's a couple different ways you could do this if you had a lot of code or if you had a lot of Agents you're calculating this a lot uh we could do some aggressive caching she didn't necessarily have to calculate use the get distance so much but again coding is the iterative process it involves a lot of choices that you have to weigh against the numerous factors that are specific to your situation model all right but from this we'll get a final local variable called final underscore candidates that lists all the potential that lists all the close positions that provide maximal uh maximal welfare all right and then I will Shuffle this so that we kind of randomize which position the agents are moving to I and so that's the random.shuffle function we used in our model class in an earlier lesson where we're just going to shuffle those final candidates so with that done we can now actually finally move our agents right so this is part four which we can do in one live which is move agents to the closest position that provide the Maxwell welfare right so do uh mesa's uh move agent function right which for us is stored uh in our grid right that we imported as part of Mesa um macespace.py file right back on instantiated Omaha right and so uh the move agent function uh takes two parameters the agent object you want to move which is just self right and the position you want to move it to all right you can see this right yeah you can see all this on GitHub um where it takes those two arguments and you can see uh exactly how that function works and this is all part of mace's space.pi file which we uh Incorporated when we instantiated our multi-grid uh in our model class right and then our final candidates list is just the list of tuples right uh and so we'll just use the closest one that we just randomly shuffled right so now to make sure it's working uh or we've tested to see if it's the way I think it's doing we'll do a print statement where I used a minimum distance and a file candidate we run that and we get an attribute there right oh because a Trader object has no attribute grid right so that's fairly simple we go to that line of code I forgot to add self dot model right which is where we put a pointer to our model class and then grid and then move agent right so again an attribute error with a Trader object didn't have an attribute grid because we I forgot to put model in there right then we print that out and sure enough right we get uh our distances right plus that position I could see uh this one has two right so then we'll just use the closest one okay and that then if you want you can save it pin a revision is this uh marks the end of session 12 and our move agent function okay so there's a pretty involved uh last four lessons as our agents look across the landscape identify which cell gives them the maximum welfare right and then moves to one of the closest cells that provides maximal welfare all right and so that wraps up our agent move function next we'll have our agents consume resources and then decide who they should trade with and we'll see you in session 13 where Trader

### Code

From `Session_12_Traders_Move_part_4.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function part 2 self.move()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)



  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

    print(min_dist, final_candidates)
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    for agent in trader_shuffle:
      agent.move()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      print(i)
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 13 — Traders Eat

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=0JHbP2vJxAw |
| Length | 13:16 |
| Video title | Session 13: Traders Eat |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+13+Traders+Eat.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17332 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_13_Traders_Eat.ipynb |

### Transcript

<!-- 1887 words -->

welcome to session 13 of complexity explorers Mesa tutorial agent-based modeling of python in the last session we finished our Traders move function and now I'll do Traders e since they've found a location that's optimal for their particular situation they will Now consume the resources and then we'll determine if they have enough resources to continue let's get started please open up your Google collab or other instance and we can start coding so for previous lessons make sure they've imported your dependencies and this one we're using the Google Mount function but you can also upload the sugarscape.tex or sugar map.txt file if you'd like right so we import our dependencies we have one helper function that gives us the distance then we have our resource classes which is our sugar and spice agents and then our Trader agent will be spending most of this session here's the move session we completed last time where just to validate that it's working uh verify that it's working we looked at the distance and the final candidates then we have our model class which is how we initialize our model and then this manages our stage random activation function that we use to determine which agents move what and then we run our model for the last one you can see we get a distance right and the new position that the agent is moving to all right now that's another validate is working all right we'll be going here to add the call for the two functions we'll be working this session so first agents each where they consume the sugar and spice that is a given cell right and then agent dot maybe die we're determine if the agent has enough resources uh to con to continue so we'll call those two functions from our Trader class and so now we need to add them to our Trader class and these are much simpler than our age of boost function so we want it so get rid of this statement from the last lesson we won't need that anymore and then we'll add the function for eat if each with self in it for python syntax and so now you can remember our agents have moved to an optimal location that should maximize their um that's to maximize their marginal rate of substitution all right and so now we gotta collect uh we have to determine if there's sugar and spice uh on the um cell so we'll do sugar patch equals self that get sugar and so this is where the helper functions we built for our move to determine whether or not we should move there that takes one argument in your position so if we go up to our helper functions we can see here that get sugar function right that we use and get sugar amount that's part of our moot function all right so we're just going to write a note to myself here so I understand what my function dependencies are all right that's used in self that so now that we determine um another way to determine whether or not we're getting uh sugar or we get the sugar from an area you know if it is a sugar patch what we want to do is we want to add this sugar to our um uh to our uh our sugar attributes right so uh so simple python function plus equals sugar underscore patched out about right and then we need to take away the sugar that is in this particular patch so now we're going to set the sugar underscore patch dot amount to zero so if this is a sugar patch we uh the agent takes that sugar and adds it to itself that Sugar uh attribute and then we uh and then we remove the sugar from the cell and then outside the IF function we'll want to uh we now need to degrade the sugar based off What that particular Trader's metabolism is so self that Sugar minus equal self dot metabolism underscore sugar right so we get the sugar if there is any sugar there we add it to the Traders uh attribute and then outside the IF function we make sure uh that we degrade the Sugar by What that particular agent's metabolism is all right now uh we are going to do the same thing with the spice patch all right so if it's a spice patch we self.spice plus equals spice patch dot amount we then degrade the spice patch so zero so we're going to zero that out because the agent took it all right and then we need to reduce the agent's amount of spice based off What that particular agent's metabolism this is how you can fairly straightforward uh deal with heterogeneous age of populations that have different attributes so this is just similar to the sugar patch right use spice patch uh and consume any spice that might be in that cell I need to add I forgot to add the getting the spice so spice underscore patch equals self that get spice right that takes one parameter which is the position so go up to our get spice helper function I'll just put a note here that we're using that this function is also used in self buddy all right and this actually makes our um our eat function so I gotta test it remember code a little test a little so make a print statement and I'm just going to put in to print out the agents um Sugar and Spice I'm going to run that oh and we get an attribute error let's try all right up we've got code out the agent maybe die function okay and so uh and so that seems to be working uh the way we want it to okay now that seems like agent.ed is working without any issues we can now create our maybe die helper function okay so again this is if an agent right after they consume their sugar and spice doesn't have any more sugar or spice resource right then they need to be removed from the simulation so again def maybe underscore dice and we can make one more helper function for this just to determine how much uh to test the resources one okay putting some uh putting our comments for our function here now remember uh kind of more formal coding when you're coding for public libraries these are called your doc strings all right and then this would help you kind of build out your API so people can more effectively understand what your code is doing in this case we just make some comments to get the Habit um so it's easier for to make our code more readable for both ourselves and anybody else who might use it so we add our uh our doc string for maybe die functions so the first thing we want to do is test and see if they have if they've run out of sugar or spice all right so we're going to create another helper function called is start all right that will turn to true or false and so if it comes back true then we'll remove them from the simulation so I'll just put that up here starved okay if you remember how we start our function with just an if statement this is good just return to true or false now we're going to add our comments here so this is a helper function for maybe die and then we're just going to be a simple return so if the agent's sugar is less than or equal to zero or that's if they run out of either they can no longer continue right if their spice is less than or equal to zero right so if either one of those is true all right then they'll meet the conditions uh for the is starved so if there is starved function returns true now we want to remove the agents right there's two places that we have to remove the agents for this simulation right so the first one is going to be um in the is the grid right so it references the agents uh model attribute which refers back to the model class so we'll look at grid uh our grid attribute where we made our uh multi-grid and then we'll just use the function remove underscore agent all right then we also have to remove it from the scheduler so refer back to the model which refers to the model class and refer to the model's schedule attribute right and then we'll do the function for that which is just remove okay so now if is starved is true which means the sugar or the spice is less than zero right that function will be true and that condition will be true so then we remove them from the grid and remove them from the schedule now I want to validate that's actually occurring so we're going to print a unique ID before it occurs and we're going to print the number uh of Trader agents in the schedule so this one's going to be self.model dot schedule right and then get type count and in this case we just want to know the number of Traders this will validate uh so we'll do that before we run uh these two remove functions and I'm just going to copy and paste it I'm going to do it afterwards as well so that shows me that it's the same agent I and that uh that they've actually been removed that the number of traders in the simulation has been removed by one all right so this is a slight verification that it's doing we think but we're actually not testing whether that is removed from the grid oh and then we're gonna have to increase our step count because only uh we're only doing it for one right now that's not really enough time for our agents uh to starve and then be removed from the scheduler right so we're going to change this to I think and then okay then it runs so as you can see when I got the agent ID and then the number of agents and it's being it's being reduced by one all right so it looks like at least they're being removed from the scheduler for this case uh and that's valid enough or verified enough for what we're trying to do here so it looks like our eat function and then maybe die function are working properly all right so again it just looks at uh collects the sugar all right and the spice and then reduces the agent's metabolism right and then it goes to the maybe die um uh to determine whether or not they've starved that uses a helper function that returns a true or false right uh and if the condition is true then they are removed from the schedule so that concludes session 13.

all right we're hoping to join the uh the tutorial so far and we'll see in the next session

### Code

From `Session_13_Traders_Eat.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function part 2 self.move()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare,
                                        rel_tol=1e-02)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved():
      print(self.unique_id, self.model.schedule.get_type_count(Trader))
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)
      print(self.unique_id, self.model.schedule.get_type_count(Trader))
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    for agent in trader_shuffle:
      agent.move()
      agent.eat()
      agent.maybe_die()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=15)
```

---

## Session 14 — Traders Trade Part I (Get Neighbors)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=ggZgf2aciNg |
| Length | 14:11 |
| Video title | Session 14: Traders Trade Part I |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+14+Traders+trade+part+1.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17333 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_14_Traders_Trade_part_1.ipynb |

### Transcript

<!-- 2106 words -->

14 of complexity explorers Mesa tutorial agent-based modeling and pipeline in this session we'll begin the first part of our four-part series on trading agents for the agents will trade Sugar and Spice in order to hopefully survive and thrive in their environment let's get started first open up your IDE or Google collab instance with your Google collab instance you want to make sure that you've set up your sugarmap.txt file either by linking your drive right or by uploading via the folders all right we have our dependencies then we have one helper function two resource classes right uh one class for sugar one class for spice our Trader agent class which is getting more and more uh complicated and as we continue to build out the functionality and our model plus all right which manages the interactions of our Asian classes we initiate and then we have a series of Step functions right from our last lesson right we're printing out each step right and watching uh the agents that uh run out of sugar and spice and that are removed from the program right so first of all remove those print statements because you won't be needing them for this section so I got one in our step function uh and then one I in our Trader age or a couple in a Trader agent function right and that's those are located uh in our uh maybe die function at the bottom of the cell now that we've removed those we can start uh beginning our Trader function all right so the first thing we have to do because we've had agents that have been removed uh from our model because they ran out of sugar or spice all right is we have to set up our list that allows us to iterate through otherwise we'll end up with an error because our dictionary of Agents um uh has changed right so now that we're going to use essentially the same two lines twice to create Trader Shuffle and then randomize it we're going to just turn that into a function so create Trader function and then we'll call this function uh itself dot uh randomize Traders and it'll take no parameters and then we can just take these two lines all right and I'm gonna cut them and then just turn that into a function inside our model class right so I'll do this above the step function as it's a helper function four-step all right I am below all the functions that we use to initiate the model okay so it's fairly simple randomized set of score Traders right then it takes a parameter self as it's part of our model class then we just have Trader Shuffle equals the list from our schedule of Agents and we want to make sure we add our comments right helper function for our step function and this just creates a randomized list of our Traders so that way we can avoid uh challenges of first mover advantage or second mover uh advantage and on some models based off what you're trying to accomplish your show you might not want to randomize it but for this model I as we're showing kind of uh functionality of uh basic or economic theory we want to make sure uh that we randomize it okay uh after we do that uh then we just return our Trader shuffle list all right so if you remember from previous lessons the random.shuffle has actually returned anything it just takes that list uh and changes the order that it's in now that we've created our helpdorf function we can go Belize uh beneath our for Loop where we iterate through and have our agents movie and possibly die and then Shuffle our Asian list again updating it so it does not include any agent that possibly died in that step right now that this is done we're going to iterate through it again using another for Loop right and this is going to be four agent in Trader Shuffle and then it's just uh going to call a new function we're about to build called Agent trade with neighbors so this will allow us to continue our somewhat unique activation of random stage Activation so go sugar spice right then our agents move eat and possibly die right uh and then after that uh our agents trade with each other so we run that cell to make sure it's stored in memory right then we go back up to our Trader agents right and as this is a main function right so like move eat and maybe die then we add uh the trade with labor functions okay so staff trade with neighbor self because it's part of our Trader agent class and we add our comments thank you and this function will proceed in three parts and it's a function for Trader agents to decide uh who to trade with the three parts uh that it's going to be is first you got to locate your neighbors and identify all the cells that are in each agent's radius of vision how many Trader agents there are that Trader agent could possibly uh trade with so first like the uh eat function all right first we have to do is identify our neighbors but this case we're actually looking for Traders not avoiding it and the second thing we do is trade and I'll actually take two sessions right and then the final bit will do is collect data off that trade so we can uh get statistics about how our models function and then just like uh the previous uh just like the move function we're going to create a we're going to do list comprehension right in order to create a list of our neighbor agents all right so first for this we'll need another helper function so that'll be self get Trader and that'll take one parameter and that'll be the agent's position then we'll be able to use maces get neighborhood function so that's part of our space.py file so that's stored as self.model.grid all right get neighborhood all right and this takes the same parameters less than so first it takes the position then it takes whether or not using your more or Von Neumann neighborhood we're using our phon Neumann that's actually stores fault so whether or not to include the center in this case we're going to say false because we don't want to include the setter uh because I want to trade with ourselves all right and then the vision of that agent which gives a radius of how far they should look and this time instead of doing if not occupied by other we're just going to say if is occupied uh by other so we can reuse that function or in this case if it has a Trader agent we want them to return that cell once again this will use list comprehension in order to create a list of neighbor agents that we can possibly trade with and so I got to build our helper function so I'm going to put this uh above our main functions right and I'm going to put it below uh our uh get spice amount right so we have this kind of series of functions kit spice get sugar get spice amount of good sugar amount uh this kind of this has that same essential kind of purpose but this time we're getting a trainer so I'm going to put it here just to help me keep my Coral code organized so if I have issues or I'm looking for something I want to update something I know where it's at okay so we create our def get Trader right take self which is part of the trader class and then one parameter which is the agent's position I'm going to add some comments all right so again these are somewhat informal uh because we're not necessarily specifying specifically the parameter data type it takes but comments are still crucial so you can come back you know months weeks days later I and better understand your code as well as help others understand it if they're using your model uh or be using it or improving upon it so this is going to be a helper function used in trade with news so similar uh to our previous functions all right this is just going to say this cell we want to retrieve all the contents of the cell and we'll use mesa's built-in function from its space.py which is self.model.grid get cell list contents position remember we stored our multi-grid class right in the model in self.grid so that's why I use self dot model.grid right and then for agent and we iterate through that cell so we do four agent in this cell we want to see if any of these agents are in fact a Trader agent so we can use Python's built-in is instance function and if it is in fact a Trader agent we just return that agent so fairly straightforward function that just iterates through all the cell contents that determines whether or not it's an instance of our Trader right as you can see we run it we have a syntax error where I added an extra parentheses right here I got a one to my parentheses right uh so I just delete that run it again okay and I've removed my syntax error okay so now we've we've completed our list comprehension to produce a list of uh neighbor agents that are actually Traders now I want to test it all right code a little test a little all right and so we'll just print out uh the list of neighbor agents to see how it's functioning run that again no syntax errors then make sure the model plus is stored and that's updated and then uh we will run our instantiation of our class so it'll get an error where I did local uh local reference error where I call this trade Shuffle instead of Trader Shuffle when I uh rebuilt those lines of code it's fairly easy fix so Trader shuffles this is outbound local area local error because I did trade Shuffle instead of Trader Shuffle so fix that and I get another error okay in this case I get a type error cannot unpack an interval you can see here it's not my code to tearing out it's mace's space dot Pi uh one that's two so that means I've in I've done something wrong when I called uh this get neighborhood function now whether or not you're in the IDE uh your own IDE or Google codelab right we can actually reference that code right but let's go up and see what the error is as you can see here's the where I call the get neighborhood function and I call itself and I forgot that dot pops right so I was passing in the agent object not just the agent's position attribute all right so that's fairly easy update that so it's passing in the wrong type of attributes expecting a tuple of X Y right as you can see here and this is the same with most Ides right I can link this and this will take me to my locally stored version of space.py right and there's where it's the issue is because I was passing in an agent object not a tuple that's the position of the agent and this is no different than what we've shown previously uh in the lessons where we show our GitHub space.p1 okay so the code is you know Turtles all the way down so to speak the code is just python for the most part all the way down as you can see we're getting a list of Trader objects so it's still exactly uh what we hope it's uh doing that looks a little bit uh visually messy okay so if we could do something else uh just to make it cleaner let's do um the length of uh neighbor agents that we're getting that so just add the length function or length function all right store that memory you can see we get a series of numbers that's the length of the agents uh in their neighborhoods so that wraps up session 14.

develop our trade function thanks for joining and we'll see you next time

### Code

From `Session_14_Traders_Trade_part_1.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try: 
  import mesa
except: 
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar: 
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn 
  """

  def __init__(self, unique_id, model, pos, max_sugar): 
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice: 
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice
  
  def step(self): 
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent): 
  """
  Trader: 
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0, 
               spice=0, metabolism_sugar=0, metabolism_spice=0, 
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision

  
  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None
  
  
  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0
  
  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell: 
      if type(agent) is Spice: 
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch: 
      return spice_patch.amount
    return 0
  
  def get_trader(self, pos):
      '''
      helper function used in self.trade_with_neighbors()
      '''

      this_cell = self.model.grid.get_cell_list_contents(pos)

      for agent in this_cell: 
        if isinstance(agent, Trader):
          return agent
  
  
  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos: 
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell: 
      # see if occupied by another agent
      if isinstance(a, Trader): 
        return True
    return False
  
  def calculate_welfare(self, sugar, spice):
    '''
    helper function part 2 self.move()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form    
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)
  
  
  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  ######################################################################
  #                                                                    #  
  #                      MAIN TRADE FUNCTIONS                          #  
  #                                                                    #
  ######################################################################
  
  
  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision  
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos)) 
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares 
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare, 
                                        rel_tol=1e-02)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved(): 
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)

  def trade_with_neighbors(self):
    '''
    Function for trader agents to decide who to trade with in three parts

    1- identify neighbors who can trade
    2- trade (2 sessions)
    3- collect data
    '''

    neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
        self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
    ]

    print(len(neighbor_agents))
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """
  
  
  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):
    
    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height 
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)    
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material 
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)
    
    agent_id = 0
    for _,x,y in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0: 
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1
    
      max_spice = spice_distribution[x,y]
      if max_spice > 0: 
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1    

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id, 
                      self,
                      (x,y),
                      moore = False, 
                      sugar = sugar, 
                      spice = spice, 
                      metabolism_sugar = metabolism_sugar, 
                      metabolism_spice = metabolism_spice, 
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def randomize_traders(self): 
    '''
    helper function for self.step()

    puts traders in randomized list for step function
    '''

    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    return trader_shuffle
  
  
  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''    
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values(): 
      sugar.step()
    
    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values(): 
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to 
    # iterate
    trader_shuffle = self.randomize_traders()
    
    for agent in trader_shuffle: 
      agent.move()
      agent.eat()
      agent.maybe_die()

    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.trade_with_neighbors()
    
    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 15 — Traders Trade Part II (MRS & Price)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=T1sQYt0mquk |
| Length | 12:54 |
| Video title | Session 15: Traders Trade Part II |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+15+Traders+trade+part+2.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17334 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_15_Traders_Trade_part_2.ipynb |

### Transcript

<!-- 2009 words -->

15 if complexity explorers makes a tutorial agent-based modeling and pipe in this session we'll complete part 2 of our trade function in which we establish the marginal rate of substitution or Mrs and price for our agents it so that they can trade with each other let's get started first open up your preferred IDE or your Google collab instance and they want to make sure your sugarmap.txt file has either been uploaded or is connected via your Google drive through this magic function so import your dependencies now uh we do our helper function which is get distance for this one we do our resource classes which is Sugar and Spice right which says that each one grows one unit per time step then we have our trainer class which is significantly longer right uh where they move uh they eat they possibly uh die and then we're working this function here which is trade with neighbors so far we've established a list of neighbor agents that we can possibly trade with based off the agent's Vision attribute which tells how far they can see then we have our model class which we initiate our model this manages the interactions of our agents so sugar spice right and then Traders using this kind of unique stage random activation function right the agents move eat and die that's what we call those functions and then they trade with nuke right run that from session 14 we end up with uh the output of the length of neighbors that each agent has during one time step so now we could delete this uh print statement and now we want to create our actual trade function so we need to iterate through our neighbor agents so remember neighbor agents is a list of agent objects and if there is a Trader agent object then we're going to call our trade function that we're about to build so we'll pass one parameter which is the other Trader agent that we want to trade with foreign here iterate through Traders right and neighborhood agents remember that the neighboring cells is determined by the vision of that particular agent and how far they can see all right now I do need to account for something so you don't call this unnecessarily right if the neighbor agents uh returns nothing right so it has no length it's just an empty list but we don't want to do all these other functions we want to end the function as it is as we saw from the previous print statement there are some neighbors that or there are some agents that have no neighbor agents right so if that happens um if the length equals zero or uh then we need to return the empty list right and this function will turn two things so I'll turn the price uh or prices that the agents exchange their sugar and spice at and who they traded with so we can monitor the trade numbers so if that's the case we'll just return to empty lists so if length neighbor agents equals zero then return empty list comment if you list and now we want to build our trade functions so this is going to be uh death trade right and then it's going to have two parameters one being self because it's part of the trader class and the other one uh being the other uh the other Trader agent right so it's sell for other and that other being an agent object a Trader agent object all right then I'll put in our comment all right so helper function right that's used in trade with Neighbors which is the main function we call from our model class and then we're going to add I got one comment here which is just saying other is a Trader agent object just to emphasize that okay the other thing you could do here right so now I've got hundreds of agents who are interacting with lots of other agents multiple times um so we're going to add uh just a sanity check here to make sure that they should be trading at the rest of our codes working properly all right so we're add Python's primitive assert function it says if self.sugar is greater than zero and self that spice is greater than zero right now we'll do the same for the other agent other dot sugar greater than zero other dot spice greater than zero then that will allow this function to run if it doesn't if that assertion fails all right then we'll get a an error and we know that there's some type of bug in our code that we need to check out so this is just a sanity check to verify uh our code is working now that we've added this additional verification inside our model the next thing we've got to do is calculate the marginal rate of substitution of each of our agents the marginal rate of substitution comes from microeconomic Theory and determines how each agent values their sugar and spice commodity in relation to the other and this is then based off each agent's unique biology which is their sugar and spice metabolism all right there's a great description of this that starts on page 101 of growing artificial societies and explains how professors actel and Epstein developed the rules that they have for trading inside this particular model in which we're what we're basing this off of so we'll create a function called calculate Mrs Right as you can see here uh each agent object will have this function so for self it'll do self.calculate Mrs and for other uh they'll use their all right Mrs function in order to calculate their marginal rate of substitution this is also then becomes important just a sense where you're building a simulation right just like data you can make it say anything that you want you can make a simulation say anything that you want right so it's important to make sure your simulations and models are built on firm theoretic foundations and that you're not just programming something to make it produce the answer that you want now that we've done that I we can look up here right so this is our calculate Mrs Right and on that similar vein when we build our Cobb uh Douglas function all right although I showed uh where a description of it on the internet you can also look this up on page 97 which gives a great description uh of the integration of Cobb the Cobb Douglas function and how they put it into this functional form also in uh growing artificial societies now the trick with uh that one is again in the power of HF base models is that each Asian is calculating their situation based on or calculating their valuation uh or based off their unique situation right so it's not a homogeneous view of every agent having the same situation it's each agent being in a unique situ situation and then making decisions based off that so pre appreciating the importance of adding Theory and that agents allow for heterogeneous decision making based off their unique situation they can now calculate the Mrs or marginal rate of substitution that will take one uh so create a helper function just above our trade function I'll take one parameter called self because it's part of our Trader class I had some comments here and helper function for trade and it's just this is just going to be a pretty straightforward calculation based off the agent attributes I'm going to add another line of uh comment here just to make sure we understand uh what it is at the marginal rate of substitutions right so super generically just determines what the agent needs and what it's willing to give up which based off the fact that they have sugar and spice in a sugar and spice metabolism right it's their will it's their need for sugar or spice and they're willingness to give up the other commodity that they don't need again sugar or spice in order uh to enhance their position so that they can hopefully continue to survive and thrive the function or the calculation is pretty straightforward so we return self.spice divided by uh our self dot metabolism of spice and then this is going to be divided by self.sugar divided by our metabolism of sugar so self dot metabolism underscore sugar and this will give us a number that's either less than or greater than one that tells us how much they uh or if it's uh greater than one they have an excess of spice and if it's less than one nav they would like some spikes right so if they get a perfectly to one then they uh have reached a point where they neither care about sugar nor spice right they have a they have enough of each and enough of each adult value one over the other Okay so now that's done so with calculate the Mrs we're going to return two float numbers so similar to what we did previously we want to compare these two float numbers and so we're going to use the math dot is close function again this will take it the two parameters of the Mrs of ourself and Mrs of under right and then it's going to be uh and then we're going to describe its tolerance which will again due to two decimal places so Rel underscore t-o-l equals one e-02 and then we're going to do a print statement just to make sure all this is working the way we think it should be I'm going to say print it was close and if it was closed so we want to end the function right so if they don't uh if the agents have a relatively close Mrs they actually don't want to trade with each other uh and so we can stop that function there and create and prevent a bunch of unnecessary calculations we run our um uh model again and we could all right I get a type error it says Rel to is an invalid argument for is close so we go back up to our is close function that we put in there because it should be Rel underscore t-o-l so we add that in there I confirm that I did add a syntax error and then we go ahead and run it again sure enough we get it was close uh so it seems to be working the way uh we think it is at least we're not getting any uh errors so now from this we can calculate the price so again if you start on page 101 and grow your artificial societies uh you could get a very in-depth description over a couple pages of each of the choices and how they SWA how and why these trade rules were set up right but to calculate the price we'll call it P and it equals the math dot square root right of the Mrs assembly itself times the Mrs of the other and again this will give it give you a great description if you look at the trade rules in the book and then we're going to print the price to make sure that it's making sense and we're getting something reasonable for what we on this we're getting prices less two and greater than one and we're not getting any assertion errors so the next lesson uh we'll talk a little bit more about what that means but through this lesson we've established the marginal rate of substitution for each Asian and calculated that in a price next we'll have our agents potentially trade their Sugar and Spice in order to help their survivability thanks for joining and we'll see you next time

### Code

From `Session_15_Traders_Trade_part_2.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0

  def get_trader(self, pos):
      '''
      helper function used in self.trade_with_neighbors()
      '''

      this_cell = self.model.grid.get_cell_list_contents(pos)

      for agent in this_cell:
        if isinstance(agent, Trader):
          return agent


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function part 2 self.move()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form; starting on p. 97 on Growing Artificial Societies
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  def calculate_MRS(self, sugar, spice):
    '''
    Helper function for self.trade()

    Determines what trader agent is needs and can give up
    '''

    return (spice/self.metabolism_spice) / (sugar/self.metabolism_sugar)


  def trade(self, other):
    '''
    helper function used in trade_with_neighbors()

    other is a trader agent object
    '''

    # sanity check to verify code is working as expected
    assert self.sugar > 0
    assert self.spice > 0
    assert other.sugar > 0
    assert other.spice > 0

    # calculate marginal rate of subsitution in Growing Artificial Socieites p. 101
    mrs_self = self.calculate_MRS(self.sugar, self.spice)
    mrs_other = other.calculate_MRS(other.sugar, other.spice)

    # calculate each agents welfare in Growing Artifcial Socieites p. 97
    welfare_self = self.calculate_welfare(self.sugar, self.spice)
    welfare_other = other.calculate_welfare(other.sugar, other.spice)

    if math.isclose(mrs_self, mrs_other, rel_tol=1e-02):
      return

    price = math.sqrt(mrs_self*mrs_other)
    print(price)

  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare,
                                        rel_tol=1e-02)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved():
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)

  def trade_with_neighbors(self):
    '''
    Function for trader agents to decide who to trade with in three parts

    1- identify neighbors who can trade
    2- trade (2 sessions)
    3- collect data
    '''

    neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
        self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
    ]

    if len(neighbor_agents) == 0:
      # trade returns price and trade network (who agent traded with)
      return [], []


    # iterate through traders in neighboring cells and trade
    for a in neighbor_agents:
      if a:
        self.trade(a)
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def randomize_traders(self):
    '''
    helper function for self.step()

    puts traders in randomized list for step function
    '''

    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    return trader_shuffle


  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.move()
      agent.eat()
      agent.maybe_die()

    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.trade_with_neighbors()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 16 — Traders Trade Part III (Trade Sugar & Spice)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=3rG52ZWy6FE |
| Length | 17:54 |
| Video title | Session 16: Traders Trade Part III |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+16+Traders+Trade+Part+3.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17335 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_16_Traders_Trade_part_3.ipynb |

### Transcript

<!-- 2543 words -->

welcome to session 16 of complexity Explorer's Mesa tutorial agent-based modeling and python in this session we'll do part three of four of our Traders trade algorithm in this case we'll really be able to do the first half where of the trade algorithm where we look at how to transfer Spice from One agent to another all right let's get started please open up your IDE or your Google collab instance so make sure our sugar map.txt files accessible either by manually uploading it or mounting our drives we import our dependencies you know at this point of what helper function of git distance so we have our sugar and spice classes then we have our Trader class in this one our trade function is where I'll be working so far we've calculated our price based off our marginal rates of substitution for our agents and then this is all part of our trade with neighbor functions where we call our trade function then of our model class which manages the interactions between the agents when we run that we can see our prices the price calculated now we can start to figure out the exchange of sugar to spice for each agent if our price is greater than one then P units are spice uh are traded for one unit of sugar and if a price is less than one then one over P units of sugar are traded for one unit of spice so the way we need to capture this in code is we need to compare the Mrs of ourself versus the marginal rate of substitution of the other that way we could figure out uh how to set the price and how to establish the flow of sugar units to spice units for each agent to this we're going to build another helper function where uh called maybe underscore sell underscore Spike so this is going to take several parameters first this could take another Asian object that's going to take the price that we just calculated which is the geometric mean between the Mrs of ourself and Mrs of the other and then it's going to take uh the welfare of our self and the welfare of the other agent now unfortunately we've already calculated this is the Cobb Douglas function that we calculated two lessons ago I mentioned briefly last lesson you can just call or calculate welfare function for both the agent or self and then the other agent who are considering a trade so just create another local variable called welfare cell and then we'll call our function calculate welfare that takes uh welfare takes two parameters self.sugar and self.spice right so once we do it for the self agent now we need to do it for the other agents another local parameter welfare underscore other and then we just call it do other dot calculate welfare and passing two parameters in this case other dot sugar then other dot spice referencing the other agents sugar and spice attributes okay I can see here uh my price is underlined red that's because I actually need my local variable P so I'm going to change that to price and just add a helper function here so again what this is actually calculating is What's called the geometric beam we take the self Mrs of self times other and then take the square root of that okay uh again this is also using the Cobb Douglas function to calculate welfare you get a description of that in its importance on page 97 of the growing artificial societies uh we're also going to add up here in the comments because we use it for self.move that we're using this in the trade function that way if we later in we come and make changes or make adjustments we can have a better understanding uh of how it might break the model or all the places that'll influence that so now that we have this done we've got to build a helper function this is a helper function for trade I'm going to put it right above the trade algorithm again this would be called maybe uh cell spice and it's going to take several parameters so first self and then the other agent then the price and the welfare of self the welfare of other next lesson this is a bit interesting because the flow just reverses and so we'll be able to Leverage The parameters uh in order to reduce the amount of repetition in our code by just switching whose self and who sell it all right but this is uh so put some comments right so uh helper function for self.trade and now we want to try and calculate what's going to be exchanged all right so they'll be exchanging sugar and spice and this will require another helper function so I'll try two Returns on this one sugar exchange and Spice Exchange and then we need to calculate the cell spice enough and we'll pass in the price to do this and all this can be found on page 105 of the growing artificial society's textbook as you see it's a pretty straightforward calculation so to calculate the cell spice amount by passing the price first create our helper function and that's going to take two parameters self since it's part of the trader class and then price all right then we add our comments this is going to be a helper function or maybe cell spice this really uh and this is then going to be used to determine how much spice or sugar is being traded for each unit of Spicer sugar based off uh the price that was established if the price is greater than one uh then it's uh P units of spice for one unit of sugar and if it's less than one then it's one over P units of sugar for one unit of spice and so just write this out of Pi is greater than or equal to ones and the sugar equals one and the spice right is going to equal the integer of the price and vice versa else so if it's less than one then the sugar is going to equal in one over the price and the spice will equal one okay and then this will return uh your sugar and spice so then this gives the amount of sugar and spice to be exchanged based off the price that was calculated uh using the geometric mean per the previous functions in the side okay so this will give us a nice unit we might have like four units of spice for one unit of sugar or if it's the other way um it might be four units of sugar for one unit of spice all right now that's completed we've identified how much sugar and spice need to be exchanged at loops and to prevent Agents from trading in a manner that's not supportive to their welfare we have to establish some criteria to stop the trade if it's not actually helping the agents right so now we'll establish that criteria which is that does the trade make both agents better off right so it increases the welfare of both agents right and does it not cause the marginal rate of substitutions to cross one of them right so that is that they're uh that the value of the trade is no longer useful and so if any of those are met then that we want to stop that we don't actually want to follow through with the trade so to do this we actually have to uh similar to our kind of uh some of our previous functions we need to plan out what happened if the sugar actually is exchanged and does this make the criteria so we need to create some more local variables self sugar where I will equal the self.sugar plus the sugar exchange right then we'll look at the other sugar and do other underscore sugar equals other dot sugar minus sugar exchanged then we'll do the same for the Spice all right so self underscore spice right equals self dot spice plus spice exchanged the correction minus spice exchanged so that's a big one it's self dot spice minus Spice Exchange because uh the Mrs is higher so that the spice is the one being reduced and then we'll switch this in the next lesson and then other underscore spice equals other dot spice right plus Spice Exchange all right so now we've figured out the flow of the exchange of uh Sugar and Spice okay so I check these to make sure your plus and minus signs are going the right direction so very a very small difference that could result in dramatically different results okay so now that we've kind of created the simulated are these variables we can assess whether or not this trade uh or this exchange of should the first check is to make sure that they actually have these resources of sugar and spice indeed to conduct it to conduct the trade so if uh so we're just going to do a couple greater or less than an equal two signs here so if self that sugar is less than uh or equal to zero or other underscore sugar is less than to equal less than or equal to zero and put everything in parentheses here or okay open parenthesis self underscore spice is less than or equal to zero okay so remember this is all at this point just simulating uh or assessing whether or not the exchange can occur that's why we're using the underscore spice versus the dot spikes we're not actually looking at the attribute we're looking at what we anticipate the attribute to be so and then other underscore spice is less than to equal to zero so if any of these conditions can occur where they don't have enough sugar spice to conduct the trade this is for one unit of sugar one unit of spice all right that will return faults and the trade's not going to occur okay so that would make sure that they have enough resources now we can check these other criteria to ensure that uh that this is in the agent's best interest and it actually increases their welfare and doesn't decrease their welfare this also has the added benefit of ensuring that we don't create an infinite Loop for agents just keep on trading uh forever and ever right so the trade criteria number one this is found again on page 105 right is that are the agents better off and so to do this you need to make sure that with their new uh Sugar and Spice so this is the underscore sugar and uh an underscore spice right that both agents are federal so create a local variable called both agents better off this will be another true or false and so is the welfare of self uh less than the calculated welfare all right so remember we create the welfare of self uh previous or we pass that in as a parameter from our trade function and then we've got to calculate our welfare using the self.sugar and self.spice variables right so if it's less than uh that then that will return true if it's not then I'll return false effectively saying that the criteria is not met and then we've got to do the same for the welfare of the other so we use an and statement well the open parentheses so welfare uh unders underscore other is uh less than the other calculate welfare other underscore sugar right and other underscore spice okay so if both these criteria are true then both agents are better off right if either of these criteria is not true then both agents better off as false and we know that the trade is not in their best interest and you want to make sure that each subcondition of welfare underscore spice uh welfare underscore self and Welfare underscore other are kind of in the parentheses just to keep everything clean and now that's done we look at our trade criteria number two which is that um that the marginal rates of substitution are not Crossing I want to see exactly what's happening through this algorithm that was a kind of incrementally exchange of sugar and spice between agents you can look on page 106 which shows the Edgewood Edgeworth box representation again this is important because it demonstrates the integration of microeconomic theory into our agent's Behavior which does add some extra validity to it as it then helps us as we then get uh predicted results as a way to validate our model right so we want to verify that our Mrs our marginal rates of substitution are not Crossing where somebody actually doesn't want to exchange their particular commodity so Mrs underscore not Crossing so again I'm just using a true or false return on this right and then South dot calculate Mrs is greater than the other dot calculate Mrs okay so these two criteria will turn both uh true both need to be true in order for the trade to continue and then if either one is false so we say okay this isn't in the best interest of the agents and we're going to stop the trade I've written quite a bit of code at this point which probably means I have several mistakes in here that I need to correct so let's see if it works I'll do a print statement if I look at these true or false outputs uh and sure enough of an attribute error where Trader object has no attribute calculate spice cell amount because I wrote uh I misspelled the uh the function intense session or plus and minus signs and how you organize your parentheses you do have an impact for whether or not it returns true or false which will have a likewise cascading impact across the rest of the performance of your model so after I fix my calculate function run it again and now I get a type error where it says it takes one positional argument but two were given so I need to go back up to calculate self spice amount and it looks like I forgot my self parameter um which is part of the trader class will cause an error so run that we are getting true and false statements that tell us whether or not the potential trade meets the criteria we need it to as you can see some are false and some are true this is half of the algorithm where we're looking at the sugar and spice flow in what direction the next lesson will complete that looking at the sugar and spice flow and the opposite direction and then that will wrap up our trading algorithm where we can then transition to collecting data and analyzing it thank you for your time and we'll see you in session 17.

### Code

From `Session_16_Traders_Trade_part_3.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0

  def get_trader(self, pos):
      '''
      helper function used in self.trade_with_neighbors()
      '''

      this_cell = self.model.grid.get_cell_list_contents(pos)

      for agent in this_cell:
        if isinstance(agent, Trader):
          return agent


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function

    part 2 self.move()
    self.trade()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form; starting on p. 97 on Growing Artificial Societies
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  def calculate_MRS(self, sugar, spice):
    '''
    Helper function for
    - self.trade()
    - maybe_sell_spice

    Determines what trader agent is needs and can give up
    '''

    return (spice/self.metabolism_spice) / (sugar/self.metabolism_sugar)

  def calculate_sell_spice_amount(self, price):
    '''
    helper function for self.maybe_sell_spice() which is called from
    self.trade()
    '''

    if price >= 1:
      sugar = 1
      spice = int(price)
    else:
      sugar = int(1/price)
      spice = 1
    return sugar, spice


  def maybe_sell_spice(self, other, price, welfare_self, welfare_other):
    '''
    helper function for self.trade()
    '''

    sugar_exchanged, spice_exchanged = self.calculate_sell_spice_amount(price)

    # Assess new sugar and spice amount - what if change did occur
    self_sugar = self.sugar + sugar_exchanged
    other_sugar = other.sugar - sugar_exchanged
    self_spice = self.spice - spice_exchanged
    other_spice = other.spice + spice_exchanged

    # double check to ensure agents have resources

    if ((self_sugar <= 0) or
        (other_sugar <=0) or
        (self_spice <= 0) or
        (other_spice <= 0)):
      return False

    # trade criteria #1 - are both agents better off?
    both_agents_better_off = (
        (welfare_self < self.calculate_welfare(self_sugar, self_spice)) and
        (welfare_other < other.calculate_welfare(other_sugar, other_spice)))

    # trade criteria #2 is their mrs crossing
    mrs_not_crossing = self.calculate_MRS(self_sugar, self_spice
                                          ) > other.calculate_MRS(
                                              other_sugar, other_spice)

    print(both_agents_better_off, mrs_not_crossing)


  def trade(self, other):
    '''
    helper function used in trade_with_neighbors()

    other is a trader agent object
    '''

    # sanity check to verify code is working as expected
    assert self.sugar > 0
    assert self.spice > 0
    assert other.sugar > 0
    assert other.spice > 0

    # calculate marginal rate of subsitution in Growing Artificial Socieites p. 101
    mrs_self = self.calculate_MRS(self.sugar, self.spice)
    mrs_other = other.calculate_MRS(other.sugar, other.spice)

    #calculate each agents welfare
    welfare_self = self.calculate_welfare(self.sugar, self.spice)
    welfare_other = other.calculate_welfare(other.sugar, other.spice)

    if math.isclose(mrs_self, mrs_other, rel_tol=1e-02):
      return

    # calcualte price
    price = math.sqrt(mrs_self*mrs_other)

    if mrs_self > mrs_other:
      sold = self.maybe_sell_spice(other, price, welfare_self, welfare_other)

  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare,
                                        rel_tol=1e-02)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved():
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)

  def trade_with_neighbors(self):
    '''
    Function for trader agents to decide who to trade with in three parts

    1- identify neighbors who can trade
    2- trade (2 sessions)
    3- collect data
    '''

    neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
        self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
    ]

    if len(neighbor_agents) == 0:
      # trade returns price and trade network (who agent traded with)
      return [], []


    # iterate through traders in neighboring cells and trade
    for a in neighbor_agents:
      if a:
        self.trade(a)
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def randomize_traders(self):
    '''
    helper function for self.step()

    puts traders in randomized list for step function
    '''

    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    return trader_shuffle


  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.move()
      agent.eat()
      agent.maybe_die()

    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.trade_with_neighbors()

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 17 — Traders Trade Part IV (Complete Trade)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=nTEai0dTCRw |
| Length | 14:33 |
| Video title | Session 17: Traders Trade part IV |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+17+Traders+Trade+part+4.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17336 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_17_Traders_Trade_part_4.ipynb |

### Transcript

<!-- 2425 words -->

welcome to session 17 of complexity Explorer's Mesa tutorial agent-based modeling and python for this session we're going to complete our trade algorithm which will actually complete our model where all our agents are doing the interactions that we expect is this is really a continuation of part three where we're finishing the model instead of recapping uh the overview of the model really going to focus on recapping where we're at in our trade algorithm right now so let's get started first you do want to make sure you got your Google collab or other ID up and running and that your model is working and it should be producing a series of true and false statements those true and false tape statements uh tell us whether or not the trade criteria is met so with that right remember we call from trade neighbors couple actions here where we determine our neighbor agents then call the trade function first as a quick check and then it calculates our marginal rate of substitution uh for each of the agents so if we go up to calculate our Mrs we could see that calculation here right which is a ratio between uh our the Aged sugar and spice endowment to metabolism so after we calculate the Mrs then we calculate their welfare then we see if their Mrs is close if it is we return however I made a mistake here uh where I made it two course grain using the Rel tall function right it should just default to the uh is close out to the vaxome which is nine decimal points all right but make it two course grain that'll have some impacts later on because people will be trading at their Optimum because it is just a ratio between their Sugar and Spice in addition I did the same thing here with candidate indices right where we did the math is closed for Max welfare I and I made it too coarse grained by making that only out to two decimal spots based off how the Douglas function is calculated right that would just be uh that's a little bit too much in this case we'll use it the other time and final candidates right uh based off the grid Square uh two decimal places is fine right because the Grid on a 50 by 50 is pretty coarse gray now let this be a critical lesson that anytime you're preparing two float numbers it's a big deal and you really got to think through how coarse grain or not coarse grained you want it to be okay all right so now that we've discussed that uh we're back in our um uh or maybe cell spice function okay this is where we have our two trade criteria we just deleted our print statement to say whether or not our criteria is met right so if our criteria are not met so if actually then we want to stop the function so if both agents are better both underscore agents underscore better underscore off which is true or false and Mrs underscore not underscore Crossing it's also false if either one of those is false then we want to return uh that we want to return faults uh which is you'll see a little bit tells us that uh sale did not happen however both criteria are true and we know that the criteria is met and we actually want to execute the exchange of sugar and spice right so criteria met uh execute uh the exchange or execute the trade and so we'll add another helper function here and we'll call this cell spice this would take three parameters so first the other agent object and then the amount of sugar to be exchanged right and the amount of spice to be exchanged so these are this is the variable we calculated at the beginning of this function foreign and if that occurs we'll just add this now we're going to return true right so this is saying that an exchange did in fact occur right now let's build this helper function of cell spice we'll put this just above our baby spells cell spice uh function that way I keep it together code located and this one will be the death cell underscore spice because it's part of the trader class we need to put the self variable and then the other which is the other agent object the amount of sugar to be exchanged the amount of space to be exchanged so just call these sugar and spice right and then this will be a fairly simple function where we just add sugar to one take it away from the other and then the same with spice first subconscious right so uh this is I'm gonna put this is used in maybe cell spice and then this fundamentally executes the trade right so it exchanges uh the Sugar and Spice it's a fairly simple function we just deprecate uh so we add sugar to the self agent foreign or we take away that Sugar from the other agent and then we're going to take away Spice from the self agent and we're going to add spice to the other agent that's kind of fairly simple uh setup we're just going to add or subtract away from agent attributes based off what they need all right so I'm going to run that just to see if I got syntax errors which I do okay and then we've got cell spice um and so now we're executing the trade if the trade criteria are met if they are then we also return true um and why this is going to happen is we're going to show you now that um uh in the trade function right so if we go back to our trade function we calculate the price and then if our Mrs self is greater than the Mrs of other right then that means that we are uh we want to buy some uh sugar and is this could get pretty confusing as we look at both variants uh we're going to add that in the comments just to make remind ourselves right so if this case if Mrs itself is greater than other itself is a sugar buyer and spice seller you can see this if you go up to the cell spice function and even by the title of the function right maybe cell spice right uh so uh spice seller right now if the criteria weren't met then sold what we returned is going to be false right so no trade because criteria is not met if that happens we're not going to be able to trade with this particular agent for whatever reason and so we're just going to return it all right we're going to end the function right so now we can instead of having to write all the different variations uh we could just use those same functions by altering how we do the parameters so if the Mrs itself is less than the Mrs of other then we can execute fundamentally the same function we just swap uh the parameters and who's calling the function so in this case self is a spice buyer right and a sugar seller right and so we'll do sold equals now in this case instead of self we're going to call the other one so the other dot maybe underscore cell underscore spice right so we're just reversing every time spice and our self and other right instead of the parameter of other it's going to be self the price will go in and then it'll be welfare of other and then the welfare uh of self right as the parameters and this will just reverse the flow of sugar and spice uh so now the person who was gaining sugar is gaining spice and the one who was losing um sugar is now gaining sugar okay so then we'll put a comment here so again this will be the same as the last one if there's no trade that if sold is false that means there's no trade the criteria was not met right so just put if not sold all right returned so now with this uh We've fundamentally completed the exchange of sugar and spice but we want to collect data to ensure that we have the price recorded and we're also going to do the trade Network which we'll use in our next uh two sessions all right so I want to capture the data of this trade is really the essence of the model so it's important to point out here that all these return statements if a trade doesn't occur effectively is creating an implicit if statement where if a sale does occur right then we're going to capture the data right but because all these return statements will terminate the trade function uh that we don't have to explicitly write out that if statement right we could just capture the data so self dot prices we're going to dot append the price right so again where we place this means that the price will only be appended if a trade happens right and we're going to uh capture our trade Partners right so uh which agents are we trading with all right we'll just do that by using their unique ID so there's self.trade partners.apent other dot unique ID so if a trade occurs then we'll capture them uh that will capture that agent's ID so we can you know later on build out the Trade Network and kind of see the Dynamics of their trade now the trick is we actually don't actually have these as attributes for our agents uh so we need to go up here uh and add them in okay so start so we just go up to when we initialize the function uh add in self.p prices we'll just make this an empty list all right and also add self.trade underscore partners and make this an empty list okay so now every time we execute a trade we'll be able to say what the price is for each trade right remember it happens incrementally um and then we'll be able to say who we traded with which will also tell us how many times a trade occurred right uh before the uh the criteria wasn't met and we terminated the function so as this function occurs incrementally for each price right we're going to use recursion to Now call the trade function again and when the criteria is not met then the trade algorithm will be terminated all right so we're going to continue trading and all we have to do there is just call self.trade and then uh the use the other agent parameter and pass in that object and then we'll use recursion if the trade criteria is not met at any point all right uh then the algorithm stops and this will prevent us from having an infinite Loop all right now we could go back to our trade neighbors function right uh and we actually made a change here right where before I said hey if there's no uh agents we'll get trades for return trade and price Network we don't need to return anything because those are now part of our agent attributes okay uh and then we'll put here just for completeness that uh if uh after you've traded with all the potential neighbors right then we're also going to return and uh and the trade with neighbors functions I'm gonna get rid of this comment because it's no longer relevant okay and again the trade with neighbors uh just uh terminates um if they have no neighbor agents to trade to and that just prevents a bunch of unnecessary faults the next thing we need to do is move down to our model class and now somewhat counter-intuitively clear our price uh our agent's price and their trade Partners the reason for this is we can use data collector to collect the price the prices and the trade partners for each step it'll just be easier to analyze this will make more sense in the next lesson when we actually do data collector so in this first part of agent.trade.shuffle before we do move eat and maybe die where we're going to clear our prices and we're going to clear our trade partners and kind of reset those attributes back to zero okay then uh to ensure since we wrote a lot of code uh we're going to add a print statement here just to make sure we're getting what we think we're getting uh which is a list of prices uh and a list of uh unique IDs of the agents that they traded with uh per the number of times that they traded with it okay so we can just add that right here so under our second uh Trader Shuffle where we right after we trade with neighbors then we're going to agent dot prices uh and agent dot trade Partners right so this should give us a list of prices that we traded at right as well as a list of Partners uh with a part with their unique ID for every time we traded with them okay um so we just call our instantiated uh version of the model we run it one time and sure enough that's we can see a lot of agents are trading right and some agents trade once um and some ages trade multiple times with the same agent uh or trade you know uh once with one agents twice with another agent et cetera right and now we have a fully functioning Trader sugarscape model where our Trader agents Traverse a sugar and spice landscape and then also trade Sugar and Spice in order to survive and thrive the next thing we have to do is validate that the model is actually working the way we expect it to so the next two lessons we'll use mesa's data collector to collect data and do a quick analysis uh in order to validate our model and make sure it's behaving the way we think it should based off growing artificial societies so that wraps up session 17.

thanks for joining and we'll see you next time

### Code

From `Session_17_Traders_Trade_part_4.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision
    self.prices = []
    self.trade_partners = []


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0

  def get_trader(self, pos):
      '''
      helper function used in self.trade_with_neighbors()
      '''

      this_cell = self.model.grid.get_cell_list_contents(pos)

      for agent in this_cell:
        if isinstance(agent, Trader):
          return agent


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function

    part 2 self.move()
    self.trade()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form; starting on p. 97 on Growing Artificial Societies
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  def calculate_MRS(self, sugar, spice):
    '''
    Helper function for
    - self.trade()
    - self.maybe_sell_spice()

    Determines what trader agent is needs and can give up
    '''

    return (spice/self.metabolism_spice) / (sugar/self.metabolism_sugar)

  def calculate_sell_spice_amount(self, price):
    '''
    helper function for self.maybe_sell_spice() which is called from
    self.trade()
    '''

    if price >= 1:
      sugar = 1
      spice = int(price)
    else:
      sugar = int(1/price)
      spice = 1
    return sugar, spice

  def sell_spice(self, other, sugar, spice):
    '''
    used in self.maybe_sell_spice()

    exchanges sugar and spice between traders
    '''

    self.sugar += sugar
    other.sugar -= sugar
    self.spice -= spice
    other.spice += spice


  def maybe_sell_spice(self, other, price, welfare_self, welfare_other):
    '''
    helper function for self.trade()
    '''

    sugar_exchanged, spice_exchanged = self.calculate_sell_spice_amount(price)

    # Assess new sugar and spice amount - what if change did occur
    self_sugar = self.sugar + sugar_exchanged
    other_sugar = other.sugar - sugar_exchanged
    self_spice = self.spice - spice_exchanged
    other_spice = other.spice + spice_exchanged

    # double check to ensure agents have resources

    if ((self_sugar <= 0) or
        (other_sugar <=0) or
        (self_spice <= 0) or
        (other_spice <= 0)):
      return False

    # trade criteria #1 - are both agents better off?
    both_agents_better_off = (
        (welfare_self < self.calculate_welfare(self_sugar, self_spice)) and
        (welfare_other < other.calculate_welfare(other_sugar, other_spice)))

    # trade criteria #2 is their mrs crossing
    mrs_not_crossing = self.calculate_MRS(self_sugar, self_spice
                                          ) > other.calculate_MRS(
                                              other_sugar, other_spice
                                          )

    if not (both_agents_better_off and mrs_not_crossing):
      return False

    # criteria met, execute trade
    self.sell_spice(other, sugar_exchanged, spice_exchanged)

    return True


  def trade(self, other):
    '''
    helper function used in trade_with_neighbors()

    other is a trader agent object
    '''

    # sanity check to verify code is working as expected
    assert self.sugar > 0
    assert self.spice > 0
    assert other.sugar > 0
    assert other.spice > 0

    # calculate marginal rate of subsitution in Growing Artificial Socieites p. 101
    mrs_self = self.calculate_MRS(self.sugar, self.spice)
    mrs_other = other.calculate_MRS(other.sugar, other.spice)

    #calculate each agents welfare
    welfare_self = self.calculate_welfare(self.sugar, self.spice)
    welfare_other = other.calculate_welfare(other.sugar, other.spice)

    if math.isclose(mrs_self, mrs_other):
      return

    # calcualte price
    price = math.sqrt(mrs_self*mrs_other)

    if mrs_self > mrs_other:
      # self is a sugar buyer, spice seller
      sold = self.maybe_sell_spice(other, price, welfare_self, welfare_other)
      # no trade - criteria not met
      if not sold:
        return
    else:
      # self is a spice buyer, sugar seller
      sold = other.maybe_sell_spice(self, price, welfare_other, welfare_self)
      # no trade - criteria not met
      if not sold:
        return

    # Capture data
    self.prices.append(price)
    self.trade_partners.append(other.unique_id)

    # continue trading
    self.trade(other)

  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved():
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)

  def trade_with_neighbors(self):
    '''
    Function for trader agents to decide who to trade with in three parts

    1- identify neighbors who can trade
    2- trade (2 sessions)
    3- collect data
    '''

    neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
        self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
    ]

    if len(neighbor_agents) == 0:
      return


    # iterate through traders in neighboring cells and trade
    for a in neighbor_agents:
      if a:
        self.trade(a)

    return
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    #initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    #initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)

    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def randomize_traders(self):
    '''
    helper function for self.step()

    puts traders in randomized list for step function
    '''

    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    return trader_shuffle


  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.prices = []
      agent.trade_partners = []
      agent.move()
      agent.eat()
      agent.maybe_die()

    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.trade_with_neighbors()
      print(agent.prices, agent.trade_partners)

    self.schedule.steps += 1 #important for data collector to track number of steps

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model(step_count=1)
```

---

## Session 18 — Data Collector (Model Level)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=ymVD4ofs8OQ |
| Length | 21:56 |
| Video title | Session 18: Data Collector Model |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+18+Data+Collector+Model.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17337 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_18_Data_Collector_Model.ipynb |

### Transcript

<!-- 3605 words -->

to session 18 of complexity explorers Mesa tutorial agent-based modeling and python now that we've completed our agent behaviors and are managing the interactions through our model class and the step function we're at the point where we can actually collect data and make sure our model is behaving in the way that we think it should and that being said let's get started so go ahead and open up your IDE or Google collab instance and we can begin so first you want to make sure that you're linked to sugarmap.txt file to your instance to do that either by mounting your drive or manually loading it we have our helper function which is currently get distance but this session we're going to add a few more to help us analyze the data and then we have our resource class of sugar and spice that grow one unit per time step which we won't be interacting with then we have our Trader class which we completed the last instance where Traders Traverse the landscape and trade sugar spice now a critical point then is to make sure and both our calculate welfare right where we use the Cobb Douglas function by calculating that marginal rate of substitution where we compare our spice and sugar and a ratio right that we uh that we've made sure that we've removed that math is close relative power tolerance so it defaults to its nine decimal points this is important to help make sure that our agents are optimizing their behavior so they're always approving their welfare by trading as much sugar and spice as possible based off how the cop Douglas function and the Mrs are calculated all right we also need to make sure that happens uh when our move function right when we try and find the optimal move locations based off welfare it's any time you're comparing two real numbers a computer programming is you really want to make sure you understand exactly what you're comparing and what the impacts of the granularity that you use are there's not going to be the trader function anymore we're going to collapse that right we will be working the model class where we initiate the model and in this initialization we'll be adding another Mesa object class for data class also manages our step function where we use a stage activation uh with random activation for our Traders so go through each of the sugar and spice functions and then we go through our agents to move e to possibly die and then we go through our agents again to have them trade with each other now with the last one we had a print statement after uh our agent.trade with neighbors function that we can now delete how do I make sure it's working and delete your print statement the next thing we're going to do is add an object the data collector object from Mesa so up here where we initiate our activation schedule and we also initiate our basic grid class we're now just going to initiate a data collector object I like the Grid in the schedule we're just calling a Mesa class that will be now be part of our model just like with our Trader or sugar spice agents so we'll call this self.data collector then that will equal Mesa dot data collector that then gives us a data collector instance right now if we go up here we could see uh from mesa's GitHub page the data collector code again this is all in Python so you can see you know you can look at the notes and see different options on how to collect data or process data using the Mesa data collector function we now put in the variables that we want to collect for the model we want to collect three variables first the number of agents that are surviving at each time step then the amount of trade volume that's occurring and finally the price so first we'll get the number of agents that are still alive after each step we'll call this one Trader and then we'll use a Lambda function in order to get the data that we need so Python's primitive Lambda and this is short for model and then they'll Follow by uh colon right there'd be n dot schedule because we want to get the number of Traders uh that we have at the bottom of every at any given time step all right so it'll be m dot schedule and then the um random activation by type uh function git type count and then Trader because we could do it for Sugar and Spice but those don't do anything uh except grow and unit so we want to get our Trader agent uh objects so Lambda n colon m.schedule git type count Trader and that will give us the number per time step of how many Traders are left next will be trade volume all right again we'll use a Lambda function so Lambda which is just shorthand for model and then we want to add together the length of all the trade partners for each of the agents would be sum open parenthesis length for length and then we're going to do open parenthesis again a for agent dot trade Partners so this will collect the trade Partners list for each agent object all right close parentheses and then using list comprehension 4A in schedule agent Sprite type and then uh Trader and brackets right so this iterates through the dictionary uh of Traders and all their values and each of those agent objects it pulls out the list of trade Partners gets the length of those trade partners and then sums them together for each step I appreciate it's pretty condensed code that's doing a lot uh but it's important right so m dot schedules dot agents underscore by type Open Bracket Trader close bracket dot values right so it's iterating through uh the dictionary of Trader objects and then pulling out the length of their trade partners and adding all those together that's how we get uh a trade volume for each step all right so we're collecting model level variables uh for specific behaviors of the bottle okay now we have one more to go which is our price and this is going to be a little bit more complicated because we're going to add two helper functions to it so I'll name this one price with a capital p and then we'll do another Lambda function again using M which is uh is called the model object okay and for this we're going to calculate the mean kind of per growing artificial societies using the geometric mean which will make a function four in a second and because it's a list of prices that we want to get the geometric mean for and each one of those is in their own list we have to flatten that list which will make also is another helper function all right so again the geometric mean open parentheses flatten open parenthesis and then list comprehension a DOT prices for a then m dot schedules that age and spy type uh Open brackets Trader with a capital T right and then value so again this iterates through uh the dictionary of uh Trader agents takes that object and then gets its uh prices price attribute from each of those agents okay and then from that we're going to do two functions first we're going to flatten it because it's a list of lifts and then from that flat list we're going to take the geometric mean and so now we got three our three uh collections that we do at each step across the whole model where you get the type count of Traders the number of traders that are in each that are still alive uh the volume of their trade by iterating through each of our Asian models uh and kind of their trade and then finally we get the price uh but we need to do some helper functions first so first we'll do flatten right work from the inside uh of our kind of cadence function out okay um and since this is we're gonna put this in our helper functions outside of our model class just where we put uh get distance for the last one okay so flatten and we'll take one parameter which is a list of lists okay so this is all the prices that the agents have collected in each one of those whether there's an empty list or not right is uh we'll provide a list right and so be item for sub list let me list comprehension again uh in lists of lists all right for item in sublist okay so what that does is it takes every item in each sublist and puts it into uh another list which is what we're returning so you gotta make sure there's brackets on beginning in the end it's item for sub list and list of the list for item and sublist right and this just goes through each list inside that list of lists and extracts any uh any price that was uh that was added during the model run it puts it into one flat list and so we got to write some comments but uh so just again some kind of simplified comments not formal comments uh but this way you can understand your model a little bit better if you come back and look or somebody else does and this would be a helper function uh for the model data collector for trade price as we're collecting three uh model level variables and what this does is collapse the agent prices from a list of lists into a single list so that we can then take the geometric mean in order to find out what the trade price was at each of those steps so now I gotta write our helper function for geometric mean right so pass in our parameter which is going to be the list of prices and then we write our comments and which is a list of prices um turns into the geometric mean it's more properly find the geometric mean from a list of prices so I got a comment all right should probably change our variable to actually describe what we're passing in so that's list of prices and this is actually coming from flattened so that return function right there is just the list of prices and then we can use numpy part because sorry imported in order to calculate this so they calculate the geometric mean as m p for numpy DOT exp open parenthesis NP log right and then pass in the list of prices dot mean and so this is uh it's not numpy it's very efficient calculated arrays all right this will give us the geometric mean uh for the list of prices that we're passing in for each step so that way for each step we can get that geometric mean for each price that was calculated right so we passed a list of prices uh we run this function to calculate the geometric mean and now our helper function is working so around that those syntax errors then we run our model class and we can see the three data points that we're collected against our model which is number of Traders after each step the trade volume of each step and then the price uh the geometric mean of the trade prices at each step all right and in the next lesson we'll look at agent variables now the one last thing to do to make sure your data collector is working is we need to put in the function to actually tell it to collect every time we run through one of the model step functions so this is just one line of code right we've initiated our data collector at the top we're in the same place we initiate our grid and our schedule and now we want to make sure that we call the data collector uh during each step so it collects these model level variables and where we do our agent data collection the next one where I will put that inside the step function so that way it collects more granular data for each agent all right so just put a quick comment here collect model level data then we call our data collector instance so self.data collector and then we just use the function collect which is part of the data collector class and then self and it will take care of the rest so we run that and then we're going to run our model okay as now we actually want to collect a lot of data well first we'll make sure it runs here quickly one step and uh didn't get any errors so now we can run a thousand steps and since our default uh keyword argument for step count is a thousand we can run that this should take if you're using Google collab about 30 seconds in the meantime we can add another a section called analyze data so I added a text field called analyze data and then once this is run we can start to extract that data we get a runtime warning which is just telling us that during one step no trade occurs sometimes these runtime warnings are really important other times they're not but it's important that you understand what they're saying as another way to verify your model's functioning the way they should okay now the way we're going to extract the data is we're going to just create a quick function called results equals model dot data collector so we're calling the model instance we created in the cell above right dot data collector and then we use the function dot get underscore model underscore vars underscore data frame this is just a meso organic model that produces a pandas data frame so it's easier to understand and analyze the results now you can just write results run that cell and sure enough we get a table with what we're hoping for so Trader as our first one number of Traders still left alive the volume you can see there's a precipitous drop all right uh and then the price uh for which is a geometric mean of all the prices that occurred uh in that step okay so we now have uh our data collection results right so now I want to analyze them to see if we're getting results similar to that and growing artificial societies one thing to remember is again all of this code is available if you want to see that particular function you just control F but I'd get model vars uh data frames look for that function and you can see the actual function uh that you're calling if you ever want to look at the code if you're getting error messages that you don't understand or you want to see how Mesa does it in case you need to make some adjustments to it all right so now that we've got our results we can start to plot things as we're using a panda's data frame pandas has some organic plotting function set for this next one we're going to leverage so I just do results Dot Plot and then our Y axis is going to equal Trader and we're going to want to use the index uh and set that to true so if you want to see this you can look at the pandas documentation and that's where getting our arguments from but usually this one line function we get a very kind of straightforward plot showing the number of agents that are living at any given time right now as always I'll put some comments so I'll plot Number of Agents per time step all right so again results Dot Plot y equals Trader in parentheses with a capital T then use index equals true okay uh now the next thing we want to prod plot I is our price now we're gonna try and plot this similar to how they plotted it in growing artificial societies which is a scatter plot right which is not part of kind of the pandas organic plotting function use the matplotlib normal functions of to plot out the prices so for this we want to plot trade prices and we need to convert our column of prices just into a list that we can use for our y-axis so Y is going to equal list open parenthesis results and then price and brackets and quotes as it's calling that column right that X is just the range uh to 1000.

all right so that gives us just zero one to one thousand now you just do PLT dot scatter remember PLT comes from how we imported matplotlib uh initially right so that'll be X and Y uh and then size uh equals one that this is the size of the dots and we get an error and that error showing us the path collection attribute has no property size so sorry it's actually s equals one and what that does is it changes the size of the dots because the default argument uh is just a little bit too big all right so go up here to plt.scatter again PLT is when we import a matplotlib it's import you know matplotlib.pi plot as PLT just kind of standard convention and then we get the result now as you can see here similar to the book the density of prices around one gets more and more than the variance uh gets smaller and smaller as uh the code reaches equilibrium right uh so this is significant is this provides validation the economic theory lets us know our model is working correctly right the number of Agents okay that's consists with growing artificial societies uh and then uh the stacks with the trade volume we'll see uh has you know is also similar but has some differences but really the one we care about uh is that our prices are converging to one all right which is consistent with economic theory right now I want to plot our trade volume that's what we're going to show you an interesting dynamic right so typically right you want a bar graph or typically might default to a bar graph because they're easy to do so you just get plt.bar results dot Index right uh and then results trade volume all right so it should be capital B and this will tell us uh roughly uh how many how much trade is occurring right we get this huge drop off uh at the beginning you can see there or we have this huge Spike and then there's a pretty significant drop off so okay let's kind of outlier I could easily get rid of that uh by just doing some uh cutting the list down starting from one right and we get this uh you know this Dynamic of trade volume or we can see as agents die off there's understandably less trade volume right or I is there right so now if we look at 10 so let's say well I saw let's start with 10 let's cut off all those two until we get the agent population stabilized right now we get this massive Spike that we didn't have in the last one that goes up to 300.

so similar to kind of math is close what's happening here right because the way uh matplotlib bar graphs work as it's creating container objects uh that for lack of render description is just picking and choosing some of the things they're looking at so if you actually want to get uh the amount of Trade A per time step and see what's happening uh you have to use a slightly different function right so before I in range 1000 and there we go PLT dot V lines for vertical lines I is your x-axis 0 is your y minimum and then results of your trade volume is your y maximum so this will plot a vertical line at each time step so you can see the trade volume foreign and then you put the I there for the index right and here it is right so this plots it out for us we'd see each one at the index which will make sure that we get each step of trade volume so the big lesson there is just you know particularly doing visualizations be careful that you understand exactly what that visualization is doing so you don't get false Impressions about what's happening all right so that wraps up session 18 uh we do data collector and then we made three visualizations where we kind of mirrored the critical result we wanted which is trade prices uh converging to one uh over time and the variance becoming less and less next lesson we'll use data collector to collect agent level data so we can look at the trade networks of each agent big lesson will be batch run or we do parameter sweeps and compare those results thanks for watching and we'll see you in session ninth

### Code

From `Session_18_Data_Collector_Model.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)

def flatten(list_of_lists):
  '''
  helper function for model datacollector for trade price
  collapses agent price list into one list
  '''
  return [item for sublist in list_of_lists for item in sublist]

def geometric_mean(list_of_prices):
  '''
  find the geometric mean of a list of prices
  '''
  return np.exp(np.log(list_of_prices).mean())
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision
    self.prices = []
    self.trade_partners = []


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0

  def get_trader(self, pos):
      '''
      helper function used in self.trade_with_neighbors()
      '''

      this_cell = self.model.grid.get_cell_list_contents(pos)

      for agent in this_cell:
        if isinstance(agent, Trader):
          return agent


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function

    part 2 self.move()
    self.trade()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form; starting on p. 97 on Growing Artificial Societies
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  def calculate_MRS(self, sugar, spice):
    '''
    Helper function

    - self.trade()
    - self.maybe_sell_spice

    Determines what trader agent is needs and can give up
    '''

    return (spice/self.metabolism_spice) / (sugar/self.metabolism_sugar)

  def calculate_sell_spice_amount(self, price):
    '''
    helper function for self.maybe_sell_spice() which is called from
    self.trade()
    '''

    if price >= 1:
      sugar = 1
      spice = int(price)
    else:
      sugar = int(1/price)
      spice = 1
    return sugar, spice

  def sell_spice(self, other, sugar, spice):
    '''
    used in self.maybe_sell_spice()

    exchanges sugar and spice between traders
    '''

    self.sugar += sugar
    other.sugar -= sugar
    self.spice -= spice
    other.spice += spice


  def maybe_sell_spice(self, other, price, welfare_self, welfare_other):
    '''
    helper function for self.trade()
    '''

    sugar_exchanged, spice_exchanged = self.calculate_sell_spice_amount(price)

    # Assess new sugar and spice amount - what if change did occur
    self_sugar = self.sugar + sugar_exchanged
    other_sugar = other.sugar - sugar_exchanged
    self_spice = self.spice - spice_exchanged
    other_spice = other.spice + spice_exchanged

    # double check to ensure agents have resources

    if ((self_sugar <= 0) or
        (other_sugar <=0) or
        (self_spice <= 0) or
        (other_spice <= 0)):
      return False

    # trade criteria #1 - are both agents better off?
    both_agents_better_off = (
        (welfare_self < self.calculate_welfare(self_sugar, self_spice)) and
        (welfare_other < other.calculate_welfare(other_sugar, other_spice)))

    # trade criteria #2 is their mrs crossing
    mrs_not_crossing = self.calculate_MRS(self_sugar, self_spice
                                          ) > other.calculate_MRS(
                                              other_sugar, other_spice)

    if not (both_agents_better_off and mrs_not_crossing):
      return False

    # criteria met, execute trade
    self.sell_spice(other, sugar_exchanged, spice_exchanged)

    return True


  def trade(self, other):
    '''
    helper function used in trade_with_neighbors()

    other is a trader agent object
    '''

    # sanity check to verify code is working as expected
    assert self.sugar > 0
    assert self.spice > 0
    assert other.sugar > 0
    assert other.spice > 0

    # calculate marginal rate of subsitution in Growing Artificial Socieites p. 101
    mrs_self = self.calculate_MRS(self.sugar, self.spice)
    mrs_other = other.calculate_MRS(other.sugar, other.spice)

    #calculate each agents welfare
    welfare_self = self.calculate_welfare(self.sugar, self.spice)
    welfare_other = other.calculate_welfare(other.sugar, other.spice)

    if math.isclose(mrs_self, mrs_other):
      return

    # calcualte price
    price = math.sqrt(mrs_self*mrs_other)

    if mrs_self > mrs_other:
      # self is a sugar buyer, spice seller
      sold = self.maybe_sell_spice(other, price, welfare_self, welfare_other)
      # no trade - criteria not met
      if not sold:
        return
    else:
      # self is a spice buyer, sugar seller
      sold = other.maybe_sell_spice(self, price, welfare_other, welfare_self)
      # no trade - criteria not met
      if not sold:
        return

    # Capture data
    self.prices.append(price)
    self.trade_partners.append(other.unique_id)

    # continue trading
    self.trade(other)

  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved():
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)

  def trade_with_neighbors(self):
    '''
    Function for trader agents to decide who to trade with in three parts

    1- identify neighbors who can trade
    2- trade (2 sessions)
    3- collect data
    '''

    neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
        self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
    ]

    if len(neighbor_agents) == 0:
      return


    # iterate through traders in neighboring cells and trade
    for a in neighbor_agents:
      if a:
        self.trade(a)

    return
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    # initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    # initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)
    # initiate datacollector
    self.datacollector = mesa.DataCollector(
        {"Trader": lambda m: m.schedule.get_type_count(Trader),
         "Trade Volume": lambda m: sum(len(a.trade_partners)
         for a in m.schedule.agents_by_type[Trader].values()),
         "Price": lambda m: geometric_mean(flatten([a.prices for a in m.schedule.agents_by_type[Trader].values()]))}
    )


    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def randomize_traders(self):
    '''
    helper function for self.step()

    puts traders in randomized list for step function
    '''

    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    return trader_shuffle


  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.prices = []
      agent.trade_partners = []
      agent.move()
      agent.eat()
      agent.maybe_die()

    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.trade_with_neighbors()

    self.schedule.steps += 1 #important for data collector to track number of steps

    # collect model level data
    self.datacollector.collect(self)

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model()
```

<!-- cell 14: markdown -->

> # Analyze Data

<!-- cell 15: code -->

```python
results = model.datacollector.get_model_vars_dataframe()

results
```

<!-- cell 16: code -->

```python
# plot number of agents per time step
results.plot(y = "Trader", use_index=True)
```

<!-- cell 17: code -->

```python
# plot trade price per step

y = list(results["Price"])
x = range(1000)

plt.scatter(x,y, s=1)
```

<!-- cell 18: code -->

```python
# Plot trade volume

plt.bar(results.index[10:], results["Trade Volume"][10:])
```

<!-- cell 19: code -->

```python
# Plot trade volume improved

for i in range(1000):
  plt.vlines(i,0,results["Trade Volume"][i])
```

---

## Session 19 — Data Collector (Agent Level)

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=w6wV7H3lCL0 |
| Length | 17:14 |
| Video title | Session 19: Data Collector (Agent Level) |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+19+Data+Collector+-+Agent+Level.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17338 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_19_Data_Collector_Agent.ipynb |

### Transcript

<!-- 2698 words -->

welcome to session 19 of complexity Explorer's Mesa tutorial agent-based modeling and python in this session we'll be looking at the data collector at the agent level we'll be collecting information about each agent for every time set step and in this case building out the Trade Network of our Asia population so let's get started as usual please open up your IDE or Google collab instance so once we get started we'll as usual make sure that your sugar Dash map.txt file is loaded either by uploading to your uh your folders or by mounting it with your Google Drive for this one we'll import another Library uh as one of our dependencies which is a very common python library for networks known as Network X right so the typical way you import Network X is import Network X as NX and then we'll run that okay we then have our helper functions which now consist of get distance flattened geometric mean which we built and those two we built in our last session and then our resource class is Sugar and Spice we also have our trade reagent class which is probably our longest class that has our agents maneuver and trade then we have our sugar Escape model where instantiate our model and this is where we also create an instance of our data collector which is right now collecting bottle reporters and we then call one instance of our sugarscape and then run it to collect agent level data now we're going to go back to ourself.data collector attribute okay and we're going to add in the keywords to differentiate between model reporters in agent reporters as you can see here we're doing Mesa dot data collector which calls data collection.py file which you can see in Mason's GitHub link or your local install version and we just add the keyword model underscore reporters this then takes as its parameter the dictionary will be built in our last lesson which collects the number of Traders our trade volume and the price so then after the dictionary at the end of the curly braces or the end of our dictionary parameter we just have to put a comma right and then we'll add the keyword agent reporters so agent underscore reporters agent reporters similar to model reporters will then be a dictionary where the key is effectively the column on our pandas data frame right so we do open curly braces to create a dictionary then we create the key for the data that we want to collect and this will call it Trade Network right so make sure it's in parentheses uh to turn into a string and then that has to equal some attribute that we collect against so again we use the Lambda function and we'll use a which indicates they're collected at the agent level and so and then git trade we're going to make a helper function for this uh and then we're going to pass in the agent object so the model can collect against it right and all that's handled uh by the data collector class that's uh part of Mesa so now that we've done that we need to build the helper function for getting information from our Trader agents challenges that we have different types of agents and the agent collector collects gets every type of agent in this case however as we're trying to look at the trade Network only the trader agent has the attribute trade Partners so we need to make sure we don't get an error by trying to collect trade Partners against sugar or spice so it's a fairly simple function the def that get trade and our helper function second section we pass in an agent object and then we see if that agent object is a Trader agent and if so then we return trade Partners otherwise we return none so if type right agent equals Trader with a capital T So agent class then it's going to be return agent dot partners crochetagent.trade underscore partners now you remember for our previous one this is just the list of unique IDs that we collect from our agents otherwise we just return nothing right so that means it's a sugar spice agent and we can ignore it and then we add some comments we can easier to understand later right says for Asian reporter and data collector and then we're just filtering through our agents uh so that way we return trade Partners the trick here is if we did do this uh we try to collect just trade Partners against everything we get an error when it reaches sugar or spice agent because they don't have uh the attribute trade partners so after our comments are done now we can run the model and start to analyze the data that comes in and as a reminder the trade Partners so how are we going to build out this network the trade Partners uh is just the list of unique agent IDs that we can use to build out our Network because the agent IDs have to be unique all right so we run those make sure we don't have any syntax errors all right run our model class again to make sure you don't have a syntax error and then we run the model as previously this will take you 30 seconds to a minute to run as you run it through 1000 steps of our kind of default model parameters and again the next lesson I will be switching uh to batch Runner we'll run multiple uh different types of models right so what we're going to do is we put on our analyze data we have results from our model data variables so now we're going to create a data frame Called Agent underscore results and then we'll it's very similar to the preview to model reports or it's model.data collector and then git underscore agent underscore vars underscore data frame model vars this will create a pandas data frame that has all the attributes that we loaded into our data collector so we can begin to analyze it and again if you want to see that code you can just go to the your local instance or go to data collector and find the git agent as far as data frame function and then I will show you how the python code is being executed all right so we're putting our comment this cell will retrieve agent level results which depend on your population can get quite large and what you're collecting against and now with this one as because of our function that we did previously all right we have a lot of events right every time it collects against sugar and spice it returned to none uh because those agents don't have the trade Partners attribute all right so we're going to do is we're going to filter those out immediately because we don't need them so we're going to do agent results again and that's going to equal the age of results data frame right and then Open Bracket agent underscore results and an Open Bracket Trade Network which is the key for the value that we had right and then it's going to be dot not null okay now this function comes from pandas where we're just filtering through uh our agent results data frame and any value that is a none uh we're going to filter out all right so we run that get an error right and we get a key error because uh it's trade space network not trade unders okay so I fixed that right and you can see here now we get to get your step and then you have your agent ID and uh sometimes with trading or many times they don't have any agents that they traded with other times um they uh do right so now we got the things we need for our uh Trade Network right as you can see there I forgot to run the results section so I run that cell all right so you're still getting reasonable results we're starting to see more density around one in the price right we know that our bar graph is actually not the best visualization so we can skip that go to our vertical line graph all right so you can see okay we're getting reasonable results uh in our trade volume and now we want to build out uh our uh we want to take that the agent results and now build out a network and run some Network statistics against it right so to do this uh we just first we got a build a network object this is no different than what we did previously where we created a instance of our model object and then ran code against that so per Network X kind of convention new NX dot graph right then I highly recommend you pull up the documentation they've got great documentation with very easy to understand tutorials right an extensive descriptions about uh how you run their code right if in this case we got g equals NX dot graph right so just Big G for a big graph so this is our creating our uh Network instance that we can now fill uh with our network of Traders okay so this is just creating a graph object and now we want to instantiate that graph object with each one of our Trader agents okay so to do this we just have to go through the schedule collect out all the Traders and our random activation by type schedule right and add each of those unique IDs as a node okay so just do uh g dot add underscore nodes underscore from and then list of open parentheses model for Asian model that we created dot schedule that agents underscore by underscore type Open brackets capital T for Trader close brackets dot keeps right so our keys are just the unique agent ID numbers from you try to run that to the gay syntax error other errors right and now that we've created that we want to create an edge list from uh to link those nodes together based off who traded with who all right now uh so to get this information we're going to iterate through the pandas uh data frame rows right so it has essentially like a dictionary or it's the index of the row and then the row itself right in agentresults.it arose then open close a parentheses since it's a pandas function right so we're just iterating through each row then in each one of those rows let's see up here right and then in each one of those rows we're going to pull in that list of INF list of trade Partners uh so that way we could build out the network okay and so we as usual we don't want to say call something if it's not useful so if the length of the row and that's the uh and then the column we want which is Trade Network so row Open brackets Trade Network in parentheses is greater than zero that means that they have that they traded with some other agent then we want to add a link between that between the nodes all right so then we're going to iterate through that list of Agents so before agent in should be Row open bracket trade underscore Network and parentheses right so now we're iterating through the list that came out as a result right if it's uh if it has any length to it greater than zero and then we do add it then we're going to add an edge so from our graph object G we do the network X function add underscore X right and then we'll use the idx which is uh effectively a list where you have zero which is the row and then one which is the agent uh number so that's why I got idx Open brackets one right and then agent right which is the agent number in that list for iterating through so run that my favorite question about what I just said always recommend take a pause right and print uh you know print out those various variables so you can see the underlying data structure that we're using okay now that we've created our Network right we can uh do some uh Network statistics just to see what our Network looks like right so I've just used primitive Network X functions I'm going to look at the node connectivity do we have uh how many networks do we got how connected are we you know what's our average clustering statistic to do the diameter how far does it take to get from one side of the network to another and then we'll look at the global efficiency of our Network which is a metric for how easily information can Traverse across the network these are just some simple Network statistics you could do different ones again if you look at the network X documentation you can pretty much run whichever one is applicable right so you got what network connectivity got one child node everybody's connected to each other right the average clustering is 0.4 right the diameter is six all right and then again any one of these you can look up in network X if I search uh average clustering then I could go the average clustering algorithm it tells me how it's calculated and even gives references uh onto how they uh made the decisions they made to calculate it that way okay it's just an example uh on how to analyze uh the potential Trade Network right another uh typical thing you might do uh is the degree distribution right so what's the degree distribution of our agents right um and so we're gonna do list comprehension again uh and so use D for um degree 4 n comma d uh in g dot degree so now we do the g dot degree function it uh is really two things that come out like key and value your node and then your degree distribution right so you want to iterate through and collect all the degree distributions and then we'll just put that into a histogram so called PLT dot h i s t right and we'll pass in uh our local variable degree this is not right because I did n which is the key and not the value of degree so D for n commodity right now this is this looks right for a degree distribution as you can see it's small numbers of Agents have especially 15 or less right and then if or lots of Agents have 15 or less right that a few agents have a lot of connections uh in the 60s or 70s all right so we gotta sorry get a heavy tail degree distribution of how trading has worked where a lot of agents are trading with a few people and a few agents are trading with a lot of people we can also use their draw function right to kind of get an image of what the network looks like and they have lots of different options for this but this at least shows you the functionality right so you can just go back into the documentation look up draw it'll give you all sorts of different options you could use to make the graph uh you know visualize it the way uh that you would like okay so that represents session 19 where we collect agent level data and start to build out views and run statistics against the Trade Network of our agents right thanks for coming and in our last lesson we'll do patreon or where we do parameter sweeps to see what kind of results we get and run each model multiple times see you next time

### Code

From `Session_19_Data_Collector_Agent.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)

def flatten(list_of_lists):
  '''
  helper function for model datacollector for trade price
  collapses agent price list into one list
  '''
  return [item for sublist in list_of_lists for item in sublist]

def geometric_mean(list_of_prices):
  '''
  find the geometric mean of a list of prices
  '''
  return np.exp(np.log(list_of_prices).mean())

def get_trade(agent):
  '''
  For agent reportes in data collector

  return list of trade partners and None for other agents
  '''
  if type(agent) == Trader:
    return agent.trade_partners
  else: return None
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision
    self.prices = []
    self.trade_partners = []


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0

  def get_trader(self, pos):
      '''
      helper function used in self.trade_with_neighbors()
      '''

      this_cell = self.model.grid.get_cell_list_contents(pos)

      for agent in this_cell:
        if isinstance(agent, Trader):
          return agent


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function

    part 2 self.move()
    self.trade()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form; starting on p. 97 on Growing Artificial Societies
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  def calculate_MRS(self, sugar, spice):
    '''
    Helper function for self.trade()

    Determines what trader agent is needs and can give up
    '''

    return (spice/self.metabolism_spice) / (sugar/self.metabolism_sugar)

  def calculate_sell_spice_amount(self, price):
    '''
    helper function for self.maybe_sell_spice() which is called from
    self.trade()
    '''

    if price >= 1:
      sugar = 1
      spice = int(price)
    else:
      sugar = int(1/price)
      spice = 1
    return sugar, spice

  def sell_spice(self, other, sugar, spice):
    '''
    used in self.maybe_sell_spice()

    exchanges sugar and spice between traders
    '''

    self.sugar += sugar
    other.sugar -= sugar
    self.spice -= spice
    other.spice += spice


  def maybe_sell_spice(self, other, price, welfare_self, welfare_other):
    '''
    helper function for self.trade()
    '''

    sugar_exchanged, spice_exchanged = self.calculate_sell_spice_amount(price)

    # Assess new sugar and spice amount - what if change did occur
    self_sugar = self.sugar + sugar_exchanged
    other_sugar = other.sugar - sugar_exchanged
    self_spice = self.spice - spice_exchanged
    other_spice = other.spice + spice_exchanged

    # double check to ensure agents have resources

    if ((self_sugar <= 0) or
        (other_sugar <=0) or
        (self_spice <= 0) or
        (other_spice <= 0)):
      return False

    # trade criteria #1 - are both agents better off?
    both_agents_better_off = (
        (welfare_self < self.calculate_welfare(self_sugar, self_spice)) and
        (welfare_other < other.calculate_welfare(other_sugar, other_spice)))

    # trade criteria #2 is their mrs crossing
    mrs_not_crossing = self.calculate_MRS(self_sugar, self_spice
                                          ) > other.calculate_MRS(
                                              other_sugar, other_spice
                                          )

    if not (both_agents_better_off and mrs_not_crossing):
      return False

    # criteria met, execute trade
    self.sell_spice(other, sugar_exchanged, spice_exchanged)

    return True


  def trade(self, other):
    '''
    helper function used in trade_with_neighbors()

    other is a trader agent object
    '''

    # sanity check to verify code is working as expected
    assert self.sugar > 0
    assert self.spice > 0
    assert other.sugar > 0
    assert other.spice > 0

    # calculate marginal rate of subsitution in Growing Artificial Socieites p. 101
    mrs_self = self.calculate_MRS(self.sugar, self.spice)
    mrs_other = other.calculate_MRS(other.sugar, other.spice)

    #calculate each agents welfare
    welfare_self = self.calculate_welfare(self.sugar, self.spice)
    welfare_other = other.calculate_welfare(other.sugar, other.spice)

    if math.isclose(mrs_self, mrs_other):
      return

    # calcualte price
    price = math.sqrt(mrs_self*mrs_other)

    if mrs_self > mrs_other:
      # self is a sugar buyer, spice seller
      sold = self.maybe_sell_spice(other, price, welfare_self, welfare_other)
      # no trade - criteria not met
      if not sold:
        return
    else:
      # self is a spice buyer, sugar seller
      sold = other.maybe_sell_spice(self, price, welfare_other, welfare_self)
      # no trade - criteria not met
      if not sold:
        return

    # Capture data
    self.prices.append(price)
    self.trade_partners.append(other.unique_id)

    # continue trading
    self.trade(other)

  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved():
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)

  def trade_with_neighbors(self):
    '''
    Function for trader agents to decide who to trade with in three parts

    1- identify neighbors who can trade
    2- trade (2 sessions)
    3- collect data
    '''

    neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
        self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
    ]

    if len(neighbor_agents) == 0:
      return


    # iterate through traders in neighboring cells and trade
    for a in neighbor_agents:
      if a:
        self.trade(a)

    return
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max

    # initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    # initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)
    # initiate datacollector
    self.datacollector = mesa.DataCollector(
        model_reporters = {"Trader": lambda m: m.schedule.get_type_count(Trader),
         "Trade Volume": lambda m: sum(len(a.trade_partners)
         for a in m.schedule.agents_by_type[Trader].values()),
         "Price": lambda m: geometric_mean(flatten([a.prices for a in m.schedule.agents_by_type[Trader].values()]))},
       agent_reporters = {"Trade Network": lambda a: get_trade(a)}
    )


    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def randomize_traders(self):
    '''
    helper function for self.step()

    puts traders in randomized list for step function
    '''

    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    return trader_shuffle


  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.prices = []
      agent.trade_partners = []
      agent.move()
      agent.eat()
      agent.maybe_die()

    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.trade_with_neighbors()

    self.schedule.steps += 1 #important for data collector to track number of steps

    # collect model level data
    self.datacollector.collect(self)

    #Need to remove excess data, as Mesa does not yet have a datacollection
    #by agent type feature we will for into datacollector to update its data
    #structures
    agent_trades = self.datacollector._agent_records[self.schedule.steps]
    #leverage None aspect of no data in data collector
    agent_trades = [agent for agent in agent_trades if agent[2] is not None]
    #reassign that step in the dictionary with lean trade data
    self.datacollector._agent_records[self.schedule.steps] = agent_trades

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model()
```

<!-- cell 14: markdown -->

> # Analyze Data

<!-- cell 15: code -->

```python
results = model.datacollector.get_model_vars_dataframe()

results
```

<!-- cell 16: code -->

```python
# retrieve agent level results
agent_results = model.datacollector.get_agent_vars_dataframe()

agent_results
```

<!-- cell 17: code -->

```python
# plot number of agents per time step
results.plot(y = "Trader", use_index=True)
```

<!-- cell 18: code -->

```python
# plot trade price per step

y = list(results["Price"])
x = range(1000)

plt.scatter(x,y, s=1)
```

<!-- cell 19: code -->

```python
# Plot trade volume improved

for i in range(1000):
  plt.vlines(i,0,results["Trade Volume"][i])
```

<!-- cell 20: code -->

```python
#  create graph object
G = nx.Graph()

# add agent keys to make initial node set
G.add_nodes_from(list(model.schedule.agents_by_type[Trader].keys()))

# create edge list
for idx, row in agent_results.iterrows():
  if len(row["Trade Network"]) > 0:
    for agent in row["Trade Network"]:
      G.add_edge(idx[1], agent)
```

<!-- cell 21: code -->

```python
print("Connectivity: ", nx.node_connectivity(G), "Clustering: ",
      nx.average_clustering(G), "Efficiency: ", nx.global_efficiency(G))

try:
  print("Diameter: ", nx.diameter(G))
except:
  print("Some traders not connected")
```

<!-- cell 22: code -->

```python
degree = [d for n,d in G.degree()]
plt.hist(degree)
```

<!-- cell 23: code -->

```python
nx.draw(G)
```

---

## Session 20 — Batch Run

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=IRCGJndsgpw |
| Length | 15:18 |
| Video title | Session 20: Batch Run |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+20+Batch+Run.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17339 |
| Notebook | https://github.com/SFIComplexityExplorer/Mesa-ABM-Tutorial/blob/main/Session_20_Batch_Runner.ipynb |

### Transcript

<!-- 2642 words -->

welcome to session 20 of complexity Explorer's Mesa tutorial this in this session we're going to look at batch Runner so that we could do parameter sweeps over a model and see how those parameters may impact the results this represents the last coding session for this tutorial and represents the near completion of this tutorial I hope you enjoyed it but to get started once again either open up your IDE or Google collab instance as usual you want to make sure that your sugar map.txt file is loaded either by mounting your Google Drive or by lowly loading it manually in the folder section then we have our helper functions right which have become four now uh based off data collector and the need to calculate our distance we have our resource classes which consist of sugar and spice then we have our Trader ad agent which is our longest class and involves their functions to maneuver through the landscape and trade then we have our model class where we built out batch runner for the last time we want to do those who want to actually comment out our agent reporters right we're doing this because Google collab only gives you so much RAM and after running this model multiple times uh you'll actually run out of ram if you're collecting your agent reporters this is not an uncommon problem it could typically be solved if you're running on your local machine to saving the disk as you collect your data next you have sugarscape either or we call our model and then we analyze our model right but now we're going to do batch so we're going to create a new section for batch run so we can add a text field and we'll call it batchroad and the analysis uh associated with that and then we'll add a code field we can collapse this back down our data or analyze the data for our signal runs right and now we want to create our batch foot so the way batch would work is you pass in a dictionary of parameters for all the parameters you want to run through your model so you capture multiple variations and you can understand how your model functions under different conditions well although this is somewhat necessary for this one for this model just to demonstrate batch front's capability you can pass in single parameters right so we're going to keep the width and height the same add 50.

because of how we use the keyword arguments again this is unnecessary all right but this does demonstrate patch Runners kind of processes so width as a keyword 50 height as a keyword 50 which is consistent with our keyword arguments in our sugar Escape g1mt model class and then we're going to start to create some variants with our other parameters right so Vision Med uh our vision underscore Min is one of our parameters uh and we're going to use a rate range function and go from one to three so this will actually run the model with a minimum vision of one and a minimum vision of two based off how Python's range function works and the next we could look at is the metabolism Mass right so how much sugar spice agents burn at any given step and for this one we'll lower it and you could pass in other things like a list I'll keep you these uh parameter sweeps potentially small just to demonstrate how to do it uh and then save some time in the runtime that it takes right so for Matt metabolism Max right instead of doing like say a continuous list of one through a hundred you could actually just put in specific values that we want so we're going to do three or five so we're gonna put a list that does three and five so really just any iterator uh you can use in order to passive parameters again these are being kept intentionally small I usually do a lot more but for the interest of time it's easier to demonstrate with just four variations okay then well we're going to do we gotta get the results that come out so we'll call this results underscore batch and then that will equal Mesa dot batch underscore Run Okay so again Mesa dot batch underscore run and then batch run takes a couple parameters so the first we got to pass in our model class so that's sugarscape G1 Mt right and then we use a keyword argument parameters and that's going to equal params which is the name of the dictionary we just built and then it has some other keyword arguments in this case we do iterations equals one right the number of processes equals one pretty sure even if you change this it doesn't matter uh ball accounts it seems that uh Google collab locks you down to one um uh One processor right and then data underscore collection underscore period right uh so that also defaults to one all right uh but we're going to put that as a keyword argument is one two uh and then whether or not to display uh progress and this will show a progress bar of how many runs uh that you've run out of uh out of your model okay now if you want a pretty good overview or an overview of each of the keyword arguments for batch run if you go to the Mesa tutorial batch run uh it walks you through what each one is and what each one uh what its default is right so these are the various parameters that go into batch run uh that you can use uh now one thing we're going to have to add uh is that because you how you terminate the program because you might get a model that runs forever right you'll see that just a second right so we run this all right and we get an error I would get an error because uh it had the sugarscape model has no attribute product right so this is just a feature that you have to have uh in order to um uh tell the model when to stop because some models could run forever unless it's got some kind of stopping function right uh and so that is part of this we can switch self.running to faults right and it'll stop it so we go into our initialization of the model and we just add an attribute so self dot running equals true run that and I could collapse this back down and then we run the model okay and so now it's start to go each one of these I think takes about uh 90 or so seconds um and so we will fast forward through time as you watch this okay so as you can see got through uh 75 percent so three of my four right based off all the combinations between Vision Min and Metabolism Max and now my model is completed okay so now that my model's completed now we analyze the results so you're going to add a code cell of the different variations and then we're just going to do uh you know code very similar to what we did before but just to be thorough we'll show you what results for batch run look like uh and or uh so you can understand how to analyze those results now in this case uh we're going to import pandas this PD kind of per standard pandas convention because we want to use our own pandas data frame all right so if I called this um without uh without doing it without importing pandas I would have got an error right so we'll create a pandas data frame uh based off results dot batch right because that's actually in a dictionary at this point now you can see what that looks like all right uh that creates our um uh our data frame for all our model runs so you get the Run ID the iteration number right uh and the step for that iteration and this would be the same if you did an agent reporter right uh but you do got to converted from the dictionary form uh into the uh into a data frame if you want to use the data frame right now typically you do more than one iteration uh but just in the sake of time we're only gonna do one iteration all right now you can see you have the standard features like trade volume uh price uh et cetera right so now I want to analyze that uh and see how our results differ over time so first let's make sure our kind of foundational result that the price equilibrium uh really kind of converges towards one is still in place so to do this we'll just do our standard scatter plot and our x-axis will be uh the number of steps right which is 0 through 999 uh four different times because we ran four different variations which you can look at the Run ID right above that zero to three all right those are four variations that we've made so results underscore death right with the X uh access being stat all right and then the y-axis will be average price or correction would just be price which is the geometric mean of the uh of all the trades that occur right so fairly simple I'm going to add the size of attribute otherwise our dots are too big and I'll just make this a 0.75 right so PLT dot scatter we run that sure enough uh we go from less dense to more and more dense uh around one as the price uh is a price converge towards one for the predictive model so that's good we ran a bunch of different very we ran some different variations uh and we're getting the main result uh that is validated uh via economic theory typically with parameter sweeps like this we want to explore different variations to see how those impact the model right so we could do uh this is again just using kind of pandas functions in order to filter out the results we want and then plot them to see uh with the impact of different parameters so I call this one results underscore explore right that's going to equal results underscore DF right and then we've got a cut down what we're looking at right so these are different parameters that we use Vision one or two metabolism three or five um and so we'll do metabolism Max and we will now just look at instead of the five uh we'll look at the three right so if this column equals three they're essentially creating a new data frame called results Explorer where we only have metabolism the runs where metabolism Max equals uh three so here's that result you can see it went from four thousand rows to two thousand rows we essentially cut our results in half okay all right it's easy to change this to whatever parameter you want right so if we change it to five that's fine uh and then you could do different columns like since we did Vision you can change your vision bin from one to two uh and explore those results all right so let's see what kind of impact it had all right we could just do the same uh be a little bit lazy here we just do this the same function we'll do plt.scatter but instead of results DF we'll do results underscore explore here right and see what happens okay so that unsurprisingly we get the exact result we expected because it's so resilient uh so now let's look at something that actually does change uh which would be the amount of agents that survive right so uh same kind of dynamic plt.plot results underscore explore right uh the x is going to be always going to or consistently the step function will be our X then results uh underscore explore right in this kit time we're going to say the Y is going to be the number of Traders okay uh so from our uh our kind of cut down we get this result and that straight line uh at a negative one slope it looks like is seems very unusual right so what's happening here well you just got to be careful because of how uh the data is being interpreted right where uh we have all the steps uh you know zero through a thousand and all the Traders right and they can cross uh iterations right across run IDs right so that's what I get that line is it tries to figure out what exactly you want to plot all right so um another way to do this then if you want to see okay what's the difference between each of these uh various runs and the impacts of the parameters that it uh that I had and in this case for Trader um for the number of traders that survived all right we could just iterate through uh the Run IDs right it should be 4 I uh and then this is uh in the number of iterations that we had which is four right so based off the different parameters we ended up with four iterations that's kind of automatically calculated uh by Mesa when you do patch Runner so before I uh in range three you're in zero to three uh actually I have to add that to four but and then we want to cut uh we essentially want to make a data frame for each of those variations so just like we uh previously uh cut it down to results explore all right we'll just uh pass that I as a parameter right to pull out the specific um I run iteration that we want right to be results underscore DF and then the column we're concerned about uh which is run ID right so run capital I lowercase D and that's going to equal I right so we're just iterating through that and then we'll make a plot of each of those and see how it works it's actually before all right so zero to three on the way python range works is this will take us to three right we then are essentially make a little data frame uh from each of the subsections and then we get one plot because I did equals one and not equals I so I gotta change this to equals I and we run it there we go we get our four parameters right where based off the metabolism and vision changes you get vastly different um vastly different ancient survivals but they also they all have a signature similar signature uh in their curve right so this then is how you kind of set up batch run where you create a dictionary of parameters right we did a very small one just for the sake of time and then you analyze it in a similar faction uh just to be careful that sometimes uh what you the results you might think you're gonna get isn't the results you're gonna all right so with that we have now concluded session 20 batra and this is the last coding session and the next session we'll wrap it up and you'll have completed all of complex explorers Mesa tutorial thanks for all the time and energy you spent into this and I hope it's been helpful for you

### Code

From `Session_20_Batch_Runner.ipynb`.

<!-- cell 1: markdown -->

> # Import Dependencies

<!-- cell 2: code -->

```python
from google.colab import drive
drive.mount('/content/drive')


try:
  import mesa
except:
  !pip install mesa --quiet
import mesa
import numpy as np
import math
import matplotlib.pyplot as plt
import networkx as nx

%matplotlib inline
```

<!-- cell 3: markdown -->

> # Helper Functions

<!-- cell 4: code -->

```python
def get_distance(pos_1, pos_2):
  '''
  Calculate the Euclidean distance between two positions

  used in trade.move()
  '''

  x1, y1 = pos_1
  x2, y2 = pos_2
  dx = x1 - x2
  dy = y1 - y2
  return math.sqrt(dx**2 + dy**2)

def flatten(list_of_lists):
  '''
  helper function for model datacollector for trade price
  collapses agent price list into one list
  '''
  return [item for sublist in list_of_lists for item in sublist]

def geometric_mean(list_of_prices):
  '''
  find the geometric mean of a list of prices
  '''
  return np.exp(np.log(list_of_prices).mean())

def get_trade(agent):
  '''
  For agent reportes in data collector

  return list of trade partners and None for other agents
  '''
  if type(agent) == Trader:
    return agent.trade_partners
  else: return None
```

<!-- cell 5: markdown -->

> # Resource Classes

<!-- cell 6: code -->

```python
class Sugar(mesa.Agent):
  """
  Sugar:
  - contains an amount of sugar
  - grows 1 amount of sugar at each turn
  """

  def __init__(self, unique_id, model, pos, max_sugar):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_sugar
    self.max_sugar = max_sugar


  def step(self):
    '''
    Sugar growth function, adds one unit of sugar each step until
    max amount
    '''
    self.amount = min([self.max_sugar, self.amount+1])
```

<!-- cell 7: code -->

```python
class Spice(mesa.Agent):
  """
  Spice:
  - contains an amount of spice
  - grows 1 amount of spice at each turn
  """

  def __init__(self, unique_id, model, pos, max_spice):
    super().__init__(unique_id, model)
    self.pos = pos
    self.amount = max_spice
    self.max_spice = max_spice

  def step(self):
    '''
    Spice growth function, adds one unit of spice each step until
    max amout
    '''
    self.amount = min([self.max_spice, self.amount+1])
```

<!-- cell 8: markdown -->

> # Trader Agent

<!-- cell 9: code -->

```python
class Trader(mesa.Agent):
  """
  Trader:
  - has a metabolism of sugar and spice
  - harvest and trade sugar and spice to survive
  """


  def __init__(self, unique_id, model, pos, moore=False, sugar=0,
               spice=0, metabolism_sugar=0, metabolism_spice=0,
               vision=0):
    super().__init__(unique_id, model)
    self.pos = pos
    self.moore = moore
    self.sugar = sugar
    self.spice = spice
    self.metabolism_sugar = metabolism_sugar
    self.metabolism_spice = metabolism_spice
    self.vision = vision
    self.prices = []
    self.trade_partners = []


  def get_sugar(self, pos):
    '''
    used in self.get_sugar_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Sugar:
        return agent
    return None


  def get_sugar_amount(self,pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    sugar_patch = self.get_sugar(pos)
    if sugar_patch:
      return sugar_patch.amount
    return 0

  def get_spice(self, pos):
    '''
    used in self.get_spice_amount()
    '''

    this_cell = self.model.grid.get_cell_list_contents(pos)
    for agent in this_cell:
      if type(agent) is Spice:
        return agent
    return None

  def get_spice_amount(self, pos):
    '''
    used in self.move() as part of self.calculate_welfare()
    '''

    spice_patch = self.get_spice(pos)
    if spice_patch:
      return spice_patch.amount
    return 0

  def get_trader(self, pos):
      '''
      helper function used in self.trade_with_neighbors()
      '''

      this_cell = self.model.grid.get_cell_list_contents(pos)

      for agent in this_cell:
        if isinstance(agent, Trader):
          return agent


  def is_occupied_by_other(self,pos):
    '''
    helper function part 1 of self.move()
    '''

    if pos == self.pos:
      # agent's position is considered unoccupied as agent can stay there
      return False
    # get contents of each cell in neighborhood
    this_cell = self.model.grid.get_cell_list_contents(pos)
    for a in this_cell:
      # see if occupied by another agent
      if isinstance(a, Trader):
        return True
    return False

  def calculate_welfare(self, sugar, spice):
    '''
    helper function

    part 2 self.move()
    self.trade()
    '''

    # calculate total resources
    m_total = self.metabolism_sugar + self.metabolism_spice
    # Cobb-Douglas functional form; starting on p. 97 on Growing Artificial Societies
    return sugar**(self.metabolism_sugar/m_total) * spice**(
        self.metabolism_spice/m_total)


  def is_starved(self):
    '''
    Helper function for self.maybe_die()
    '''

    return (self.sugar <= 0) or (self.spice <= 0)

  def calculate_MRS(self, sugar, spice):
    '''
    Helper function for
    - self.trade()
    - self.maybe_sell_spice()

    Determines what trader agent is needs and can give up
    '''

    return (spice/self.metabolism_spice) / (sugar/self.metabolism_sugar)

  def calculate_sell_spice_amount(self, price):
    '''
    helper function for self.maybe_sell_spice() which is called from
    self.trade()
    '''

    if price >= 1:
      sugar = 1
      spice = int(price)
    else:
      sugar = int(1/price)
      spice = 1
    return sugar, spice

  def sell_spice(self, other, sugar, spice):
    '''
    used in self.maybe_sell_spice()

    exchanges sugar and spice between traders
    '''

    self.sugar += sugar
    other.sugar -= sugar
    self.spice -= spice
    other.spice += spice


  def maybe_sell_spice(self, other, price, welfare_self, welfare_other):
    '''
    helper function for self.trade()
    '''

    sugar_exchanged, spice_exchanged = self.calculate_sell_spice_amount(price)

    # Assess new sugar and spice amount - what if change did occur
    self_sugar = self.sugar + sugar_exchanged
    other_sugar = other.sugar - sugar_exchanged
    self_spice = self.spice - spice_exchanged
    other_spice = other.spice + spice_exchanged

    # double check to ensure agents have resources

    if ((self_sugar <= 0) or
        (other_sugar <=0) or
        (self_spice <= 0) or
        (other_spice <= 0)):
      return False

    # trade criteria #1 - are both agents better off?
    both_agents_better_off = (
        (welfare_self < self.calculate_welfare(self_sugar, self_spice)) and
        (welfare_other < other.calculate_welfare(other_sugar, other_spice)))

    # trade criteria #2 is their mrs crossing
    mrs_not_crossing = self.calculate_MRS(
        self_sugar, self_spice
    ) > other.calculate_MRS(other_sugar, other_spice)

    if not (both_agents_better_off and mrs_not_crossing):
      return False

    # criteria met, execute trade
    self.sell_spice(other, sugar_exchanged, spice_exchanged)

    return True


  def trade(self, other):
    '''
    helper function used in trade_with_neighbors()

    other is a trader agent object
    '''

    # sanity check to verify code is working as expected
    assert self.sugar > 0
    assert self.spice > 0
    assert other.sugar > 0
    assert other.spice > 0

    # calculate marginal rate of subsitution in Growing Artificial Socieites p. 101
    mrs_self = self.calculate_MRS(self.sugar, self.spice)
    mrs_other = other.calculate_MRS(other.sugar, other.spice)

    #calculate each agents welfare
    welfare_self = self.calculate_welfare(self.sugar, self.spice)
    welfare_other = other.calculate_welfare(other.sugar, other.spice)

    if math.isclose(mrs_self, mrs_other):
      return

    # calcualte price
    price = math.sqrt(mrs_self*mrs_other)

    if mrs_self > mrs_other:
      # self is a sugar buyer, spice seller
      sold = self.maybe_sell_spice(other, price, welfare_self, welfare_other)
      # no trade - criteria not met
      if not sold:
        return
    else:
      # self is a spice buyer, sugar seller
      sold = other.maybe_sell_spice(self, price, welfare_other, welfare_self)
      # no trade - criteria not met
      if not sold:
        return

    # Capture data
    self.prices.append(price)
    self.trade_partners.append(other.unique_id)

    # continue trading
    self.trade(other)

  ######################################################################
  #                                                                    #
  #                      MAIN TRADE FUNCTIONS                          #
  #                                                                    #
  ######################################################################


  def move(self):
    '''
    Function for trader agent to identify optimal move for each step in 4 parts
    1 - identify all possible moves
    2 - determine which move maximizes welfare
    3 - find closest best option
    4 - move
    '''

    # 1. identify all possible moves

    neighbors = [i
                 for i in self.model.grid.get_neighborhood(
                   self.pos, self.moore, True, self.vision
                 ) if not self.is_occupied_by_other(i)]

    # 2. determine which move maximizes welfare

    welfares = [
        self.calculate_welfare(
            self.sugar + self.get_sugar_amount(pos),
            self.spice + self.get_spice_amount(pos))
        for pos in neighbors
    ]

    # 3. Find closest best option

    # find the highest welfare in welfares
    max_welfare = max(welfares)
    # get the index of max welfare cells
    candidate_indices = [i for i in range(len(welfares))
                        if math.isclose(welfares[i], max_welfare)]

    # convert index to positions of those cells
    candidates = [neighbors[i] for i in candidate_indices]

    min_dist = min(get_distance(self.pos, pos) for pos in candidates)

    final_candidates = [ pos for pos in candidates
                       if math.isclose(get_distance(self.pos, pos), min_dist, rel_tol=1e-02
                                       )]
    self.random.shuffle(final_candidates)

    # 4. Move Agent
    self.model.grid.move_agent(self, final_candidates[0])

  def eat(self):
    # get sugar
    sugar_patch = self.get_sugar(self.pos)

    if sugar_patch:
        self.sugar += sugar_patch.amount
        sugar_patch.amount = 0
    self.sugar -= self.metabolism_sugar

    # get_spice
    spice_patch = self.get_spice(self.pos)

    if spice_patch:
        self.spice += spice_patch.amount
        spice_patch.amount = 0
    self.spice -= self.metabolism_spice

  def maybe_die(self):
    '''
    Function to remove Traders who have consumed all their sugar or spice
    '''

    if self.is_starved():
      self.model.grid.remove_agent(self)
      self.model.schedule.remove(self)

  def trade_with_neighbors(self):
    '''
    Function for trader agents to decide who to trade with in three parts

    1- identify neighbors who can trade
    2- trade (2 sessions)
    3- collect data
    '''

    neighbor_agents = [self.get_trader(pos) for pos in self.model.grid.get_neighborhood(
        self.pos, self.moore, False, self.vision) if self.is_occupied_by_other(pos)
    ]

    if len(neighbor_agents) == 0:
      return


    # iterate through traders in neighboring cells and trade
    for a in neighbor_agents:
      if a:
        self.trade(a)

    return
```

<!-- cell 10: markdown -->

> # Model Class

<!-- cell 11: code -->

```python
class SugarscapeG1mt(mesa.Model):
  """
  Manager class to run Sugarscape with Traders
  """


  def __init__(self, width=50,height=50, initial_population=200,
               endowment_min=25, endowment_max=50, metabolism_min=1,
               metabolism_max=5, vision_min=1, vision_max=5):

    #Initiate width and heigh of sugarscape
    self.width = width
    self.height = height
    #Initiate population attributes
    self.initial_population = initial_population
    self.endowment_min = endowment_min
    self.endowment_max = endowment_max
    self.metabolism_min = metabolism_min
    self.metabolism_max = metabolism_max
    self.vision_min = vision_min
    self.vision_max = vision_max
    self.running = True

    # initiate activation schedule
    self.schedule = mesa.time.RandomActivationByType(self)
    # initiate mesa grid class
    self.grid = mesa.space.MultiGrid(self.width, self.height, torus=False)
    # initiate datacollector
    self.datacollector = mesa.DataCollector(
        model_reporters = {"Trader": lambda m: m.schedule.get_type_count(Trader),
         "Trade Volume": lambda m: sum(len(a.trade_partners)
         for a in m.schedule.agents_by_type[Trader].values()),
         "Price": lambda m: geometric_mean(flatten([a.prices for a in m.schedule.agents_by_type[Trader].values()]))},
       agent_reporters = {"Trade Network": lambda a: get_trade(a)}
    )


    #read in landscape file from supplmentary material
    sugar_distribution =np.genfromtxt("/content/drive/MyDrive/sugar-map.txt")
    spice_distribution = np.flip(sugar_distribution, 1)

    agent_id = 0
    for _,(x,y) in self.grid.coord_iter():
      max_sugar = sugar_distribution[x,y]
      if max_sugar > 0:
        sugar = Sugar(agent_id, self, (x,y), max_sugar)
        self.schedule.add(sugar)
        self.grid.place_agent(sugar, (x,y))
        agent_id += 1

      max_spice = spice_distribution[x,y]
      if max_spice > 0:
        spice = Spice(agent_id, self, (x,y), max_spice)
        self.schedule.add(spice)
        self.grid.place_agent(spice, (x,y))
        agent_id += 1

    for i in range(self.initial_population):
      #get agent position
      x = self.random.randrange(self.width)
      y = self.random.randrange(self.height)
      #see Growing Artificial Societies p. 108 for initialization
      #give agents initial endowment
      sugar = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      spice = int(self.random.uniform(self.endowment_min, self.endowment_max+1))
      #give agents initial metabolism
      metabolism_sugar = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      metabolism_spice = int(self.random.uniform(self.metabolism_min, self.metabolism_max+1))
      #give agents vision
      vision = int(self.random.uniform(self.vision_min, self.vision_max+1))
      #create Trader object
      trader = Trader(agent_id,
                      self,
                      (x,y),
                      moore = False,
                      sugar = sugar,
                      spice = spice,
                      metabolism_sugar = metabolism_sugar,
                      metabolism_spice = metabolism_spice,
                      vision = vision)
      #place agent
      self.grid.place_agent(trader, (x,y))
      self.schedule.add(trader)
      agent_id += 1

  def randomize_traders(self):
    '''
    helper function for self.step()

    puts traders in randomized list for step function
    '''

    trader_shuffle = list(self.schedule.agents_by_type[Trader].values())
    self.random.shuffle(trader_shuffle)

    return trader_shuffle


  def step(self):
    '''
    Unique step function that does staged activation of sugar and spice
    and then randomly activates traders
    '''
    # step Sugar agents
    for sugar in self.schedule.agents_by_type[Sugar].values():
      sugar.step()

    # step Spice agents
    for spice in self.schedule.agents_by_type[Spice].values():
      spice.step()

    # step trader agents
    # to account for agent death and removal we need a seperate data strcuture to
    # iterate
    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.prices = []
      agent.trade_partners = []
      agent.move()
      agent.eat()
      agent.maybe_die()

    trader_shuffle = self.randomize_traders()

    for agent in trader_shuffle:
      agent.trade_with_neighbors()

    self.schedule.steps += 1 #important for data collector to track number of steps

    # collect model level data
    self.datacollector.collect(self)

    #Need to remove excess data, as Mesa does not yet have a datacollection
    #by agent type feature we will for into datacollector to update its data
    #structures
    agent_trades = self.datacollector._agent_records[self.schedule.steps]
    #leverage None aspect of no data in data collector
    agent_trades = [agent for agent in agent_trades if agent[2] is not None]
    #reassign that step in the dictionary with lean trade data
    self.datacollector._agent_records[self.schedule.steps] = agent_trades

  def run_model(self, step_count=1000):

    for i in range(step_count):
      self.step()
```

<!-- cell 12: markdown -->

> # Run Sugarscape

<!-- cell 13: code -->

```python
model = SugarscapeG1mt()
model.run_model()
```

<!-- cell 14: markdown -->

> # Analyze Data

<!-- cell 15: code -->

```python
results = model.datacollector.get_model_vars_dataframe()

results
```

<!-- cell 16: code -->

```python
# retrieve agent level results
agent_results = model.datacollector.get_agent_vars_dataframe()
# filter out Nones from non-trader agents
agent_results
```

<!-- cell 17: code -->

```python
# plot number of agents per time step
results.plot(y = "Trader", use_index=True)
```

<!-- cell 18: code -->

```python
# plot trade price per step

y = list(results["Price"])
x = range(1000)

plt.scatter(x,y, s=1)
```

<!-- cell 19: code -->

```python
# Plot trade volume improved

for i in range(1000):
  plt.vlines(i,0,results["Trade Volume"][i])
```

<!-- cell 20: code -->

```python
#  create graph object
G = nx.Graph()

# add agent keys to make initial node set
G.add_nodes_from(list(model.schedule.agents_by_type[Trader].keys()))

# create edge list
for idx, row in agent_results.iterrows():
  if len(row["Trade Network"]) > 0:
    for agent in row["Trade Network"]:
      G.add_edge(idx[1], agent)
```

<!-- cell 21: code -->

```python
print("Connectivity: ", nx.node_connectivity(G), "Clustering: ",
      nx.average_clustering(G), "Efficiency: ", nx.global_efficiency(G))

try:
  print("Diameter: ", nx.diameter(G))
except:
  print("Some traders not connected")
```

<!-- cell 22: code -->

```python
degree = [d for n,d in G.degree()]
plt.hist(degree)
```

<!-- cell 23: code -->

```python
nx.draw(G)
```

<!-- cell 24: markdown -->

> # Batch Run and Analysis

<!-- cell 25: code -->

```python
params = { "width": 50, "height": 50,
          "vision_min": range(1,3),
          "metabolism_max": [3,5]}

results_batch = mesa.batch_run(
    SugarscapeG1mt,
    parameters = params,
    iterations = 1,
    number_processes = 1,
    data_collection_period = 1,
    display_progress = True
)
```

<!-- cell 26: code -->

```python
import pandas as pd

results_df = pd.DataFrame(results_batch)
results_df
```

<!-- cell 27: code -->

```python
plt.scatter(results_df["Step"], results_df["Price"], s=0.75)
```

<!-- cell 28: code -->

```python
results_explore = results_df[results_df["metabolism_max"]== 3]
results_explore
```

<!-- cell 29: code -->

```python
plt.scatter(results_explore["Step"], results_explore["Price"], s=0.75)
```

<!-- cell 30: code -->

```python
for i in range(4):
  results_explore = results_df[results_df["RunId"] ==i]
  plt.plot(results_explore["Step"], results_explore["Trader"])
```

<!-- cell 31: code -->

```python
#Agent results
G = nx.Graph()

trade = results_df.dropna(subset=["Trade Network"])
# add agent keys to make initial node set
G.add_nodes_from(list(trade["AgentID"].unique()))

# create edge list
for idx, row in trade.iterrows():
    if len(row["Trade Network"]) > 0:
        for agent in row["Trade Network"]:
            G.add_edge(row["AgentID"], agent)
```

<!-- cell 32: code -->

```python
#Get some statistics

print(f"Node Connectivity {nx.node_connectivity(G)}")
print(f"Average Clustering {nx.average_clustering(G)}")
print(f"Global Efficiency {nx.global_efficiency(G)}")
```

<!-- cell 33: code -->

```python
#Plot a histogram of number of links

degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
degree_sequence = [d for n, d in G.degree()]
plt.hist(degree_sequence)
```

<!-- cell 34: code -->

```python
# Plot network
nx.draw(G)
```

---

## Session 21 — Conclusion

| | |
|---|---|
| YouTube | https://www.youtube.com/watch?v=JeqhJuUmqy4 |
| Length | 1:02 |
| Video title | Session 21: Conclusion |
| MP4 (direct) | https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/Videos/Session+21+Conclusion.mp4 |
| Lesson page | https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa/segments/17340 |

### Transcript

<!-- 158 words -->

congratulations you successfully completed your complexity Explorer Mesa tutorial we hope along the way you learned a lot about Mesa agent-based modeling and some things about python as well as discussed in the lectures every session is available in a Jupiter notebook in addition to the completed model and Dot Pi files is available through mesa's example repository in the file sugarscape underscore G1 Mt Mesa is an open source project and as mentioned is successful on GitHub being an open source project has been built by Community contributions since 2015. contributions are made by people with deep expertise in programming and or agent-based modeling but also individuals just getting started we hope that you will not only use Mesa in your research but as you identify improvements that could be made you will join us in mesa's forums to discuss and develop them we look forward to seeing you and you your participation in the Mesa ecosystem

### Code

*No notebook for this session — it is lecture, demo or discussion only.*

---

## Appendix — course-wide notes for a scriptwriter

**The model in one paragraph.** Sugarscape-with-Traders is a grid world where each cell
holds a quantity of two resources, *sugar* and *spice*. Agents (traders) hold sugar and
spice, have a metabolism that burns each resource every step, can see a limited distance,
and move toward the cell that best satisfies their needs. Traders who meet on the same
cell trade: each has a marginal rate of substitution (MRS) between the two goods, and
they exchange until no further mutually beneficial trade exists. Epstein & Axtell used it
to grow trade, prices and wealth inequality out of individual behaviour.

**Concept order the course follows.**

| Phase | Sessions | What gets built |
|-------|----------|-----------------|
| Setup | 1–2 | Mesa, the model, the goal |
| World | 3–6 | Colab, `mesa.Model`, the grid from `sugarmap.txt`, `CellAgent` |
| Population | 7–8 | Trader agents, sugar/spice endowment, metabolism, step functions |
| Movement | 9–12 | Neighbourhood lookup, welfare ranking, moving to the best cell |
| Consumption | 13 | `eat()` and starvation |
| Trade | 14–17 | Finding partners, MRS, price, executing the swap |
| Measurement | 18–20 | `DataCollector` at model and agent level, `batch_run` |
| Wrap-up | 21 | What to take away |

**Mesa API surface used across the course** (great checklist for an explainer video):

```text
mesa.Model            model container, .grid, .schedule, .datacollector
mesa.agent.Agent      base agent, .model, .pos, .unique_id
mesa.space.*          MultiGrid / PropertyLayer, .get_neighborhood, .move_agent
mesa.time.*           BaseScheduler / RandomActivation, .add, .step
mesa.DataCollector    model_reporters, agent_reporters, .collect, .get_model_vars_dataframe
mesa.batch_run        parameter sweeps -> pandas DataFrame
mesa.visualization    SolaraViz / browser renderer
```

**Note on Mesa versions.** The course was recorded against an older Mesa (the
`mesa.space.MultiGrid` + `BaseScheduler` era). Current Mesa (3.x) renamed and reshaped
much of this — `mesa.space` → `mesa.discrete_space`, `BaseScheduler` →
`mesa.time.DiscreteTime`, `CellAgent` → `Agent` with `Cell` neighbours. If the script
teaches *current* Mesa, flag the differences per session instead of repeating the
recorded API blindly.
