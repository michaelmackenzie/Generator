# Auto generated configuration file
# using: 
# Revision: 1.341 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: TTToHqToWWqTo2L2Nuq_M_125_TuneZ2_7TeV_pythia6_cff.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --conditions auto:mc --pileup mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi --datatier GEN-SIM-RECO --eventcontent RECOSIM -n 100000 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic7TeV2011Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
         'file:/uscms_data/d2/akub19/DYtoLL_MADGRAPH_LHE.root'
    )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.341 $'),
    annotation = cms.untracked.string('ZtoMuMu_7TeV_pythia8_cff.py nevts:10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('DYtoLL_Madgraph_Pythia8_Tune4C_GEN.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RECO')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition
#process.AODSIMEventContent.outputCommands.append('keep *_ak5GenJetsNoMuNoNuMPI_*_*')

# Other statements
#process.GlobalTag.globaltag = 'MC_44_V7::All'
process.GlobalTag.globaltag = 'START44_V10::All'

# process.load("Configuration.Generator.Hadronizer_MgmMatchTune4C_7TeV_madgraph_pythia8_cff")

#process.generator = cms.EDFilter("Pythia8HadronizerFilter",
#    maxEventsToPrint = cms.untracked.int32(1),
#    pythiaPylistVerbosity = cms.untracked.int32(1),
#    filterEfficiency = cms.untracked.double(1.0),
#    pythiaHepMCVerbosity = cms.untracked.bool(False),
#    comEnergy = cms.double(7000.),
#    jetMatching = cms.untracked.PSet(
#       scheme = cms.string("Madgraph"),
#       mode = cms.string("exclusive"),	# soup, or "inclusive"/"exclusive"
#       MEMAIN_etaclmax = cms.double(5.0),
#       MEMAIN_qcut = cms.double(20.),       
#       MEMAIN_minjets = cms.int32(-1),
#       MEMAIN_maxjets = cms.int32(-1),
#       MEMAIN_showerkt = cms.double(0),    # use 1=yes only for pt-ordered showers !
#       MEMAIN_nqmatch = cms.int32(5),      # PID of the flavor until which the QCD radiation are kept in the matching procedure. 
#       MEMAIN_excres = cms.string(""),
#       outTree_flag = cms.int32(0)         # 1=yes, write out the tree for future sanity check
#    ),    
#    PythiaParameters = cms.PSet(
#        pythia8_mg = cms.vstring(''), # this pset is for very initial testing
        # this pset below is actually used in large-scale (production-type) tests
#	processParameters = cms.vstring(
#            'Tune:pp = 5',
#            'Main:timesAllowErrors    = 10000',
#            'ParticleDecays:limitTau0 = on',
#            'ParticleDecays:tauMax = 10',
#            'PartonLevel:MI = on',
#            'MultipleInteractions:Kfactor = 0.5',
#            'BeamRemnants:reconnectColours = off'
#        ),
#        parameterSets = cms.vstring('processParameters')
#    )
#)


process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(7000.),
    jetMatching = cms.untracked.PSet(
        scheme = cms.string("Madgraph"),
        mode = cms.string("auto"),# soup, or "inclusive" / "exclusive"
        MEMAIN_etaclmax = cms.double(5.0),
        MEMAIN_qcut = cms.double(20.0),
        MEMAIN_minjets = cms.int32(-1),
        MEMAIN_maxjets = cms.int32(-1),
        MEMAIN_showerkt = cms.double(0), # use 1=yes only for pt-ordered showers !
        MEMAIN_nqmatch = cms.int32(5),   #PID of the flavor until which the QCD radiation are kept in the matching procedure;
                                         # if nqmatch=4, then all showered partons from b's are NOT taken into account
         # Note (JY): I think the default should be 5 (b); anyway, don't try -1  as it'll result in a throw...
        MEMAIN_excres = cms.string(""),
        outTree_flag = cms.int32(0)      # 1=yes, write out the tree for future sanity check
    ),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
	    'Main:timesAllowErrors    = 10000', 
        'ParticleDecays:limitTau0 = on',
	    'ParticleDecays:tauMax = 10',
        'Tune:ee 3',
        'Tune:pp 5',
        'MultipartonInteractions:Kfactor = 1.05',
        #'PartonLevel:MPI = off',
    ),
        parameterSets = cms.vstring('processParameters')
    )
)


process.filter1 = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MaxEta = cms.untracked.vdouble(2.4, 2.4),
    MinEta = cms.untracked.vdouble(-2.4, -2.4),
    MinPt = cms.untracked.vdouble(19.0, 19.0),
    ParticleID1 = cms.untracked.vint32(13, -13),
    ParticleID2 = cms.untracked.vint32(13, -13)
#    MaxInvMass = cms.untracked.double(120.0),
#    MinInvMass = cms.untracked.double(70.0)
)

process.filter2 = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.5),
    Status = cms.untracked.vint32(1),
    MinEta = cms.untracked.vdouble(-2.5),
    MinPt = cms.untracked.vdouble(5.0),
    ParticleID = cms.untracked.vint32(22)
)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen * process.filter1)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step)
#process.schedule.extend(process.HLTSchedule)
#process.schedule.extend([process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step])
process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        default = cms.untracked.PSet( limit = cms.untracked.int32(0) ),
        FwkJob = cms.untracked.PSet( limit = cms.untracked.int32(0) )
    ),
    categories = cms.untracked.vstring('FwkJob'),
    destinations = cms.untracked.vstring('cout')
)

