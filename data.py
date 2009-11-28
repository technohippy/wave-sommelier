from google.appengine.ext import db
from extension import Extension

def StoreData():
  Extension(
    type='gadget',
    title="""LuckyYou""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=75023&img_type=screenshot'),
    desc="""This gadget lets you bet money of a number, and win money if that number shows up after 30 seconds. (Fake money only).""",
    gadgetXml='http://www.voizle.com/luckyyou.xml',
    techDesc="""
""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Exporty""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=75018&img_type=screenshot'),
    desc="""Exports the root blip of a Wave to a static page on App Engine. Note: If the original Wave isn't public, it tries to authenticate the user by assuming their username maps to their Google login username.""",
    robotAddr='exporty-bot@appspot.com',
    techDesc="""Demonstrates using the App Engine datastore to save information about Waves.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Rating Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=74011&img_type=screenshot'),
    desc="""A wave robot that allows participants to rate blips.""",
    robotAddr='rating-bot@appspot.com',
    techDesc="""Uses Form elements and the FORM_BUTTON_CLICKED event.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Buddy Robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=73031&img_type=screenshot'),
    desc="""This robot helps the users to reference key words to Wikipedia and create Mathematical equations (using LaTeX) automatically and in real time, while communicating with other users.""",
    robotAddr='ozobuddyrobo@appspot.com',
    techDesc="""Shows:

 Handling Blips on DOCUMENT_CHANGED Event and BLIP_SUBMITTED
Usage of TextView object.
Usage of Annotations (for Hyper Links)
Usage of Image (to show Image URLs)
Real-time parsing of messages from the Blip


More info http://ozaaazo.appspot.com/
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Wave Linker""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=72033&img_type=screenshot'),
    desc="""Links selected text to first result on Google.""",
    robotAddr='wavelinker@appspot.com',
    techDesc="""Shows how to use annotateSelection with a custom named key, and then find that annotation with the robot.""",
    apis=["Robots","Installer"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Poll Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=72028&img_type=screenshot'),
    desc="""Features the ability to add/remove options, set votes per participant, and embed the result as a chart.""",
    gadgetXml='http://wave.samuirai.de/poll.xml',
    techDesc="""Uses the Google Charts API.""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Annoty""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=72023&img_type=thumbnail'),
    desc="""Annoty the annotation bot.

Annoty replaces regexps with annotations. It has static rules, as well as rules added by users of a Wave.""",
    robotAddr='annoty@appspot.com',
    techDesc="""Demonstrates the use of SetTextInRange, placing Annotations and using the appengine datastore to store Wave data.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""CrazyMath""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=73015&img_type=screenshot'),
    desc=""""CrazyMath" as the name suggested is a game developed in JavaScript which involves doing mathematical calculation and the charisma lies in who does it the quickest. "CrazyMath" offers 3 increasing levels of difficulties viz. Beginners, intermediate and Expert. 
Powered by http://www.voizle.com
Google Code Project : http://u.voizle.com/qkztn
Live demo : http://u.voizle.com/crazymathlive""",
    gadgetXml='http://www.voizle.com/crazymath-U.xml',
    techDesc="""
""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""List gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=73005&img_type=screenshot'),
    desc="""This gadget can be used to manage and display lists in your wavelets. The list is sortable and the headings and columns are customizable (to do). When inviting participants to add to a list, the list gadget forces them to split their entry in fields, enhancing the overall structure of the blip.""",
    gadgetXml='http://list-gadget.googlecode.com/svn/branches/stable/gadget.xml',
    techDesc="""Demonstrates using gadgets.json, and dynamic height.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Jaapy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=72006&img_type=screenshot'),
    desc="""Its a robot that replaces JAAP.NL urls with a gadget showing the details of the property (after the blip is submitted). The gadget can be reduced/expanded. (more to come)

(I used the IMDBotty sample code as a reference but implemented using java only, in stead of python)""",
    gadgetXml='http://jaap-y.appspot.com/servlet/gadget.xml?id=5254977',
    techDesc="""Shows using a JSP to generate the served gadgt XML, fetching webservice data in the servlet, adding gadget from robot.
- pattern matching URLs in the text""",
    apis=["Robots","Gadgets"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Wave Flashcards""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=72003&img_type=screenshot'),
    desc="""Allows the user to add simple flashcard gadgets to their waves. The gadgets are multiplayer-friendly so you could compete with your friends. Custom flashcard decks can be created at the app website.""",
    robotAddr='wave-flashcards@appspot.com',
    techDesc="""Shows a robot creating gadgets, Spring 3.0 as a GAE web interface and serving dynamic gadgets, and avoiding race conditions.""",
    apis=["Robots","Gadgets"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""wave code prettifier""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=70046&img_type=screenshot'),
    desc="""A Gadget that allows automatic syntax highlighting of source code snippets in Google Wave.""",
    gadgetXml='http://wave-code-prettifier.googlecode.com/svn/trunk/prettifier.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Flammard Bible Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=70035&img_type=screenshot'),
    desc="""This is a generic Wave Bible Bot, which supports BibleGateway, ESV, NET and lire.la-bible.net versions.""",
    robotAddr='flammard@appspot.com',
    techDesc="""This bot shows some specific parts of the API: setting text in range in blip (SetTextInRange), using annotations (style, links) in blip (SetAnnotation), dealing with languages ("lang" annotations), using the datastore to record data.
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Roster List""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=70027&img_type=screenshot'),
    desc="""Roster list is a humble gadget for Google \/\/AVE that allows you to search through participants of the current wave.

Project homepage: http://code.google.com/p/wave-roster-list/""",
    gadgetXml='http://wave-roster-list.googlecode.com/svn/trunk/rosterlist.xml',
    techDesc="""Exhibits Gadget capabilities including registering wave.setStateCallback() and wave.setParticipantCallback() handlers, accessing the participant list, and adjusting dynamic height.""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""XO5""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=70023&img_type=screenshot'),
    desc="""Play a variation on tic-tac-toe in Wave.""",
    gadgetXml='http://dizbits.googlecode.com/svn/trunk/xo5/xo5.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()

# error:Url Freezer


  Extension(
    type='gadget',
    title="""Nimbb Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=70016&img_type=screenshot'),
    desc="""Sample gadget to add webcam video recording to any wave.
""",
    gadgetXml='http://service.nimbb.com/GoogleWave/Nimbb.xml',
    techDesc="""Uses setModeCallback to refresh the gadget and use submitDelta/getState to save data in the wave.  Update gadget based on video recording status and check for Host/Viewer object for interacting with Nimbb Player using Javascript.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Rock Paper Scissors Lizard Spock""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=70011&img_type=screenshot'),
    desc="""Lets you play "Rock Paper Scissors Lizard Spock"   against your fellow wavers. Live public wave: https://wave.google.com/wave/#restored:wave:googlewave.com!w%252BEXmHDfzsB""",
    gadgetXml='http://hafstroms.net/wave/rpsls/rpsls.xml',
    techDesc="""
""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Progressy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=71014&img_type=screenshot'),
    desc="""Adds a progress bar to the wave that can be used to show how far a projekt or checkpoint has to go.

Live public wave: https://wave.google.com/wave/#restored:wave:googlewave.com!w%252Blwe_LGHAA""",
    gadgetXml='http://hafstroms.net/wave/progressy/Progressy.xml',
    techDesc="""
""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Messy the Wave Robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=69028&img_type=screenshot'),
    desc="""""",
    robotAddr='Messy is a Google Wave Robot that adds SMS communication to a Wave.',
    techDesc="""Uses robot cron jobs, Java Document Objects (JDO) and shows how to connect with an external API.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""CirBot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=68027&img_type=screenshot'),
    desc="""Converts Serbian cyrillic alphabet into its latin equivalent.  """,
    robotAddr='cirbot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Taskboardy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=68026&img_type=screenshot'),
    desc="""This gadget allows to maintain a taskboard, as used in XP or Scrum. It provides all its basic operatons, such as Create a User Story, a task, delete them, change the statuses of the tasks and assign the tasks.""",
    gadgetXml='http://taskboardy.googlecode.com/svn/trunk/taskboard.xml',
    techDesc="""Shows how to save and get the state of a wave + integration with google ajax libraries.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Urloidy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=69019&img_type=screenshot'),
    desc="""Google wave robot that transforms the urls of a wavelet in short urls.""",
    robotAddr='urloidy@appspot.com',
    techDesc="""Shows using URL fetcher with remote APIs.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Scripty""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=69014&img_type=screenshot'),
    desc="""Evaluate code snippets and respond with the results.""",
    robotAddr='code-wave@appspot.com',
    techDesc="""Robot w/ App Engine functionality, Extension manifest""",
    apis=["Robots","Installer"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""5x5""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=68013&img_type=screenshot'),
    desc="""Simple little puzzle game.""",
    gadgetXml='http://serenity.davep.org/5x5/5x5.xml',
    techDesc="""
""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""trendy-robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=68012&img_type=screenshot'),
    desc="""Replace text like ~~topic1,topic2.  in waves by a trend gadget showing the trends of up to 4 comma-separated topics.""",
    robotAddr='trendy-robot@appspot.com',
    techDesc="""Shows how to insert a dynamically generated gadget into a wave.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""mliawavebot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=68002&img_type=screenshot'),
    desc="""A robot that grabs a random story from http://mylifeisaverage.com or displays the word of the day""",
    robotAddr='mliawavebot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Norton SafeWave""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=67001&img_type=screenshot'),
    desc="""This robot will validate any links typed into a wave conversation.  The links are validated against the Norton SafeWeb API (http://safeweb.norton.com). This will keep waves safe from phishing links, malware sites and infected sites...""",
    robotAddr='nortonwave@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Animal Shogi (Japanese Chess)""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=66003&img_type=screenshot'),
    desc="""Animal Shogi or Dobutsu Shogi is a simplified version of Shogi (Japanese Chess). Though a board is narrow (3x4), its strategy must be deeper than you expect. Let's play with your wave friend. To know more detail about Animal Shogi, please read: http://en.wikipedia.org/wiki/D%C5%8Dbutsu_sh%C5%8Dgi""",
    gadgetXml='http://apps.technohippy.net/animal-shogi/gadget.xml',
    techDesc="""`toJSON' function defined in prototype.js conflicts with Wave API. You should comment out the function to use the library with Wave.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Pick Several""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=66001&img_type=screenshot'),
    desc="""Pick one or more choices from a list (aka approval voting).""",
    gadgetXml='http://www.randomhacks.net/gadgets/pickseveral/pickseveral.gadget.xml',
    techDesc="""This gadget is written using GWT. It shows how to access gadget state from Java, and how to represent state using an asynchronous model and an event bus.""",
    apis=["Gadgets","Installer"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Word Network""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=63098&img_type=screenshot'),
    desc="""http://antimatter15.com/misc/wordassoc/""",
    gadgetXml='http://antimatter15.com/misc/wordassoc/assoc.xml',
    techDesc="""State Changes""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""mywaveid""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=64069&img_type=thumbnail'),
    desc="""Upon being added, creates a blip at the end of the wave, containing the current wave ID, both in "wave" and full url formats. Can just be taken out of the wave afterwards.""",
    robotAddr='mywaveid@appspot.com',
    techDesc="""Shows the use of setAnnotation in Python and retrieval of waveID.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Voicy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=64064&img_type=screenshot'),
    desc="""A voice recording/messaging/sharing system. A new way to share greetings, thoughts and brainstormings with real voice communication.""",
    gadgetXml='http://wave-gadgets.googlecode.com/svn/trunk/voicy/gadget.xml',
    techDesc="""Shows tabs, flash integration, identifying the current viewer and customizing the gadget accordingly (between Host and non-host, giving the host more options), Shows retrieving participant information (name) dynamically, shows communication via postMessage to/from external page in iframe, use of set/get state to dynamically update everyone's message list in realtime, shows the use of persistent data through gadget's prefs.""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Grails Wave plugin samples""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=63094&img_type=screenshot'),
    desc="""Learn how to use the Embed and Robots API with the Grails Wave plugin. Grails is a rapid application development framework for the Java environment.

