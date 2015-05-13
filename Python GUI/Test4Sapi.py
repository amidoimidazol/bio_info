
#THE NEXT TO LAST TEST IS THE ISFILE AND I COMMENTED IT OUT FOR THERE IS AN ERROR!
import Sapi5, time, os

av = Sapi5.SynthDriver()
av.init()
SYNC = av._sync
ASYNC = av._async
PURGE = av._purge
ISFILE = av._is_filename
XML = av._xml
NOT_XML = av._not_xml
PERSIST = av._persist_xml
PUNC = av._punc
WAIT = av._wait

av.Speak("Hello!")
av.Speak( "I am speaking in the default voice!")
av.Speak( "Number of voices is: %d" % av.getVoiceCount())
av.Speak( "Hello! Now saying the punctuation in this sentence.", PUNC)
time.sleep(.5)
av.setVoiceByName( "Mike")
av.setVolume( 100)
av.Speak( " The Volume Is Set At Speaker Volume!")
av.setRate( 5)
av.setPitch(0)
av.setVoiceByName( "Mary")
av.setPitch(5)
av.Speak( "Set To Voice Mary and Pitch 5 or 75% of maximum pitch!")
time.sleep(1)
av.setPitch(0)
av.setRate(0)
av.Speak( "The rate and pitch are now set for normal!")
time.sleep(1)
av.read_Voices()
av.setVoiceByName( "Mary")
av.Speak( "Hit enter key to stop speaking!")
av.setPitch(10)
av.Speak("Pitch 100%", ASYNC)
av.setPitch(5)
av.Speak("Pitch 75%", ASYNC)
av.setPitch(0)
av.Speak("Pitch 50%", ASYNC)
av.setPitch( -5)
av.Speak("Pitch 25%", ASYNC)
av.setPitch( -10)
av.Speak("Pitch 0%", ASYNC)
av.setPitch(0)
av.Speak( "Hit enter key!", ASYNC)
hit = raw_input("Hit enter key >")
#av.SpeakFile( "readthis.txt", ASYNC, ISFILE)	
av.Speak(" Now Good bye", ASYNC, PURGE)
av.setVoiceByName( "Sam")
av.Speak( "<volume level='50'/> goodbye")
