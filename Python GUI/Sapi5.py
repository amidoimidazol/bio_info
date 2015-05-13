
#DRIVERS FOR SAPI 5 AND VOICES!
#NOTE THE CONSTANTS AND IN THE SPEAK FUNCTION AND THE ADDING/OR OF THE VALUES.
from comtypes.client import CreateObject
import _winreg

class constants4tts:
    Wait = -1
    Sync = 0
    Async = 1
    Purge = 2
    Is_filename = 4
    XML = 8
    Not_XML = 16
    Persist = 32
    Punc = 64

class SynthDriver():
    name="sapi5"
    description="Microsoft Speech API version 5 (sapi.SPVoice)"
    _voice = 0
    _pitch = 0
    _voices = []
    _wait = -1 #WAIT INDEFINITELY
    _sync = 0 #WAIT UNTIL SPEECH IS DONE.
    _async = 1 #DO NOT WAIT FOR SPEECH
    _purge = 2 #CLEAR SPEAKING BUFFER
    _is_filename = 4 #OPEN WAV FILE TO SPEAK OR SAVE TO WAV FILE
    _xml = 8 #XML COMMANDS, PRONUNCIATION AND GRAMMER.
    _not_xml = 16 #NO XML COMMANDS
    _persist_xml = 32 #Changes made in one speak command persist to other calls to Speak.
    _punc = 64 #PRONOUNCE ALL PUNCTUATION!
    def check(self):
        try:
            r=_winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT,"SAPI.SPVoice")
            r.Close()
            return True
        except:
            return False
#INITIALIZE ENGINE!
    def init(self):
        try:
            self.tts = CreateObject( 'sapi.SPVoice')
            self._voice=0
            self._voiceCount = len(self.tts.GetVoices())
            for v in range(self._voiceCount):
                self._voices.append( self.tts.GetVoices()[v])
            return True
        except:
            return False
#TERMINATE INSTANCE OF ENGINE!
    def terminate(self):
        del self.tts
#NUMBER OF VOICES FOR ENGINE!
    def getVoiceCount(self):
        return len(self.tts.GetVoices())
#NAME OF A VOICE BY NUMBER!
    def getVoiceNameByNum(self, num):
        return self.tts.GetVoices()[num-1].GetDescription()
#NAME OF A VOICE!
    def getVoiceName(self):
        return self.tts.GetVoices()[ self._voice].GetDescription()
#WHAT IS VOICE RATE?
    def getRate(self):
        "MICROSOFT SAPI 5 RATE IS -10 TO 10"
        return (self.tts.rate)
#WHAT IS THE VOICE PITCH?
    def getPitch(self):
        "PITCH FOR MICROSOFT SAPI 5 IS AN XML COMMAND!"
        return self._pitch
#GET THE ENGINE VOLUME!
    def getVolume(self):
        "MICROSOFT SAPI 5 VOLUME IS 1% TO 100%"
        return self.tts.volume
#GET THE VOICE NUMBER!
    def getVoiceNum(self):
        return self._voice
#SET A VOICE BY NAME!
    def setVoiceByName(self, name):
        "VOICE IS SET BY NAME!"
        for i in range( self._voiceCount):
            if self.tts.GetVoices()[ i].GetDescription().find( name) >= 0:
                self.tts.Voice = self._voices[i]
#                self.tts.Speak( "%s Set!" % name)
                self._voice=i
                break
        if i >= self._voiceCount:
            self.tts.Speak( "%s Not Found!" % name)
#USED FOR BOOKMARKING AND USE LATER!
    def _get_lastIndex(self):
        bookmark=self.tts.status.LastBookmark
        if bookmark!="" and bookmark is not None:
            return int(bookmark)
        else:
            return -1
#NOW SET ENGINE PARMS!
#SET THE VOICE RATE!
    def setRate(self, rate):
        "MICROSOFT SAPI 5 RATE IS -10 TO 10"
        if rate > 10: rate = 10
        if rate < -10: rate = -10
        self.tts.Rate = rate
#SET PITCH OF THE VOICE!
    def setPitch(self, value):
        "MICROSOFT SAPI 5 pitch is really controled with xml around speECH TEXT AND IS -10 TO 10"
        if value > 10: value = 10
        if value < -10: value = -10
        self._pitch=value
#SET THE VOICE VOLUME!
    def setVolume(self, value):
        "MICROSOFT SAPI 5 VOLUME IS 1% TO 100%"
        self.tts.Volume = value
#CREATE ANOTHER INSTANCE OF A VOICE!
    def createVoice(self, name):
        num = 0
        for i in range( self._voiceCount):
            if self.tts.GetVoices()[ i].GetDescription().find( name) >= 0:
                num=i
                break
        new_tts = CreateObject( 'sapi.SPVoice')
        new_tts.Voice = self._voices[ num]
        return (new_tts)