The plugin home and docs can be found at http://grails.org/plugin/wave and the sample implementation here: http://grails-wave-plugin.appspot.com (Wave Preview account required).""",
    robotAddr='grails-wave-plugin@appspot.com',
    techDesc="""See how you can easily embed a wave with the provided tag library or watch your own robots talking in Groovy.""",
    apis=["Robots","Embed"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Mind Map Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=64007&img_type=screenshot'),
    desc="""A Mindmap gadget which allows for collaborative editing of hierarchical data and ideas, including icons, import and export to freemind, voting and drag & drop.  """,
    gadgetXml='http://cactus-wave.appspot.com/net.brucecooper.mindmapgadget.MindMapGadget/net.brucecooper.mindmapgadget.client.MindMapGadget.gadget.xml',
    techDesc="""Gadgets API, loading state within """,
    apis=["Gadgets","Installer"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Saliery""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=64003&img_type=thumbnail'),
    desc="""GUIDO music notation support for Wave. More information at 
http://saliery-wave.appspot.com""",
    gadgetXml='http://saliery-wave.appspot.com/gadget/score.xml',
    techDesc="""
""",
    apis=["Robots","Gadgets","Installer"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Tricky""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=63022&img_type=screenshot'),
    desc="""Responds to 'trick or treat' requests with a picture of either a trick or a treat.""",
    gadgetXml='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/robots/python/tricky/gadget.xml',
    techDesc="""Shows how to insert a gadget programmatically, stylize an embedded wave, and have the installer put an option in the new wave menu.""",
    apis=["Robots","Gadgets","Embed","Installer"],
    langs=["Python","JavaScript"]
  ).put()

# error:tic-tak-toe


  Extension(
    type='robot',
    title="""Traffic Update Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=63017&img_type=screenshot'),
    desc="""Gives realtime traffic update when the user types Traffic Zipcode.""",
    robotAddr='trafficupdatebot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""News-y""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=63008&img_type=screenshot'),
    desc="""Now you don't have to make your friends (or yourself) search for the news you're sharing =]""",
    robotAddr='newsy-wave@appspot.com',
    techDesc="""Demonstrates text processing within a blip, after blip submission.""",
    apis=["Robots"],
    langs=[""]
  ).put()



  Extension(
    type='invalid',
    title="""Dicy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=63007&img_type=screenshot'),
    desc="""Vesatile dice rolling robot with configuration gadget.""",
    techDesc="""Demonstrates robot-gadget interaction, manipulating robot and gadget state, form elements inside gadget.""",
    apis=["Robots","Gadgets"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Dragon Conquest""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=63003&img_type=screenshot'),
    desc="""'Dragon Conquest' is a cool variation of a classic board game representing good and evil. Play solo or with up to 9 other players in a wave. While this is best played in real time, it is designed to pause when a wave is closed and and resume when it is open.""",
    gadgetXml='http://gadgets.sapplica.com/Dragonconquest/slmalty_new/com.sapplica.apps.slm.client.SLMulty.gadget.xml',
    techDesc="""Effective use of GWT. And collaborative communication.""",
    apis=["Gadgets"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""LaTeXy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=58014&img_type=screenshot'),
    desc="""A simple robot that renders LaTeX code in a wave. I finds code beween $$ and $$ and replaces it with an image generated with the service http://sciencesoft.at/latex/""",
    robotAddr='kevinalle@appspot.com',
    techDesc="""It features a simple robot written in python that searches text as you write (on document_changed) and uses the API to remove the code snippets and insert the appropiate image.

It also features a very simple extension installer""",
    apis=["Robots","Installer"],
    langs=["Python"]
  ).put()



  Extension(
    type='invalid',
    title="""Create New Wave""",
    desc="""APIs: Robots""",
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""WaveToTweeps""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=58013&img_type=screenshot'),
    desc="""Resolves twitter names when an @twitter format is typed, appending a badge to the blip.

To report issues please visit: http://code.google.com/p/wavetotweeps/issues/list""",
    robotAddr='wavetotweeps@appspot.com',
    techDesc="""Demonstrates a fusion of the Twitter API with a Google Wave robot""",
    apis=["Robots","Installer"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""FMyLifeBOT""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=60007&img_type=screenshot'),
    desc="""FmylifeBOT is a robot for Google Wave. When added to a wave it will introduce itself and then wait for a blip(message) starting with FML. Once found it will replace the text FML with a random entry on the popular website fmylife.com. """,
    robotAddr='fmylifebot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""MyTweet on a Wave""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=58009&img_type=screenshot'),
    desc="""A gadget to collaboratively browse twitter streams.""",
    gadgetXml='http://haru1ban-wave.googlecode.com/svn/trunk/twitter/twitter.xml',
    techDesc="""
""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()

# error:Character Entity


  Extension(
    type='robot',
    title="""Translabot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=58005&img_type=screenshot'),
    desc="""Translates a Wave to a selected language.""",
    robotAddr='translabot@appspot.com',
    techDesc="""Shows Robot API, AppEngine (DB + API), and interaction between Gadgets and Robots.""",
    apis=["Robots","Gadgets"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Map Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=59001&img_type=screenshot'),
    desc="""Lets users edit a map together, adding markers and polys with titles and descriptions. Users can also search for addresses and businesses and add those.""",
    gadgetXml='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/gadgets/mappy/mappy.xml',
    techDesc="""Uses setModeCallback to have an edit mode versus a view mode for the gadget, depending on current state of the blip. Uses JQueryUI for dialogs and buttons.""",
    apis=["Gadgets","Installer"],
    langs=[""]
  ).put()



  Extension(
    type='robot',
    title="""Craigslist Searchy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=53002&img_type=screenshot'),
    desc="""Craigslist Searchy is a Google Wave robot that monitors results of a given search on Craigslist.
It simply takes the URL of the results page of a search on Craigslist, and adds each result item (with its title, date, text, and pictures) to the wave, in a separate blip. The bot includes code to update the Wave when new results are found, but it is not yet functioning due to API issues.""",
    robotAddr='craigslist-searchy@appspot.com',
    techDesc="""Uses memcache to cache wepages, the app engine datastore to store internal data, the cron feature to update waves periodically and regular expressions to parse and extract data from Craigslist.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Dr. Musical Wave""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=51002&img_type=screenshot'),
    desc="""Dr. Music will tell you:

1. What a last.fm user is listening to you (includes you)
2. Music compatibility between people
3. Similar artists to an artist you like

All of this with pictures to make it colorful. Once you add Dr. Music he'll tell you how you can get him to do things for you.""",
    robotAddr='dr-music@appspot.com',
    techDesc="""Demonstrates reading text from blips, adding images to them, quoting strings, fetching URLs, extracting text using regex, using DOM to parse XML, and error logging.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Wave Dice Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=53001&img_type=screenshot'),
    desc="""Simple dice rolling gadget that supports standard PnP dice types. Full wave support, so other users can see your rolls immediately. """,
    gadgetXml='http://wavedicegadget.googlecode.com/svn/trunk/dice.xml',
    techDesc="""Uses shared state in the Gadget API.""",
    apis=["Gadgets","Installer"],
    langs=[""]
  ).put()



  Extension(
    type='gadget',
    title="""Retro Chat""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=48024&img_type=screenshot'),
    desc="""Chat room gadget, for old-fashioned IMing.""",
    gadgetXml='http://wave-retro-chat.googlecode.com/svn/trunk/chat.xml',
    techDesc="""Stores messages in the state using timestamps as keys.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""IMDbotty""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=48018&img_type=screenshot'),
    desc="""IMDbotty replaces links to movies on IMDb with a small gadget that displays useful information about the movie (title, year, rating, cover, director(s), actors).

The gadget can be reduced or expanded whether we ant all details or not, and the state is saved in the wave and shared between users.""",
    gadgetXml='http://imdbotty.appspot.com/gadget.xml?movieID=0047478',
    techDesc="""It uses memcache to store movie information, templates to display the gadget, regex to parse and extract information from IMDb and the gadget state to store its status.""",
    apis=["Robots","Gadgets"],
    langs=["Python","JavaScript"]
  ).put()

# error:MandelWave
# error:Kanjy


  Extension(
    type='gadget',
    title="""Pick-up Sticks""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=48011&img_type=screenshot'),
    desc="""Wave implementation of pick-up sticks. Players simultaneously remove free sticks off the board to earn points; they lose points whenever they pick a stick below other sticks. """,
    gadgetXml='http://wave.bryanbibat.com/pick-up-sticks.xml',
    techDesc="""Demonstrates avoiding race conditions by isolating states and limiting delta submissions.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""oxyxy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=47007&img_type=screenshot'),
    desc="""Collaborative LaTeX authoring Gadget for Google Wave. This Gadget allows the authoring of Waves containing LaTeX markup, which is converted and displayed as MathML. It makes use of the LaTeXMathML javascript library. Sort of in the spirit of how you pronounce 'LaTeX' the project's name is pronounced a bit like 'easy' and a bit like 'oxygen' without the 'gen'.""",
    gadgetXml='http://oxyxy.googlecode.com/svn/tags/oxyxy_0.1.1/oxyxy.xml',
    techDesc="""Shows how easy it is to integrate existing javascript libraries into Gadgets.""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Ego Robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=47003&img_type=screenshot'),
    desc="""A simple, but entertaining robot designed to stroke your ego. It will reply to all your blips with 'praise phrases' like "You're Very Talented". """,
    robotAddr='kimalvetti@appspot.com',
    techDesc="""Demonstrates EventType.BLIP_SUBMITTED with the Java SDK.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()

# error:Emaily


  Extension(
    type='gadget',
    title="""Likey""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=46001&img_type=screenshot'),
    desc="""A simple like/dislike gadget that can be added to a blip for intuitive user rating. It tells you how many people have liked, how many have disliked, and what you selected. You can also change your selection.""",
    gadgetXml='http://www.nebweb.com.au/wave/likey.xml',
    techDesc="""Demonstrates identifying the current viewer and customizing the gadget accordingly.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Map Cluster Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=41005&img_type=screenshot'),
    desc="""Lets each participant locate themselves on the map, and clusters all the locations.""",
    gadgetXml='http://google-wave-resources.googlecode.com/svn/trunk/samples/extensions/gadgets/mapcluster/mapcluster.xml',
    techDesc="""Shows retrieving participant information (picture and name) dynamically.""",
    apis=["Gadgets","Installer"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Google News gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=41001&img_type=screenshot'),
    desc="""Search and share google news in real time with your friends. You can search in private mode as well.""",
    gadgetXml='http://hosting.gmodules.com/ig/gadgets/file/112392185100245511748/newsgadget.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Eqygadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=40001&img_type=thumbnail'),
    desc="""A gadget for writing math equations inside Wave, and a robot for automatically turning marked text into equations.""",
    gadgetXml='waveyscience.appspot.com/eqygadget/eqygadget.xml',
    techDesc="""
""",
    apis=["Robots","Gadgets"],
    langs=["Python","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Row of Four""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=36022&img_type=screenshot'),
    desc="""Play against a robot, with the goal to get four cells in a row of your color before the robot does.""",
    robotAddr='rowoffour@appspot.com',
    techDesc="""Demonstrates how to communicate between a robot and a gadget (2 ways) using the Python SDK.""",
    apis=["Robots","Gadgets"],
    langs=["Python","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Drubot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=36020&img_type=screenshot'),
    desc="""A Robot for posting wave to a drupal site.""",
    robotAddr='ethos-drubot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Flickrey""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=36019&img_type=screenshot'),
    desc="""Replace flickr image URLs with the image from flickr. Currently only replaces URLs of the form: http://www.flickr.com/photos/username/flickr_image_id""",
    robotAddr='flickrey@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Notifiy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=37014&img_type=screenshot'),
    desc="""Google Wave Email Notifications it's a wave robot that sends an email to the participants of a wave whenever the wave is updated.""",
    robotAddr='wave-email-notifications@appspot.com',
    techDesc="""Sends an email to all participants when a PARTICIPANTS_ADDED, BLIP_SUBMITTED or BLIP_DELETED event is fired.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Short Emoticon Service (SES)""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=36017&img_type=screenshot'),
    desc="""When you have an idle wave open for a long time with a friend, and want to attract his or her attention, you can click you your friend's emoticon so that he or she gets notified with a sound. Otherwise, this gadget is useful for telling your friend(s) how you are feeling, which is quite handy if you're playing a game in another gadget or if you're just chatting.""",
    gadgetXml='http://wave-projects.googlecode.com/hg/gadgets/wave-ses.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Tagdef - tags explained""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=36008&img_type=screenshot'),
    desc="""This wave looks for #hashtags in your wave/blips, and uses the API at http://tagdef.com to look up definitions for these tags. It then adds a reply to the wave with the definitions. """,
    robotAddr='tagdef@appspot.com',
    techDesc="""Uses URLFetch with the REST api at http://api.tagdef.com, and uses Memcache to cache the results.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""All for Good""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=37005&img_type=screenshot'),
    desc="""Google Wave extension that helps you find and share ways to do good in real time. All For Good helps you take up volunteer opportunities, thus play a role in improving our communities and country.""",
    gadgetXml='http://www.allforgood.org/gadget/wave/wave_gadget.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""QRdataBot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=36005&img_type=screenshot'),
    desc="""Wave bot  that inserts QRcode image for each link inserted in the current wave.""",
    robotAddr='qrdatabot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Installer XML Creator""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=36001&img_type=screenshot'),
    desc="""This gadget is a GUI for creating an Extension Installer XML, currently limited to gadgets. It lets you enter values in a form or inport a current installer XML file.""",
    gadgetXml='http://wave-as-client.googlecode.com/svn/trunk/example/wave_install_creator/web/wave_install_creator.xml',
    techDesc="""
""",
    apis=["Installer"],
    langs=["ActionScript"]
  ).put()



  Extension(
    type='robot',
    title="""YQL Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=35031&img_type=screenshot'),
    desc="""A Google Wave robot that executes YQL queries and retrieves back the results.""",
    robotAddr='wavy-robot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""SoundCloud Player""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34042&img_type=screenshot'),
    desc="""""",
    gadgetXml='http://wave-projects.googlecode.com/hg/gadgets/wave-soundcloud-player.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Magic 8 Ball Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34039&img_type=screenshot'),
    desc="""Click to shake the ball and the ball will show the answer to you and everyone else.   Built using Wave ActionScript client library.  http://code.google.com/p/wave-as-client
""",
    gadgetXml='http://wave-as-client.googlecode.com/svn/trunk/example/wavemagic8/web/wavemagic8.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["ActionScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Brainstorming""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34038&img_type=screenshot'),
    desc="""A simple brainstroming tool to collaborate on an idea tree. 
Participants can add, edit and move nodes.""",
    gadgetXml='http://www.madin.jp/gadget/index.xml',
    techDesc="""Stores participant actions in the State object as JSON strings which contain labels, relations with parent nodes, etc. Draws nodes using CANVAS.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='invalid',
    title="""Yellow Highlighter""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=35019&img_type=screenshot'),
    desc="""This sample is an extension installer that uses annotateSelection to annotate the selected text when a toolbar icon is clicked. It annotates it using the key used by the Wave client for specifying the background color of text, and specifies the value as yellow. This results in the text being highlighted.""",
    techDesc="""Demonstrates using annotateSelection in the extension installer XML.""",
    apis=["Installer"],
    langs=[""]
  ).put()



  Extension(
    type='invalid',
    title="""Send Mail from Robot""",
    desc="""APIs: Robots""",
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Trippy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34028&img_type=screenshot'),
    desc="""Co-create an itinerary: choose points of interest -- including Lonely Planet recommendations, organize, share, print, or export to My Maps!""",
    gadgetXml='http://trippywave.appspot.com/static/travel-gadget.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Cards""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34025&img_type=screenshot'),
    desc="""Play card games in Wave. Almost any game is possible!""",
    gadgetXml='http://wave-cards.googlecode.com/svn/trunk/cards.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Tuxaios""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=35013&img_type=screenshot'),
    desc="""Tuxaios is a dice rolling robot for Google Wave written in Python.""",
    robotAddr='tuxaios@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Pongy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34019&img_type=screenshot'),
    desc="""Pongy is a real-time 2 player Pong game written to run as a Google wave gadget.""",
    gadgetXml='http://playpongy.appspot.com/pongy/org.cobogw.pongy.client.Pongy.gadget.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Wave TV""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=35005&img_type=screenshot'),
    desc="""Watch video streams from ZDF & 3sat with your friends while chatting.

Everybody can remote control the players of others in the wave, so that one can pause all the players at once, change streams, or start playback synchronously.

One drawback: German only.""",
    gadgetXml='http://wave-projects.googlecode.com/hg/gadgets/wave-player-multi.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Connect 4""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34015&img_type=screenshot'),
    desc="""Let's you play "connect 4" aka "four in a row" with your friends.""",
    gadgetXml='http://wave-projects.googlecode.com/hg/gadgets/wave-connect-four.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""XMPP""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=35001&img_type=screenshot'),
    desc="""Forwards new messages to your IM client in realtime.
Google Talk, Pidgin, Miranda, any XMPP-compatible IM client which has your Google Wave address configured will notify you without needing you to be signed into Google Wave.""",
    robotAddr='wave-xmpp@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Skimmy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34014&img_type=screenshot'),
    desc="""Changes text emoticons to images.""",
    robotAddr='wave-skimmy@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Wordpress bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34003&img_type=screenshot'),
    desc="""Publish the current wave to wordpress as an embedded Wave""",
    robotAddr='wp-bot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Tic Tac Toe""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=34001&img_type=screenshot'),
    desc="""Play Tic Tac Toe game with your friends on wave.""",
    gadgetXml='http://wave-as-client.googlecode.com/svn/trunk/example/wavetictactoe/web/wavetictactoe.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["ActionScript"]
  ).put()



  Extension(
    type='robot',
    title="""SAP-ES""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=31006&img_type=screenshot'),
    desc="""A robot which intergrates with the SAP Enterprise Services. The robot can guide in the creation of a equipment Service request. """,
    robotAddr='sap-es@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Emoticony""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=32002&img_type=screenshot'),
    desc="""Emoticony is a robot for Google Wave which replaces text representations of emoticons with the relevant image. 
There are currently over 50 different emoticons available, with this number continuing to grow. Look out for themed emoticons focused around specific events (Halloween, Christmas etc.)

More details can be found at: http://emoticony.leestone.co.uk
""",
    robotAddr='emoticonbot@appspot.com',
    techDesc="""Using the Image Element along with Positions""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""BingyBot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=31003&img_type=screenshot'),
    desc="""BingyBot allows users to create FAQ Waves collaboratively.  Create an FAQ quickly on any topic - like Space science, Google Wave or Social Media.

Ask anything that ends with a question mark, like "what is google wave?" or "what is a delegate in C#?" or just key in a flight no to get the status. Bingy will answer if it knows. 

Goto the Live Demo Link below. 

More to come, I'll post more details including source code soon in http://amazedsaint.blogspot.com""",
    robotAddr='bingybot@appspot.com',
    techDesc="""Uses the Google .NET Wave Robot APIs (ported by Jon Skeet) and interfaces with Bing APIs.""",
    apis=["Robots","Embed"],
    langs=[""]
  ).put()



  Extension(
    type='robot',
    title="""Starify bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=29024&img_type=screenshot'),
    desc="""Starify allows you to star waves and load the list of starred waves later. Visit http://wave.to/robots/starifybot/ for more information""",
    robotAddr='starifybot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=[""]
  ).put()



  Extension(
    type='robot',
    title="""plotzie""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=29022&img_type=screenshot'),
    desc="""Looks in your new blip for a string formatted a certain way and replaces that string with a sparkline. For more information, read the technical write-up: http://lee-phillips.org/wave/plotzie.xhtml.""",
    robotAddr='plotzie@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Rssybot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=30012&img_type=screenshot'),
    desc="""Rssybot lets your watch RSS feeds from Google Wave. Just add it to a wave, enter the link to the RSS feed you want to subscribe to and wait for new posts to appear in your inbox as unread blips. For more information, visit:
http://www.wave.to/robots/rssybot/""",
    robotAddr='rssybot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Blip-debug""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=30011&img_type=screenshot'),
    desc="""A robot, which helps with debugging what annotations are in each blip, as each event is triggered. 
Notice: This robot creates a lot of blips to the wave, so do not add it to a large conversation. """,
    robotAddr='blipdebug@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Jmp Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=30008&img_type=screenshot'),
    desc="""Shorten urls in you message. Just type in your message in the message box and click Shorten button. For more details, visit: http://j.mp/jmpbot
""",
    robotAddr='jmp-bot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Using jQuery and YQL in a Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=29015&img_type=screenshot'),
    desc="""This gadget fetches the latest 5 tweets that are tagged with "gtugfra". """,
    gadgetXml='http://dl.getdropbox.com/u/1609812/jqWaveTest.xml',
    techDesc="""Shows how to use jQuery & YQL together in a gadget.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Treeify""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=29013&img_type=screenshot'),
    desc="""Multi-wave robots are agents that in some way operate on more than one wave. Treeify is a multi-wave robot which lets you connect waves into tree structures. With it you can build and navigate trees of waves.""",
    robotAddr='treeify@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Wave Live Messenger""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=29011&img_type=screenshot'),
    desc="""Wave Live Messenger allows you to log in to your Windows Live Messenger account from within Google Wave and have conversations with your messenger contacts right from within a wave. Even if you leave the wave and start reading a different wave, Wave Live Messenger will keep your conversation up to date so you can return to it at any time and continue chatting. For more details, visit:
