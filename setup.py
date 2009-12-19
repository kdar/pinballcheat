from distutils.core import setup
import py2exe

class Target:
  def __init__(self, **kw):
    self.__dict__.update(kw)
    # for the versioninfo resources
    self.version = "0.0.1"
    self.company_name = "No Company"
    self.copyright = "No copyright"
    self.name = ""

pinballcheat = Target (
    description = "A cheat for Window's Pinball",
    script = "MainApp.pyw",
    dest_base = "PinballCheat")

setup(windows=[pinballcheat])