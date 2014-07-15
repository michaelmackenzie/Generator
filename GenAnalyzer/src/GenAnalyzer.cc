// -*- C++ -*-
//
// Package:    GenAnalyzer
// Class:      GenAnalyzer
// 
/**\class GenAnalyzer GenAnalyzer.cc GenAnalyzer/GenAnalyzer/src/GenAnalyzer.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
 */
//
// Original Author:  Nate Odell
//         Created:  Sun Sep 29 20:09:27 CDT 2013
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// Generator data formats
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "TFile.h"
#include "TH1D.h"
#include "TMath.h"

//
// class declaration
//

using namespace reco;
using namespace std;

class GenAnalyzer : public edm::EDAnalyzer {
    public:
        explicit GenAnalyzer(const edm::ParameterSet&);
        ~GenAnalyzer();

        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        virtual void beginJob() ;
        virtual void analyze(const edm::Event&, const edm::EventSetup&);
        virtual void endJob() ;

        virtual void beginRun(edm::Run const&, edm::EventSetup const&);
        virtual void endRun(edm::Run const&, edm::EventSetup const&);
        virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
        virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

        TFile*  histFile;

        TH1D   *h1_HiggsMass, *h1_HiggsPt, *h1_HiggsEta, *h1_HiggsPhi;
        TH1D   *h1_TopMass, *h1_TopPt, *h1_TopEta, *h1_TopPhi;
        //TH1D   *h1_W1Mass, *h1_W1Pt, *h1_W1Eta, *h1_W1Phi;
        //TH1D   *h1_W2Mass, *h1_W2Pt, *h1_W2Eta, *h1_W2Phi;
        //TH1D   *h1_W3Mass, *h1_W3Pt, *h1_W3Eta, *h1_W3Phi;

        //TH1D   *h1_Lepton1Mass, *h1_Lepton1Pt, *h1_Lepton1Eta, *h1_Lepton1Phi;
        //TH1D   *h1_Lepton2Mass, *h1_Lepton2Pt, *h1_Lepton2Eta, *h1_Lepton2Phi;
        //TH1D   *h1_Neutrino1Mass, *h1_Neutrino1Pt, *h1_Neutrino1Eta, *h1_Neutrino1Phi;
        //TH1D   *h1_Neutrino2Mass, *h1_Neutrino2Pt, *h1_Neutrino2Eta, *h1_Neutrino2Phi;
        //TH1D   *h1_Jet1Mass, *h1_Jet1Pt, *h1_Jet1Eta, *h1_Jet1Phi;
        //TH1D   *h1_Jet2Mass, *h1_Jet2Pt, *h1_Jet2Eta, *h1_Jet2Phi;

};

GenAnalyzer::GenAnalyzer(const edm::ParameterSet& iConfig)
{
    //now do what ever initialization is needed
}


GenAnalyzer::~GenAnalyzer()
{
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
}

void GenAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;

    Handle<GenParticleCollection> genParticleColl;
    iEvent.getByLabel("genParticles", genParticleColl);

    for (GenParticleCollection::const_iterator iGenPart = genParticleColl->begin(); iGenPart != genParticleColl->end(); ++iGenPart) {
        const GenParticle myParticle = GenParticle(*iGenPart);

        // Look for the ttbar pair
        if (abs(myParticle.pdgId()) == 6 && myParticle.status() == 3) {
            cout << "\ntop found:\t " << myParticle.pdgId() << ", " << myParticle.status() << endl;

            h1_TopMass->Fill(myParticle.mass());
            h1_TopPt->Fill(myParticle.pt());
            h1_TopEta->Fill(myParticle.eta());
            h1_TopPhi->Fill(myParticle.phi());

            for (unsigned i = 0; i < myParticle.numberOfDaughters(); ++i) {
                const Candidate *ancestor = myParticle.daughter(i);

                // Look for Higgs
                if (abs(ancestor->pdgId()) == 25 && ancestor->status() == 3) {
                    cout  << "\t"<< ancestor->pdgId() << endl;

                    h1_HiggsMass->Fill(ancestor->mass());
                    h1_HiggsPt->Fill(ancestor->pt());
                    h1_HiggsEta->Fill(ancestor->eta());
                    h1_HiggsPhi->Fill(ancestor->phi());

                    for (unsigned i = 0; i < ancestor->numberOfDaughters(); ++i) {
                        const Candidate *ancestor2 = ancestor->daughter(i);
                        cout << "\t" << ancestor2->pdgId() << endl;

                        // Looking for Ws, Zs, or taus
                        if ((abs(ancestor2->pdgId()) == 24 || abs(ancestor2->pdgId()) == 23 || abs(ancestor2->pdgId()) == 15) && ancestor2->status() == 3) {
                            cout << "\t" << ancestor2->pdgId() << endl;

                            for (unsigned i = 0; i < ancestor2->numberOfDaughters(); ++i) {
                                const Candidate *ancestor3 = ancestor2->daughter(i);

                                // Looking for leptons from W
                                cout << "\t";
                                if (
                                        (abs(ancestor3-> pdgId()) >= 11 && abs(ancestor3->pdgId()) <= 16) 
                                        || (abs(ancestor3-> pdgId()) >= 1 && abs(ancestor3->pdgId()) <= 5)
                                   ) {
                                    cout << "\t" << ancestor3->pdgId();
                                }
                            }
                            cout << endl;
                        }
                    }
                } else if (ancestor->status() == 3) { // Should be Ws and bs

                    cout  << "\t"<< ancestor->pdgId() << endl;

                    // Get the leptons from the W decay
                    if (abs(ancestor->pdgId()) == 24) {

                        cout << "\t";
                        for (unsigned i = 0; i < ancestor->numberOfDaughters(); ++i) {
                            const Candidate *ancestor2 = ancestor->daughter(i);

                            // Looking for leptons
                            if (
                                    (abs(ancestor2-> pdgId()) >= 11 && abs(ancestor2->pdgId()) <= 16)
                                    || (abs(ancestor2-> pdgId()) >= 1 && abs(ancestor2->pdgId()) <= 5) 
                                    ) {
                                cout << "\t" << ancestor2->pdgId();
                            }
                        }
                        cout << endl;
                    } 
                }
            } 
        }
    }
    cout << "----------------------" << endl;
}