http://www.wave.to/robots/wavelivemessenger""",
    robotAddr='wavelivemessenger@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Google Calendar Robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=30005&img_type=thumbnail'),
    desc="""Robot recognizes date pattern in form YYYY-MM-DD ('.' or '/' can be used for separator also) and updates it to link to add an event to user's Google Calendar.""",
    robotAddr='calendar-robot@appspot.com',
    techDesc="""Uses the DailyDev Wave Robot library (http://www.dailydev.org/p/wave-robot) and Spring framework.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Wave Alpha""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=30003&img_type=screenshot'),
    desc="""Query and retrieve Wolfram|Alpha right from the comfort of your wave.""",
    robotAddr='wave-alpha@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Polling Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=29004&img_type=screenshot'),
    desc="""The owner can set the title of the poll e.g "Which movie we should go to?", and the bar graphs indicate votes from participants.""",
    gadgetXml='http://pune-gtug-wave-samples.googlecode.com/svn/trunk/wave-polling-gadget/polling.xml',
    techDesc="""Stores poll data in the shared Wave state object.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Search-y""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=30001&img_type=screenshot'),
    desc="""Links to your queries, specified within square brackets, after blip submits.""",
    robotAddr='searchy-wave@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""WaveQuote""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=26003&img_type=screenshot'),
    desc="""Will add a random quote to a wavelet when a user types &quot;&quot;&quot; (three quotes)""",
    robotAddr='wave-quote@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Buddy As A Service""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=27032&img_type=screenshot'),
    desc="""Buddy as a Service is a wave robot, using Yahoo YQL API, Google API and other services to do searches and some other stuff (translations, weather forecast, etc) for you. """,
    robotAddr='buddyasaservice@appspot.com',
    techDesc="""Searching for informations without leaving the current wave.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""CodeBot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=28023&img_type=screenshot'),
    desc="""A code formatting bot. Getting better periodically based on user feedback.""",
    robotAddr='codebot-wave@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""buglinky""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=27027&img_type=screenshot'),
    desc="""buglinky automatically links "issue #NN" to a bug tracker of your choice, and replaces raw bug URLs with the equivalent text. All the annotations and replacements happen while typing.
