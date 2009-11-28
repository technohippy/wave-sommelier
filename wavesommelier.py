import logging
from waveapi import document
from waveapi import events
from waveapi import model
from waveapi import robot
from extension import Extension

GADGET_URL = 'http://wave-sommelier.appspot.com/gadget/gadget.xml'

def OnSelfAdded(properties, context):
  blip = context.GetBlipById(context.GetRootWavelet().GetRootBlipId())
  if blip:
    blip.GetDocument().AppendElement(document.Gadget(GADGET_URL))

def OnBlipSubmitted(properties, context):
  blip = context.GetBlipById(properties['blipId'])
  gadget = blip.GetGadgetByUrl(GADGET_URL)
  key = gadget.get('extend')
  logging.info(key)
  extension = Extension.get(key)
  if extension:
    extension.extend(context)
  doc = blip.GetDocument()
  doc.GadgetSubmitDelta(gadget, {'extend':''})

if __name__ == '__main__':
  myRobot = robot.Robot('Wave Sommelier', 
      image_url='http://wave-sommelier.appspot.com/images/knife.png',
      version='16',
      profile_url='http://wave-sommelier.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnSelfAdded)
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()