//void GenAnalyzer::DrawGenHisotgrams(Candidate* particle, TString pName)
//{
//
//}


void GenAnalyzer::beginJob()
{
    histFile        = new TFile("histFile.root", "RECREATE");

    h1_HiggsMass    = new TH1D("h1_HiggsMass", "M_{h};M_{h};Entries / 1 GeV", 50, 120., 130.);
    h1_HiggsPt      = new TH1D("h1_HiggsPt", "p_{T,h};p_{T,h};Entries / 2 GeV", 50, 0., 250.);
    h1_HiggsEta     = new TH1D("h1_HiggsEta", "#eta_{h};#eta_{h};Entries / bin", 50, -10., 10.);
    h1_HiggsPhi     = new TH1D("h1_HiggsPhi", "#phi_{h};#phi_{h};Entries / bin", 36, -TMath::Pi(), TMath::Pi());

    h1_TopMass      = new TH1D("h1_TopMass", "M_{h};M_{h};Entries / 1 GeV", 50, 150., 200.);
    h1_TopPt        = new TH1D("h1_TopPt", "p_{T,h};p_{T,h};Entries / 2 GeV", 50, 0., 250.);
    h1_TopEta       = new TH1D("h1_TopEta", "#eta_{h};#eta_{h};Entries / bin", 50, -10., 10.);
    h1_TopPhi       = new TH1D("h1_TopPhi", "#phi_{h};#phi_{h};Entries / bin", 36, -TMath::Pi(), TMath::Pi());

    //h1_W1Mass       = new TH1D("h1_W1Mass", "M_{W1};M_{W1};Entries / 1 GeV", 50, 0., 100.);
    //h1_W1Pt         = new TH1D("h1_W1Pt", "p_{T,h};p_{T,h};Entries / 2 GeV", 50, 0., 100.);
    //h1_W1Eta        = new TH1D("h1_W1Eta", "#eta_{W1};#eta_{W1};Entries / bin", 50, -10., 10.);
    //h1_W1Phi        = new TH1D("h1_W1Phi", "#phi_{W1};#phi_{W1};Entries / bin", 36, -TMath::Pi(), TMath::Pi());

    //h1_W2Mass       = new TH1D("h1_W2Mass", "M_{W2};M_{W2};Entries / 1 GeV", 50, 0., 100.);
    //h1_W2Pt         = new TH1D("h1_W2Pt", "p_{T,h};p_{T,h};Entries / 2 GeV", 50, 0., 100.);
    //h1_W2Eta        = new TH1D("h1_W2Eta", "#eta_{W2};#eta_{W2};Entries / bin", 50, -10., 10.);
    //h1_W2Phi        = new TH1D("h1_W2Phi", "#phi_{W2};#phi_{W2};Entries / bin", 36, -TMath::Pi(), TMath::Pi());
}

void GenAnalyzer::endJob() 
{
    h1_HiggsMass->Write(); // p00p
    h1_HiggsPt->Write(); // p00p
    h1_HiggsEta->Write(); // p00p
    h1_HiggsPhi->Write(); // p00p
    h1_TopMass->Write(); // p00p
    h1_TopPt->Write(); // p00p
    h1_TopEta->Write(); // p00p
    h1_TopPhi->Write(); // p00p

    histFile->Write();
    histFile->Close();
}

void GenAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

void GenAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

void GenAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

void GenAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

void GenAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenAnalyzer);
