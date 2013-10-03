# Auto generated configuration file
# using: 
# Revision: 1.341 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: TTToHqToWWqTo2L2Nuq_M_125_TuneZ2_7TeV_pythia6_cff.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --conditions auto:mc --pileup mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi --datatier GEN-SIM-RECO --eventcontent RECOSIM -n 100000 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

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

# global options
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("EmptySource")
process.options = cms.untracked.PSet()

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.341 $'),
    annotation = cms.untracked.string('TTToHqToWWqTo2L2Nuq_M_125_TuneZ2_7TeV_pythia6_cff.py nevts:100000'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('/tmp/naodell/TTToHqWbToWWqWbTo3L3Nubq_M_125_TuneZ2_8TeV_pythia6.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Filter out
process.dileptonFilter = cms.EDFilter("MCParticlePairFilter",
    Status  = cms.untracked.vint32(1, 1),
    MaxEta  = cms.untracked.vdouble(10., 10.),
    MinEta  = cms.untracked.vdouble(-10., -10.),
    MinPt   = cms.untracked.vdouble(0., 0.),
    MinP    = cms.untracked.vdouble(0., 0.),
    ParticleID1 = cms.untracked.vint32(-11, -13, -15, 11, 13, 15),
    ParticleID2 = cms.untracked.vint32(-11, -13, -15, 11, 13, 15),
#    MaxInvMass = cms.untracked.double(120.0),
#    MinInvMass = cms.untracked.double(70.0)
)


#process.filter2 = cms.EDFilter("MCSingleParticleFilter",
#    MaxEta = cms.untracked.vdouble(2.5),
#    Status = cms.untracked.vint32(1),
#    MinEta = cms.untracked.vdouble(-2.5),
#    MinPt = cms.untracked.vdouble(5.0),
#    ParticleID = cms.untracked.vint32(22)
#)


# Other statements
process.GlobalTag.globaltag = 'START53_V7A::All'

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),

    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring(
            'PMAS(25,1)=125.0        !mass of Higgs', 
            'MSEL=0                  ! user selection for process', 
            'MSUB(81)  = 1           ! qqbar to QQbar', 
            'MSUB(82)  = 1           ! gg to QQbar', 
            'MSTP(7)   = 6           ! flavor = top', 
            'PMAS(6,1) = 172.5       ! top quark mass', 

            'MDME(45,1)=2            ! t decay into Ws', 
            'KFDP(45,1)=25           ! change W to Higgs (hopefully) ', 
            'KFDP(45,2)=4            ! change s to c quark', 
            'MDME(46,1)=3            ! t decay', 

            'MSUB(102)=0             !ggH', 
            'MSUB(123)=0             !ZZ fusion to H', 
            'MSUB(124)=0             !WW fusion to H', 
            'MSUB(24)=0              !ZH production', 
            'MSUB(26)=0              !WH production', 
            'MSUB(121)=0             !gg to ttH', 
            'MSUB(122)=0             !qq to ttH', 

            'MDME(210,1)=0           !Higgs decay into dd', 
            'MDME(211,1)=0           !Higgs decay into uu', 
            'MDME(212,1)=0           !Higgs decay into ss', 
            'MDME(213,1)=0           !Higgs decay into cc', 
            'MDME(214,1)=0           !Higgs decay into bb', 
            'MDME(215,1)=0           !Higgs decay into tt', 
            'MDME(216,1)=0           !Higgs decay into', 
            'MDME(217,1)=0           !Higgs decay into Higgs decay', 
            'MDME(218,1)=0           !Higgs decay into e nu e', 
            'MDME(219,1)=0           !Higgs decay into mu nu mu', 
            'MDME(220,1)=0           !Higgs decay into tau nu tau', 
            'MDME(221,1)=0           !Higgs decay into Higgs decay', 
            'MDME(222,1)=0           !Higgs decay into g g', 
            'MDME(223,1)=0           !Higgs decay into gam gam', 
            'MDME(224,1)=0           !Higgs decay into gam Z', 
            'MDME(225,1)=0           !Higgs decay into Z Z', 
            'MDME(226,1)=1           !Higgs decay into W W', 

            'MDME(182,1)=0           !Z decay into e- e+', 
            'MDME(183,1)=0           !Z decay into nu_e nu_ebar', 
            'MDME(184,1)=0           !Z decay into mu- mu+', 
            'MDME(185,1)=0           !Z decay into nu_mu nu_mubar', 
            'MDME(186,1)=0           !Z decay into tau- tau+', 

            'MDME(190,1) = 1         !W decay into dbar u', 
            'MDME(191,1) = 1         !W decay into dbar c', 
            'MDME(192,1) = 0         !W decay into dbar t', 
            'MDME(194,1) = 1         !W decay into sbar u', 
            'MDME(195,1) = 1         !W decay into sbar c', 
            'MDME(196,1) = 0         !W decay into sbar t', 
            'MDME(198,1) = 1         !W decay into bbar u', 
            'MDME(199,1) = 1         !W decay into bbar c', 
            'MDME(200,1) = 0         !W decay into bbar t', 
            'MDME(205,1) = 0         !W decay into bbar tp', 
            'MDME(206,1) = 1         !W decay into e+ nu_e', 
            'MDME(207,1) = 1         !W decay into mu+ nu_mu', 
            'MDME(208,1) = 1         !W decay into tau+ nu_tau'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen * process.dileptonFilter)
#process.simulation_step = cms.Path(process.psim)
#process.digitisation_step = cms.Path(process.pdigi)
#process.L1simulation_step = cms.Path(process.SimL1Emulator)
#process.digi2raw_step = cms.Path(process.DigiToRaw)
#process.raw2digi_step = cms.Path(process.RawToDigi)
#process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.output_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step)#,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
#process.schedule.extend(process.HLTSchedule)
#process.schedule.extend([process.raw2digi_step,process.reconstruction_step])
process.schedule.extend([process.genfiltersummary_step, process.endjob_step, process.output_step])

# filter all path with the production sequence
for path in process.paths:
    getattr(process,path)._seq = process.generator * getattr(process,path)._seq 
