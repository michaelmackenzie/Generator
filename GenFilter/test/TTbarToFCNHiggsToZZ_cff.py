# Auto generated configuration file
# using: 
# Revision: 1.341 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: TTToHqToWWqTo2L2Nuq_M_125_TuneZ2_7TeV_pythia6_cff.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --conditions auto:mc --pileup mix_E7TeV_Fall2011_Reprocess_50ns_PoissonOOTPU_cfi --datatier GEN-SIM-RECO --eventcontent RECOSIM -n 100000 --no_exec
import FWCore.ParameterSet.Config as cms

doFullReco = False

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Input source
process.source = cms.Source("EmptySource")
process.options = cms.untracked.PSet()

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.341 $'),
    annotation = cms.untracked.string('TTbarToFCNHiggsToZZ_cff.py nevts:100000'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('FCNH_ZZ_GEN-SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)


# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V27::All', '')

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring(
            'MSTU(21)=1     ! Check on possible errors during program execution', 
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
            #'KFDP(46,1)=25           ! change W to Higgs (hopefully) ', 
            #'KFDP(46,2)=4            ! change s to c quark', 

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
            'MDME(225,1)=1           !Higgs decay into Z Z', 
            'MDME(226,1)=0           !Higgs decay into W W', 

            'MDME(174,1)=1           !Z decay into d dbar', 
            'MDME(175,1)=1           !Z decay into u ubar', 
            'MDME(176,1)=1           !Z decay into s sbar', 
            'MDME(177,1)=1           !Z decay into c cbar', 
            'MDME(178,1)=1           !Z decay into b bbar', 
            'MDME(182,1)=1           !Z decay into e- e+', 
            'MDME(183,1)=1           !Z decay into nu_ebar', 
            'MDME(184,1)=1           !Z decay into mu- mu+', 
            'MDME(185,1)=1           !Z decay into nu_mu nu_mubar', 
            'MDME(186,1)=1           !Z decay into tau- tau+', 
            'MDME(187,1)=1           !Z decay into nu_tau nu_taubar', 

            'MDME(190,1) = 0         !W decay into dbar u', 
            'MDME(191,1) = 0         !W decay into dbar c', 
            'MDME(192,1) = 0         !W decay into dbar t', 
            'MDME(194,1) = 0         !W decay into sbar u', 
            'MDME(195,1) = 0         !W decay into sbar c', 
            'MDME(196,1) = 0         !W decay into sbar t', 
            'MDME(198,1) = 0         !W decay into bbar u', 
            'MDME(199,1) = 0         !W decay into bbar c', 
            'MDME(200,1) = 0         !W decay into bbar t', 
            'MDME(205,1) = 0         !W decay into bbar tp', 
            'MDME(206,1) = 1         !W decay into e+ nu_e', 
            'MDME(207,1) = 1         !W decay into mu+ nu_mu', 
            'MDME(208,1) = 1         !W decay into tau+ nu_tau'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

process.leptonFilter = cms.EDFilter('GenFilter') 

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen * process.leptonFilter)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.simulation_step = cms.Path(process.psim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.RAWSIMoutput_step,process.simulation_step,process.endjob_step)

# filter all paths with the production filter sequence
for path in process.paths:
   getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

