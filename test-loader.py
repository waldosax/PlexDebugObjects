# import imp
import importlib
import sys

Agent = importlib.import_module('Plex.Agent')

spec = importlib.util.spec_from_file_location("SampleAgent", "SampleAgent.bundle/Contents/Code/__init__.py")
SampleAgent = importlib.util.module_from_spec(spec)

SampleAgent.__setattr__("Agent", Agent)

spec.loader.exec_module(SampleAgent)

agent = SampleAgent.SampleAgent()
print(agent.name)

SampleAgent.Start()