""",
    robotAddr='buglinky@appspot.com',
    techDesc="""Contains a reusable BlipProcessor class that tries to simplify the process of writing well-behaved real-time bots.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Cody""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=27026&img_type=screenshot'),
    desc="""Cody is a syntax highlighter for Google Wave that will read submitted blips for any code and color the code based on the language that it either detects or the language you specify.""",
    robotAddr='http://codeditor.appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""FML Blipper""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=28014&img_type=screenshot'),
    desc="""FML Blipper is a very simple google wave extension that randomly pulls FML story from www.fmylife.com website. """,
    robotAddr='fmlblipper@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""What is?""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=27017&img_type=screenshot'),
    desc="""A simple robot which will answer questions in the form of "what is ".""",
    robotAddr='wave-whatis@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Techcrunch""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=28012&img_type=screenshot'),
    desc="""Shows RSS feed for Techcrunch.""",
    gadgetXml='http://www.lekanger.no/wave/techcrunch/hello.xml',
    techDesc="""Uses a iframe and a RSS feed php script.""",
    apis=["Robots"],
    langs=[""]
  ).put()



  Extension(
    type='invalid',
    title="""ForceAutomaton""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=27016&img_type=screenshot'),
    desc="""A small sample demonstration of a Google Wave robot pulling data (Accounts initially) from the Force.com platform using the Force.com Web Service Connector (http://code.google.com/p/sfdc-wsc/). """,
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""troco""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=27014&img_type=screenshot'),
    desc="""An experimental peer-to-peer currency system. Troco is a set of wave extensions that aims to provide a decentralized complementary community currency system, i.e., a peer-to-peer currency system. You can also view it as an IOU or promissory note based system.

At the current point, troco consists only in an experimental (unfinished and insecure) Wave gadget with a toolbar installer.

For more info visit: http://troco.ourproject.org""",
    gadgetXml='http://troco.ourproject.org/gadget/org.ourproject.troco.client.TrocoWaveGadget.gadget.xml',
    techDesc="""Uses GWT for the frontend.""",
    apis=["Gadgets"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""iWave""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=28008&img_type=screenshot'),
    desc="""A gadget that allows you to upload your profile to wave. You can then add new participants so they know who you are. This gadget also uses facebook connect so it will fill in some details automatically, publish posts on your wall when you update your details and automatically update your comment every time you visit the gadget.

For more information visit http://www.wave.to/gadgets/iWave/""",
    gadgetXml='http://gadget.wave.to/iWave/iWave.xml',
    techDesc="""Uses the Facebook Connect javascript API.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""TheWaveBank""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=27006&img_type=screenshot'),
    desc="""A sample application which demonstrated how robots can be used to control workflow.  

When you add your robot to a wave a loan application will is created. When the form is submitted, your -test user can approve or reject the application. """,
    robotAddr='TheWaveBank@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Verse Seeker""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=28001&img_type=screenshot'),
    desc="""Want to add a verse to your blip?  Verse seeker does it for you.  

Looks up verses in the Bible.  For example, typing v/John 1:1/ in a blip is replaced with the text of the verse.

Bible verses courtesy of ESV Bible web service (http://www.esvapi.org/).  Thanks to Stocky for the inspiration.""",
    robotAddr='verseseeker@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='invalid',
    title="""Joomla! Google Wave Plugin""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=24001&img_type=screenshot'),
    desc="""A simple Joomla! content plugin to embed multiple waves and style them. """,
    techDesc="""Using the Joomla framework & PHP.""",
    apis=["Embed"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""VectorEditor""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=22025&img_type=screenshot'),
    desc="""Draw and edit vector graphics in real time with SVG and VML (Modern browsers and IE). Includes support for Lines, Rectangles, Text, Ellipses, Paths, Polygons, and more. Updates state while the shape is being drawn or manipulated and has measures to prevent multiple users from editing the same shape at the same time.""",
    gadgetXml='http://jsvectoreditor.googlecode.com/svn/trunk/wave/vectoreditor.xml',
    techDesc="""Renders graphics using the Raphael (http://raphaeljs.com) library to support not only the modern browsers but IE as well.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='invalid',
    title="""Calcbot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23022&img_type=thumbnail'),
    desc="""This bot will do in place calculations for simple mathematical expressions and allow you to use user defined variables.

""",
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Regexey""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23020&img_type=screenshot'),
    desc="""This is a simple find-and-replace robot.  After you add it, it will display an introduction message.  Then any blip you create should be of the format:
seach string
replace string
text to process
It will search for the "search string" in the "text to process" and replace it with the "replace string."  Then it will append the results in a reply blip.""",
    robotAddr='regexey@appspot.com',
    techDesc="""Processes text using the java.util.regex library.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Wikify""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23018&img_type=screenshot'),
    desc="""This robot replaces specific marked-up text with links to (or definitions from) Wikipedia. Supports several languages.""",
    robotAddr='wikifier@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Graphy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23016&img_type=screenshot'),
    desc="""Graphy extends Google Wave with the ability to collaborate on flow charts and graphs. Graphy searches for a marker (#!dot) at the top of a blip, and when found, adds a gadget to the bottom of the blip which presents an image of the graph. Graph edges are expressed with simple statements like

a -> b """,
    robotAddr='graph-wave@appspot.com',
    techDesc="""Shows robot/gadget interaction. The robot watches blips for edits and uses a 3rd-party server to generate images in SVG format. The gadget is responsible for displaying the graph and switching between views.""",
    apis=["Robots","Gadgets"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Reddit""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23015&img_type=screenshot'),
    desc="""This robot is able to post the top articles from Reddit.com and any sub-reddits. Simply reply to a wave for which it has been invited with the word "reddit" followed by a colon ":" and then the name of the subreddit (or "homepage"). You can specify the number of articles to return by appending an additional colon ":" followed by the number of articles.

Examples: reddit:wave, reddit:pics:15, reddit:technology""",
    robotAddr='wave-reddit@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Posterous-Robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=22017&img_type=screenshot'),
    desc="""Allows you to post blog to your posterous site in Google Wave. """,
    robotAddr='http://blog.kangye.org/first-release-of-google-wave-robot-for-poster',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Piano Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=22015&img_type=screenshot'),
    desc="""Play piano with your friends on Wave.""",
    gadgetXml='http://wave-instruments.appspot.com/gadget/piano.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Seekdroid""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=22011&img_type=thumbnail'),
    desc="""Seekdroid is a wave extension directory.

It allows invitation, adhesion and votation among others of the robots in it's database. 

It's part of a tutorial that can be found in the author URL. """,
    gadgetXml='http://seekdroid.appspot.com/inc/seekdroid_gadget.xml',
    techDesc="""
""",
    apis=["Robots","Gadgets"],
    langs=["Python","JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""The Button""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=22009&img_type=screenshot'),
    desc="""Probably the most useless game created ever...
I'll let you guess the rules :)""",
    gadgetXml='http://hyperthese.net/wave-gadgets/the-button-xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='invalid',
    title="""Yelpful""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23008&img_type=screenshot'),
    desc="""This is a robot that will take your input and return yelp results based on the location and keyword. Usage: /yelp [location @ least 1 word] [keyword - 1 word]""",
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""PlusOne""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23006&img_type=screenshot'),
    desc="""Add this gadget to a blip to allow viewers to vote "thumbs up" or "thumbs down" on it.  The gadget keeps track of the number of votes for each.""",
    gadgetXml='http://www.elizabethsgadgets.appspot.com/public/gadget.xml',
    techDesc="""Stores the votes in the state, with keys associated with each viewer's ID, to prevent people voting more than once.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Blogbot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=22004&img_type=screenshot'),
    desc="""Organizes related waves (blog posts, FAQ, etc) in a central Table of Contents wave.""",
    robotAddr='blogbot-wave@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='invalid',
    title="""Baatey""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=23002&img_type=screenshot'),
    desc="""Baatey is a robot that converts @symbols inside a google wave into a URL that links directly to the user's twitter page. """,
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Magic 8-Ball""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=20031&img_type=screenshot'),
    desc="""Magic 8 Ball Sees and Knows All. Just add this Robot to your wave and ask the magic 8-ball any question and receive your answer.""",
    robotAddr='magic-8ball@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='invalid',
    title="""GoogleWave MediaWiki extension""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18035&img_type=screenshot'),
    desc="""The GoogleWave extension for mediaWiki makes it possible to embed Google Waves in your wiki.

""",
    techDesc="""
""",
    apis=["Embed"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Alphabet Soup""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18030&img_type=screenshot'),
    desc="""Multi-user drag and drop "fridge magnets".
It's been done before in Flex, but heres a wave version.""",
    gadgetXml='http://www.krandor.net/demos/alpha/alpha.xml',
    techDesc="""
""",
    apis=[""],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Bitly Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18029&img_type=screenshot'),
    desc="""BitlyBot - shorten urls in you message.

Just type in your message in the message box and click Shorten button. It will find the urls in your message and shorten them.""",
    robotAddr='bitly-bot@appspot.com',
    techDesc="""Fetches JSON content from the Bitly API and parses using JSONObject.""",
    apis=["Robots"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""msg-in-a-bottle""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=20023&img_type=screenshot'),
    desc="""This is a very simple robot that allows you to throw a message into the waves by embedding your message in a bottle and then wrapping the bottle in a wave, like so:

~~{your message here}~~

Then, at some random time, on some random wave where the robot is functioning, someone will find your bottle. Although the robot does keep track of some extra information, the only message that is found by the recipient is whatever you include in the {bottle}.""",
    robotAddr='msg-in-a-bottle@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Wave Blogadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=20022&img_type=screenshot'),
    desc="""Use this configurable gadget to easily embed any wave into any site that supports gadgets.* (i.e. iGoogle, Orkut, Ning, Blogger, or any FriendConnect enabled site). Simpler than using the Embed API, and offers configuration options.""",
    gadgetXml='http://hosting.gmodules.com/ig/gadgets/file/116844733254275818014/blogadget.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Lasty""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18025&img_type=screenshot'),
    desc="""This bot lets you shout what song you are listening to. You must own a Last.fm account, and then you write YourLastFMUser-is-listening and it replaces it by the song that you're listening to and a link to it.

""",
    robotAddr='last-robot@appspot.com',
    techDesc="""Inserts images and styles on an inline blip.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Dr. Maps""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18024&img_type=screenshot'),
    desc="""Dr. Maps Robot allows you to get a map from an address.

Give it an address and it will insert into the wave a mini-map locating the address and a link to the Google Map locating the address.""",
    robotAddr='dr-maps@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Watexy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=20018&img_type=screenshot'),
    desc="""Robot for writing Latex in Waves with editing possibilities.""",
    robotAddr='watexy@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Canvas""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18016&img_type=screenshot'),
    desc="""You can draw picture and other people can see it and modify it in real time.""",
    gadgetXml='http://ichikawa-public.appspot.com/wave/canvas/canvas.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Piratify Robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18014&img_type=screenshot'),
    desc="""Turns whatever you type into "Pirate Speak" .. Arrrr.""",
    robotAddr='piratify@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Google Wave Drupal Integration""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18013&img_type=screenshot'),
    desc="""A Drupal module and corresponding robot that enabled the embedding of Google Waves""",
    robotAddr='drupalembedbot@appspot.com',
    techDesc="""embedding, robot""",
    apis=["Robots","Embed"],
    langs=["Python","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""BotURL""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18012&img_type=screenshot'),
    desc="""Replaces FULL URLs with hyperlinks whose title are the domain names.
Replaces TinyURLs/bit.ly URLs with original URL domain names and links them to the original URLs.""",
    robotAddr='boturl@appspot.com',
    techDesc="""Uses URLFetch with the  TinyURL API and bit.ly API.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""censorshiprobot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=19002&img_type=screenshot'),
    desc="""Google wave robot, that filters specific words from dictionary and then replaces with random chars. 

The dictionary can be updated from any blip with two commands:
     censor:someword - add someword to dictionary
     uncensor:someword - remove someword from dictionary""",
    robotAddr='http://censorshiprobot.appspot.com/',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Raffly Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=20010&img_type=thumbnail'),
    desc="""Insert this gadget to select a random participant from your wave to be the winner. The winner of what? Well that's up to you :-)
""",
    gadgetXml='http://raffly.googlecode.com/svn/trunk/sandbox/raffly-xml1/raffly.xml',
    techDesc="""Uses wave.getParticipants().""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='invalid',
    title="""Drupal Waves""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18009&img_type=screenshot'),
    desc="""How to add a Google Wave to a fresh Drupal installation.""",
    techDesc="""
""",
    apis=["Embed"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Hobbity""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18008&img_type=screenshot'),
    desc="""A robot to make the urls shorten in the waves.""",
    robotAddr='hobbiturl@appspot.com ',
    techDesc="""Use URLFetch with the migre.me API to shorten the URL.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Example qooxdoo Google Wave Gadgets""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=20005&img_type=screenshot'),
    desc="""The google wave gadgets from the wave gadget tutorial written using the JavaScript framework qooxdoo.

The gadget URL for the counter example is http://qxwave.appspot.com/client/counter.xml""",
    gadgetXml='http://qxwave.appspot.com/client/auction.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Slashdot Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18006&img_type=screenshot'),
    desc="""Grabs the top headlines from Slashdot and displays them in the Wave.""",
    gadgetXml='http://www.m1cr0sux0r.com/slashdot.xml',
    techDesc="""Uses the Google AJAX Feed and Search APIs.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""ActionScript Button Counter Gadget Example""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=19001&img_type=screenshot'),
    desc="""A simple button counter example built in ActionScript.  This serves as an example of wave-as-client (http://code.google.com/p/wave-as-client).""",
    gadgetXml='http://wave-as-client.googlecode.com/svn/trunk/example/button_counter/web/button-counter.xml',
    techDesc="""Uses ActionScript to communicate with the JS Gadgets API.""",
    apis=["Gadgets"],
    langs=["ActionScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Rickrolley""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=18001&img_type=screenshot'),
    desc="""Adds an embedded YouTube player to a wave and fights to stop people from deleting it!""",
    gadgetXml='http://rickrolley.appspot.com/gadgets/rickroll.xml',
    techDesc="""Shows adding gadgets to a Wave using the Python API, and using BLIP_DELETED event.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Checky the Checklist Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=14009&img_type=screenshot'),
    desc="""Basecamp-like to-do checklists with drag and drop.""",
    gadgetXml='http://wave-gadgets.appspot.com/checky.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()

# error:Syntaxy


  Extension(
    type='robot',
    title="""Hangman (Robot)""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=15007&img_type=screenshot'),
    desc="""A robot that lets you play hangman""",
    robotAddr='wavehangman@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='gadget',
    title="""Hangman (Gadget)""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=15004&img_type=screenshot'),
    desc="""A gadget that allows you to play hangman.""",
    gadgetXml='http://gadget.wave.to/hangman/game.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""floodit game""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=16001&img_type=screenshot'),
    desc="""A simple turn based two player game. You take it in turns to choose a colour; choosing your colour changes every adjacent square that is the same colour (starting at the top left). For each square that you change you are awarded one point. Change more squares each turn to rack up more points and beat your opponent!""",
    gadgetXml='http://gadget.wave.to/floodit/game.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='invalid',
    title="""wp-wave-shortcodes""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=15002&img_type=screenshot'),
    desc="""Adds a shortcode to WordPress that makes it easy to embed waves in a post or page. It also adds a media button so one is not required to remember how a shortcode is structured.""",
    techDesc="""
""",
    apis=["Embed"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Coin Toss Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=11011&img_type=screenshot'),
    desc="""Use the Coin Toss gadget to decide who buys the next lunch or who should bring donuts to the next meeting.  Heads you win, tails you lose.

1. Fill out a title for you "contest"
2. Select who will be "heads" and who will be "tails"
3. Click "Flip Coin" and let the Coin Toss Gadget determine the winner.""",
    gadgetXml='http://cointoss.googlecode.com/svn/trunk/cointoss.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Surreal Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=12004&img_type=screenshot'),
    desc="""Uses the Surrealist Compliment Generator to "compliment" each new Wave participant.""",
    robotAddr='surrealbot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Twiliobot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=12002&img_type=screenshot'),
    desc="""twiliobot is a Wave Robot written in Python that uses the Twilio Phone API to create "voice waves." When a user adds twiliobot to a wave, the robot automatically finds and transforms the phone numbers in that wave into click-to-call links. When a user clicks a link, a call is placed to the user's cell phone or landline and to the phone number in the link and the two are connected.""",
    robotAddr='twiliobot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Swedish Chef robot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=11004&img_type=screenshot'),
    desc="""Translates anything written in a wave intro Swedish Chef speak.""",
    gadgetXml='http://borkforceone.appspot.com/_wave/capabilities.xml',
    techDesc="""A really simple and silly application that pokes fun at the Swedes working on Wave project, even though the "Swedish" chef sounds more Danish than Swedish.

Importantly, I wrote this without ever having written Python or used App Engine, and it took an afternoon.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Converts-y""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=12001&img_type=screenshot'),
    desc="""Convert units from one type to another.

1.23km (?miles) -> 1.23km (0.76 miles)
""",
    gadgetXml='http://convertsy.appspot.com/_wave/capabilities.xml',
    techDesc="""Uses DOCUMENT_CHANGED to update text as you type.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Dr. Weather""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=10008&img_type=screenshot'),
    desc="""Get weather information, and weather forecasts.""",
    robotAddr='shiny-sky@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Embeddy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=10004&img_type=screenshot'),
    desc="""Generates code to embed a wave in your webpage.""",
    robotAddr='embeddy@appspot.com',
    techDesc="""Demonstrates using a robot to communicate with a gadget (change its state).""",
    apis=["Robots","Gadgets","Embed"],
    langs=["Java","JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Monty""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=9003&img_type=screenshot'),
    desc="""Evaluates Python expressions.""",
    robotAddr='i-cron@appspot.com',
    techDesc="""Demonstrates using the Python SDK to process root blips/child blips, and create blips.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""HTML Gadget""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=10001&img_type=screenshot'),
    desc="""Allows you to add any piece of HTML inside a wave.""",
    gadgetXml='http://wave-ide.appspot.com/html.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Groupy-the-bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=8009&img_type=screenshot'),
    desc="""A Wave robot for managing your own groups.  Groupy has following commands.

1) list groups
2) desc GROUPNAME
3) add me to GROUPNAME
4) remove me from GROUPNAME (not implemented yet)
5) invite people in GROUPNAME
6) help