#SPEAKING TEXT!
#SPEAK TEXT USING BOOKMARKS AND PITCH!
    def SpeakText(self, text, wait=False, index=None):
        "SPEAK TEXT AND XML FOR PITCH MUST REPLACE ANY <> SYMBOLS BEFORE USING XML BRACKETED TEXT"
        flags = constants4tts.XML
        text = text.replace( "<", "&lt;")
        pitch = ((self._pitch*2)-100)/10
        if isinstance(index, int):
            bookmarkXML = "<Bookmark Mark = \"%d\" />" % index #NOTE \" FOR XML FORMAT CONVERSION!
        else:
            bookmarkXML = ""
        flags = constants4tts.XML
        if wait is False:
            flags += constants4tts.Async
        self.tts.Speak( "<pitchabsmiddle = \"%s\">%s%s</pitch>" % (pitch, bookmarkXML, text), flags)
#CANCEL SPEAK IN PROGRESS!
    def cancel(self):
        #if self.tts.Status.RunningState == 2:
        self.tts.Speak(None, 1|constants4tts.Purge)
#SET AUDIO STREAM FOR OUTPUT TO A FILE!
    def SpeakToWav(self, filename, text, voice):
        """THIS METHOD ASSUMES THE IMPORT OF COMTYPES.CLIENT createObject SO
            A VOICE AND FILE STREAM OBJECT ARE CREATED WITH THE PASSING IN OF 3 STRINGS:
            THE FILE NAME TO SAVE THE VOICE INTO, THE TEXT, AND THE VOICE SPOKEN IN.
            ONCE THE TEXT IS SPOKEN INTO THE FILE, IT IS CLOSED AND THE OBJECTS DESTROYED!"""
        num = 0
        for i in range( self._voiceCount):
            if self.tts.GetVoices()[ i].GetDescription().find( voice) >= 0:
                num=i
                break
        stream = CreateObject("SAPI.SpFileStream")
        tts4file = CreateObject( 'sapi.SPVoice')
        tts4file.Voice = self._voices[ num]
        from comtypes.gen import SpeechLib
        stream.Open( filename, SpeechLib.SSFMCreateForWrite)
        tts4file.AudioOutputStream = stream
        tts4file.Speak( text, 0)
        stream.Close()
        del tts4file
        del stream
#NOW SPEAK THE WAV FILE SAVED!
    def SpeakFromWav(self, filename, sync=0, async=0, purge=0):
        "SPEAKING A WAV FILE ONLY!"
        self.tts.Speak( filename, sync |async |purge |self._is_filename)
#SPEAK TEXT!
    def Speak(self, text, wait=0, sync=0, async=0, purge=0, isfile=0, xml=0, not_xml=0, persist=0, punc=0):
        "SAPI 5 HAS NO PITCH SO HAS TO BE IN TEXT SPOKEN!"
        pitch=self._pitch
        self.tts.Speak( "<pitch absmiddle='%s'/>%s" % (pitch, text), wait |sync |async |purge |isfile |xml |not_xml |persist |punc)
#SPEAK TEXT WITHOUT PITCH!
    def Speaking(self, text, wait=0, sync=0, async=0, purge=0, isfile=0, xml=0, not_xml=0, persist=0, punc=0):
        "SPEAKING A FILE WITHOUT PITCH"
        self.tts.Speak( text, wait |sync |async |purge |isfile |xml |not_xml |persist |punc)
#SET THE VOICE BY VALUE!
    def setVoice(self,value):
        "SET VOICE AND SAY ITS DESCRIPTION!"
        if value < 1:
            value=1
        if value > self._voiceCount:
            value = self._voiceCount
        self.tts.Voice = self._voices[ value-1]
        vd = self.tts.GetVoices()[ value-1].GetDescription().find( " ")
#        self.tts.Speak( vd[ vd.find(" "):])
        self._voice=value-1
#READ ALL THE VOICES IN THE ENGINE!
    def read_Voices(self):
        self.tts.Speak( "Voices are:")
        for i in range( self._voiceCount):
            print self.getVoiceNameByNum(i+1)
            self.tts.Voice = self.tts.GetVoices()[i]
            vd = self.tts.GetVoices()[ i].GetDescription()
            self.tts.Speak( "%d) %s" % (i+1, vd[ vd.find(" "):]))

def Create( vs={}):
    "CREATE A SAPI VOICE INSTANCE!"
    vp = {"name":"Sam", "volume":100, "rate":0, "pitch":0}
    for i in vs: vp[i] = vs[i]
    newVoice = SynthDriver()
    if newVoice.check():
        newVoice.init()
        newVoice.setVoiceByName( vp["name"])
        newVoice.setVolume( vp["volume"])
        newVoice.setRate( vp["rate"])
        newVoice.setPitch( vp["pitch"])
        return newVoice
    else:
        print "SAPI Engine Is Not Installed On This Computer!"
        return Null

