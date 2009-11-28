from google.appengine.ext import db
from waveapi import document

class Extension(db.Model):
  type = db.StringProperty()
  title = db.StringProperty()
  imageUrl = db.LinkProperty()
  desc = db.StringProperty(multiline=True)
  robotAddr = db.StringProperty()
  gadgetXml = db.StringProperty()
  techDesc = db.StringProperty(multiline=True)
  apis = db.StringListProperty()
  langs = db.StringListProperty()

  def extend(self, context):
    if self.type == 'gadget':
      root_wavelet = context.GetRootWavelet()
      new_doc = root_wavelet.CreateBlip().GetDocument()
      new_doc.AppendElement(document.Gadget(self.gadgetXml))
    elif self.type == 'robot':
      context.GetRootWavelet().AddParticipant(self.robotAddr)