Groupy also has a web interface for managing your own groups
http://groupy-the-bot.appspot.com/""",
    robotAddr='groupy-the-bot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Embedded Search Results""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=8006&img_type=screenshot'),
    desc="""This simple robot allows you to quickly and easily perform a search and have the results embedded in your Wave.

Currently supports Google & Flickr Searches.

Support for more search providers will be coming soon.


For full information visit http://wave-sandbox.appspot.com""",
    robotAddr='wave-sandbox@appspot.com',
    techDesc="""Uses URLFetch with the Google Search API & Flick API.""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='invalid',
    title="""Wave ActionScript Gadgets API""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=8003&img_type=screenshot'),
    desc="""This open source library acts as a bridge to Wave Gadgets JavaScript API from Flex/Flash (AS3). """,
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["ActionScript"]
  ).put()



  Extension(
    type='robot',
    title="""Kay-the-bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=8001&img_type=screenshot'),
    desc="""It is a cute wave robot. It responds to every blip with a new blip that sounds like baby talk (but is in fact just that blip scrambled up randomly).""",
    robotAddr='kay-the-bot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Anti-Swear Bot""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5026&img_type=screenshot'),
    desc="""A simple bot in Python that stops people being rude on a wave it is added to. Note: The rude words have been blocked out in the screenshot to avoid offending anyone.""",
    robotAddr='invectivedeleted@appspot.com',
    techDesc="""Uses an existing site (www.noswearing.com) via its POST interface and scrapes the result. """,
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='gadget',
    title="""Napkin""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5023&img_type=screenshot'),
    desc="""Adds the ability to do quick "back of a napkin" sketches to a wave - collaborative doodling!""",
    gadgetXml='http://my-wave-gadgets.appspot.com/wave/NapkinGadget.xml',
    techDesc="""Uses a bridge to allow the Wave Gadget API functions to be called from within the Flex """,
    apis=["Gadgets"],
    langs=["JavaScript","ActionScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Bidder""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=6001&img_type=screenshot'),
    desc="""Turns a wave into an auction by displaying a field that lets the participants bid. It shows the picture and name of the highest bidder so far and also the highest bid.""",
    gadgetXml='http://wave-api.appspot.com/public/gadgets/bidder.xml',
    techDesc="""Demonstrates using getDisplayName and getThumbnailUrl on participants in the Gadgets API.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Ratings""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5021&img_type=screenshot'),
    desc="""Lets participants rate and review a topic (movie, restaurant, etc) in a wave and shows a tally of the result.""",
    gadgetXml='http://pesta.appspot.com/gadgets/ratings/ratings.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Magnetic Poetry""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5018&img_type=screenshot'),
    desc="""Displays a magnetic fridge poetry in the form of a bunch of tiles with words on them. Any participant on the wave can then move those words around to compose poems (or prose of their fancy). Uses the preferences API for storing state.""",
    gadgetXml='http://wave-api-dmo.appspot.com/public/fridge.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Are you coming?""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5016&img_type=screenshot'),
    desc="""Combines the participant and state api to show a list of all people that have said whether they will come or not. Insert in a wave about a shared activity. Uses the preferences API for storing state.""",
    gadgetXml='http://wave-api.appspot.com/public/gadgets/areyouin/gadget.xml',
    techDesc="""
""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='invalid',
    title="""Bidder""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=4015&img_type=screenshot'),
    desc="""Turns a wave into an auction by displaying a field that lets the participants bid. It shows the picture and name of the highest bidder so far and also the highest bid.""",
    techDesc="""
""",
    apis=[""],
    langs=[""]
  ).put()



  Extension(
    type='gadget',
    title="""OpenSocial Templates""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5011&img_type=screenshot'),
    desc="""Displays the current list of participants on the Wave.""",
    gadgetXml='http://wave-api.appspot.com/public/gadgets/wave.xml',
    techDesc="""Demonstrates using setParticipantCallback with getParticipants() in the Gadgets API, and outputting the list in an OpenSocial template.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Click me""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5009&img_type=screenshot'),
    desc="""Shows a button with a counter. Each time the button gets clicked, the counter is incremented by one.""",
    gadgetXml='http://wave-api.appspot.com/public/gadgets/hellowave.xml',
    techDesc="""Demonstrates using the Gadgets API to set/get state on a single value.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Complety """,
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=4010&img_type=screenshot'),
    desc="""Uses the Google Search API to replace "???" in a blip (after it's submitted) with a suggested word.""",
    robotAddr='wave-complete@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Yasr""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=4007&img_type=screenshot'),
    desc="""Replaces emoticons in the wave (after blip submitted) with smiley images.""",
    robotAddr='wave-api-dmo@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Bloggy""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=4004&img_type=screenshot'),
    desc="""Publishes the contents of a wave to a blog site.""",
    robotAddr='blog-wave@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Python"]
  ).put()



  Extension(
    type='robot',
    title="""Tweety""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=5002&img_type=screenshot'),
    desc="""Tweets wave blips to twitter, and displays tweets from it.""",
    robotAddr='tweety-wave@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Polly""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=4001&img_type=screenshot'),
    desc="""Creates a Wave to poll recipients and store their answers. Users are able to dynamically alter their choices.""",
    robotAddr='polly-wave@appspot.com',
    techDesc="""Demonstrates using FormView in the Java SDK.""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Stocky""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=1009&img_type=screenshot'),
    desc="""Stocky automatically retrieves the live stock price for any stock symbols in your blip text that begins with "$" (ie. $GOOG)""",
    robotAddr='stocky-wave@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='invalid',
    title="""Multiple Extensions Embed""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=7&img_type=screenshot'),
    desc="""Embeds two waves on the same page, the first containing a gadget and the second containing a robot.""",
    techDesc="""
""",
    apis=["Embed"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='invalid',
    title="""Youtube Playlist Discuss""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=1005&img_type=screenshot'),
    desc="""Embeds a Youtube playlist with a custom player, and then embeds a wave below it.""",
    techDesc="""
""",
    apis=["Embed"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='gadget',
    title="""Collaborative Sudoku""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=3&img_type=screenshot'),
    desc="""Multi-player collaborative sudoku gadget.""",
    gadgetXml='http://blah.appspot.com/wave/sudoku/sudoku.xml',
    techDesc="""Demonstrates using serializing gadget state into JSON strings, to store a more complex state.""",
    apis=["Gadgets"],
    langs=["JavaScript"]
  ).put()



  Extension(
    type='robot',
    title="""Debuggy """,
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=1002&img_type=screenshot'),
    desc="""Responds to each event on a wave with debug information about the event and the associated blips and wavelets.""",
    robotAddr='debuggybot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()



  Extension(
    type='robot',
    title="""Cartoony""",
    imageUrl=db.Link('http://wave-samples-gallery.appspot.com/images?img_id=1&img_type=screenshot'),
    desc="""Replaces the text of every submitted blip with a cartoon balloon that contains the text instead. Colors the balloons based on username.""",
    robotAddr='cartoonybot@appspot.com',
    techDesc="""
""",
    apis=["Robots"],
    langs=["Java"]
  ).put()

