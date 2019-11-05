# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Generator/GenFilter/python/ZMuTau_13TeV_Tauola_TuneCUETP8M1_cfi.py -s GEN --conditions auto:mc --datatier GEN-SIM-RAW --eventcontent RAWSIM -n 10 --no_exec --python_filename ZMuTau_13TeV_Tauola_TuneCUETP8M1_cfi_py_GEN_IDEAL.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Generator/GenFilter/python/ZMuTau_13TeV_Tauola_TuneCUETP8M1_cfi.py nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('ZMuTau_13TeV_Tauola_TuneCUETP8M1_cfi_py_GEN.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAW')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    # ExternalDecays = cms.PSet(
    #     Tauola = cms.untracked.PSet(
    #         UseTauolaPolarization = cms.bool(True),
    #         InputCards = cms.PSet(
    #             mdtau = cms.int32(0),
    #             pjak2 = cms.int32(0),
    #             pjak1 = cms.int32(0)
    #         )
    #     ),
    #     parameterSets = cms.vstring('Tauola')
    # ),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        processParameters = cms.vstring('WeakSingleBoson:ffbar2gmZ = on', 
            '23:onMode = off', 
            '23:addChannel = 1 0.0000000001 100 -13 15', 
            '23:addChannel = 1 0.0000000001 100 13 -15'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters')
    )
)

#Gen level filter
process.dileptonFilter = cms.EDFilter('GenFilter',
                                      verbose   = cms.untracked.int32(2),
                                      id        = cms.untracked.vint32 ( 11,  13,  15),
                                      ptmin     = cms.untracked.vdouble(20., 15., 15.),
                                      etamin    = cms.untracked.vdouble(-3., -3., -3.),
                                      etamax    = cms.untracked.vdouble( 3.,  3.,  3.),
                                      naccepted = cms.untracked.uint32(1),
                                      nhadtaus  = cms.untracked.uint32(1)
) 

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen * process.dileptonFilter)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

