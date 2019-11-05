import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

# process = cms.Process('HLT')
generator = cms.EDFilter("Pythia8GeneratorFilter",
                         comEnergy = cms.double(13000.0),
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         # crossSection = cms.untracked.double(0.0000),
                         ExternalDecays = cms.PSet(
                             Tauola = cms.untracked.PSet(
                                 TauolaPolar,
                                 TauolaDefaultInputCards
                             ),
                             parameterSets = cms.vstring('Tauola')
                         ),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'WeakSingleBoson:ffbar2gmZ = on',
                                 '23:onMode = off',
                                 '23:addChannel = 1 0.0000000001 100 -13 15',
                                 '23:addChannel = 1 0.0000000001 100 13 -15'
                             ),
                             parameterSets = cms.vstring('pythia8CommonSettings',
                                                         'pythia8CUEP8M1Settings',
                                                         'processParameters',
                             )
                         )
)

# dileptonFilter = cms.EDFilter('GenFilter',
#                               verbose = cms.untracked.int32(2),
#                               ptmin = cms.untracked.double(5.),
#                               etamin = cms.untracked.double(-3.),
#                               etamax =  cms.untracked.double(3.)
# ) 
